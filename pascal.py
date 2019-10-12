from helpers import coef_binomial, bernoulli, monte_carlo
from matplotlib import pyplot as plt

def media_variancia_pmf(k: int, p: float):
    """
    faz o cálculo esperado da média, variância e pmf da distribuição de pascal

    :param k: número de sucessos
    :param p: probabilidade de sucesso
    """

    print('-' * 70)
    print(f'A média teórica da distribuição de pascal com k={k} e p={p} é de {k/p}')
    print(f'A variância teórica da distribuição de pascal com k={k} e p={p} é de {k*(1-p)/p**2}')
    print('-' * 70)
    pmf = [coef_binomial(n-1, k-1)*p**k*(1-p)**(n-k) for n in range(k, k+100)]
    for _ in range(k-1):
        pmf.insert(0, 0)
    f = plt.figure()
    plt.stem(pmf, use_line_collection=True)
    plt.title(f'PMF teórico da distribuição de pascal com k={k} e p={p}')
    f.show()


def rand_pascal(k: int, p: int):
    """
      retorna o valor da VA de acordo com a distribuição de pascal

      :param k: número de sucessos
      :param p: probabilidade de sucesso
      :return: número de jogadas necessárias para alcançar k sucessos
    """

    if p < 0 or p > 1:
        raise ValueError('Parâmetro p numa binomial precisa ser entre 0 e 1')
    if k < 0:
        raise ValueError('Parâmetro k numa binomial precisa ser maior ou igual a 0')

    sucessos = 0
    jogadas = 0
    while sucessos != k:
        jogadas += 1
        sucessos += bernoulli(p)    # pode se fazer a soma direto, porque se a bernoulli falhar o seu retorno é 0.
    return jogadas

if __name__ == '__main__':
    media_variancia_pmf(2, 1/2)
    media_variancia_pmf(5, 2/5)

    monte_carlo(rand_pascal, (2, 1/2), 100000, 'distribuição de pascal')
    monte_carlo(rand_pascal, (5, 2/5), 100000, 'distribuição de pascal')
