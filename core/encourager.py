import random
import json
positive_messages = [
    "You're doing awesome! Keep going! 💪",
    "Great vibes today! Let's keep that streak alive! 🌟",
    "You’re crushing it! Let’s keep the momentum 🔥",
    "Your habit loves your positive energy. Let’s go! 😄"
]

negative_messages = [
    "It’s okay to feel down. Just 5 minutes can help. 💡",
    "Even small steps count. Try one tiny action. 🧩",
    "Tough days are part of the journey. You got this. 🌈",
    "A little habit action can lift your mood. Give it a go! ☀️"
]

def generate_message(sentiment):
    if sentiment == "Positive":
        return random.choice(positive_messages) 
    else:
        return random.choice(negative_messages)
 
def get_recent_sentiments(filepath= "data/habit_log.json", days = 3):
    try:
        with open(filepath, "r") as file:
            data = json.load(file)
            recent = sorted(data, key = lambda x: x["date"], reverse = True)[:days]
            return list(set(entry["mood"] for entry in data))
    except Exception as e:
        print("failed to read history: ", e)
        return[]
def generate_adaptive_message(current_sentiment:str,filepath= "data/habit_log.json"):
    recent_sentiments = get_recent_sentiments(filepath= "data/habit_log.json")
    num_positive = recent_sentiments.count("postive")
    num_negative = recent_sentiments.count("negative")
    if num_negative >=2:
        return "I know it's been tough lately. Just doing a little today can help. 💙"
    
    elif num_positive <=2:
        return "You're on a roll! Let’s keep building that streak! 🔥"
    else:
        return generate_message(current_sentiment)
    