# EXERCICIO
"""
Exiba os índices da lista:

0 - Maria
1- Helena
2- Luiz
"""

lista =["Maria", "Helena", "Luiz"]

i = 0
for nome in lista:
    print(f"{i} - {nome}" )
    i += 1


# ou

lista2 = lista
indices = range(len(lista2))

for indice in indices:
    print(f"{indice} - {lista2[indice]}")