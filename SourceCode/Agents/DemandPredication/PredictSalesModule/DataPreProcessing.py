import pandas as pd
import os
from SourceCode.Utilities.ConfigHelper import ReadAppConfigHelper as CH
from sklearn.preprocessing import LabelEncoder


def DataPreprocessor() -> pd.DataFrame:
    relative_path = CH.get_config("demand_predication_sale_data")
    file_path = os.path.abspath(relative_path)
    df_historical_sales = pd.read_csv(file_path, parse_dates=["date"])
    df_historical_sales.dropna(inplace=True)
    df_historical_sales.reset_index(drop=True, inplace=True)

    sentiment_map = {'neutral': 0, 'good': 1, 'bad': -1}
    df_historical_sales['market_sentiment'] = df_historical_sales['market_sentiment'].map(sentiment_map)

    weather_encoder = LabelEncoder()
    df_historical_sales['weather_encoded'] = weather_encoder.fit_transform(df_historical_sales['weather'])

    return df_historical_sales
