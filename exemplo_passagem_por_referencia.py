var1 = [4, 6, 7, 8, 9, 12]


def multiplicadorDeArrays(array, multiplicador):
    for i, n in enumerate(array):
        array[i] = n * multiplicador


multiplicadorDeArrays(var1, 10)


print(var1)
