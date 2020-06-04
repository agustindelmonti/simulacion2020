import seaborn as sns
import random as rn
import matplotlib.pyplot as plt
import math


def rand_triangular(a, b, c):
    """
    Random triangular distribution generator
    a,b,c max, min and mode where a<c<b
    """
    prop = (c - a) / (b - a)
    r = rn.random()

    if r < prop:
        return math.sqrt(r * (c - a) * (b - a)) + a
    else:
        return -math.sqrt((1 - r) * (b - c) * (b - a)) + b


if __name__ == "__main__":
    data = []
    for i in range(10000):
        data.append(rand_triangular(1, 7, 5))
    sns.distplot(data, kde=False, color="b")
    plt.show()
