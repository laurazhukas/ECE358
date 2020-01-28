import Event
import Generator


class SimulatorK:

    def __init__(self, L, duration, C, rho, k):
        self.avg_pkt_size = L  # average package size (bits)
        self.duration = duration  # simulation duration time
        self.transmission_rate = C  # transmission time (bps)
        self.events = []  # buffer/queue to hold events
        self.max_queue_size = k  # max queue size for finite M/M/K/1 queue
        self.p_loss = 0
        self.En = 0  # average num of packets in queue

        lam = (rho * C) / L  # average number of packets arrived (packets per sec)
        alpha = 5 * lam  # average number of observer events per second

        self.run(lam, alpha)  # start the simulation

    def generate_observations(self, alpha):
        time = 0
        while True:
            time += Generator.generate_exponential_random_var(alpha)
            if time > self.duration:
                break
            current_event = Event.Event('OBSERVER', time, False)
            self.events.append(current_event)
            
    def generate_arrivals(self, lam):
        time = 0
        while True:
            time += Generator.generate_exponential_random_var(lam)
            packet_length = Generator.generate_exponential_random_var(1/self.avg_pkt_size)
            if time > self.duration:
                break
            current_event = Event.Event('ARRIVAL', time, False, packet_length)
            self.events.append(current_event)

    def should_drop(self, queue_size):
            if queue_size == self.max_queue_size:
                return True
            else:
                return False

    def calculate_departures(self):
        current_time = 0
        for head_pkt in self.events:
            # Do not process dropped packets or observation events
            if not head_pkt.type == "ARRIVAL" or head_pkt.dropped:
                continue

            # Update current time
            if head_pkt.time > current_time:
                    current_time = head_pkt.time  # skip time forward to this event

            # Calculate the departure time
            service_time = head_pkt.packet_length/self.transmission_rate
            departure_time = current_time + service_time  # departure time for head packet

            # Check if packet is arriving after departure time
            if head_pkt.time > departure_time:
                break 

            # Find packets currently in queue --> arrived between head_pkt arrival and departure time
            queue_size = 0
            for pkt in self.events:
                if pkt.type == "ARRIVAL" and not pkt.dropped and pkt.time >= head_pkt.time and (pkt.time < departure_time):
                    # only look at arrival packets between head arrival and departure time that haven't been dropped
                    dropped = self.should_drop(queue_size)
                    if dropped:
                        pkt.dropped = True
                    else:
                        queue_size += 1
            
            # Create departure event
            current_event = Event.Event('DEPARTURE', departure_time)
            self.events.append(current_event)
            current_time = departure_time  # skip time forward

    def observe_events(self):
        packets_in_buffer = 0
        packets_lost = 0
        Nd = 0  # number of departures
        Na = 0  # number of arrivals
        No = 0  # number of observations
        for event in self.events:
            if event.type == 'ARRIVAL':
                if event.dropped:
                    packets_lost += 1
                else:
                    Na += 1  # increase if we processed the arrival
            elif event.type == 'DEPARTURE':
                Nd += 1
            elif event.type == 'OBSERVER':
                No += 1
                curr_packets_in_buffer = Na - Nd
                packets_in_buffer += curr_packets_in_buffer  # sum of packet waiting in buffer
            else:
                pass
        self.En = packets_in_buffer / No
        self.p_loss = packets_lost / No
    
    def sort_events(self):
        self.events.sort(key=lambda event: event.time)

    def run(self, lam, alpha):
        self.generate_observations(alpha)
        self.generate_arrivals(lam)
        self.calculate_departures()
        self.sort_events()
        self.observe_events()