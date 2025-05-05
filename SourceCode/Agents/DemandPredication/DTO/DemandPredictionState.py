from typing import Optional, TypedDict
import pandas as pd


class InternalDemandPredictionState(TypedDict):
    weather_forecast: Optional[pd.DataFrame]
    fuel_price_region: Optional[pd.DataFrame]
    market_sentiments: Optional[pd.DataFrame]
    historical_sales: Optional[pd.DataFrame]
    demand_predict_path: Optional[str]
    customer_segmentation_path: Optional[str]
    segment_by_purchase_behavior_path: Optional[str]
    segment_by_part_preference_path: Optional[str]
    demand_prediction_model_refine: Optional[bool]
