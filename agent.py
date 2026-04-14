from langchain_classic.agents import AgentExecutor, create_react_agent
from langchain_groq import ChatGroq
from langsmith import Client
from tools import calculator, string_length, word_count
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    temperature=0
)

tools = [calculator, string_length, word_count]

client = Client()
prompt = client.pull_prompt("hwchase17/react")

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)


agent_executer = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

if __name__ == "__main__":
    response = agent_executer.invoke({
        "input": "how many words and characters are in i am ai agent?"
    })
    print(response["output"])