import random
import math

def generate_exponential_random_var(lam):
    random.seed()
    u = random.random()
    return int(-(1/lam)*math.log(1-u)*100)

def exponential_backoff(backoff_counter):
    random.seed()
    r = random.randrange(0,(2**backoff_counter), 1)  # TODO: verify this is correct NOTE: no -1 because non-inclusive
    return int(r*512) # NOTE: 512 bit time

