from SourceCode.Agents.DemandPredication.DTO.DemandPredictionState import InternalDemandPredictionState
from SourceCode.Agents.DemandPredication.PredictSalesModule import TimeSeriesSalesPrediction as SP
from SourceCode.Agents.DemandPredication.DTO import InputSalePredication
from sklearn.preprocessing import LabelEncoder
from langgraph.graph import StateGraph
from SourceCode.DataPersistence.Folder import SaveData
from SourceCode.Agents.DemandPredication.PredictSalesModule import RefineSalesPrediction
import os
from SourceCode.Utilities.ConfigHelper import ReadAppConfigHelper as CH
import pandas as pd


def RefineDemandForecastAgent(state: InternalDemandPredictionState) -> InternalDemandPredictionState:
    relative_path = CH.get_config("real_time_sales_data")
    file_path = os.path.abspath(relative_path)
    actual_df = pd.read_csv(file_path, parse_dates=["date"])
    actual_df.dropna(inplace=True)
    actual_df.reset_index(drop=True, inplace=True)

    file_path = state["demand_predict_path"]
    state["demand_prediction_model_refine"] = False
    if file_path is not None or file_path != "":
        df_forecast_sales = pd.read_csv(file_path, parse_dates=["ds"])
        df_forecast_sales.dropna(inplace=True)
        df_forecast_sales.reset_index(drop=True, inplace=True)

        retrain_threshold = CH.get_config("RETRAIN_THRESHOLD")
        Re_forecast_required = RefineSalesPrediction.Is_Model_ReTraining_Required(df_forecast_sales, actual_df, retrain_threshold)

        if Re_forecast_required:
            df_weather = state["weather_forecast"]
            df_fuel_price = state["fuel_price_region"]
            df_market_sentiments = state["market_sentiments"]

            relative_path = CH.get_config("demand_predication_sale_data")
            file_path = os.path.abspath(relative_path)
            df_historical_sales = pd.read_csv(file_path, parse_dates=["date"])
            df_historical_sales.dropna(inplace=True)
            df_historical_sales.reset_index(drop=True, inplace=True)

            sentiment_map = {'neutral': 0, 'good': 1, 'bad': -1}
            df_historical_sales['market_sentiment'] = df_historical_sales['market_sentiment'].map(sentiment_map)

            weather_encoder = LabelEncoder()
            df_historical_sales['weather_encoded'] = weather_encoder.fit_transform(df_historical_sales['weather'])

            df_historical_sales = pd.concat([df_historical_sales, actual_df], ignore_index=True)
            df_weather['weather_encoded'] = weather_encoder.fit_transform(df_weather['WeatherForecast'])

            input_data = InputSalePredication.InputSalesPredication(weather_forecast=df_weather, fuel_price=df_fuel_price,
                                                                    market_sentiments=df_market_sentiments,
                                                                    upcoming_promotion_event=False,
                                                                    historical_sales=df_historical_sales)

            df_sale_predict = SP.TimeSeriesPrediction(input_data).predict()
            output_path = SaveData.Demand_Prediction(df_sale_predict)
            state["demand_predict_path"] = output_path
            state["demand_prediction_model_refine"] = True

    return state
