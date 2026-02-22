# EXERCICIO CÁLCULO do PRIMEIRO DÍGITO do CPF
"""
CPF: 764.824.890-70
Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores por uma contagem regressiva começando de 10

EX: 746.824.890-70 (746824890)
10  9   8   7   6   5   4   3   2   
7   4   6   8   2   4   8   9   0
70  36  48  56  12  20  32  27  0

somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301

Multiplicar o resultado por 10
301 * 10 = 3010

Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7

Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
"""

cpf = input("Digite seu CPF: ")
print(f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]} ")

# calcula os nove digitos regressivamente
nove_digitos = cpf[:9]
contador_regressivo1 = 10

resultado_digito1 = 0
for digito_1 in nove_digitos:
    resultado_digito1 += int(digito_1) * contador_regressivo1
    contador_regressivo1 -= 1
digito_1 = (resultado_digito1 * 10) % 11

digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)


