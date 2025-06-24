'''本代码使用Python的typing模块和LangChain框架定义了一个状态类型，用来管理聊天信息'''
#TypedDict：用来创建带类型提示的字典
#Annotated：用于给类型添加元数据（如验证器、描述）
from typing import TypedDict, Annotated
#AnyMessage：LangChain 中所有消息类型的基类（如 HumanMessage、AIMessage）
from langchain_core.messages import AnyMessage
#add_messages：LangGraph 框架中的装饰器或函数，用于处理消息添加逻辑
from langgraph.graph import add_messages

#State：继承自TypedDict类型，代表应用状态
#该字段在添加时需要特殊处理
class State(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
