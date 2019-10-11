from math import factorial
from random import random # Função que retorna um número uniformemente distribuído entre 0 e 1
                          # não vou codificar isso :(

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
    print(rand_binom(10, 1/10))