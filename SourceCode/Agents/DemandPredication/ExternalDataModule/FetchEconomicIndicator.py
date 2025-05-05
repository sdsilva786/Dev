# Get Fuel price
# Get Weather Conditions
from tavily import TavilyClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()


def get_fuel_price(region: str)->dict:
    """Fetch the current fuel price in the US."""
    tavily_api_key = os.getenv("TAVILY_API_KEY")
    if not tavily_api_key:
        raise ValueError("TAVILY_API_KEY not found in environment variables")

    client = TavilyClient(tavily_api_key)
    try:
        response = client.search(
            query=f"provide current fuel price in US {region} region",
            topic="finance",
            search_depth="advanced",
            max_results=3
        )
    except Exception as e:
        print(f"Error fetching fuel price: {e}")
        return None

    return response


def get_weather_forecast(region: str)->dict:
    """Fetch the weather forecast for a specific region in the US for the next 3 days."""
    tavily_api_key = os.getenv("TAVILY_API_KEY")
    if not tavily_api_key:
        raise ValueError("TAVILY_API_KEY not found in environment variables")

    client = TavilyClient(tavily_api_key)
    try:
        response = client.search(
            query=f"provide weather forecast in US {region} region for next 3 days",
            search_depth="advanced",
            max_results=3
        )
    except Exception as e:
        print(f"Error fetching weather forecast: {e}")
        return None

    return response
