# filter

'''def pares(i):
    if i % 2 == 0:
        return i
'''

lista = [i for i in range(10)]

# lista_pares = filter(pares, lista)
lista_pares = filter(lambda i: i % 2 == 0, lista)

print(list(lista_pares))
