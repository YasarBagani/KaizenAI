import streamlit as st
from models.sentiment_analyzer import get_sentiment
from core.encourager import generate_message
st.title("KaizenAI")
mood=st.text_input("How are you feeling today?")
if mood:
    sentiment = get_sentiment(mood) 
    message = generate_message(sentiment)
    st.write(message)
    if st.button("I did everything i could to do to be this happy" ):
        st.success("Habit logged, Basic Kaizen is successfully created")