from agents import Agent, Runner, RunConfig, function_tool, ModelSettings
import requests
import json

@function_tool
def get_weather_tool(latitude: float, longitude: float):
    """
    Retrieves weather data from the Open-Meteo API.

    Args:
        latitude (number): The latitude of the location.
        longitude (number): The longitude of the location.

    Returns:
        object: The weather data.
    """
    assert isinstance(latitude, (int, float)), "Latitude must be a number"
    assert isinstance(longitude, (int, float)), "Longitude must be a number"

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m",
        "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m,precipitation"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()  

    return response.json()

agent_landmarks = Agent(name="Landmarks Agent", instructions="You can provide information about landmarks in a location.", tools=[{ type: "web_search_preview" }])
agent_weather = Agent(name="Weather Agent", instructions="You can provide the current weather when prompted for weather in a location.",tools=[get_weather_tool])
triage_agent = Agent(name="Triage Agent", instructions="Route the user to the appropriate agent based on the user's request.", handoffs=[agent_weather,agent_landmarks])

result = Runner.run_sync(triage_agent, "Which city is currently the warmest? Melbourne, Chicago, Oslo, Dublin, or Shanghai? Will I need an umbrella in this city in the next few days? Finally given this city, can you suggest a famous landmark for me to visit in that city, and suggest the most appropriate public transport to use?")
print(result.final_output)
