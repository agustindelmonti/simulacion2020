import matplotlib.pyplot as plt
import random as rn
import math

from utils import *


def poisson(alpha):
    """Poisson process"""
    x = 0
    p = 1

    while p >= math.exp(-alpha):
        r = rn.random()
        p *= r
        x += 1

    return x


if __name__ == "__main__":
    _lambdas = [15, 7, 1]
    for l in _lambdas:
        data = []
        for i in range(10000):
            data.append(poisson(l))
        discrete_plot(data)

    plt.legend([f'λ={l}' for l in _lambdas])
    plt.show()
