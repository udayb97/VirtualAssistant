import requests
import json
import os

# Load configuration settings (e.g., API keys)
CONFIG_FILE = "src/data/config.json"

def load_config():
    """ Load API keys and settings from config.json """
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    return {}

config = load_config()

# Function to fetch weather details
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

# Function to save a reminder
def set_reminder(text):
    """ Save a reminder to a local file """
    with open("src/data/reminders.txt", "a") as file:
        file.write(text + "\n")
    return f"Reminder set: {text}"

# Function to view saved reminders
def get_reminders():
    """ Retrieve saved reminders """
    if not os.path.exists("src/data/reminders.txt"):
        return "No reminders set."

    with open("src/data/reminders.txt", "r") as file:
        reminders = file.readlines()
    
    return "Your Reminders:\n" + "".join(reminders) if reminders else "No reminders set."

# Function to search for a file
def search_file(filename, directory="C:/Users"):
    """ Search for a file in the given directory and subdirectories """
    for root, _, files in os.walk(directory):
        if filename in files:
            return f"File found: {os.path.join(root, filename)}"
    return "File not found."

# Command processing
def process_command(command):
    """ Process user commands and call appropriate functions """
    command = command.lower().strip()

    if command.startswith("weather"):
        city = command.replace("weather", "").strip()
        city = city if city else "New York"  # Default city
        return get_weather(city)

    elif command.startswith("reminder add"):
        reminder_text = command.replace("reminder add", "").strip()
        return set_reminder(reminder_text)

    elif command == "reminder view":
        return get_reminders()

    elif command.startswith("search file"):
        filename = command.replace("search file", "").strip()
        return search_file(filename)

    else:
        return "I'm not sure how to respond to that."
