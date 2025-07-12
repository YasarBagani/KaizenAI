def generate_message(sentiment):
    if sentiment == "Postive":
        return "You are doing Great!"
    elif sentiment == "Negative":
        return "No Worries, Have a nice day"
    else:
        return "You are Alright"