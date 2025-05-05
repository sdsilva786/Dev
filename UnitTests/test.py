from SourceCode.Agents.DemandPredication.ProcessModule import ProcessDemandPredication
from SourceCode.Utilities.ConfigHelper import ReadAppConfigHelper as CH
# # Initialize the LabelEncoder
# weather_encoder = LabelEncoder()
#
# # Define the weather categories
# weather_categories = ["Hot", "Cold", "Cool", "Mild", "Warm", "Rainy"]
#
# # Fit the encoder with the weather categories
# weather_encoder.fit(weather_categories)
#
# # Encode the weather forecast
# weather_forecast = "Cold"
# encoded_weather = weather_encoder.transform([weather_forecast])
#
# print(f"The encoded value for '{weather_forecast}' is: {encoded_weather[0]}")

#ProcessDemandPredication.process_request()
import pandas as pd
from datetime import timedelta
import os
# Load your historical sales data

relative_path = CH.get_config("demand_predication_sale_data")
file_path = os.path.abspath(relative_path)
sales_data = pd.read_csv(file_path, parse_dates=["date"])
sales_data.dropna(inplace=True)
sales_data.reset_index(drop=True, inplace=True)


# Assume today is just 1 day after the max date in dataset
historical_max_date = sales_data['date'].max()
simulated_today = historical_max_date + timedelta(days=1)

print(f"Simulated today: {simulated_today.date()}")

# Generate "real-time" sales for today
# Let's simulate sales by copying yesterday's sales with some randomness
yesterday_sales = sales_data[sales_data['date'] == historical_max_date]

# Introduce some variation (5%-20%)
import numpy as np
variation = np.random.uniform(0.95, 1.2, size=len(yesterday_sales))
yesterday_sales['quantity_sold'] = (yesterday_sales['quantity_sold'] * variation).round().astype(int)
yesterday_sales['quantity_sold'] = yesterday_sales['quantity_sold'].clip(lower=0)  # No negative sales

# Update date to today
yesterday_sales['date'] = simulated_today

# This is your real-time new sales data for today
real_time_latest_sales = yesterday_sales.copy()
real_time_latest_sales.to_csv('C:/Mywork/CAMS/Auto_Supply_Chain_Agents/output.csv', index=False)

real_time_latest_sales.head(10)  # Display sample

