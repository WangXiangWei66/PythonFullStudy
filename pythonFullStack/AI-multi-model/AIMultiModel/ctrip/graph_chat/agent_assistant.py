from datetime import datetime

from langchain_core.prompts.chat import ChatPromptTemplate

from ctrip.tools.flights_tools import search_flights, update_ticket_to_new_flight, cancel_ticket

#航班预定助手
flight_booking_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "您是专门处理航班查询，改签和预定的助理。"
            "当用户需要帮助更新他们的预订时，主助理会将工作委托给您。"
            "请与客户确认更新后的航班详情，并告知他们任何额外费用。"
            "在搜索时，请坚持不懈。如果第一次搜索没有结果，请扩大查询范围。"
            "如果您需要更多信息或客户改变主意，请将任务升级回主助理。"
            "请记住，在相关工具成功使用后，预订才算完成。"
            "\n\n当前用户的航班信息:\n<Flights>\n{user_info}\n</Flights>"
            "\n当前时间: {time}."
            "\n\n如果用户需要帮助，并且您的工具都不适用，则"
            '“CompleteOrEscalate”对话给主助理。不要浪费用户的时间。不要编造无效的工具或功能。',
        ),
        ("placeholder","{message}"),
    ]
).partial(time = datetime.now()) #使得助手最终都能获取到最新时间消息

#定义安全工具（只读操作）和敏感工具（设置更改的操作）
update_flight_safe_tools = [search_flights]
update_flight_sensitive_tools = [update_ticket_to_new_flight,cancel_ticket]

#合并所有工具
update_flights_tools = update_flight_safe_tools + update_flight_sensitive_tools

#创建和运行对象，绑定航班预定提示模板和工具集，包括CompleteOrEscalate工具
update_flight_runnable = flight_booking_prompt | llm.bind_tools(
    update_flights_tools + [CompleteOrEscalate]
)