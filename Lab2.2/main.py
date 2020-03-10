import PersistentSimulation
import NonpersistentSimulation
import matplotlib.pyplot as plt

def simulate_persistent_case():

    print("In Lab 2 main")

    ################# PARAMETERS ################# 
    d = 10 # meters
    c = 3*(10**8) # meters/sec
    s = float((2/3)*c) # meters/sec 2*10**8
    L = 1500 # bits
    R = 1*10**6 # bps --> 1Mbps
    t = 10 # time in ticks
    n = [20, 40, 60, 80, 100] # number of nodes
    A = [7, 10, 20] # packets/second

    n_test = 10 # TODO: delete
    t_test = 100 # TODO: delete

    throughput_data = [[], [], []]
    efficiency_data = [[], [], []]

    ################# RUN SIMULATION ################# 
    for i, lam in enumerate(A):
        print("lamda: " + str(lam))
        for j , node_count in enumerate(n):
            sim = PersistentSimulation.PersistentSimulation(lam, node_count, t_test, d, s, L, R)
            throughput_data[i].append(sim.get_throughput())
            efficiency_data[i].append(sim.get_efficiency())

    ################# PLOT EFFICIENCY ################# 
    plt.figure()
    plt.title("Efficiency vs Number of Nodes: Persistent")
    plt.xlabel('Number of Nodes')
    plt.ylabel('Efficiency')
    for i, lam in enumerate(A):
        plt.plot(n, efficiency_data[i], label='Arrival Rate: T= {}'.format(lam))
    plt.legend()
    plt.show()

    ################# PLOT THROUGHPUT ################# 
    plt.figure()
    plt.title("Throughput vs Number of Nodes: Persistent")
    plt.xlabel('Number of Nodes')
    plt.ylabel('Throughput (Mbps)')
    for i, lam in enumerate(A):
        plt.plot(n, throughput_data[i], label='Arrival Rate: T= {}'.format(lam))
    plt.legend()
    plt.show()

def simulate_nonpersistent_case():

    ################# PARAMETERS ################# 
    d = 10 # meters
    c = 3*(10**8) # meters/sec
    s = float((2/3)*c) # meters/sec 2*10**8
    L = 1500 # bits
    R = 1*10**6 # bps --> 1Mbps
    t = 10 # time in ticks
    n = [20, 40, 60, 80, 100] # number of nodes
    A = [7, 10, 20] # packets/second

    n_test = 10 # TODO: delete
    t_test = 100 # TODO: delete

    throughput_data = [[], [], []]
    efficiency_data = [[], [], []]

    ################# RUN SIMULATION ################# 
    for i, lam in enumerate(A):
        print("lamda: " + str(lam))
        for j , node_count in enumerate(n):
            sim = NonpersistentSimulation.NonpersistentSimulation(lam, node_count, t_test, d, s, L, R)
            throughput_data[i].append(sim.get_throughput())
            efficiency_data[i].append(sim.get_efficiency())

    ################# PLOT EFFICIENCY ################# 
    plt.figure()
    plt.title("Efficiency vs Number of Nodes: Non-Persistent")
    plt.xlabel('Number of Nodes')
    plt.ylabel('Efficiency')
    for i, lam in enumerate(A):
        plt.plot(n, efficiency_data[i], label='Arrival Rate: T= {}'.format(lam))
    plt.legend()
    plt.show()

    ################# PLOT THROUGHPUT ################# 
    plt.figure()
    plt.title("Throughput vs Number of Nodes: Non-Persistent")
    plt.xlabel('Number of Nodes')
    plt.ylabel('Throughput (Mbps)')
    for i, lam in enumerate(A):
        plt.plot(n, throughput_data[i], label='Arrival Rate: T= {}'.format(lam))
    plt.legend()
    plt.show()

def main():
    print("Persistent Case")
    # simulate_persistent_case()

    print("Non-Persistent Case")
    simulate_nonpersistent_case()

    print("simulation complete")


if __name__ == "__main__":
    main()