import pandas as pd
import os
from SourceCode.Utilities.ConfigHelper import ReadAppConfigHelper as CH


def get_Data() -> pd.DataFrame:
    relative_path = CH.get_config("inventory_history_data")
    file_path = os.path.abspath(relative_path)
    df_historical_data = pd.read_csv(file_path)

    return df_historical_data
