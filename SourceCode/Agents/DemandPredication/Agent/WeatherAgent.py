from SourceCode.Agents.DemandPredication.ExternalDataModule import ExtractWeatherForecast
from SourceCode.Agents.DemandPredication.DTO.DemandPredictionState import InternalDemandPredictionState
from langgraph.graph import StateGraph


def WeatherAgent(state: InternalDemandPredictionState) -> InternalDemandPredictionState:
    df_weather_forecast = ExtractWeatherForecast.get_weather_forecast_all()
    state["weather_forecast"] = df_weather_forecast
    return state
