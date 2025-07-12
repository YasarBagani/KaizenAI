from textblob import TextBlob

def get_sentiment(mood):
    blob = TextBlob(mood)
    pol = blob.sentiment.polarity
    if pol > 0:
        sentiment = "Positive"
    elif pol < 0 :
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    return sentiment