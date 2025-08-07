import random
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