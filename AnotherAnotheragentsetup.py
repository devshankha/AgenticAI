from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

import os
from dotenv import load_dotenv
env_path = r'/Users/devshankha/Documents/Jupyter/.env'
load_dotenv(env_path)
chat_model = ChatOpenAI(model="gpt-3.5-turbo")

def get_weather(city:str)-> str:
    """Get the weather for a city."""
    return f"The weather in {city} is sunny."

agent=create_agent(
    model="gpt-5",
    tools=[get_weather],
    system_prompt="You are a helpful assistant."
)

response =agent.invoke({"messages":"write me an essay of about 100 words about Narendra Modi"})
print(response["messages"][-1].content)
