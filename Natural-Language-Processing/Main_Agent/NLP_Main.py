from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.agents import Tool, AgentExecutor
from langchain.llms import OpenAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from tools_all import knowlege_base
from prompt_template import template_prompt
from langchain_community.llms import OpenAI
import os



load_dotenv()


knowlege_base_tool = Tool(
    name="Tennis Knowledge Base", 
    func=knowlege_base,
    description="Useful for answering questions about tennis technique, rules, training and strategy"
)

tools = [knowlege_base_tool]

llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=os.environ['OpenAI_api_key'])


class CustomPromptTemplate(StringPromptTemplate):
    template: str
    tools: List[Tool]

agent = initialize_agent(tools=tools, llm=llm, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION)

input_string = "What is the capital of Alabama?"

out=agent.run(input_string)