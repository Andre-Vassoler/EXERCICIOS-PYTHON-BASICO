# EXERCICIO COM WHILE
#imprimir cada letra de um nome

nome = input("Digite seu nome: ")

qnt_letra = len(nome)

vr = 0
while vr < qnt_letra:
    print(nome[vr])
    vr += 1
 
# ou 
vr2 = 0
nome_separado = ""
while vr2 < len(nome):
    letra = nome[vr2]
    nome_separado += f"*{letra}"
    vr2 += 1
print(nome_separado)