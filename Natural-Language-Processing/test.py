#imports

from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent, AgentOutputParser
from langchain.prompts import StringPromptTemplate
from langchain.chat_models import ChatOpenAI
from typing import List, Union
from langchain.schema import AgentAction, AgentFinish, OutputParserException
from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from query import query

# loads the .env file
load_dotenv()

#establish LLM model
llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key="")



#Canvas Query
canvas = Tool(
    name="Canvas",
    func=query,
    description="always run unless another tool applies"
)
tools = [canvas]



# Step 3: Define the prompt template
template = """

Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [Calculator, Stock DB]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}
"""

# Step 4: Create a custom prompt template class
class CustomPromptTemplate(StringPromptTemplate):
    template: str
    tools: List[Tool]

# Step 5: Initialize the Langchain agent
agent = initialize_agent(tools=tools, llm=llm, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION)

# Step 6: Run the Langchain agent
user_input = "What are my assignments"


print(agent.run(user_input))