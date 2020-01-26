import Event
import Generator

class Simulator:

    def __init__(self, L, duration, C, rho):
        self.avg_pkt_size = L # average package size
        self.duration = duration # simulation duration time
        self.transmission_rate = C
        lam = (rho*C)/L
        alpha = 5*lam
        self.Na = 0 # number of arrivals
        self.Nd = 0 # number of departures
        self.No = 0 # number of observations
        self.queue_size = 0
        self.Ne = 0 # number of events
        self.events = [] # keeps track of all events
        self.p_idle = 0
        self.En = 0

        self.run(lam, alpha)

    def generate_observations(self, alpha):
        # alpha is the of observation events per second
        time = 0
        while(True):
            time += Generator.generate_exponential_random_var(alpha)
            if time > self.duration: break
            current_event = Event.Event('OBSERVER', time, False)
            self.events.append(current_event)
            self.Ne += 1
            
    def generate_arrivals(self, lam):
        time = 0
        while(True):
            time += Generator.generate_exponential_random_var(lam)
            packet_length = Generator.generate_exponential_random_var(1/self.avg_pkt_size)
            if time > self.duration: break
            current_event = Event.Event('ARRIVAL', time, False, packet_length)
            self.events.append(current_event)
            self.Ne += 1

    def calculate_departures(self):
        current_time = 0
        for event in self.events:
            if(event.type == 'ARRIVAL'):
                if event.time > current_time:
                    current_time = event.time # skip time forward to this event
                service_time = event.packet_length/self.transmission_rate
                departure_time = current_time + service_time

                current_event = Event.Event('DEPARTURE', departure_time)
                self.events.append(current_event)
                self.Ne += 1
                current_time = departure_time # skip time forward
            else:
                pass

    def observe_events(self):
        packets_in_buffer = 0
        curr_packets_in_buffer = 0
        num_idle = 0
        for event in self.events:
            if event.type == 'ARRIVAL':
                self.Na += 1
            elif event.type == 'DEPARTURE':
                self.Nd += 1
            elif event.type == 'OBSERVER':
                self.No += 1
                curr_packets_in_buffer = self.Na - self.Nd
                if curr_packets_in_buffer == 0: 
                    num_idle += 1 # sum of ticks where buffer was empty
                packets_in_buffer += curr_packets_in_buffer # sum of packet waiting in buffer
            else:
                pass
        self.p_idle = num_idle / self.No
        self.En = packets_in_buffer / self.No
    
    def sort_events(self):
        self.events.sort(key = lambda event: event.time)
        
    def run(self, lam, alpha):
        self.generate_observations(alpha)
        self.generate_arrivals(lam)
        self.calculate_departures()
        self.sort_events()
        self.observe_events()



