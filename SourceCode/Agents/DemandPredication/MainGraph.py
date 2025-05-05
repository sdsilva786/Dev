from langgraph.graph import StateGraph, START, END
from SourceCode.Agents.DemandPredication.DTO.DemandPredictionState import InternalDemandPredictionState

from SourceCode.Agents.DemandPredication.Agent import WeatherAgent, FuelPriceAgent, MarketSentimentAgent, \
    ExtractHistoricalSalesAgent, DemandForecastAgent, SegmentCustomerAgent, RefineDemandForecastAgent

from SourceCode.Agents.StateTypes.GlobalState import GlobalState


def run(global_state: GlobalState) -> GlobalState:
    builder = StateGraph(InternalDemandPredictionState)
    builder.add_node("WeatherAgent", WeatherAgent.WeatherAgent)
    builder.add_node("FuelPriceAgent", FuelPriceAgent.FuelPriceAgent)
    builder.add_node("MarketSentimentAgent", MarketSentimentAgent.MarketSentimentAgent)
    builder.add_node("ExtractHistoricalSalesAgent", ExtractHistoricalSalesAgent.ExtractHistoricalSalesAgent)
    builder.add_node("DemandForecastAgent", DemandForecastAgent.DemandForecastAgent)
    builder.add_node("SegmentCustomerAgent", SegmentCustomerAgent.SegmentCustomerAgent)
    builder.add_node("RefineDemandForecastAgent", RefineDemandForecastAgent.RefineDemandForecastAgent)

    # builder.set_entry_point("WeatherAgent")
    builder.add_edge(START, "WeatherAgent")
    builder.add_edge("WeatherAgent", "FuelPriceAgent")
    builder.add_edge("FuelPriceAgent", "MarketSentimentAgent")
    builder.add_edge("MarketSentimentAgent", "ExtractHistoricalSalesAgent")
    builder.add_edge("ExtractHistoricalSalesAgent", "DemandForecastAgent")
    builder.add_edge("DemandForecastAgent", "SegmentCustomerAgent")
    builder.add_edge("SegmentCustomerAgent", "RefineDemandForecastAgent")
    builder.add_edge("RefineDemandForecastAgent", END)

    graph = builder.compile()
    data = graph.invoke({})
    global_state["demand_predict_path"] = data["demand_predict_path"]
    global_state["segment_by_purchase_behavior_path"] = data["segment_by_purchase_behavior"]
    global_state["segment_by_part_preference_path"] = data["segment_by_part_preference"]
    global_state["customer_segmentation_path"] = data["customer_segmentation_path"]
    global_state["demand_prediction_model_refine"] = data["demand_prediction_model_refine"]

    return global_state
