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

        # initialize member variables
        self.node_list = []
        self.network = Network.Network()
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
            self.node_list.append(Node.Node(self.duration, self.lam, self.network, self.L, self.calculate_prop_delay(n)))
    
    def start_simulation(self):
        print("Starting Simulation")
        time = 0
        while time <= self.duration:
            for node in self.node_list:
                node.update_state()
            time += 1
        self.metrics()
        print("Ending Simulation")

    def metrics(self):
        print("Calculating Data Metrics")

        # allocate counters
        total_sent = 0
        total_delay = 0
        total_attempted = 0

        # update counters
        for node in self.node_list:
            total_attempted += node.get_total_attempted()
            total_sent += node.get_total_sent()
            total_delay += node.get_delay_time()
        
        # TODO: remove when done
        if total_sent == 0:
            total_sent = 1000
            print("FUCK") # TODO: total sent is coming out to 0... nodes seem to be stuck in transmission

        self.throughput = total_sent/self.duration
        self.efficiency = 100*(total_sent)/total_attempted

    def get_throughput(self):
        return self.throughput
    
    def get_efficiency(self):
        return self.efficiency


    
    