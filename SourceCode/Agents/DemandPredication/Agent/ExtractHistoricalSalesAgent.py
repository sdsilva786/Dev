from SourceCode.Agents.DemandPredication.PredictSalesModule import DataPreProcessing
from SourceCode.Agents.DemandPredication.DTO.DemandPredictionState import InternalDemandPredictionState
from langgraph.graph import StateGraph


def ExtractHistoricalSalesAgent(state: InternalDemandPredictionState) -> InternalDemandPredictionState:
    historical_sales_df = DataPreProcessing.DataPreprocessor()
    state["historical_sales"] = historical_sales_df
    return state
