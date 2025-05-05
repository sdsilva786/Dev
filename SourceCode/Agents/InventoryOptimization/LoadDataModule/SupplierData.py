import pandas as pd
import os
from SourceCode.Utilities.ConfigHelper import ReadAppConfigHelper as CH


def get_Data() -> pd.DataFrame:
    relative_path = CH.get_config("supplier_master_data")
    file_path = os.path.abspath(relative_path)
    df_supplier_data = pd.read_csv(file_path)

    return df_supplier_data
