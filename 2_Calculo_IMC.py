"""
EXERCICIO - CÁLCULO IMC (Indice de Massa Corpórea)
"""

#calculo IMC: peso(kg) / altura ao quadrado (altura * altura)
nome = "André Fiordiluglio Vassoler"
altura = 1.75
peso = 60.0
imc = peso / (altura * altura)  #pode ser calculado assim
imc2 = peso / (altura ** 2)     #ou assim

print("IMG:", imc)
print("IMG:", imc2)

print(nome, "\ntem:", altura, "de altura", "\npesa:", peso, "kg", "\nPortanto, seu IMC é:", imc)
