def lcg(a, c, m, initial_seed):
    seed = initial_seed
    while True:
        rand = (a * seed + c) % m
        seed = rand
        yield rand


def random_sample(n, seed):
    sample = []
    varAux = lcg(1103590199, 419329, (2 ** 32), seed)
    for i in range(n):
        observation = next(varAux) / (2 ** 32)
        sample.append(observation)

    return sample