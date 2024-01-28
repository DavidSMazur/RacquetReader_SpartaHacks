#tools_all

#imports for tools
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, StructuredTool, tool
from typing import Optional, Type
import os
from langchain.callbacks.manager import (AsyncCallbackManagerForToolRun,CallbackManagerForToolRun,)
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import Tool
from openai import OpenAI



from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv('OpenAI_api_key')
os.environ['OPENAI_API_KEY'] = openai_api_key

client = OpenAI()



def knowlege_base(query: str) -> str:
    
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a tennis coach, and you help answer questions"},
      {"role": "user", "content": "{query}"}
    ]
  )

  audio_out=completion.choices[0].message