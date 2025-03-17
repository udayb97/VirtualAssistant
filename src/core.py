import requests
import json
import os
from src.conversation import get_conversational_response 

# Load configuration settings (e.g., API keys)
CONFIG_FILE = "src/data/config.json"

def load_config():
    """ Load API keys and settings from config.json """
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    return {}

config = load_config()

def get_weather(city="New York"):
    """ Fetch current weather for a given city using OpenWeatherMap API """
    api_key = config.get("weather_api_key", "")
    if not api_key:
        return "Weather API key missing. Please set it in config.json."

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            return f"Error: {data['message']}"

        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        return f"Weather in {city}: {temp}°C, {weather_desc.capitalize()}"

    except Exception as e:
        return f"Error fetching weather: {e}"

def get_news():
    """ Fetch latest news headlines using News API """
    api_key = config.get("news_api_key", "")
    if not api_key:
        return "News API key missing. Please set it in config.json."

    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    try:
        response = requests.get(url)
        data = response.json()

        if data["status"] != "ok":
            return f"Error: {data['message']}"

        headlines = [f"{i+1}. {article['title']}" for i, article in enumerate(data["articles"][:5])]
        return "Top News Headlines:\n" + "\n".join(headlines)

    except Exception as e:
        return f"Error fetching news: {e}"


# Process user commands
def process_command(command):
    """ Process user commands and call appropriate functions """
    command = command.lower().strip()

    # Check if it's a conversational command
    response = get_conversational_response(command)
    if response:
        return response 

    # Handle API-powered responses
    if "weather" in command:
        return get_weather("New York") 

    if "news" in command:
        return get_news()

    return "I'm not sure how to respond to that."
