import streamlit as st
from models.sentiment_analyzer import get_sentiment
from core.encourager import generate_message
from core.tracker import log_habit
from utils.notifier import run_scheduler
st.title("KaizenAI")
if "mood" not in st.session_state:
    st.session_state.mood = ""

# Show input box (auto-filled from session state if a button was clicked)
mood = st.text_input("How are you feeling today?", value=st.session_state.mood, key="mood_input")

# Optional: Show suggested buttons below
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("😊 I am happy"):
        st.session_state.mood = "I am happy"
        st.stop()  # Stop execution so next rerun picks up updated state

with col2:
    if st.button("😢 I am sad"):
        st.session_state.mood = "I am sad"
        st.stop()

with col3:
    if st.button("😌 I am calm"):
        st.session_state.mood = "I am calm"
        st.stop()
# mood=st.text_input("How are you feeling today?")
if mood:
    sentiment = get_sentiment(mood) 
    message = generate_message(sentiment)
    st.write(message)
    if st.button("I did my Habit" ):
        log_habit(mood, sentiment)
        run_scheduler()
        st.success("Habit logged, Basic Kaizen is successfully created")