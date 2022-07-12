# *args é um tipo de paramentro que não possui uma definição quantitativa, ou seja, a função pode receber
# varios argumetos que deveram ser tratados dentro da mesma

def func(*args):
    var1 = args  # var1 recebe uma tupla de *args

    var2 = []
    for i, v in enumerate(var1):  # a estrutura deve fazer o desempacotamento das variaveis
        var2.append(f'{v}')

    var3 = (tuple(var2))

    code = f'insert into table values {var3}'

    print(code)


func(3, 4, 5, 'fernando')
