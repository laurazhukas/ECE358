class Network:
    def __init__(self):
        self.state = "IDLE"
        self.active_nodes = 0

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