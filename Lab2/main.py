import PersistentCsmaCd
import matplotlib.pyplot as plt

def simulate_persistent_case():
    print("In Lab 2 main")
    d = 10 # meters
    c = 3*(10**8) # meters/sec
    s = float((2/3)*c) # meters/sec 2*10**8
    L = 1500 # bits
    R = 1*10**6 # bps
    t = 10 # time in ticks
    n = [20, 30, 40, 50, 60, 70, 80] # number of nodes
    A = [7, 10, 20] # packets/second

    n_test = 20
    t_test = 1000

    throughput_data = []
    efficiency_data = []

    for node in n:
        sim = PersistentCsmaCd.PersistentCsmaCd(node, t_test, L, 12, s)
        throughput_data.append(sim.get_efficiency())
        efficiency_data.append(sim.get_throughput())

    plt.figure()
    plt.plot(n, efficiency_data)
    plt.show()

def main():
    print("Starting Lab 2")
    simulate_persistent_case()


if __name__ == "__main__":
    main()