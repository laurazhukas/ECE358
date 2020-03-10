import PersistentNode

class PersistentSimulation:

    def __init__(self, _lam, _n, _T, _d, _s, _L, _R):
        # set member variables
        self.lam = _lam  # pkt/sec
        self.number_nodes = _n  # node count
        self.sim_duration = _T  # ticks
        self.time_prop_one_link = (_d/_s)  # sec
        self.time_trans = _L/_R  # sec
        self.packet_length = _L  # bits

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
        # initialize values to those at first node
        first_scheduled_dep_time = self.node_list[0].head_pkt_send_time
        index = 0

        # find first transmitting packet and the node it is stored at
        for i, node in enumerate(self.node_list):
            if node.head_pkt_send_time < first_scheduled_dep_time:
                first_scheduled_dep_time = node.head_pkt_send_time # update
                index = i # update

        return (index, first_scheduled_dep_time)

    def transmit_packet(self, sender_id, t_sent):

        # initialize
        collision_occurred = False
        max_prop_delay = 0

        # sending node trying to transmit
        self.trans_attempts += 1 

        # check all other nodes on the bus for collision or bus sensing
        for node in self.node_list:
            # do not consider the sending node
            if node.id == sender_id:
                continue # skip to next node in list
            
            # calculations for specific node
            t_prop = abs(sender_id - node.id) * self.time_prop_one_link  # (d between sender and receiver)*(prop for one link)
            t_first_bit = t_sent + t_prop  # first bit arrival at node of interest
            t_last_bit = t_first_bit + self.time_trans  # last bit arrival at node of interest
            
            # check if a node will try to transmit before receiving first bit --> COLLISION
            if t_first_bit >= node.head_pkt_send_time:
                # node of interest on bus also tries to transmit
                collision_occurred = True  # collision occurs
                self.trans_attempts += 1  # update
                max_prop_delay = max(max_prop_delay, t_prop) # update

                node.experienced_collision() # handle collision on receiving node

            # check if bus is busy --> wait and try to transmit when sending node is finished
            elif t_first_bit <= node.head_pkt_send_time <= t_last_bit:
                node.reschedule_bus_sense(t_last_bit) # handle wait on receiving node for persistent case
            # node is scheduled to transmit when sending frame has already passed
            else:
                pass

        # store sending node for access
        sending_node = self.node_list[sender_id]
        
        # COLLISION
        if collision_occurred:
            # node must retransmit
            sending_node.handle_sending_collisions(max_prop_delay, self.time_trans) # handle collision on sending node
        
        # NO COLLISION
        else:
            self.trans_success += 1  # update
            sending_node.completed_transmission()  # handle successful transmission on sending node

                
    ################# INITIALIZE ################# 
    def generate_nodes(self):
        for n in range(0, self.number_nodes):
            self.node_list.append(
                PersistentNode.PersistentNode(n, self.lam) # initialize node
            )


    ################# METRICS ################# 
    def calculate_metrics(self):
        self.efficiency = self.trans_success / self.trans_attempts
        self.throughput = (self.trans_success * self.packet_length * (10**-6) )/ (self.sim_duration) # Mbps

    def get_efficiency(self):
        return self.efficiency

    def get_throughput(self):
        return self.throughput


    ################# RUN SIMULATION ################# 
    def start_simulation(self):
        
        curr_time = 0

        # process packets for duration of simulation, then end simulation. 
        # NOTE: packets still remaining at the end of the simulation ARE NOT processed
        while curr_time <= self.sim_duration:
            id_sending_node, pkt_send_time = self.next_transmitting_node()
            self.transmit_packet(id_sending_node, pkt_send_time)
            curr_time = pkt_send_time # skip time forward
        
        # set metric variables
        self.calculate_metrics()
