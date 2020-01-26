import Generator
import statistics
import numpy as np
import Simulator
import SimulatorK
import matplotlib.pyplot as plt

def question_1 ():
    print("QUESTION 1")
    num_list = []
    for i in range(0, 1000):
        num_list.append(Generator.generate_exponential_random_var(75))
    mean = statistics.mean(num_list)
    print(f"The random variable mean is: {mean}")

def question_3 ():
    print("QUESTION 3")
    rho_values = [0.35, 0.45, 0.55, 0.65, 0.75, 0.85] # 0.25 < rho < 0.95
    average_num_pkts = []
    p_idle = []
    L = 2000
    C = 1000000
    duration = 10
    for rho in rho_values:
        print(f"Running Simulation at Rho: {rho}")
        sim = Simulator.Simulator(L, duration, C, rho)
        print(f"this is the value for sim.En: {sim.En}")
        average_num_pkts.append(sim.En)
        print(f"this is the value for sim.En: {sim.p_idle}")
        p_idle.append(sim.p_idle)
    print("Preparing Graphs")
    # plt.title("Rho Values vs Average Number of Packets")
    # plt.plot(rho_values, average_num_pkts)
    # plt.show()
    # plt.plot(rho_values, p_idle)
    # plt.show()


def question_4 ():
    print("QUESTION 4")
    rho_value = 1.2
    L = 2000
    C = 1000000
    duration = 1000
    print(f"Running Simulation at Rho: {rho_value}")
    sim = Simulator.Simulator(L, duration, C, rho_value)
    print(f"Average number of packets: {sim.En}")
    print(f"Average number of packets: {sim.p_idle}")


def question_6 ():
    print("QUESTION 6")
    rho_values = [0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4] # 0.5 < rho < 1.5
    k_values = [10, 25, 50]
    average_num_pkts = []
    p_loss = []
    L = 2000
    C = 1000000
    duration = 10
    for k in k_values:
        for rho in rho_values:
            print(f"Running Simulation at Rho: {rho}")
            sim = SimulatorK.SimulatorK(L, duration, C, rho, k)
            print(f"this is the value for sim.En: {sim.En}")
            average_num_pkts.append(sim.En)
            print(f"this is the value for sim.p_loss: {sim.p_loss}")
            p_loss.append(sim.p_loss)
        print("Preparing Graphs")
        # plt.title("Rho Values vs Average Number of Packets")
        # plt.plot(rho_values, average_num_pkts)
        # plt.show()
        # plt.plot(rho_values, p_loss)
        # plt.show()



def main ():
    print("Running ECE 358 Lab 1")
    question_1()
    question_3()
    # question_4()
    # question_6()

if __name__ == "__main__":
    main()