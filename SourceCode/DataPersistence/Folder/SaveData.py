from SourceCode.Utilities.ConfigHelper import ReadAppConfigHelper as CH
import pandas as pd
import os
import uuid


def Demand_Prediction(df_sale_predict: pd.DataFrame):
    base_path = CH.get_config("output_base_path")
    uid = str(uuid.uuid4())
    filename = uid[-4:]
    file_path = os.path.abspath(base_path + "Demand_Prediction/" + "demand_forecast_" + filename + ".csv")
    df_sale_predict.to_csv(file_path)

    return file_path


def Customer_Segmentation(df_customer_segment: pd.DataFrame):
    base_path = CH.get_config("output_base_path")
    uid = str(uuid.uuid4())
    filename = uid[-4:]
    file_path = os.path.abspath(base_path + "Segmentation/" + "customer_segmentation_" + filename + ".csv")
    df_customer_segment.to_csv(file_path)

    return file_path


def Purchase_Behavior_Segmentation(df_segment_by_purchase_behavior: pd.DataFrame):
    base_path = CH.get_config("output_base_path")
    uid = str(uuid.uuid4())
    filename = uid[-4:]
    file_path = os.path.abspath(base_path + "Segmentation/" + "Purchase_Behavior_Segmentation_" + filename + ".csv")
    df_segment_by_purchase_behavior.to_csv(file_path)

    return file_path


def segment_by_part_preference(df_segment_by_part_preference: pd.DataFrame):
    base_path = CH.get_config("output_base_path")
    uid = str(uuid.uuid4())
    filename = uid[-4:]
    file_path = os.path.abspath(base_path + "Segmentation/" + "Part_Preference_Segmentation_" + filename + ".csv")
    df_segment_by_part_preference.to_csv(file_path)

    return file_path
