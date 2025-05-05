import sys
import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from retry import retry
import httpx

# Dev setting
http_client = httpx.Client(verify=False)

load_dotenv()

az_openai_api_key = os.getenv("AZURE_OPENAI_API_KEY")
openai_api_type = os.getenv("OPENAI_API_TYPE")
az_openai_api_base_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
openai_api_key = os.getenv("AZURE_OPENAI_API_KEY")
openai_api_version = os.getenv("OPENAI_API_VERSION")
deployment_id = os.getenv("DEPLOYMENT_NAME")
az_temperature = os.getenv("AZURE_MODEL_TEMPERATURE")


def Get_Instance():
    llm = AzureChatOpenAI(
        model_name=deployment_id,
        openai_api_key=openai_api_key,
        temperature=az_temperature, http_client=http_client)

    return llm


@retry(tries=3, delay=2, backoff=2, exceptions=(TimeoutError, Exception))
def Get_Response(prompt):
    llm = Get_Instance()
    out_text = llm.invoke(prompt)
    response = out_text.content
    return response
