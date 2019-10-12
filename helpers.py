from statistics import mean, variance
from matplotlib import pyplot as plt
from numpy import histogram
from math import factorial
from random import random # Função que retorna um número uniformemente distribuído entre 0 e 1
                          # não vou codificar isso :(

def monte_carlo(func, params: tuple, n: int, titulo: str):
    """
    função genérica que realiza uma simulação de monte carlo para uma outra função qualquer.

    foi escolhido fazer desta maneira para evitar repetição no código, utilizando isso em
    ambas as questões que pediram monte carlo.

    :param func: função a ser testada, deve ter como valor de retorno um número inteiro
    :param params: tupla contendo os parâmetros a serem passados para a função func
    :param n: número de experimentos a serem realizados na monte carlo
    :param titulo: string genérica para ser passada ao título das figuras
    """

    # res = []
    # for _ in range(n):
    #     res.append(func(*params))
    res = [func(*params) for _ in range(n)]     # Roda a função n vezes, colocando os valores de retorno na lista
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


def bernoulli(p: float) -> int:
    """
    retorna o resultado da VA de acordo com a bernoulli

    a função random(), em python, retorna um número uniformemente distribuído entre 0 e 1
    pode-se fazer uma bernoulli utilizando este valor pseudo-aleatório, comparando-o com p
    se ele estiver abaixo de p, a bernoulli é sucesso, se estiver acima, é fracasso.

    :param p: probabilidade de sucesso
    :return: sucesso (1) ou fracasso (0), de acordo com a probabilidade
    """

    if p < 0 or p > 1:
        raise ValueError('Parâmetro p numa bernoulli precisa ser entre 0 e 1')

    return int(random() < p)


def coef_binomial(n: int, k: int) -> float:
    """
    retorna o coeficiente binomial

    :return: coeficiente binomial de n e k
    """

    return factorial(n)/(factorial(k)*factorial(n-k))