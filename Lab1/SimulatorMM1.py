import Event
import Generator


class SimulatorMM1:

    def __init__(self, L, duration, C, rho):
        self.avg_pkt_size = L  # average package size (bits)
        self.duration = duration  # simulation duration time
        self.transmission_rate = C  # transmission time (bps)
        self.events = []  # buffer/queue to hold events
        self.p_idle = 0   # proportion of time the server is idle
        self.En = 0  # average number of packets in the buffer

        lam = (rho*C)/L  # average number of packets arrived (packets per sec)
        alpha = 5*lam  # average number of observer events per second

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

    def calculate_departures(self):
        current_time = 0
        for head_pkt in self.events:
            # Only process arrival events
            if head_pkt .type == 'ARRIVAL':

                # Update current time
                if head_pkt.time > current_time:
                    current_time = head_pkt.time  # skip time forward to this event

                # Calculate the departure time
                service_time = head_pkt.packet_length/self.transmission_rate
                departure_time = current_time + service_time

                # Create departure event
                current_event = Event.Event('DEPARTURE', departure_time)
                self.events.append(current_event)
                current_time = departure_time  # skip time forward
            else:
                pass

    def observe_events(self):
        packets_in_buffer = 0
        num_idle = 0
        Nd = 0  # number of departures
        Na = 0  # number of arrivals
        No = 0  # number of observations
        for event in self.events:
            if event.type == 'ARRIVAL':
                Na += 1
            elif event.type == 'DEPARTURE':
                Nd += 1
            elif event.type == 'OBSERVER':
                No += 1
                curr_packets_in_buffer = Na - Nd
                # if buffer is idle
                if curr_packets_in_buffer == 0: 
                    num_idle += 1  # sum of ticks where buffer was empty
                packets_in_buffer += curr_packets_in_buffer  # sum of packet waiting in buffer
            else:
                pass
        self.p_idle = num_idle / No
        self.En = packets_in_buffer / No
    
    def sort_events(self):
        self.events.sort(key=lambda event: event.time)
        
    def run(self, lam, alpha):
        self.generate_observations(alpha)
        self.generate_arrivals(lam)
        self.calculate_departures()
        self.sort_events()
        self.observe_events()



