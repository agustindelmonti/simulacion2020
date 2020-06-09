import seaborn as sns
import matplotlib.pyplot as plt
import random as rn
import numpy as np

from utils import *


def empirical_discrete(fx):
    """ Discrete custom categorization"""
    cum = np.cumsum(fx)  # Cumulative distribution from density function
    r = rn.random()
    for i in range(len(cum)):
        if r < cum[i]:
            return i


if __name__ == "__main__":
    fx0 = [.11, .12, .09, .08, .12, .1, .09, .09, .1, .1]
    fx1 = [.2, .3, .4, .1]

    data = []
    for i in range(10000):
        data.append(empirical_discrete(fx0))

    discrete_plot(data)
    plt.show()
