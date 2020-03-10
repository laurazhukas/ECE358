import random
import math

def generate_exponential_random_var(lam):
    random.seed()
    u = random.random()
    return -(1/lam)*math.log(1-u)

def generate_exp_backoff(backoff_counter):
    random.seed()
    r = random.randrange(0,(2**backoff_counter), 1)  # NOTE: do not subtract "1" because of non-inclusive bounds
    return r * (512/10**6)  # 512 is the bit time, 10**6 for scaling