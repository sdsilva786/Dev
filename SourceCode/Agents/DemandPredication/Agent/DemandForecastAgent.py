from SourceCode.Agents.DemandPredication.DTO.DemandPredictionState import InternalDemandPredictionState
from SourceCode.Agents.DemandPredication.PredictSalesModule import TimeSeriesSalesPrediction as SP
from SourceCode.Agents.DemandPredication.DTO import InputSalePredication
from sklearn.preprocessing import LabelEncoder
from langgraph.graph import StateGraph
from SourceCode.DataPersistence.Folder import SaveData


def DemandForecastAgent(state: InternalDemandPredictionState) -> InternalDemandPredictionState:
    df_weather = state["weather_forecast"]
    df_fuel_price = state["fuel_price_region"]
    df_market_sentiments = state["market_sentiments"]
    df_historical_sales = state["historical_sales"]

    weather_encoder = LabelEncoder()
    df_weather['weather_encoded'] = weather_encoder.fit_transform(df_weather['WeatherForecast'])

    input_data = InputSalePredication.InputSalesPredication(weather_forecast=df_weather, fuel_price=df_fuel_price,
                                                            market_sentiments=df_market_sentiments,
                                                            upcoming_promotion_event=False,
                                                            historical_sales=df_historical_sales)

    df_sale_predict = SP.TimeSeriesPrediction(input_data).predict()
    output_path = SaveData.Demand_Prediction(df_sale_predict)
    state["demand_predict_path"] = output_path

    return state
