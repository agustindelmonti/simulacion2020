import random as rn
import math
import numpy as np

from utils import *
from bernoulli import *

def geometric(p):
    """k trials of a Bernoulli event"""
    x = 1
    while bernoulli(p)!=1:
    	x+=1
    return x

def geometric_inverse(p):
    """Inverse transform method"""
    r = rn.random()
    return 1 +  math.floor(np.log(r)/np.log(1-p))


if __name__ == "__main__":
    success = [0.2]
    for s in success:
        data = []
        for i in range(10000):
            data.append(geometric(0.2))
        discrete_plot(data)

    plt.legend([f'p={s}' for s in success])
    plt.show()