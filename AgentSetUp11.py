from dotenv import load_dotenv
from openai import OpenAI
from langchain_core.tools import Tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_classic.chains import create_retrieval_chain
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

# Load environment variables (e.g., OpenAI API keys) from a .env file located on the local system
env_path = r'/Users/devshankha/Documents/Jupyter/.env'
load_dotenv(env_path)
prompt_template = PromptTemplate(
    input_variables=["name"],
    template="Hello, {name}! How can I help you today?"
)

# Generate the prompt by filling in the variable
formatted_prompt = prompt_template.format(name="David")
print(formatted_prompt) 
chat_model = ChatOpenAI(model="gpt-3.5-turbo")

# Send a message to the model and get the response
response = chat_model.invoke("What is Capital of USA?")
print(response)