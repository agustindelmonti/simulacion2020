import random as rn
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("white")


def uniform(a, b):
    r = rn.random()
    return r*(b-a) + a


if __name__ == "__main__":
    data = []
    for i in range(10000):
        data.append(uniform(3,8))
    sns.distplot(data, kde=False)
    plt.show()
