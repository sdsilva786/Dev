import pandas as pd


class InputSalesPredication:
    def __init__(self, upcoming_promotion_event: bool, weather_forecast: pd.DataFrame, fuel_price: pd.DataFrame,
                 market_sentiments: pd.DataFrame, historical_sales: pd.DataFrame):
        self.upcoming_promotion_event = upcoming_promotion_event
        self.market_sentiments = market_sentiments
        self.weather_forecast = weather_forecast
        self.fuel_price = fuel_price
        self.historical_sales = historical_sales
