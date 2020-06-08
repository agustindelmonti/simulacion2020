import math
import seaborn as sns
import matplotlib.pyplot as plt

# LCG Implementation
def lcg(a, c, m, initial_seed):
    seed = initial_seed
    while True:
        rand = (a * seed + c) % m
        seed = rand
        yield rand

def random_sample(seed):
    sample = []
    varAux = lcg(1103590199, 419329, (2 ** 32), seed)
    for i in range(100):
        observation = next(varAux) / (2 ** 32)
        sample.append(observation)

    return sample

#Exponential generator
def exponencial(media, seed):
    sample = []
    array = (random_sample(seed))
    for r in range(len(array)):
        x = - media * math.log(array[r])
        sample.append(x)
    return sample

#Main
seed = 4294966661
media = 9
data = []
data = (exponencial(media, seed))

sns.distplot(data, kde=False, color="b")
plt.show()
