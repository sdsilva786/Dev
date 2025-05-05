# Get Market Sentiment about overall spare parts
import pandas as pd
import os
from SourceCode.Utilities.ConfigHelper import ReadAppConfigHelper as CH


def get_market_sentiments() -> pd.DataFrame:
    relative_path = CH.get_config("social_media_data")
    file_path = os.path.abspath(relative_path)
    df_market_sentiments = pd.read_csv(file_path)

    sentiment_map = {'neutral': 0, 'good': 1, 'bad': -1}
    df_market_sentiments['market_sentiment'] = df_market_sentiments['market_sentiment'].map(sentiment_map)
    return df_market_sentiments
