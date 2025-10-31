from datetime import datetime
from subscriber import Subscriber

class User(Subscriber):
    def __init__(self, broker, name=None, birthday=None):
        self.name = name or input("What is your name?")
        self.birthday = birthday or self.birth_date_validation()
        self.broker = broker
        self.reminder_channel = f"{self.name}-rmeinders"
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
        if self.name not in message:
            print(f"{self.name} received the message: \n{message}")

    def send(self, message, channel):
        self.broker.publish(f"{self.name}: {message}", channel)