import PersistentSimulation
import NonpersistentSimulation
import matplotlib.pyplot as plt

def simulate_persistent_case(A, N, T, d, s, L, R):
    # initialize
    throughput_data = [[], [], []]
    efficiency_data = [[], [], []]

    ################# RUN SIMULATION ################# 
    for i, lam in enumerate(A):
        for node_count in N:
            sim = PersistentSimulation.PersistentSimulation(lam, node_count, T, d, s, L, R)
            throughput_data[i].append(sim.get_throughput())
            efficiency_data[i].append(sim.get_efficiency())

    ################# PLOT METRICS ################# 
    plot_efficiency(efficiency_data, N, A, "Persistent")
    plot_throughput(throughput_data, N, A, "Persistent")

def simulate_nonpersistent_case(A, N, T, d, s, L, R):
    # initialize
    throughput_data = [[], [], []]
    efficiency_data = [[], [], []]

    ################# RUN SIMULATION ################# 
    for i, lam in enumerate(A):
        for node_count in N:
            sim = NonpersistentSimulation.NonpersistentSimulation(lam, node_count, T, d, s, L, R)
            throughput_data[i].append(sim.get_throughput())
            efficiency_data[i].append(sim.get_efficiency())

    ################# PLOT METRICS ################# 
    plot_efficiency(efficiency_data, N, A, "Non-Persistent")
    plot_throughput(throughput_data, N, A, "Non-Persistent")


def plot_efficiency(efficiency_data, N, A, case):
    plt.figure()
    plt.title("Efficiency vs Number of Nodes: " + str(case))
    plt.xlabel('Number of Nodes')
    plt.ylabel('Efficiency')
    for i, lam in enumerate(A):
        plt.plot(N, efficiency_data[i], label='Arrival Rate: T= {}'.format(lam))
    plt.legend()
    plt.show()

def plot_throughput(throughput_data, N, A, case):
    plt.figure()
    plt.title("Throughput vs Number of Nodes: " + str(case))
    plt.xlabel('Number of Nodes')
    plt.ylabel('Throughput (Mbps)')
    for i, lam in enumerate(A):
        plt.plot(N, throughput_data[i], label='Arrival Rate: T= {}'.format(lam))
    plt.legend()
    plt.show()

def main():    
    print("Starting Lab 2:")
    ################# PARAMETERS ################# 
    d = 10 # meters
    c = 3*(10**8) # meters/sec
    s = float((2/3)*c) # meters/sec 2*10**8
    L = 1500 # bits
    R = 1*10**6 # bps --> 1Mbps
    T = 1000 # time in ticks
    N = [20, 40, 60, 80, 100] # number of nodes
    A = [7, 10, 20] # packets/second

    ################# SIMULATIONS ################# 
    print("Persistent Case")
    simulate_persistent_case(A, N, T, d, s, L, R)

    print("Non-Persistent Case")
    simulate_nonpersistent_case(A, N, T, d, s, L, R)

    print("Lab 2 Simulation Complete")


if __name__ == "__main__":
    main()