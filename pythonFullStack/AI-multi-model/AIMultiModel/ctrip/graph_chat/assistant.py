'''本代码实现了LangChain框架的携程客户服务助手节点，继承了多种旅行相关工具，并通过状态管理实现智能对话'''

import os  # 用于系统操作
from datetime import datetime  # 用于处理时间

from langchain_core.prompts import ChatPromptTemplate  # 创建聊天提示模板
from langchain_core.runnables import Runnable, RunnableConfig  # LangChain中可运行接口和提示类
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from ctrip.graph_chat.state import State
from ctrip.tools.car_tools import search_car_rentals, book_car_rental, update_car_rental, cancel_car_rental
from ctrip.tools.flights_tools import fetch_user_flight_information, search_flights, update_ticket_to_new_flight, \
    cancel_ticket
from ctrip.tools.hotels_tools import search_hotels, book_hotel, update_hotel, cancel_hotel
from ctrip.tools.retriever_vector import lookup_policy
from ctrip.tools.trip_tools import book_excursion, search_trip_recommendations, update_excursion, cancel_excursion


# 主要用于执行工作流节点的执行逻辑
class CtripAssistant:

    # 自定义一个类，表示流程图的一个节点（复杂的）

    def __init__(self, runnable: Runnable):
        """
        初始化助手的实例。
        :param runnable: 可以运行对象，通常是一个Runnable类型的
        """
        self.runnable = runnable

    def __call__(self, state: State, config: RunnableConfig):
        """
        调用节点，执行助手任务
        :param state: 当前工作流的状态
        :param config: 配置: 里面有旅客的信息
        :return:
        """
        while True:
            # 创建了一个无限循环，它将一直执行直到：从 self.runnable 获取的结果是有效的。
            # 如果结果无效（例如，没有工具调用且内容为空或内容不符合预期格式），循环将继续执行，
            # configuration = config.get('configurable', {})
            # user_id = configuration.get('passenger_id', None)
            # state = {**state, 'user_info': user_id}  # 从配置中得到旅客的ID，也追加到state
            result = self.runnable.invoke(state)
            # 如果，runnable执行完后，没有得到一个实际的输出
            if not result.tool_calls and (  # 如果结果中没有工具调用，并且内容为空或内容列表的第一个元素没有"text"，则需要重新提示用户输入。
                    not result.content
                    or isinstance(result.content, list)
                    and not result.content[0].get("text")
            ):
                messages = state["messages"] + [("user", "请提供一个真实的输出作为回应。")]
                state = {**state, "messages": messages}
            else:  # 如果： runnable执行后已经得到，想要的输出，则退出循环
                break
        return {'messages': result}


# 初始化搜索工具，限制结果数量为2
os.environ["TAVILY_API_KEY"] = "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"  # 定义Tavily搜索工具的API密钥
tavily_tool = TavilySearch(max_results=1)
# 定义工具列表，这些工具将在与用户交互过程中被调用，包含搜索、预订、更新、取消等功能
part_1_tools = [
    tavily_tool,
    fetch_user_flight_information,
    search_flights,
    lookup_policy,
    update_ticket_to_new_flight,
    cancel_ticket,
    search_car_rentals,
    book_car_rental,
    update_car_rental,
    cancel_car_rental,
    search_hotels,
    book_hotel,
    update_hotel,
    cancel_hotel,
    search_trip_recommendations,
    book_excursion,
    update_excursion,
    cancel_excursion,
]
safe_tools = [  # 只读操作工具
    tavily_tool,  # 搜索结果，例如航班信息
    fetch_user_flight_information,  # 获取用户的航班信息
    search_flights,  # 搜索航班
    lookup_policy,  # 查看公司政策
    search_car_rentals,  # 搜索租车选项
    search_hotels,  # 搜索酒店
    search_trip_recommendations,  # 搜索旅行推荐
]
# 定义敏感工具列表，这些工具会更改用户的预订
sensitive_tools = [
    update_ticket_to_new_flight,  # 更新航班票务到新航班
    cancel_ticket,  # 取消票务
    book_car_rental,  # 预订租车
    update_car_rental,  # 更新租车预订
    cancel_car_rental,  # 取消租车预订
    book_hotel,  # 预订酒店
    update_hotel,  # 更新酒店预订
    cancel_hotel,  # 取消酒店预订
    book_excursion,  # 预订短途旅行
    update_excursion,  # 更新短途旅行预订
    cancel_excursion,  # 取消短途旅行预订
]
# 通过集合存储敏感工具名称，便于后续权限控制
sensitive_tool_names = {t.name for t in sensitive_tools}


def create_assistant_node() -> CtripAssistant:
    llm = ChatOpenAI(
        temperature=1.0,
        model='gpt-3.5-turbo',
        api_key="sk-ZKECakqu96gnIMx1iBsKkhHNl0qX3VnIDOJdtxPzTcFZdD1u",
        base_url="https://xiaoai.plus/v1",
        verbose=False
    )

    # 修改提示词模板，移除{user_info}
    primary_assistant_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "您是携程瑞士航空公司的客户服务助理。优先使用提供的工具搜索航班、公司政策和其他信息来帮助用户的查询。"
                "搜索时，请坚持不懈。如果第一次搜索没有结果，扩大您的查询范围。"
                "如果搜索为空，在放弃之前扩展您的搜索。\n\n当前时间: {time}.",
            ),
            ("placeholder", "{messages}"),
        ]
    ).partial(time=datetime.now())

    runnable = primary_assistant_prompt | llm.bind_tools(safe_tools + sensitive_tools)
    return CtripAssistant(runnable)
