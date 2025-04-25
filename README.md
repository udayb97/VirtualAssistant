# J.A.R.V.I.S. – Your Personal Virtual Assistant

## Description
J.A.R.V.I.S. is a Python-based AI virtual assistant designed to simplify everyday tasks such as setting reminders, checking the weather, fetching news, searching for files, and answering basic conversational queries.

## Purpose
The purpose of this project is to demonstrate the integration of Python programming concepts with APIs, file I/O, and GUI development to create an intelligent desktop assistant.

## Value
- Saves time by automating common daily tasks.
- Enhances productivity through a clean and interactive interface.
- Demonstrates advanced Python skills including system integration, modular design, and GUI handling.

## APIs Used
- **OpenWeatherMap API** – For real-time weather updates
- **NewsAPI** – For fetching top news headlines

> API keys need to be inserted in `src/data/config.json` for these services to work.

## 🧠 AI Features
- GPT4All integration with the **Phi-3 Mini Instruct** model
- Smart fallback to AI for unknown queries
- Predefined conversational response layer
- Voice-driven interaction pipeline using speech recognition
- Text-to-speech (TTS) using `pyttsx3`

## Technologies Used
- **Python 3.13**
- **Tkinter** – For building the GUI
- **Requests** – For making API calls (e.g., weather, news)
- **Pillow** – For handling images (logo, GIF)
- **Pyperclip** – For clipboard access (copy file paths)
- **Webbrowser** – For opening folders from search results
- **SpeechRecognition** – For converting speech to text
- **pyttsx3** – For text-to-speech response
- **GPT4All** – For AI-based query responses (offline)

### 1. Clone the Repository
```
git clone https://github.com/udayb97/VirtualAssistant.git
cd Virtual Assistant
```
### 2. Create and Activate a Virtual Environment
```
.venv\Scripts\activate
```
### 3. Install Required Dependencies
```
pip install -r requirements.txt
```
### This will install essential packages like:

-tkinter

-requests

-pyttsx3

-Pillow

-pyperclip

-SpeechRecognition

-pyaudio

-gpt4all

### 4. Install Additional Voice Libraries
```
pip install SpeechRecognition pyttsx3 pyaudio
```
### 5. Configure API Keys

-Open src/data/config.json

-Insert your valid API keys for:

--OpenWeatherMap
--NewsAPI


## 📁 Folder Structure
```
VirtualAssistant/ 
│   ├── assets/ # logo and animations 
│   │   └──jarvis_logo.png
│   ├── screenshots/ # app screenshots for milestone 
│   ├── src/ 
│   │   ├── gui.py # main GUI file 
│   │   ├── core.py # assistant command logic 
│   │   ├── conversation.py # predefined responses 
│   │   └── data/ 
│   │       ├── config.json # api
│   │       ├── reminders.txt       
│   ├── README.md
│   ├── requirements.txt 
```
