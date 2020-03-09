import Generator

class PersistentNode:
    def __init__(self,):
        self.id = _id
        self.lam = _lam
        self.head_pkt_send_time = self.generate_pkt_arrival_time(0) # TODO: make sure works
        self.collision_counter = 0

        self.packet_dropped_counter = 0

    def experienced_collision(self):
        # packet dropped
        if self.collision_counter > 10:
            self.collision_counter = 0 # reset counter
            self.packet_dropped_counter += 1 # increment
            self.head_pkt_send_time = self.generate_pkt_arrival_time(self.head_pkt_send_time, self.lam) # new packet arrival time
        else:
            self.collision_counter += 1 # increment
            self.head_pkt_send_time = self.generate_exp_backoff_time(self.head_pkt_send_time, self.collision_counter) # new scheduled departure time


    def handle_sending_collisions(self, num_collisions, max_prop_delay):
        self.experienced_collision()
        self.head_pkt_send_time = max_prop_delay + trans_delay + self.head_pkt_send_time
       
        

def generate_pkt_arrival_time(current_time, lam):
    return current_time + Generator.generate_exponential_random_var(lam)

def generate_exp_backoff_time(current_time, backoff_counter):
    return current_time + Generator.generate_exp_backoff()
