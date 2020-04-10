import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import math

out_folder = './results'

# Hiperparametros del modelo
min = 0
max = 37
num = 7

prob = 1 / (max - min)
mu = (max - min -1) / 2
sigma = (max - min) / math.sqrt(12)


def params(freq, mean, std, file):
    fig, axes = plt.subplots(3, 1, figsize=(10, 6), sharex=True)

    # f'Frecuencia relativa vs probabilidad \n x = {num} (n = {N})'
    sns.lineplot(data=freq, ax=axes[0], legend=False,  dashes=False)
    axes[0].set_ylabel('freq ')
    axes[0].axhline(prob, color='black', ls='--', alpha=0.3,
                    label=f"p = {format(prob, '.4f')}")
    axes[0].legend(loc='best')

    # f'Promedio acomulado por tirada vs µ teorica \n (n = {N})'
    sns.lineplot(data=mean, ax=axes[1], legend=False,  dashes=False)
    axes[1].set_ylabel('prom')
    axes[1].axhline(mu, color='black', ls='--', alpha=0.3,
                    label=f"µ = {format(mu, '.2f')}")
    axes[1].legend(loc='best')

    # f'Desviacion standard acomulada por tirada vs σ teorica \n (n = {N})'
    sns.lineplot(data=std, ax=axes[2], legend=False,  dashes=False)
    axes[2].set_ylabel('std')
    axes[2].axhline(sigma, color='black', ls='--', alpha=0.5,
                    label=f"σ = {format(sigma, '.2f')}")
    axes[2].legend(loc='best')

    fig.savefig(f"{out_folder}/stats_{file}.png")


if __name__ == "__main__":
    df = pd.read_csv("./results/out.txt", header=None)
    sns.set(style="darkgrid", palette="muted", color_codes=True)

    data = df.T
    series = data.expanding()
    mean, std = series.mean(), series.std()

    # Cuenta las ocurrencias historicas del numero num
    freq = series.apply(lambda x: np.count_nonzero(x == num)).apply(lambda x: pd.Series(x).div(x.index + 1))

    params(freq, mean, std, "")

    # Promedio acomulados de parametros entre simulaciones
    freq, mean, std = freq.mean(axis=1), mean.mean(axis=1), std.mean(axis=1)
    params(freq, mean, std, "joined")
