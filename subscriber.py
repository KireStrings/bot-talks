from broker import PubSubBroker

class Subscriber:
    def receive(self, event):
        raise NotImplementedError("Subscribers must implement their own receive() method")