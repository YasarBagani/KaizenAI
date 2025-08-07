import schedule
import time 
from plyer import notification

def send_reminder():
    notification.notify(title = "Urgent", message = "Its time for your Habit.", timeout = 5)
def run_scheduler():
    schedule.every(10).seconds.do(send_reminder)
    # schedule.every().day.at("21:19").do(send_reminder)
    while True: 
        schedule.run_pending()
        time.sleep(1)
