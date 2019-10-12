from matplotlib import pyplot as plt
from helpers import monte_carlo, bernoulli, coef_binomial


def media_variancia_pmf(n: int, p: float):
    print('-'*70)
    print(f'A média teórica da distribuição binomial com n={n} e p={p} é de {n*p}')
    print(f'A variância teórica da distribuição binomial com n={n} e p={p} é de {n*p*(1-p)}')
    print('-'*70)
    pmf = [coef_binomial(n, k)*p**k*(1-p)**(n-k) for k in range(n+1)]
    f = plt.figure()
    plt.stem(pmf, use_line_collection=True)
    plt.title(f'PMF teórico da binomial com n={n} e p={p}')
    f.show()


def rand_binom(n: int, p: float) -> int:
    if p < 0 or p > 1:
        raise ValueError('Parâmetro p numa binomial precisa ser entre 0 e 1')
    if n < 0:
        raise ValueError('Parâmetro n numa binomial precisa ser maior ou igual a 0')

    nSucessos = 0
    for _ in range(n):
        if bernoulli(p):
            nSucessos += 1
    return nSucessos


if __name__ == '__main__':
    media_variancia_pmf(10, 1/10)
    media_variancia_pmf(50, 1/4)

    monte_carlo(rand_binom, (10, 1/10), 100000, 'binomial')
    monte_carlo(rand_binom, (50, 1/4), 100000, 'binomial')
    input()