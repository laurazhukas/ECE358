# changes for nodes in persistant case

import Generator
import Network

class Node:

    def __init__(self, duration, lam, _network, _pkt_length, prop_delay, packet_queue=[], bus_collision=0, wait_time=0):
        # set member variables
        self.sim_duration = duration
        self.L = _pkt_length
        self.lam = lam
        self.prop_delay = prop_delay
        self.network = _network
        self.bus_collision = bus_collision # counter for when medium is busy when sensed
        self.wait = wait_time # time a node must wait, during exponential backoff
        self.packet_list = []
        self.R = 1000000 # 1Mbps
        # self.generate_pkt_arrivals(0.01) # initalize packet arrival time list

        # generate packets
        time = 0
        while True:
            time += Generator.generate_exponential_random_var(self.lam)
            if time > self.sim_duration:
                break
            self.packet_list.append(time)

        # initial conditions
        self.state = "IDLE"
        self.time = Generator.generate_exponential_random_var(self.lam)
        self.delay = 0
        self.backoff_counter = 0
        self.completed_pkts_sent = 0

        print("Node made")

    def start_sensing_time(self):
        self.time = 96 # defined ticks for sensing medium
    
    def idle(self):
        print("Idle")
        # update idle --> sensing
        if self.time == 0:
            self.state = "SENSING"
            self.start_sensing_time()

    def sensing(self):
        print("Sensing")
        # update sensing --> waiting
        if self.network.get_state() != "IDLE":
            # executes if network is not free
            return sensing(self)
            
            # TODO: check this code
            # self.state = "WAITING" # update node state -> no waiting state in persistant
            # the wait time can be incorporated into the non-persistant case
            # self.time = Generator.exponential_backoff(self.backoff_counter) # random wait time

            print("busy network")  # TODO: delete when done   
            
        # update sensing --> transmitting
        if self.time == 0:
            self.state = "TRANSMITTING"  # update node state
            self.network.add_traffic()  # update network state
            self.time = self.prop_delay + self.L/self.R  # time packet needs to fully transmit

    # def waiting(self):
    #     print("Waiting")
    #     # update waiting --> sensing
    #     if self.time == 0:
    #         self.state = "SENSING" # update node state
    #         self.start_sensing_time() # update time to sensing

    def transmitting(self):
        print("Transmitting")
        # update trasmitting --> collision --> backoff
        if self.network.get_state() == "COLLISION":
            self.network.remove_traffic() # update network
            self.collision() # collision occurs
            return

        # update transmitting --> idle
        # packet has been fully received
        if self.time == 0:
            self.state = "IDLE" # update node state
            self.network.remove_traffic() # update network state
            self.time = Generator.generate_exponential_random_var(self.lam) # generate next arrival time
            self.backoff_counter = 0 # reset backoff counter
            self.completed_pkts_sent += 1 # update packets sent

    def collision(self):
        print("Collision")
        # update collision --> backoff
        self.currentState = "BACKOFF"

        # update backoff counter
        if self.backoff_counter < 10: # TODO: reset the backoff counter to zero -> on or after 10?
            self.backoff_counter += 1

        # set exponential backoff time
        self.time = Generator.exponential_backoff(self.backoff_counter)
    
    def backoff(self):
        # update backoff --> sensing
        if self.time == 0:
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
    
