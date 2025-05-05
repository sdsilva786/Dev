from SourceCode.Agents.GeopoliticalRiskManagement.DTO import NewsAgentState
from SourceCode.Agents.GeopoliticalRiskManagement.NewsModule import FetchNews
from langgraph.graph import StateGraph


def FetchNewsAgent(state: NewsAgentState) -> NewsAgentState:
    news_data = FetchNews.FetchNews()
    state["news_text"] = news_data

    return state
