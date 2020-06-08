from RandomGenerator import random_sample
import math
import seaborn as sns
import matplotlib.pyplot as plt

#Exponential generator
def exponencial(media, seed, n):
    sample = []
    lista = (random_sample(n, seed))
    for r in range(len(lista)):
        x = - media * math.log(lista[r])
        sample.append(x)
    return sample

#Main
seed = 4294966661
media = 9
n = 50
data = []
data = (exponencial(media, seed, n))

sns.distplot(data, kde=False, color="b")
plt.show()
