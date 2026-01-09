import logging
from livekit.agents import function_tool, RunContext
import requests
from langchain_community.tools import DuckDuckGoSearchRun

@function_tool()
async def get_weather(
        context: RunContext,
        city: str) -> str:
    """get the current weather for a given city"""
    try:
        response = requests.get(
            f"https://wttr.in/{city}?format=3")
        if response.status_code == 200:
            logging.info(f"Weather data retrieved for {city}: {response.text.strip()}")
            return response.text.strip()
        else:
            logging.error(f"failed to get weather for {city} : {response.status_code}")
            return f"Could not retrieve weather for {city}."    
    except Exception as e:
        logging.error(f"Error retrieving weather for {city}: {e}")
        return f"An error occured while retrieving weather for {city}"   
    
@function_tool()
async def search_web(
    context: RunContext,  # type: ignore
    query: str) -> str:
    """
    Search the web using DuckDuckGo.
    """
    try:
        results = DuckDuckGoSearchRun().run(tool_input=query)
        logging.info(f"Search results for '{query}': {results}")
        return results
    except Exception as e:
        logging.error(f"Error searching the web for '{query}': {e}")
        return f"An error occurred while searching the web for '{query}'."  
           
        