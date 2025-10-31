from collections import defaultdict

class PubSubBroker:
    def __init__(self):
        self.channels = defaultdict(set)

    def subscribe(self, subscriber, channel):
        self.channels[channel].add(subscriber)

    def unsubscribe(self, subscriber, channel):
        self.channels[channel].discard(subscriber)

    def publish(self, event, channel):
        for subscriber in self.channels[channel]:
            subscriber.receive(event)
