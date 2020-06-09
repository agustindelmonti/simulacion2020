import random as rn
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def exp(alpha):
    r = rn.random()
    return -np.log(r)/alpha


if __name__ == "__main__":
    alphas = [.8]
    for a in alphas:
        data = []
        for i in range(100000):
            data.append(exp(a))
        sns.distplot(data, kde=False)

    plt.legend([f'α={a}' for a in alphas])
    plt.show()