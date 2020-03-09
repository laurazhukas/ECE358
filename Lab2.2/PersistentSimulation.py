import PersistentNode as Node

class PersistentSimulation:

    def __init__(self, _lam, _n, _T, _d, _s, _L, _R):
        # set member variables
        self.lam = _lam
        self.number_nodes = _n
        self.sim_duration = _T
        self.time_prop_one_link = (_d/_s)
        self.time_trans = _L/_R
        self.packet_length = _L

        # initialize member variables
        self.node_list = []
        self.trans_attempts = 0
        self.trans_success = 0
        self.efficiency = 0
        self.throughput = 0
        
        # start computations
        self.generate_nodes()
        self.start_simulation()

    def next_transmitting_node(self):
        first_scheduled_dep_time = self.node_list[0].head_pkt_send_time
        index = 0

        for i, node in enumerate(self.node_list):
            if node.head_pkt_send_time < first_scheduled_dep_time:
                first_scheduled_dep_time = node.head_pkt_send_time
                index = i

        return (index, first_scheduled_dep_time)

    def check_for_collisions(self, sender_id, t_sent):

        collision_occurred = False
        max_prop_delay = 0
        self.trans_attempts += 1 # sending node trying to transmit

        for node in self.node_list:
            # do not consider the sending node
            if node.id == sender_id:
                continue
            t_prop = abs(sender_id - node.id) * self.time_prop_one_link # TODO: scaling??? *(10**6)
            t_first_bit = t_sent + t_prop
            t_last_bit = t_first_bit + self.time_trans
            
            # check if a node will try to transmit before receiving first bit --> COLLISION
            if t_first_bit >= node.head_pkt_send_time:
                self.trans_attempts += 1 # node on bus also tries to transmit
                collision_occurred = True # collision occurs
                max_prop_delay = max(max_prop_delay, t_prop) # update
                node.experienced_collision() # handle collision on receiving node
            # check if bus is busy --> wait and try to transmit when sending node is finished
            elif t_first_bit <= node.head_pkt_send_time <= t_last_bit:
                node.reschedule_bus_sense(t_last_bit)
        
        sending_node = self.node_list[sender_id]
        
        if collision_occurred:
            # node must retransmit
            sending_node.handle_sending_collisions(max_prop_delay, self.time_trans) # handle collision on sending node
        else:
            self.trans_success += 1 # node successfully trasnmitted
            sending_node.completed_transmission()

                
    ################# INITIALIZE ################# 
    def generate_nodes(self):
        for n in range(0, self.number_nodes):
            self.node_list.append(
                Node.PersistentNode(n, self.lam) # initialize node
            )


    ################# METRICS ################# 
    def calculate_metrics(self):
        self.efficiency = self.trans_success / self.trans_attempts
        self.throughput = self.trans_success * self.packet_length / self.sim_duration

    def get_efficiency(self):
        return self.efficiency

    def get_throughput(self):
        return self.throughput


    ################# RUN SIMULATION ################# 
    def start_simulation(self):
        
        curr_time = 0

        # process packets for duration of simulation
        while curr_time <= self.sim_duration:
            print("Current Time: " + str(curr_time))
            id_sending_node, pkt_send_time = self.next_transmitting_node()
            self.check_for_collisions(id_sending_node, pkt_send_time)
            curr_time = pkt_send_time # skip time forward
        
        # set metric variabless
        self.calculate_metrics()
