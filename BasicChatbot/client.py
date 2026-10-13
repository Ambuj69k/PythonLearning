from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()
import asyncio
import os
import sys

async def main():
    math_server_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mathserver.py")
    client=MultiServerMCPClient(
        {
            "math":{
                "command":sys.executable,
                "args":[math_server_path],
                "transport":"stdio",
            },
            "wheather":{
                "url":"http://127.0.0.1:8000/mcp",
                "transport":"streamable_http"
            }
        }
    )

    os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
    tools= await client.get_tools()
    model=ChatGroq(model="openai/gpt-oss-20b")
    agent=create_react_agent(
        model,tools
    )

    math_response= await agent.ainvoke(
        {"messages":[{"role":"user","content":"what is the (3+5) * 12?"}]}
    )

    print("math response", math_response['messages'][-1].content)

    wheather_response= await agent.ainvoke(
        {"messages":[{"role":"user","content":"what is the wheather in mumbai?"}]}
    )
    print("wheather response:" ,wheather_response['messages'][-1].content)

asyncio.run(main())