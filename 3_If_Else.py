# EXERCÍCIO COM IF e COMPARAÇÃO
# criar um código que o usuáro digita dois números e a gente fala se são iguais ou diferentes

print("COMPARAÇÃO DE NÚMEROS")
numero1 = input("Digite um Número: ")
numero2 = input("Digite outro Número: ")

int_numero1 = int(numero1)
int_numero2 = int(numero2)

if int_numero1 > int_numero2:
    print("O primeiro número(", int_numero1, ") é maior do que o segundo número(", int_numero2, ")")
elif int_numero1 < int_numero2:
    print("O segundo número(", int_numero2, ") é maior que o primeiro número(", int_numero1, ")")
else:
    print("Os números inseridos são iguais")
print("fim do programa")

"""
poderia ser:
print(
f"{int_numero1} é maior que {int_numero2}

)
"""