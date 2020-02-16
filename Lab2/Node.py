class Node:

    def __init__(self, _id, packet_queue=[], collision_count=0, bus_collision=0, wait_time=0):
        self.id = _id # unique ID for each node
        self.queue = packet_queue # stores all the packets arriving to the queue
        self.collision = collision_count # the number of collison that occur after transmitting packet
        self.bus_collision = bus_collision # counter for when medium is busy when sensed
        self.wait = wait_time # time a node must wait, during exponential backoff

