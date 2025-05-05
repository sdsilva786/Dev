from typing import Optional, TypedDict
import pandas as pd


class GlobalState(TypedDict):
    demand_predict_path: Optional[str]
    segment_by_purchase_behavior_path: Optional[str]
    segment_by_part_preference_path: Optional[str]
    customer_segmentation_path: Optional[str]
    demand_prediction_model_refine: Optional[bool]
    geo_news_data: Optional[str]
