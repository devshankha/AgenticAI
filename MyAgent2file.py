from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool

# Load environment variables (e.g., OpenAI API keys) from a .env file located on the local system
env_path = r'/Users/devshankha/Documents/Jupyter/.env'
load_dotenv(env_path)
chat_model = ChatOpenAI(model="gpt-3.5-turbo")
@tool
def search(query: str) -> str:
    """Search for information."""
    return f"Results for: {query}"
agent = create_agent(
   # "openai:gpt-5.5",
    chat_model,
    tools=[search],
    system_prompt="You are a helpful assistant. Be concise and accurate.",
)

response = agent.invoke({"input": "What is the capital of France?"})
print(response)

