class Event:

    def __init__(self, event_type, time, was_dropped = False, packet_length = None):
        self.type = event_type
        self.time = time
        self.dropped = was_dropped
        self.packet_length = packet_length
