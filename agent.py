from langchain.agents import AgentExecuter, create_react_agent
from langchain_groq import ChatGroq
from langchain import hub
from tools import calculator, string_length, word_count
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    temperature=0
)

tools = [calculator, string_length, word_count]

prompt = hub.pull("hwchase17/react")

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)


agent_executer = AgentExecuter(
    agent=agent,
    tools=tools,
    verbose=True
)