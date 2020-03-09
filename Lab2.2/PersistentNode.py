import Generator

class PersistentNode:
    def __init__(self,_id, _lam):
        # set member variables
        self.id = _id
        self.lam = _lam

        # initialize member varaibles
        self.head_pkt_send_time = generate_pkt_arrival_time(0, self.lam) # TODO: make sure works
        self.collision_counter = 0
        self.packet_dropped_counter = 0 # TODO: remove unneeded code

    def experienced_collision(self):
        
        self.collision_counter += 1 # increment for backoff
        # packet dropped
        if self.collision_counter > 10:
            self.collision_counter = 0 # reset counter
            self.packet_dropped_counter += 1 # increment
            self.head_pkt_send_time = generate_pkt_arrival_time(self.head_pkt_send_time, self.lam) # new packet arrival time
        # backoff
        else:
            self.head_pkt_send_time = generate_exp_backoff_time(self.head_pkt_send_time, self.collision_counter) # new scheduled departure time

    def reschedule_bus_sense(self, new_time):
        # node sensed bus was busy --> node waits to transmit until last bit of currently transmitting frame arrives
        self.head_pkt_send_time = new_time
    
    def handle_sending_collisions(self, max_prop_delay, trans_delay):
        self.experienced_collision() # check whether to drop or backoff
        self.head_pkt_send_time = max_prop_delay + trans_delay + self.head_pkt_send_time # update time until after unsuccessful transmission completed
       
    def completed_transmission(self):
        self.collision_counter = 0 # reset
        self.head_pkt_send_time = generate_pkt_arrival_time(self.head_pkt_send_time, self.lam) # new packet arrival time

################ GENERATOR HELPER FUNCTIONS ################
def generate_pkt_arrival_time(current_time, lam):
    return current_time + Generator.generate_exponential_random_var(lam)

def generate_exp_backoff_time(current_time, backoff_counter):
    return current_time + Generator.generate_exp_backoff(backoff_counter)
