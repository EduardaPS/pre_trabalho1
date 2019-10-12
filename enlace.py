from pascal import rand_pascal
from binomial import rand_binom
from statistics import mean

def com_codificador(pacotes: int, p: float, n: int):
    """
    Simula transmissões por um enlace digital com um codificador que adiciona 4 pacotes de redundância.
    O número de pacotes recebidos em cada transmissão distribui-se de acordo com a binomial

    :param pacotes: número de pacotes a ser enviado pelo enlace
    :param p: probabilidade de sucesso de cada pacode chegar ao destino
    :param n: número de experimentos
    """

    total = pacotes+4
    pacotes_recebidos = [rand_binom(total, p) for _ in range(n)]

    media = mean(pacotes_recebidos)
    arquivos_sucesso = len(list(filter(lambda x: x >= pacotes, pacotes_recebidos)))
    prob_sucesso = arquivos_sucesso/n

    print('-' * 70)
    print(f'A média de pacotes recebidos pelo enlace é de {media}')
    print(f'A probabilidade do arquivo ser recuperado é de {prob_sucesso}')
    print('-' * 70)


if __name__ == '__main__':
    com_codificador(16, 0.9, 10000)