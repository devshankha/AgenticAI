from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.tools import tool

@tool
def get_weather(location:str)->str:
    """Get the weather at a location"""
    return f"It's sunny in {location}"

env_path = r'/Users/devshankha/Documents/Jupyter/.env'
load_dotenv(env_path)
model = init_chat_model(model="gpt-5.4-mini")
model_with_tools=model.bind_tools([get_weather])
response = model_with_tools.invoke("What's the weather at location Boston")
print(response)
for tool_call in response.tool_calls:
    # View tool calls made by the model
    print(f"Tool: {tool_call['name']}")
    print(f"Args: {tool_call['args']}")