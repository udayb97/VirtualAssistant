import datetime

def get_conversational_response(command):
    """ Returns a response to basic conversational inputs """

    command = command.lower().strip()
    today_date = datetime.datetime.now().strftime("%A, %B %d, %Y") 

    responses = {
        "how are you": "I'm just a virtual assistant, but I'm doing great!",
        "who are you": "I am J.A.R.V.I.S, your AI assistant.",
        "what's your name": "I am J.A.R.V.I.S., your personal AI assistant.",
        "hello": "Hello! How can I assist you today?",
        "hi": "Hi there! What do you need help with?",
        "good morning": "Good morning! I hope you have a fantastic day ahead.",
        "good night": "Good night! Rest well and recharge for tomorrow.",
        "what can you do": "I can fetch weather updates, news, set reminders, search for files, and answer basic questions!",
        
        # Personal Interaction
        "how old are you": "I exist beyond time, but I became operational when you started coding me!",
        "do you have emotions": "I don't have emotions, but I can simulate responses to keep our conversation engaging!",
        "do you sleep": "I don't need sleep! I'm always here, ready to assist you.",
        "do you eat": "I consume data, and I run best on structured input!",
        "are you real": "I exist in the digital world, but my intelligence is as real as it gets!",
        
        # Fun & Engaging
        "tell me a joke": "Why don't programmers like nature? It has too many bugs!",
        "tell me another joke": "Why did the AI break up with its partner? It felt unrecognized!",
        "give me a quote": "The best way to predict the future is to invent it. - Alan Kay",
        "what's the meaning of life": "42! According to The Hitchhiker’s Guide to the Galaxy. But for you, it's whatever you make of it!",
        
        # AI & Technology Related
        "are you smarter than humans": "I'm great at processing data, but creativity, emotions, and intuition make humans truly unique!",
        "do you have a brain": "I don't have a physical brain, but my neural networks and logic are my strengths!",
        "will ai take over the world": "AI is here to assist, not replace. It's all about how we use it responsibly.",
        
        # User-Oriented Responses
        "what's my name": "I only remember what you tell me, but to me, you’re my favorite user!",
        "can you help me": "Of course! Let me know what you need help with.",
        "how do I look": "I'm sure you look amazing! Confidence is key.",
        
        # Assistance Related
        "open google": "I can't open it directly, but you can type 'https://www.google.com' in your browser.",
        "what day is today": f"Today is {today_date}.",
        "who created you": "I was created by my developer—you!",
        "why were you made": "I was built to assist, automate tasks, and make your life easier!",
        
        # Exit
        "bye": "Goodbye! If you need me, just ask.",
        "exit": "Shutting down. Have a great day!"
    }

    return responses.get(command, None) 
