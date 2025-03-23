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
    
def set_reminder(text):
    """ Save a reminder to a local file """
    path = "src/data/reminders.txt"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a") as file:
        file.write(text + "\n")
    return f"Reminder saved: {text}"

def get_reminders():
    """ Retrieve saved reminders """
    path = "src/data/reminders.txt"
    if not os.path.exists(path):
        return "No reminders set."

    with open(path, "r") as file:
        lines = file.readlines()

    if not lines:
        return "No reminders found."
    return "Your Reminders:\n" + "".join(f"- {line}" for line in lines)

def search_file(filename, search_path="C:/"):
    """Search for a file with the given name across the system"""
    matches = []
    for root, dirs, files in os.walk(search_path):
        if "$Recycle.Bin" in root:
            continue  # skip system folder
        if filename in files:
            matches.append(os.path.join(root, filename))
    
    if matches:
        return "Found:\n" + "\n".join(matches)
    else:
        return f"File '{filename}' not found in {search_path}"


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
    
    if command.startswith("reminder add"):
        text = command.replace("reminder add", "").strip()
        return set_reminder(text)

    if command == "reminder view":
        return get_reminders()
    
    if command.startswith("search file"):
        filename = command.replace("search file", "").strip()
        return search_file(filename)
    return "I'm not sure how to respond to that."
