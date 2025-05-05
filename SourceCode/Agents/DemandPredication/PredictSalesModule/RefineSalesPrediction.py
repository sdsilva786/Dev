import pandas as pd
import numpy as np


def mape(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / np.maximum(1, y_true))) * 100


def should_retrain_model(forecast_df, actual_df, threshold):
    df_compare = pd.merge(forecast_df[['ds', 'yhat']], actual_df[['ds', 'y']], on='ds', how='inner')
    if df_compare.empty:
        return False
    error = mape(df_compare['y'], df_compare['yhat'])
    # print(f"MAPE: {error:.2f}%")
    return error > threshold


def Is_Model_ReTraining_Required(df_forecast_sales, df_actual_sales, retrain_threshold):
    Re_forecast_required = False

    df_actual_sales['date'] = pd.to_datetime(df_actual_sales['date'])
    df_actual_sales['date'] = df_actual_sales['date'].dt.strftime('%d-%m-%Y') # check this format
    actual_dates = df_actual_sales["date"].unique()

    filtered_prev_forecast_df = df_forecast_sales[df_forecast_sales["ds"].isin(actual_dates)]
    print(filtered_prev_forecast_df)
    for (part, warehouse, region), group_df in filtered_prev_forecast_df.groupby(["part_name", "warehouse", "region"]):
        ts_df = group_df[["ds", "yhat"]].copy()

        actual_df = df_actual_sales.query(
            "part_name == @part and warehouse == @warehouse and region == @region"
        )[["date", "quantity_sold"]].rename(columns={"date": "ds", "quantity_sold": "y"})

        Re_forecast_required = should_retrain_model(ts_df, actual_df, threshold=retrain_threshold)
        if Re_forecast_required:
            break

    return Re_forecast_required
