from langchain_google_vertexai import VertexAI
from langchain import PromptTemplate, LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.agents import Tool
from langchain.agents import tool
from langchain.agents import AgentType
from langchain.agents import initialize_agent
import os

load_dotenv()

model = VertexAI(model_name="gemini-pro")

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

llm = VertexAI(
    model_name=model,
    llm=VertexAI(), 
    verbose=True
    
    memory="chat_history", 
    max_output_tokens=256,
    temperature=0.1,
    top_p=0.8,
    top_k=40,
)

res = chat([
        SystemMessage(
            content="You are a nice AI bot that helps a user figure out what to eat in one short sentence"
        ),
        HumanMessage(content="I like tomatoes, what should I eat?"),
    ])

print(res.content)

