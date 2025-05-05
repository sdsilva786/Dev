# Historical Sales data, Economic Indicators : Fuel Prices, Market Trends : market sentiment, Segment customers : 3, Region : 4

import pandas as pd
from prophet import Prophet


class TimeSeriesPrediction:
    def __init__(self, input_sale_predication_data):
        self.input_data = input_sale_predication_data

    def predict(self) -> pd.DataFrame:
        results = []
        final_forecast = pd.DataFrame()
        df_historical_sales = self.input_data.historical_sales
        for (part, warehouse, region), group_df in df_historical_sales.groupby(["part_name", "warehouse", "region"]):
            ts_df = group_df[["date", "quantity_sold", "fuel_price", "promotion_event", "market_sentiment",
                              "weather_encoded"]].copy()
            ts_df.rename(columns={"date": "ds", "quantity_sold": "y"}, inplace=True)

            # Prophet model
            model = Prophet()
            model.add_regressor("fuel_price")
            model.add_regressor("promotion_event")
            model.add_regressor('market_sentiment')
            model.add_regressor('weather_encoded')

            model = Prophet(weekly_seasonality=True, yearly_seasonality=True)
            model.fit(ts_df)

            future = model.make_future_dataframe(periods=30)
            fuel_price = self.__get_fuel_price(region)
            if fuel_price is None:
                fuel_price = ts_df["fuel_price"].iloc[-1]

            future["fuel_price"] = fuel_price
            if self.input_data.upcoming_promotion_event:
                future["promotion_event"] = 1
            else:
                future["promotion_event"] = 0

            future["market_sentiment"] = self.__get_market_sentiment(part, region)

            weather_forecast = self.__get_weather_forecast(region)
            if weather_forecast is None:
                weather_forecast = ts_df["weather_encoded"].iloc[-1]

            future["weather_encoded"] = weather_forecast
            forecast = model.predict(future)

            future_forecast = forecast[forecast['ds'] > ts_df['ds'].max()].copy()
            future_forecast["yhat"] = future_forecast["yhat"].round()

            forecast_output = future_forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].copy()
            forecast_output["part_name"] = part
            forecast_output["warehouse"] = warehouse
            forecast_output["region"] = region
            results.append(forecast_output)
            del model

        final_forecast = pd.concat(results, ignore_index=True)
        return final_forecast

    def __get_market_sentiment(self, part_name: str, region: str) -> int:
        sentiment_value = 0
        df_market_sentiments = self.input_data.market_sentiments
        filtered_df = df_market_sentiments[
            (df_market_sentiments['sparepart'] == part_name) & (df_market_sentiments['region'] == region)]
        if len(filtered_df) > 0:
            sentiment_value = filtered_df['market_sentiment'].iloc[0]

        return sentiment_value

    def __get_fuel_price(self, region: str) -> float:
        fuel_price = None
        df_fuel_price = self.input_data.fuel_price
        filtered_df = df_fuel_price[
            (df_fuel_price['region'] == region)]
        if len(filtered_df) > 0:
            fuel_price = filtered_df['FuelPrice'].iloc[0]

        return fuel_price

    def __get_weather_forecast(self, region: str) -> str:
        weather_forecast = None
        df_weather_forecast = self.input_data.weather_forecast
        filtered_df = df_weather_forecast[
            (df_weather_forecast['region'] == region)]
        if len(filtered_df) > 0:
            weather_forecast = filtered_df['WeatherForecast'].iloc[0]

        return weather_forecast
