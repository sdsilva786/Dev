
from SourceCode.Agents.DemandPredication.ExternalDataModule import FetchEconomicIndicator
import pandas as pd
from SourceCode.GenAIModel import AzureOpenAI
from SourceCode.Utilities.ConfigHelper import ReadAppConfigHelper as CH
from langchain.prompts import PromptTemplate
import xml.etree.ElementTree as ET
import json
import time
import os


def get_weather_forecast_all() -> pd.DataFrame:
    relative_path = CH.get_config("master_wh_data")
    file_path = os.path.abspath(relative_path)
    df_region = pd.read_csv(file_path)

    df_region['WeatherForecast'] = None

    template_with_docs = """You are Expert in Extracting Weather Forecast data from the provided content.\n 
    Follow below Instructions:\n
    1) Accuracy is paramount, and your expertise lies in extracting the Weather Forecast data.\n
    2) Extract the weather forecast data and classify it using only one of the following categories: Hot, Cold, Cool, Mild, Warm, or Rainy. \n 
    3) If no data of weather forecast is found then set weather forecast value to "Warm".\n
    Instructions for Answer Formatting:\n
        1) Provide the output in the following XML format:\n <xml><WeatherForecast></WeatherForecast></xml> \n
          Ensure consistency and accuracy while populating the fields with relevant content.\n
        2) Always generate a complete and well-formatted XML output strictly adhering to the provided format. Ensure all required tags are present, properly nested, and structured according to the defined schema. \n
        Validate that the XML is syntactically correct and includes all necessary information based on the input context. \n
        3) Generate XML output without including the "```xml".\n

    {context}
    """
    for index, row in df_region.iterrows():
        response_data = FetchEconomicIndicator.get_weather_forecast(row['region'])
        content = ""
        if response_data is not None:
            results = response_data['results']
            for result in results:
                content = content + " " + result['content']

            prompt_template = PromptTemplate(template=template_with_docs)
            formatted_prompt = prompt_template.format(context=content)

            response = AzureOpenAI.Get_Response(formatted_prompt)
            root = ET.fromstring(response)
            weather_forecast = root.find('WeatherForecast').text
            df_region.at[index, 'WeatherForecast'] = weather_forecast
            time.sleep(10)

    return df_region
