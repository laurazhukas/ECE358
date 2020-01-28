import Generator
import statistics
import SimulatorMM1
import SimulatorMM1K
import matplotlib.pyplot as plt


def question_1():
    print("QUESTION 1")
    num_list = []
    for i in range(0, 1000):
        num_list.append(Generator.generate_exponential_random_var(75))
    mean = statistics.mean(num_list)
    variance = statistics.variance(num_list)
    print(f"The exponential random variable mean is: {mean}")
    print(f"The exponential random variable variance is {variance}")


def question_3():
    print("QUESTION 3")
    rho_values = [0.35, 0.45, 0.55, 0.65, 0.75, 0.85]  # 0.25 < rho < 0.95
    average_num_pkts = []
    p_idle = []
    L = 2000
    C = 1000000
    duration = 10
    for rho in rho_values:
        print(f"Running Simulation at Rho: {rho}")
        sim = SimulatorMM1.SimulatorMM1(L, duration, C, rho)
        print(f"this is the value for sim.En: {sim.En}")
        average_num_pkts.append(sim.En)
        print(f"this is the value for sim.En: {sim.p_idle}")
        p_idle.append(sim.p_idle)
    print("Preparing Graphs")
    # Graph 1
    plt.title("Average Number of Packets vs Rho Values")
    plt.plot(rho_values, average_num_pkts)
    plt.xlabel('Rho Values')
    plt.ylabel('Average Number of Packets')
    # plt.show()
    plt.savefig('Question3-1.png', bbox_inches='tight')
    plt.close()

    # Graph 2
    plt.title("Proportion of Time Server Is Idle vs Rho Values")
    plt.xlabel('Rho Values')
    plt.ylabel('Proportion of Time Idle')
    plt.plot(rho_values, p_idle)
    # plt.show()
    plt.savefig('Question3-2.png', bbox_inches='tight')
    plt.close()


def question_4():
    print("QUESTION 4")
    rho_value = 1.2
    L = 2000
    C = 1000000
    duration = 1000
    print(f"Running Simulation at Rho: {rho_value}")
    sim = SimulatorMM1.SimulatorMM1(L, duration, C, rho_value)
    print(f"Average number of packets: {sim.En}")
    print(f"P_idle: {sim.p_idle}")


def question_6():
    print("QUESTION 6")
    rho_values = [0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4] # 0.5 < rho < 1.5
    p_loss_data = []
    avg_packets_data = []
    k_values = [10, 25, 50]
    L = 2000
    C = 1000000
    duration = 10

    for k in k_values:
        avg_packet_num_at_k = []
        p_loss_at_k = []
        for rho in rho_values:
            print(f"Running Simulation at K: {k}, Rho: {rho}")
            sim = SimulatorMM1K.SimulatorMM1K(L, duration, C, rho, k)
            print(f"this is the value for sim.En: {sim.En}")
            avg_packet_num_at_k.append(sim.En)
            print(f"this is the value for sim.p_loss: {sim.p_loss}")
            p_loss_at_k.append(sim.p_loss)
        
        p_loss_data.append(p_loss_at_k)
        avg_packets_data.append(avg_packet_num_at_k)

    print("Preparing Graphs")
    # Graph 1
    plt.title("PLoss vs Rho Values")
    plt.xlabel('Rho Value')
    plt.ylabel('PLoss')
    for i in p_loss_data:
        plt.plot(rho_values, i)
    plt.legend(['k = 10', 'k = 25', 'k = 50'], loc = 'upper left')
    # plt.show()
    plt.savefig('Question6-1.png', bbox_inches='tight')
    plt.close()
    
    # Graph 2
    plt.title("Average Number of Packets vs Rho Values")
    plt.xlabel('Rho Values')
    plt.ylabel('Average Number of Packets')
    for i in avg_packets_data:
        plt.plot(rho_values, i)
    plt.legend(['k = 10', 'k = 25', 'k = 50'], loc = 'upper left')
    # plt.show()
    plt.savefig('Question6-2.png', bbox_inches='tight')
    plt.close()


def main():
    print("Running ECE 358 Lab 1")
    question_1()
    question_3()
    question_4()
    question_6()


if __name__ == "__main__":
    main()
