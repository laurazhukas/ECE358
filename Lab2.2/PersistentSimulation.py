import PersistentNode as Node

class PersistentSimulation:

    def __init__(self):
        self.node_list = []
        self.number_nodes = _n
        self.sim_duration = _T
        self.time_prop_one_link = _d/_s

        self.generate_nodes()
    

def next_transmitting_node(self):
    prev_time = self.node_list[0].head_pkt_send_time
    min_time = 0
    index = 0

    for i, node in enumerate(self.node_list):
        if node.head_pkt_send_time < prev_time:
            prev_time = node.head_pkt_send_time
            index = i

    return (index, min_time)

# def get_propagation_delays(self, sender_id):
#     prop_delay_list = []
#     for node in self.node_list:
#         prop_delay = abs(sender_id - node.id) * self.time_prop_one_link
#         prop_delay_list.append(prop_delay)
#     return prop_delay_list

def check_for_collisions(self, sender_id, t_sent)
    # get propagation time from sending node to each node in network (time for 1st bit to arrive)
    # prop_times = self.get_propagation_delays(sender_id)

    collisions_occurred = 0
    max_prop_delay = 0

    for node in self.node_list:
        # do not consider the sending node
        if node.id == sender_id:
            pass

        t_prop = abs(sender_id - node.id) * self.time_prop_one_link
        t_first_bit = t_sent + t_prop

        # check if node will try to transmit before receiving first bit --> COLLISION
        if t_first_bit >= node.head_pkt_send_time:
            collisions_occurred += 1
            max_prop_delay = max(max_prop_delay, t_prop)
            node.experienced_collision() # handle collision on receiving node
        
    # handle collision on sending node
    if collision_occurred > 0:
        sending_node = self.node_list[sender_id]
        sending_node.handle_sending_collisions() # handle collision on sending node
            


################# INITIALIZE ################# 
    def generate_nodes(self):
        for n in range(0, self.number_nodes):
            self.node_list.append(
                Node() # initialize node
            )
        
################# RUN SIMULATION ################# 
    def start_simulation(self):
        curr_time = 0
        while curr_time <= self.sim_duration:
            node_trans_id, pkt_send_time = self.next_transmitting_node()
            will_collide = self.check_for_collisions(node_trans_id, pkt_send_time)
            # do stuff

            # time += 1