from typing import Annotated
from typing_extensions import TypedDict
from langchain_groq import ChatGroq
from langgraph.graph.state import StateGraph
from langgraph.graph import START,END
from langgraph.prebuilt import tools_condition
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from langchain_core.tools import tool
from langchain_core.messages import BaseMessage
import os 
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
os.environ["LANGSMITH_API_KEY"]= os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGSMITH_TRACING"]="true"
os.environ["LANGSMITH_PROJECT"]="Test_Project"
llm= ChatGroq(model="openai/gpt-oss-20b")

class State(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]


def make_state_graph():
    @tool 
    def add(a:float,b:float)->float:
        """It Add Two Numbers"""
        return a+b

    @tool
    def multiply(a:float,b:float)->float:
        """to multiply simply two numbers"""
        return a*b

    tool_node=ToolNode([add,multiply])
    llm_with_tool=llm.bind_tools([add,multiply])

    def call_llm_model(state:State):
        return{"messages":[llm_with_tool.invoke(state['messages'])]}

    builder=StateGraph(State)
    # def tool_calling_llm(state:State):
    #     return {
    #         "messages":[llm_with_tool.invoke(state["messages"])]
    #     }
    ##adding node for the same
    builder.add_node("tool_calling_llm",call_llm_model)
    builder.add_node("tools",tool_node)
    ##here we are going to add edges simply which will going to define 
    builder.add_edge(START,"tool_calling_llm")
    builder.add_conditional_edges("tool_calling_llm",
    #if the latest message (result) from assistant is a tool call then simply tools_condition routes to tools
    # if the latest message (result) from assistant is not a tool call then simply tools_condition routes to End
    tools_condition)
    builder.add_edge("tools","tool_calling_llm")
    graph=builder.compile()

    return graph

agent=make_state_graph()