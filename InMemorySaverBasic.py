from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_core.utils.uuid import uuid7
from langgraph.checkpoint.memory import InMemorySaver

env_path = r'/Users/devshankha/Documents/Jupyter/.env'
load_dotenv(env_path)
chat_model = ChatOpenAI(model="gpt-3.5-turbo")


agent = create_agent(
    # "openai:gpt-5.5",
    chat_model,
    checkpointer=InMemorySaver(),
)


config = {"configurable": {"thread_id": str(uuid7())}}
response = agent.invoke(
    {"messages": [{"role": "user", "content": "What is the name of Salim Khan's eldest son?"}]
     },config=config,
)

response = agent.invoke(
    {"messages": [{"role": "user", "content": "And what is the name of his youngest son?"}]
     },config=config,
)
print(response)