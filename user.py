from datetime import datetime
from subscriber import Subscriber
from utils.event import build_event

class User(Subscriber):
    def __init__(self, broker, name=None, birthday=None):
        self.name = name or input("What is your name?")
        self.birthday = birthday or self.birth_date_validation()
        self.broker = broker
        self.reminder_channel = f"{self.name}-reminders"
        self.broker.subscribe(self, self.reminder_channel)

    def birth_date_validation(self):
        date_format = "%m/%d/%Y"
        
        while True:
            birthday_input = input("What is your birthday? (format: mm/dd/yyyy) ")
            try:
                return datetime.strptime(birthday_input, date_format)
            except ValueError:
                print("Please, verify the provided date's format and try again.")
    
    def receive(self, message):
        sender = message["sender"]
        channel = message["channel"]
        text = message["text"]
        timestamp = message["timestamp"]

        dt = datetime.fromisoformat(timestamp)

        date_str = dt.strftime("%Y-%m-%d")
        time_str = dt.strftime("%H:%M:%S")

        if sender != self.name:
            print(f"Channel: {channel}")
            print(f"Date: {date_str}")
            print(f"Time: {time_str}")
            print(f"{self.name} received from {sender}: {text}")

    def send(self, text, channel):
        event = build_event(self.name, text, channel)
        self.broker.publish(event, channel)