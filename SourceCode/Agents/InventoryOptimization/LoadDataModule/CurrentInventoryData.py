import pandas as pd
import os
from SourceCode.Utilities.ConfigHelper import ReadAppConfigHelper as CH


def get_Data() -> pd.DataFrame:
    relative_path = CH.get_config("real_time_inventory_data")
    file_path = os.path.abspath(relative_path)
    df_current_data = pd.read_csv(file_path)

    return df_current_data
