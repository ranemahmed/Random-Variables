import numpy as np
import matplotlib.pyplot as plt

def discrete_uniform_pmf(k, a, b):
    if a <= k <= b:
        return 1 / (b - a + 1)
    else:
        return 0

def discrete_uniform_cdf(x, a, b):
    if x < a:
        return 0
    elif a <= x <= b:
        return (x - a + 1) / (b - a + 1)
    else:
        return 1

def discrete_uniform_variance(a, b):
    return ((b - a + 1)**2 - 1) / 12

def discrete_uniform_expectation(a, b):
    return (a + b) / 2

a = 1
b = 6
size = 10000
X = np.random.randint(a, b + 1, size=size)

unique_values, counts = np.unique(X, return_counts=True)
pmf_values = [discrete_uniform_pmf(k, a, b) for k in unique_values]

x_ecdf = np.sort(X)
y_ecdf = [discrete_uniform_cdf(x, a, b) for x in x_ecdf]

variance = discrete_uniform_variance(a, b)
expectation = discrete_uniform_expectation(a, b)

print("variance =", variance)
print("expectation =", expectation)

plt.bar(unique_values, pmf_values, align='center', alpha=0.7, width=0.5)
plt.xticks(unique_values)
plt.xlabel('X')
plt.ylabel('PMF')
plt.title(f'Probability Mass Function for Discrete Uniform Distribution ({a}-{b})')
plt.show()

plt.step(x_ecdf, y_ecdf, where='post', label='Empirical CDF')
plt.title(f'Cumulative Distribution Function for Discrete Uniform Distribution ({a}-{b})')
plt.xlabel('X')
plt.ylabel('CDF')
plt.legend()
plt.show()