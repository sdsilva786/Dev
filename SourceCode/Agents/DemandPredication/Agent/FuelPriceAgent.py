from SourceCode.Agents.DemandPredication.ExternalDataModule import ExtractFuelPrice
from SourceCode.Agents.DemandPredication.DTO.DemandPredictionState import InternalDemandPredictionState
from langgraph.graph import StateGraph


def FuelPriceAgent(state: InternalDemandPredictionState) -> InternalDemandPredictionState:
    df_fuel_price = ExtractFuelPrice.get_fuel_price_all()
    state["fuel_price_region"] = df_fuel_price
    return state
