import matplotlib.pyplot as plt
import random as rn

from utils import *


def bernoulli(p):
    r = rn.random()
    if r < p:
        return 1
    else:
        return 0


def binomial(n, p):
    """n trials of a Bernoulli event"""
    x = 0
    for i in range(n):
        x += bernoulli(p)
    return x


if __name__ == "__main__":
    params = [(10, .8), (6, .4)]
    for p in params:
        data = []
        for i in range(10000):
            data.append(binomial(p[0], p[1]))
        discrete_plot(data)

    plt.legend([f'n={p[0]} p={p[1]}' for p in params])
    plt.show()
