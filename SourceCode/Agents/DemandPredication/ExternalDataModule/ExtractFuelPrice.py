from SourceCode.Agents.DemandPredication.ExternalDataModule import FetchEconomicIndicator
import pandas as pd
from SourceCode.GenAIModel import AzureOpenAI
from SourceCode.Utilities.ConfigHelper import ReadAppConfigHelper as CH
from langchain.prompts import PromptTemplate
import xml.etree.ElementTree as ET
import json
import time
import os


def get_fuel_price_all() -> pd.DataFrame:
    relative_path = CH.get_config("master_wh_data")
    file_path = os.path.abspath(relative_path)
    df_region = pd.read_csv(file_path)

    df_region['FuelPrice'] = None

    template_with_docs = """You are Expert in Extracting Fuel Price from the provided content.\n 
    Follow below Instructions:\n
    1) Accuracy is paramount, and your expertise lies in extracting the fuel price.\n
    2) Exclude currency symbol and "per gallon" from fuel price
    Instructions for Answer Formatting:\n
        1) Provide the output in the following XML format:\n <xml><FuelPrice></FuelPrice></xml> \n
          Ensure consistency and accuracy while populating the fields with relevant content.\n
        2) Always generate a complete and well-formatted XML output strictly adhering to the provided format. Ensure all required tags are present, properly nested, and structured according to the defined schema. \n
        Validate that the XML is syntactically correct and includes all necessary information based on the input context. \n
        3) Generate XML output without including the "```xml".\n
    
    {context}
    """
    for index, row in df_region.iterrows():
        response_data = FetchEconomicIndicator.get_fuel_price(row['region'])
        content = ""
        if response_data is not None:
            results = response_data['results']
            for result in results:
                content = content + " " + result['content']

            prompt_template = PromptTemplate(template=template_with_docs)
            formatted_prompt = prompt_template.format(context=content)

            response = AzureOpenAI.Get_Response(formatted_prompt)
            root = ET.fromstring(response)
            fuel_price = root.find('FuelPrice').text
            df_region.at[index, 'FuelPrice'] = float(str(fuel_price).strip())
            time.sleep(10)

    return df_region
