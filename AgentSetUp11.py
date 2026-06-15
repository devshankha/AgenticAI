from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables (e.g., OpenAI API keys) from a .env file located on the local system
env_path = r'/Users/devshankha/Documents/Jupyter/.env'
load_dotenv(env_path)
chat_model = ChatOpenAI(model="gpt-3.5-turbo")

# Send a message to the model and get the response
response = chat_model.invoke("What is Capital of USA?")
print(response)
