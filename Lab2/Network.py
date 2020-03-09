class Network:
    def __init__(self, n, d, s):
        self.num_nodes = n
        self.state = "IDLE"
        self.active_nodes = 0
        self.time_until_aware = [0] * n 
        self.t_prop = d/s

    def get_state(self):
        if self.active_nodes == 0:
            return "IDLE"
        elif self.active_nodes == 1:
            return "BUSY"
        else:
            return "COLLISION"
    
    def add_traffic(self):
        self.active_nodes += 1
    
    def remove_traffic(self):
        self.active_nodes -= 1
    
    def is_node_aware(self, _id):
        time = self.time_until_aware[_id]
        if time == 0:
            return True
        else:
            return False
    
    def initialize_aware_list(self, id_sender):
        for i in range(0, self.num_nodes):
            self.time_until_aware[i] = abs(id_sender - i)*self.t_prop

    def get_aware_list(self):
        return self.time_until_aware
        
    def update(self):
        for t in self.time_until_aware:
            if t > 0:
                t -=1
