import json
from datetime import date

def log_habit(mood, sentiment):
    log = {"date": str(date.today()), "mood" : mood, "sentiment" : sentiment}
    try:
        with open("data/habit_log.json", "r+") as file:
            data = json.load(file)
            data.append(log)
            file.seek(0)
            json.dump(data, file, indent = 2)
    except FileNotFoundError:
        with open ("data/habit_log.json", "w") as file:
            json.dump([log], file, indent = 2) 