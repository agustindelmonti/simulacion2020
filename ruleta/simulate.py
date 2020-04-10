import sys
import os
import numpy as np
import pandas as pd

out_folder = './results'
min = 0
max = 36

if not os.path.exists(out_folder):
    os.makedirs(out_folder)

M = int(sys.argv[1])
N = int(sys.argv[2])

simulations = []
for i in range(M):
    # Generate a different random seed for every simulation run
    np.random.seed()
    throw = np.random.randint(min, max + 1, N)

    simulations.append(throw)

df = pd.DataFrame(simulations)
df.to_csv(f'./results/out.txt', index=False, header=False)
