import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import math

out_folder = './results'

# Hiperparametros del modelo
min = 0
max = 37
prob = 1 / (max - min)


def distribution(df):
    fig, axes = plt.subplots(1, 1, figsize=(6, 3), sharex=True)
    sns.distplot(df, color="m", bins=37, label='frec. relativa')

    axes.axhline(prob, color='red', ls='--', alpha=0.5,
                 label=f"p = {format(prob, '.4f')}")

    axes.legend(loc='lower center')
    axes.set_ylabel("frec. relativa")
    plt.tight_layout()
    fig.savefig(f"{out_folder}/distr.png")


if __name__ == "__main__":
    df = pd.read_csv("./results/out.txt", header=None)
    sns.set(style="darkgrid", palette="muted", color_codes=True)
    distribution(df)