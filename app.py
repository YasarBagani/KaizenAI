import streamlit as st
import os
import json
from models.sentiment_analyzer import get_sentiment
from core.encourager import generate_adaptive_message
from core.tracker import log_habit
from utils.notifier import run_scheduler

def load_unique_moods(filepath= "data/habit_log.json"):
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r") as file:
        data = json.load(file)
        return list(set(entry["mood"] for entry in data))

st.title("KaizenAI")
past_moods = load_unique_moods()
selected_mood = None
if past_moods: 
    cols = st.columns(min(5,len(past_moods)))
    for i,mood in enumerate(past_moods):
        if cols[i % len(cols)].button(mood):
            selected_mood = mood
new_mood = st.text_input("How are you feeling today?")
if new_mood:
    selected_mood = new_mood

if selected_mood:
    sentiment = get_sentiment(selected_mood) 
    message = generate_adaptive_message(sentiment)
    st.write(message)
    if st.button("I did my Habit" ):
        log_habit(selected_mood, sentiment)
        run_scheduler()
        st.success("Habit logged, Basic Kaizen is successfully created")

