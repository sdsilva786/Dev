from SourceCode.Agents.StateTypes.GlobalState import GlobalState
from SourceCode.GenAIModel import AzureOpenAI
from langchain_core.prompts import ChatPromptTemplate


def Supervisor(state: GlobalState):
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are Supply Chain Supervisor. Analyze the current state and decide the next agent:

        Options:
        - inventory_agent: Stock levels critical, restocking needed
        - demand_agent: Demand forecast accuracy below threshold
        - supplier_agent: Supplier performance issues detected
        - risk_agent: Geopolitical risks emerging
        - END: All objectives achieved

        Current State: current_step}
         History: {workflow_history}"""),
        ("human", "Input: {user_input}")
    ])
    llm = AzureOpenAI.Get_Instance()
    chain = prompt | llm
    response = chain.invoke(state)
    next_agent = response.content.strip().lower().replace("next agent: ", "")
    print(f"Supervisor decided next agent: {next_agent}")  # Debugging output
    return {"current_agent": next_agent}
