from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool

env_path = r'/Users/devshankha/Documents/Jupyter/.env'
load_dotenv(env_path)
chat_model = ChatOpenAI(model="gpt-3.5-turbo")


agent = create_agent(
    # "openai:gpt-5.5",
    chat_model,
   None
)

response = agent.invoke(
    {"messages": [{"role": "user", "content": "What is the capital of France?"}]}
)
print(response)
