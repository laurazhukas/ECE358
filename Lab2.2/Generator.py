import random
import math

def generate_exponential_random_var(lam):
    # random.seed()
    u = random.random()
    return -(1/lam)*math.log(1-u)

def generate_exp_backoff(backoff_counter):
    # random.seed() # TODO: do we need this...?
    r = random.randrange(0,(2**backoff_counter), 1)  # TODO: verify this is correct NOTE: no -1 because non-inclusive
    return r * (512/10**6)