from math import factorial
from matplotlib import pyplot as plt
from random import random # Função que retorna um número uniformemente distribuído entre 0 e 1
                          # não vou codificar isso :(


def coef_binomial(n, k):
    return factorial(n)/(factorial(k)*factorial(n-k))

#TODO: Ver com o professor se pode ser feito assim.
def media_variancia_pmf(n, p):
    media = n*p
    var = n*p*(1-p)
    pmf = [coef_binomial(n, k)*p**k*(1-p)**(n-k) for k in range(n+1)]

    print('-'*70)
    print(f'A média da distribuição binomial com n={n} e p={p} é de {media}')
    print(f'A variância da distribuição binomial com n={n} e p={p} é de {var}')
    print('-'*70)
    f = plt.figure()
    plt.stem(pmf, use_line_collection=True)
    plt.title(f'PMF teórico da binomial com n={n} e p={p}')
    f.show()


def bernoulli(p):
    if p < 0 or p > 1:
        raise ValueError('Parâmetro p numa bernoulli precisa ser entre 0 e 1')

    return random() < p

def rand_binom(n, p):
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

    input()