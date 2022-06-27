def soma(a, b):
    return a + b


def func(funcao, multiplicador, n1, n2):  # função soma passada como parametro
    somador = funcao(n1, n2)  # função soma incorporada indiretamente
    soma = 0
    for i in range(multiplicador):
        soma += somador

    return soma


print(func(soma, 5, 4, 2))
