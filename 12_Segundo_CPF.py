# EXERCICIO CÁLCULO do SEGUNDO DÍGITO do CPF
"""
CPF: 764.824.890-70
Colete a soma dos 9 primeiros digitos do CPF
MAIS O PRIMEIRO DIGITO
multiplicando cada um dos valores por uma contagem regressiva começando de 11

EX: 746.824.890-70 (746824890)
11  10  9   8   7   6   5   4   3   2   
7   4   6   8   2   4   8   9   0   7(primeiro digito)
77  40  54  64  14  24  40  36  0   14

somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363

Multiplicar o resultado por 10
363 * 10 = 3630

Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0

Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
"""

cpf = input("Digite os nove primeiros dígitos do seu CPF: ")

if len(cpf) > 9 or len(cpf) < 9:
    print("CPF inválido!")
else:
    #mostra o CPF formatado 
    print(f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}")
    verifica = input("Esses são os nove dígitos do seu CPF? [s]im  [n]ão: ").lower()

    if verifica == "s":
        #guarda os nove primeiros digitos do CPF
        nove_digitos = cpf[:9]
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
        print(f"Primeiro Digito: {digito_1}")

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
        print(f"Segundo Dígito: {digito_2}")

        print(f"Dois últimos digitos do seu CPF: {digito_1}{digito_2}")

        print(f"CPF completo:{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{digito_1}{digito_2} ")
    else:
        print("Tente novamente!")


# POSSIVEIS PROBLEMAS E SOLUÇÕES NO NOSSO CÓDIGO
"""
Se o usuário digitar o CPF com ponto, da erro
cpf = input("Digite os nove primeiros dígitos do seu CPF: ").replace('.', "") \
      .replace('-', '')  substitui o - por nada \
      .replace(',', '')  substitui o - por nada \

EXPRESSÃO REGULAR:
import re
cpf_corrigido = re.sub(r'[^0-9]'), '', cpf

"eu quero substituir tudo que não seja 0-9 e substituir por nada


- SE o usuário digitar várias vezes 111111111111
import sys

verifica = cpf == cpf[0] * len(cpf)
if  verifica:
    print("Você enviou dados sequênciais)
    sys.exit()
"""