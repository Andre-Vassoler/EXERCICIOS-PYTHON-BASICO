"""
Faça um algoritmo que peça ao usuário digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número inteiro, informa que não é um número inteiro
"""

numero_str = input("Digite um número: ")

try:    
    numero_int = int(numero_str)
    if numero_int % 2 == 0:
        print("O número é par")
    else:
        print("O número é impar")
except:
    print("Por favor, digite um número inteiro!")

# DIFERENÇA entre TRY/EXCEPT e IF/ELSE
# try/except - se pode quebrar (o usuário poderia não escrever um número (int))
# if/else - se é só decisão

# #if numero_str.isdigit():
#     #numero_int = int(numero_str)

#     if numero_int % 2 == 0:
#         print("O número é par")
#     else:
#         print("O número é ímpar")
# else:
#     print("Por favor, digite um número inteiro!")
#PODERIAMOS USAR ASSSIM, PORÉM O .isdigit() só funciona com números positivos e inteiros

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito,
exiba a saudação apropriada. 
Ex: Bim dia 0-11, Boa tarde 12-17 e Boa noite
"""

hora_str = (input("Digite a hora(ex:13): "))

try:
    hora_int = int(hora_str)

    if hora_int < 0 or hora_int > 24:
        print("Digite um horário válido")

    elif hora_int <= 11:
        print("Bom dia")

    elif hora_int <= 17:
        print("Boa tarde")

    else:
        print("Boa noite")

except ValueError:
    print("Digite um número válido")


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos
escreva "Seu nome è curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"
; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input("Digite o seu Primeiro Nome: ")
quantd_letras = len(nome)

if quantd_letras <= 4:
    print("Seu nome é muito curto")
elif quantd_letras <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")





