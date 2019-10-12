from helpers import coef_binomial, bernoulli, monte_carlo
from matplotlib import pyplot as plt

def media_variancia_pmf(k: int, p: float):
    print('-' * 70)
    print(f'A média teórica da distribuição de pascal com k={k} e p={p} é de {k/p}')
    print(f'A variância teórica da distribuição de pascal com k={k} e p={p} é de {k*(1-p)/p**2}')
    print('-' * 70)
    pmf = [coef_binomial(n - 1, k - 1) * p ** k * (1 - p) ** (n - k) for n in range(k, k + 100)]
    f = plt.figure()
    plt.stem(range(k, k+100), pmf, use_line_collection=True)
    plt.title(f'PMF teórico da distribuição de pascal com k={k} e p={p}')
    f.show()


def rand_pascal(k: int, p: int):
    if p < 0 or p > 1:
        raise ValueError('Parâmetro p numa binomial precisa ser entre 0 e 1')
    if k < 0:
        raise ValueError('Parâmetro k numa binomial precisa ser maior ou igual a 0')

    sucessos = 0
    jogadas = 0
    while sucessos != k:
        jogadas += 1
        if bernoulli(p):
            sucessos += 1
    return jogadas

if __name__ == '__main__':
    media_variancia_pmf(2, 1/2)
    media_variancia_pmf(5, 2/5)

    monte_carlo(rand_pascal, (2, 1/2), 100000, 'distribuição de pascal')
    monte_carlo(rand_pascal, (5, 2/5), 100000, 'distribuição de pascal')
