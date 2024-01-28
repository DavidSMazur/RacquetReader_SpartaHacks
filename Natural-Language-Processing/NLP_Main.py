from langchain_google_vertexai import VertexAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.agents import Tool, AgentType
from langchain.agents import initialize_agent
from langchain.prompts import SystemMessage, HumanMessage
from langchain.chains import ConversationChain
import os
import tools_all
import prompt_template



def create_model(model_name="gemini-pro", verbose=True):
    return VertexAI(
        model_name=model_name,
        verbose=verbose,
        memory="chat_history",
        max_output_tokens=256,
        temperature=0.1,
        top_p=0.8,
        top_k=40,
    )

model = create_model()
llm = create_model()
tools=[knowlege_base]  # tool comes from tools_all import

agent = initialize_agent(
    tools=tools,  # tools should be a list of tools
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

prompt=PromptTemplate(
    input_variables=["system_message", "human_message"],
    template=template_prompt,
)

input_string = "I like tomatoes, what should I eat?"