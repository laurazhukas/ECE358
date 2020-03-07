import PersistentCsmaCd
import matplotlib.pyplot as plt

def simulate_persistent_case():
    print("In Lab 2 main")
    d = 10 # meters
    c = 3*(10**8) # meters/sec
    s = float((2/3)*c) # meters/sec
    L = 1500 # bits
    R = 1 # Mbps
    t = 10 # time in ticks
    n = [20, 40, 60, 80] # number of nodes
    n_test = 20
    t_test = 100
    A = [7, 10, 20] # packets/second

    throughput_data = []
    efficiency_data = []

    sim = PersistentCsmaCd.PersistentCsmaCd(n_test, t_test, L, A[0], s)
    throughput_data.append(sim.get_efficiency())
    efficiency_data.append(sim.get_throughput())

    plt.figure()
    plt.plot(n_test, efficiency_data[0])
    plt.show()


def main():
    print("Starting Lab 2")
    simulate_persistent_case()


    
    
if __name__ == "__main__":
    main()