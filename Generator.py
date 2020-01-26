import random
import math
import numpy as np

# def get_lambda(avg_packet_size):
#     return 1/avg_packet_size


# def gen_observer_times(lam:int):
#     # the observer times are at 5 times the rate of the packet arrival
#     # to achieve above you multiply lamda by 5
#     return generate_exponential_random_var(lam*5)


# def calculate_service_time(length: int, c: int):
#     # length passed in has unit bits
#     # C is transmission rate of the output link in bits per second
#     return length/c


def generate_exponential_random_var(lam):
    random.seed()
    u = random.random()
    return -(1/lam)*math.log(1-u)


# def generate_arrival_time(previous_arrival_time, lam):
#     arrival_time_delta = generate_exponential_random_var(lam)
#     return previous_arrival_time + arrival_time_delta


# def generate_packet_length(lam):
#     return generate_exponential_random_var(lam)


# def get_mean(exp_ran_var):
#     return np.mean(exp_ran_var)


# def get_variance(exp_ran_var):
#     return np.var(exp_ran_var)