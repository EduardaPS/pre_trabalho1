from statistics import mean, variance
from matplotlib import pyplot as plt
from numpy import histogram

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