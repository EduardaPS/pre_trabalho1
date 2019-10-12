from statistics import mean, variance
from matplotlib import pyplot as plt
from numpy import histogram
from math import factorial
from random import random # Função que retorna um número uniformemente distribuído entre 0 e 1
                          # não vou codificar isso :(

def monte_carlo(func, params: tuple, n: int, titulo: str):
    # res = []
    # for _ in range(n):
    #     res.append(func(*params))
    res = [func(*params) for _ in range(n)]     # Roda a função n vezes
    print('-'*70)
    print(f'A média simulada de uma {titulo} para os parâmetros {params} é de {mean(res)}')
    print(f'A variância simulada de uma {titulo} para os parâmetros {params} é de {variance(res)}')
    print('-'*70)

    hist = histogram(res, bins=range(max(res)+1))[0]
    pmf = hist/n
    f = plt.figure()
    plt.stem(pmf, use_line_collection=True)
    plt.title(f'PMF simulado de uma {titulo} com parâmetros {params}')
    f.show()

def bernoulli(p: float) -> bool:
    if p < 0 or p > 1:
        raise ValueError('Parâmetro p numa bernoulli precisa ser entre 0 e 1')

    return random() < p

def coef_binomial(n: int, k: int) -> float:
    return factorial(n)/(factorial(k)*factorial(n-k))