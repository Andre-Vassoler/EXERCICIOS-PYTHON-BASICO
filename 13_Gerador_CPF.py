# CRIANDO UM GERADOR DE CPFs com nosso algoritmo e Python

import random
# print(random.dandint(0, 9))

nove_digitos = ""
for i in range(9):  #cria 9 vezes
    nove_digitos += str(random.randint(0, 9))   #cria números aleatórios de 0 a 9


# calcula os nove digitos regressivamente
#começa com 10 e ai vai diminuindo
contador_regressivo1 = 10

#variavel que aramzena a soma dos cáculos
resultado_digito1 = 0
for digito_1 in nove_digitos:
    resultado_digito1 += int(digito_1) * contador_regressivo1
    contador_regressivo1 -= 1
digito_1 = (resultado_digito1 * 10) % 11

#se o resultado for maior que 9, vira 0
digito_1 = digito_1 if digito_1 <= 9 else 0


# SEGUNDO DÍGITO
#cálcula os dez digitos regressivamente
dez_digitos = nove_digitos +str(digito_1)
#começa com 11
contador_regressivo2 = 11

resultado_digito2 = 0
for digito_2 in dez_digitos:
    resultado_digito2 += int(digito_2) * contador_regressivo2
    contador_regressivo2 -= 1
digito_2 = (resultado_digito2 * 10) % 11

digito_2 = digito_2 if digito_2 <= 9 else 0

#imprime o CPF
print(f"{nove_digitos}-{digito_1}{digito_2}")

"""
Para criar 100 CPFs é só fazer isso:
import random

for _ in range(100):
    nove_digitos = ""
    for i in range(9):
        ...
    ...

e so dar um tab
"""
