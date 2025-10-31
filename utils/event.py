from datetime import datetime

def build_event(sender, text, channel, timestamp=None):
    return {
        "sender": sender,
        "channel": channel,
        "text": text,
        "timestamp": timestamp or datetime.now().isoformat()
    }