import pandas as pd
import os
from SourceCode.Utilities.ConfigHelper import ReadAppConfigHelper as CH
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from datetime import datetime, timedelta


def get_segment():
    relative_path = CH.get_config("demand_predication_sale_data")
    file_path = os.path.abspath(relative_path)
    df_historical_sales = pd.read_csv(file_path, parse_dates=["date"])
    df_historical_sales.dropna(inplace=True)
    df_historical_sales.reset_index(drop=True, inplace=True)

    latest_date = df_historical_sales['date'].max()
    six_months_ago = latest_date - timedelta(days=180)

    sales_data_last_6_months = df_historical_sales[df_historical_sales['date'] >= six_months_ago]
    df_customer_segment = segment_by_customer_type(sales_data_last_6_months)
    df_segment_by_purchase_behavior = segment_by_purchase_behavior(sales_data_last_6_months)
    df_segment_by_part_preference = segment_by_part_preference(sales_data_last_6_months)

    return df_customer_segment, df_segment_by_purchase_behavior, df_segment_by_part_preference


def segment_by_customer_type(df_sales):
    segment_analysis = df_sales.groupby('customer_segment').agg(
        total_orders=('quantity_sold', 'count'),
        total_quantity=('quantity_sold', 'sum'),
        avg_order_size=('quantity_sold', 'mean'),
        order_frequency=('date', lambda x: x.nunique())
    ).reset_index()

    return segment_analysis


def segment_by_purchase_behavior(df_sales):
    behavior_features = df_sales.groupby('customer_segment').agg(
        order_frequency=('date', 'nunique'),
        avg_order_size=('quantity_sold', 'mean')
    ).reset_index()

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(behavior_features[['order_frequency', 'avg_order_size']])

    kmeans = KMeans(n_clusters=2, random_state=42)
    behavior_features['cluster'] = kmeans.fit_predict(scaled_features)

    return behavior_features


def segment_by_part_preference(df_sales):
    part_matrix = df_sales.pivot_table(
        index='customer_segment',
        columns='part_name',
        values='quantity_sold',
        aggfunc='sum',
        fill_value=0
    )
    scaler = StandardScaler()
    scaled_parts = scaler.fit_transform(part_matrix)

    kmeans = KMeans(n_clusters=3, random_state=42)
    part_matrix['cluster'] = kmeans.fit_predict(scaled_parts)

    return part_matrix
