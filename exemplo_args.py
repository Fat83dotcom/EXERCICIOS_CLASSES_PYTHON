# *args é um tipo de paramentro que não possui uma definição quantitativa, ou seja, a função pode receber
# varios argumetos que deveram ser tratados dentro da mesma

def func(*args):
    var1 = args  # var1 recebe uma tupla de *args

    for v in var1:  # a estrutura deve fazer o desempacotamento das variaveis
        print(v)


func(3, 4, 5, 'fernando')
