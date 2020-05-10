from random import randint

# Metodo de los cuadrados
data = [[0 for i in range(3)] for i in range(100)]

data[0][0] = 9731
data[0][2] = str(data[0][0] ** 2)

if len(data[0][2]) < 8:
    data[0][2] = ("0" * (8 - len(data[0][2]))) + data[0][2]

data[1][0] = data[0][2][2:-2]

for fila in range(1, len(data) - 1):

    data[fila][1] = "0." + data[fila][0]

    data[fila][2] = str(int(data[fila][0]) ** 2)
    if len(data[fila][2]) < 8:
        data[fila][2] = ("0" * (8 - len(data[fila][2]))) + data[fila][2]

    data[fila + 1][0] = data[fila][2][2:-2]

for fi in data:
    print(str(fi[0]) + " , " + str(fi[1]) + " , " + str(fi[2]) )


# chi2
k = 10
n = 100

freqs = [[0 for i in range(k)] for i in range(k)]

for i in range(1, k + 1):
    maxI = i / k
    minI = maxI - (1 / k)
    for j in range(1, k + 1):
        maxJ = j / k
        minJ = maxJ - (1 / k)
        for d in data:

            if int(d[0]) < maxI and int(d[0]) >= minI and int(d[1]) < maxJ and int(d[1]) >= minJ:
                freqs[i - 1][j - 1] += 1

chi2 = ((k ** 2) / n) * sum([sum((i - (n / (k ** 2))) ** 2 for i in row) for row in freqs])

print("chi2 = " + str(chi2))

# GCL
n = 100
a = 5
c = 3
m = 16

data = [0 for i in range(n)]
data[0] = 7

for i in range(1, len(data) - 1):
    data[i] = ((a * data[i - 1]) + c) % m

for i in data:
    print(i)

# chi2
k = 20


def gen_chi2(data_arr):
    freqs = [0 for i in range(k)]

    for i in range(1, k + 1):
        max = i / k
        min = max - (1 / k)
        for d in data_arr:
            if d < max and d >= min:
                freqs[i - 1] += 1

    chi2 = (k / n) * sum([(i - (n / k)) ** 2 for i in freqs])
    return chi2


chi2 = gen_chi2(data)
print("chi2 = " + str(chi2))