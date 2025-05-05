from langgraph.graph import StateGraph, START, END
from SourceCode.Agents.GeopoliticalRiskManagement.DTO.NewsAgentState import NewsAgentState
from SourceCode.Agents.GeopoliticalRiskManagement.Agent import FetchNewsAgent, ExtractRelevantNewsAgent

from SourceCode.Agents.StateTypes.GlobalState import GlobalState


def run(global_state: GlobalState) -> GlobalState:
    builder = StateGraph(NewsAgentState)

    builder.add_node("FetchNewsAgent", FetchNewsAgent.FetchNewsAgent)
    builder.add_node("ExtractRelevantNewsAgent", ExtractRelevantNewsAgent.ExtractRelevantNewsAgent)

    builder.add_edge(START, "FetchNewsAgent")
    builder.add_edge("FetchNewsAgent", "ExtractRelevantNewsAgent")
    builder.add_edge("ExtractRelevantNewsAgent", END)

    graph = builder.compile()
    data = graph.invoke({})

    global_state["geo_news_data"] = data["summary"]

    return global_state
