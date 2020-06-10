import random as rn

def bernoulli(p):
    r = rn.random()
    if r < p:
        return 1
    else:
        return 0