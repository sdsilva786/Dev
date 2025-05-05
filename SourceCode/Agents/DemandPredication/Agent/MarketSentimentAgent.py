from SourceCode.Agents.DemandPredication.ExternalDataModule import FetchSocialMediaTrends
from SourceCode.Agents.DemandPredication.DTO.DemandPredictionState import InternalDemandPredictionState
from langgraph.graph import StateGraph


def MarketSentimentAgent(state: InternalDemandPredictionState) -> InternalDemandPredictionState:
    df_market_sentiments = FetchSocialMediaTrends.get_market_sentiments()
    state["market_sentiments"] = df_market_sentiments
    return state
