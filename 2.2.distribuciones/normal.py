import math
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from uniform import *
sns.set_style("white")


def normal(mu=0, sigma=1):
    """Box-Muller method"""
    s = 0
    while s == 0 or s >= 1:
        u = uniform(-1, 1)
        v = uniform(-1, 1)
        s = u ** 2 + v ** 2

    k = math.sqrt(np.log(s) * (-2) / s)
    z1 = u * k * sigma + mu
    z2 = v * k * sigma + mu
    return z1, z2


if __name__ == "__main__":
    x, y = [], []
    data = []
    mu = 0
    sigma = 1
    for i in range(10000):
        u, v = normal(mu, sigma)
        x.append(u)
        y.append(v)

    sns.jointplot(x, y, kind="hex", color="#4CB391")
    plt.show()

    data = x + y
    sns.distplot(data, kde=False)
    plt.show()
