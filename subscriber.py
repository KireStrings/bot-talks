from broker import PubSubBroker

class Subscriber:
    def receive(self, message):
        raise NotImplementedError("Subscribers must implement their own receive() method")