from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

import os
from dotenv import load_dotenv
env_path = r'/Users/devshankha/Documents/Jupyter/.env'
load_dotenv(env_path)
chat_model = ChatOpenAI(model="gpt-3.5-turbo")



for chunk in chat_model.stream("write me an essay of about 100 words about Narendra Modi"):
    print(chunk.text, end="|", flush=True)


