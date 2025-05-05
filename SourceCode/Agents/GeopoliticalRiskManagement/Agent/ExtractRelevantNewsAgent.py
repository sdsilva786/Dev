from SourceCode.Agents.GeopoliticalRiskManagement.DTO import NewsAgentState
from SourceCode.Agents.GeopoliticalRiskManagement.NewsModule import IdentifyRelevantNews
from langgraph.graph import StateGraph


def ExtractRelevantNewsAgent(state: NewsAgentState) -> NewsAgentState:
    news_data = state['news_text']
    relevant_news_data = IdentifyRelevantNews.GetRelevantNews(news_data)
    state["summary"] = relevant_news_data

    return state
