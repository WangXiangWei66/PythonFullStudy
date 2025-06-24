from langgraph.graph import StateGraph

from ctrip.graph_chat.assistant import create_assistant_node
from ctrip.graph_chat.state import State

#定义一个流程图的构建对象
builder = StateGraph(State)

#自定义函数代表节点，Runnable，或者一个自定义的类都可以是节点
builder.add_node('assistant',create_assistant_node())
