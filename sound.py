from matplotlib import pyplot as plt
import numpy as np
plt.xkcd()
# plt.style.use("seaborn-dark-palette")
R = 8.3144598

def max(table):
    value = 0
    output = 0
    for i, item in enumerate(table):
        if item > value:
            value = item
            output = i
    print(output)
    return output

def min(table):
    value = 1e6
    output = 0
    for i, item in enumerate(table):
        if item < value:
            value = item
            output = i
    print(output)
    return output

def v0(v, T):
    return v * (273 / T) ** 0.5

def molar_mass(molar_mass, perc):
    output = 0
    for i, element in enumerate(molar_mass):
        output += element * perc[i]
    return output

def Kappa(v, mi, T):
    return 0.001 * v ** 2 * mi / (R * T)




offset = 320

data = np.array([
    335.311,
    338.58,
    340.6,
    332.71,
    349.86,
    346.39,
    341.1,
    339.7,
    341.96,
    338.688,
    341.145,
    342.314,
    343.728,
    342.88,
    343.064,
    344.23,
    342.637,
    344.043,
    342.332
])

freq = np.array([
    613,
    627,
    650,
    679,
    714,
    737,
    758,
    790,
    830,
    882,
    945,
    998,
    2016,
    2143,
    2257,
    2374,
    2501,
    2667,
    2806
])
d_min = min(data)
data = np.delete(data, d_min)
freq = np.delete(freq, d_min)

d_min = min(data)
data = np.delete(data, d_min)
freq = np.delete(freq, d_min)

d_max = max(data)
data = np.delete(data, d_max)
freq = np.delete(freq, d_max)

d_max = max(data)
data = np.delete(data, d_max)
freq = np.delete(freq, d_max)

for i in range(len(data)):
    data[i] -= offset


std = np.std(data + offset)
mean = (data + offset).mean()
T = 21+273
m_mass = molar_mass(
    [28, 32, 39.95],
    [0.78, 0.2095, 0.0093]
)



plt.bar(
    range(1, len(data)+1),
    data,
    yerr=2 * std,
    bottom=offset,
    color="#0000cc"
)


print(f"\n\nStandarad deviation: {std}, mean: {mean}\n\n")
print(f"speed in 0 degrees: {v0(mean, T)}")
print(f"molar mass of air is {m_mass}")
print(f"Kappa is: {Kappa(mean, m_mass, T)}\n\n")

plt.axhline((data+offset).mean(), color="red", linestyle='--', label="wartość średnia")
plt.xticks(range(0, len(data) + 1, 5))

plt.legend()

plt.title("Wyznaczanie prędkości dźwięku")
plt.xlabel("Numer pomiaru")
plt.ylabel("prędkość dźwięku [m/s]")

plt.tight_layout()

plt.show()
