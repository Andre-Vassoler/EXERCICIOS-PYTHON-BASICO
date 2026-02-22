"""
EXERCICIO
Peça ao usuário para digitar seu nome e sua idade.
Se seu nome e idade forem digitados:
    Exiba:
    Seu nome é:
    Seu nome invertido é:
    Seu nome contém (ou não) espaços
    Seu nome tem (n) letras
    A primeira letra do seu nome é
    a ultima letra do seu nome é:
Se nada for digitado em nome ou idae:
    exiba "Desculpe, você deixou campos vazios
"""

nome = input("Digite seu nome: ") 
idade = input("Digite sua idade: ") 

espaco = " "

if nome and idade != "":
    int_idade = int(idade)
    print(f"Seu nome é: {nome}")
    print(f"Seu nome invertido é: {nome[::-1]}")
    if not espaco in nome:
        print("Seu nome não tem espaço(s)")
    else:
        print("Seu nome tem espaço(s)")
    print(f"Seu nome tem {len(nome)} letras")
    print(f'A primeira letra do seu nome é: "{nome[0]}"')
    print(f'A última letra do seu nome é: "{nome[-1]}"')
else:
    print("Desculpe, mas você deixou campos vazios")
