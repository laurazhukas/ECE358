
import Generator
import Network

class Node:

    def __init__(self, duration, lam, _network, pkt_length, prop_delay, _id):
        # set member variables
        self.sim_duration = duration
        self.L = pkt_length
        self.lam = lam
        self.prop_delay = prop_delay
        self.network = _network
        self.id = _id
        self.neg_count = 0
        self.R = 1000000 # 1Mbps
        self.t_trans = self.L/self.R

        # initial conditions
        self.state = "IDLE"
        self.time = Generator.generate_exponential_random_var(self.lam) # time of first pkt arrival
        if self.time < 0:
            self.neg_count += 1
        self.delay = 0
        self.backoff_counter = 0
        self.completed_pkts_sent = 0
        self.transmissions_attempted = 0 

        print("Node made")

    def start_sensing_time(self):
        self.time = 96 # defined ticks for sensing medium
    
    def idle(self):
        print("Idle")
        # update idle --> sensing
        if self.time <= 0:
            self.state = "SENSING"
            self.start_sensing_time()

    def sensing(self):
        print("Sensing")
        # update sensing --> waiting
        if self.network.get_state() != "IDLE":
            # executes if network is not free
             return

        #     # TODO: check this code
        #     self.state = "WAITING" # update node state
        #     self.time = Generator.exponential_backoff(self.backoff_counter) # random wait time
        #     print("busy network")  # TODO: delete when done  
        #     return 
            
        # update sensing --> transmitting
        if self.time <= 0:

            self.state = "TRANSMITTING"  # update node state
            self.network.add_traffic()  # update network state
<<<<<<< Updated upstream
            self.time = self.prop_delay + self.t_trans  # time packet needs to fully transmit
=======
            self.time = self.prop_delay + self.trans_delay # time packet needs to fully transmit
>>>>>>> Stashed changes

    # def waiting(self):
    #     print("Waiting")
    #     # update waiting --> sensing
    #     if self.time == 0:
    #         self.state = "SENSING" # update node state
    #         self.start_sensing_time() # update time to sensing

    def transmitting(self):
        print("Transmitting")
        # self.transmissions_attempted += 1
        # # update trasmitting --> collision --> backoff
        # if self.network.get_state() == "COLLISION":
        #     print("collision! :(")
        #     self.network.remove_traffic() # update network
        #     self.collision() # collision occurs
        #     return

        # # update transmitting --> idle
        # # packet has been fully received
        # if self.time <= 0:
        #     self.state = "IDLE" # update node state
        #     self.network.remove_traffic() # update network state
        #     self.time = Generator.generate_exponential_random_var(self.lam) # generate next arrival time
        #     if self.time < 0:
        #         self.neg_count += 1
        #     self.backoff_counter = 0 # reset backoff counter
        #     self.completed_pkts_sent += 1 # update packets sent
        if self.time <= 0:
<<<<<<< Updated upstream
            # node has something to transmit at this tick
            if self.network.get_state() == "BUSY":
                # someone is currently transmitting
                if self.network.is_node_aware(self.id):
                    # True if current node is aware of other transmission
                    # keep trying to transmit until bus is free
                    return
                else:
                    # network is busy, but this node doesn't know about the tranmission yet
                    # collision will occur
                    self.state = "COLLISION"
                    self.network.state = "COLLISION"
                    self.collision() # collision occurs
            elif self.network.get_state() == "IDLE":
                self.network.add_traffic()
                self.network.initialize_aware_list(self.id)
                self.time = max(self.network.get_aware_list()) + self.t_trans
                self.state = "TRANSMISSION IN PROGRESS"

    def trans_in_progress(self):
        if self.network.get_state == "COLLISION":
            self.collision()

        if self.time <= 0:
            self.state = "IDLE"
            self.network.remove_traffic()
            self.time = Generator.generate_exponential_random_var(self.lam)
            self.completed_pkts_sent += 1

=======
            print("god bless")
            self.state = "IDLE" # update node state
            self.network.remove_traffic() # update network state
            self.time = Generator.generate_exponential_random_var(self.lam) # generate next arrival time
            self.backoff_counter = 0 # reset backoff counter
            self.completed_pkts_sent += 1 # update packets sent
>>>>>>> Stashed changes

    def collision(self):
        print("Collision")
        
        if self.backoff_counter <= 10:
            # update collision --> backoff
            self.currentState = "BACKOFF"
            # set exponential backoff time
            self.time = Generator.exponential_backoff(self.backoff_counter)
            # increment counter
            self.backoff_counter += 1
        # drop packet
        else:
            # update collision --> idle (packet dropped)
            self.state = "IDLE" 
            self.network.remove_traffic() # update network state
            self.time = Generator.generate_exponential_random_var(self.lam) # generate next arrival time
            if self.time < 0:
                self.neg_count += 1
            self.backoff_counter = 0 # reset backoff counter
            return
        
    
    def backoff(self):
        # update backoff --> sensing
        if self.time <= 0:
            self.state = "SENSING"
            self.start_sensing_time()

    def update_state(self):
        # print("updating node state") # TODO: delete when done
        # update time
        self.time -= 1

        # update delay counter
        if self.state != "IDLE":
            self.delay += 1

        # execute proper state function
        if self.state == "IDLE":
            self.idle()
        elif self.state == "SENSING":
            self.sensing()
        elif self.state == "WAITING":
            self.waiting()
        elif self.state == "TRANSMITTING":
            self.transmitting()
        elif self.state == "COLLISION":
            self.collision()
        elif self.state == "BACKOFF":
            self.backoff()
    
    #################### USED FOR DATA METRICS ####################
    def get_total_sent(self):
        return self.completed_pkts_sent
    
    def get_delay_time(self):
        return self.delay
    
    def get_total_attempted(self):
        return self.transmissions_attempted

    def get_neg(self):
        return self.neg_count
