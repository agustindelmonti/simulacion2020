
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
import pandas as pd
import math
import os

sns.set(style="darkgrid", palette="muted", color_codes=True)
np.random.seed()

# Hiperparametros del modelo
N = 10000
min = 0
max = 36
prob = 1 / (max - min)
results_path = f'./graphs/iter_{N}'


def simular():
    return np.random.randint(min, max + 1, N)


def mu_approx(data):
    mu = (max - min) / 2
    fig, ax = plt.subplots()

    # Aproximacion teorica
    plt.axhline(y=mu, xmin=0.0, xmax=1.0, label=f"µ = {format(mu, '.2f')}", color="r")

    accum_mean = []
    for k in range(1, len(data)):
        mean = np.mean(data[:k])
        accum_mean.append(mean)
    plt.plot(accum_mean, 'm-', label='promedio')

    ax.legend(loc='best')
    ax.set(xlabel='iteracion', ylabel='promedio', title=f'Promedio acomulado por tirada vs µ teorica \n (n = {N})')
    plt.tight_layout()
    fig.savefig(f"{results_path}/accum_mean{N}.png")
    plt.show()


def uniform_dist(data):
    fig, ax = plt.subplots()
    sns.distplot(data, color="m", bins=37, label='frec. relativa')
    plt.axhline(y=prob, xmin=0.0, xmax=1.0, label=f"prob. teorica (p = {format(prob, '.4f')})", color="r")

    ax.legend(loc='best')
    ax.set(ylabel='frecuencia relativa (fr)', title=f'Distribucion muestra (n = {N}) vs probabilidad')
    plt.tight_layout()
    fig.savefig(f"{results_path}/uniforme_{N}.png")
    plt.show()


def relative_freq(data, num):
    accum_relative_freq = np.zeros(N)

    for i in range(0, len(data) - 1):
        abs = accum_relative_freq[i] * i
        if data[i + 1] == num:
            abs += 1
        accum_relative_freq[i + 1] = abs / (i + 1)

    fig, ax = plt.subplots()
    df = pd.DataFrame(accum_relative_freq)
    sns.lineplot(data=df[0], color="m", label='frec. relativa')

    plt.axhline(y=prob, xmin=0.0, xmax=1.0, label=f"prob. teorica (p = {format(prob, '.4f')})", color="r")

    ax.legend(loc='best')
    ax.set(ylabel='frecuencia relativa (fr)', xlabel='iteracion',
           title=f'Frecuencia relativa vs probabilidad \n x = {num} (n = {N})')
    fig.savefig(f"{results_path}/accum_relative_freq_{N}.png")
    plt.show()


def std_approx(data):
    sigma = (max - min) / math.sqrt(12)
    fig, ax = plt.subplots()

    # Aproximacion teorica
    plt.axhline(y=sigma, xmin=0.0, xmax=1.0, label=f"σ = {format(sigma, '.2f')}", color="r")

    accum_std = []
    for k in range(1, len(data)):
        std = np.std(data[:k])
        accum_std.append(std)
    plt.plot(accum_std, 'm-', label='Desviacion standard')

    ax.legend(loc='best')
    ax.set(xlabel='iteracion', ylabel='desviacion standard', title=f'Desviacion standard acomulada por tirada vs σ teorica \n (n = {N})')
    plt.tight_layout()
    fig.savefig(f"{results_path}/accum_std{N}.png")
    plt.show()


if __name__ == "__main__":
    tirada = simular()

    if not os.path.exists(results_path):
        os.makedirs(results_path)

    mu_approx(tirada)
    uniform_dist(tirada)
    relative_freq(tirada, 6)
    std_approx(tirada)
