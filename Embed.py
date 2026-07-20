import dataclasses
from typing import TypedDict, NotRequired

from dotenv import load_dotenv
from langchain_community.embeddings import OpenAIEmbeddings


env_path = r'/Users/devshankha/Documents/Jupyter/.env'
load_dotenv(env_path)
embeddings =OpenAIEmbeddings(model="text-embedding-3-small")
text="How"
query_result =embeddings.embed_documents(text)
print(query_result)





