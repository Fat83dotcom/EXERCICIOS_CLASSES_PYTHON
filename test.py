def func(**kwargs):
    dados = (kwargs)
    for i, u in dados.items():
        print(i)


print(func(rua='casa', fepartamento='eee', numero=8888))
