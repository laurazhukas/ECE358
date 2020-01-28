import random
import math


def generate_exponential_random_var(lam):
    random.seed()
    u = random.random()
    return -(1/lam)*math.log(1-u)
