import Node
import Network

class PersistentCsmaCd:

    def __init__(self, number_of_nodes, sim_duration, L, A, s):
        # set parameters
        self.N = number_of_nodes
        self.duration = sim_duration
        self.L = L
        self.lam = A  # average number of packets arrived (packets per sec)
        self.s = s
        self.d = 10
        self.pkts_sent_success = 0

        # initialize member variables
        self.node_list = []
        self.network = Network.Network(number_of_nodes, self.d, s)
        self.throughput = 0
        self.efficiency = 0

        self.generate_nodes()
        self.start_simulation()

    def calculate_prop_delay(self, node_number):
        distance = 10*node_number # (m) 
        delay_time = distance/self.s # d/s (s)
        return delay_time # TODO: check to make sure correct units

    # generate nodes
    def generate_nodes(self):
        for n in range(0, self.N):
            self.node_list.append(Node.Node(self.duration, self.lam, self.network, self.L, self.calculate_prop_delay(n), n))

    def start_simulation(self):
        print("Starting Simulation")
        time = 0
        while time <= self.duration:
            self.network.update()
            for node in self.node_list:
                node.update_state()
                # if nework state was busy and noow sum awarness is 0 --> full rtanssmission
                if self.network.get_state() == "BUSY" and sum(self.network.get_aware_list()) == 0:
                    self.pkts_sent_success += 1 # increase successful transmission
                    self.network.remove_traffic()
            time += 1
        self.metrics()
        print("Ending Simulation")

    def metrics(self):
        print("Calculating Data Metrics")

        # allocate counters
        total_sent = 0
        total_delay = 0
        total_attempted = 0
        total_neg_count = 0

        # update counters
        for node in self.node_list:
            total_attempted += node.get_total_attempted()
            total_sent += node.get_total_sent()
            total_delay += node.get_delay_time()
            total_neg_count += node.get_neg()
        
        # TODO: remove when done
        if total_sent == 0:
            total_sent = 1000
            print("FUCK") # TODO: total sent is coming out to 0... nodes seem to be stuck in transmission

        print(f"this is neg count {total_neg_count}")
        self.throughput = total_sent/self.duration
        print(f"this is total delay {total_delay}")
        # should we be using the (1/(1+5tprop/ttrans)) formula?
        self.efficiency = 100*(total_sent)/total_attempted

    def get_throughput(self):
        return self.throughput
    
    def get_efficiency(self):
        return self.efficiency


    
    