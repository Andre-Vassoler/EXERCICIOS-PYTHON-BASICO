# EXERCICIO LISTA DE COMPRAS
"""
Faça uma lista de compras com listas.
O usuário deve ter a possibilidade de inseir, apagar, e listar valores da sua lista.
Não permita que o programa quebre com erros de índices inexistentes na lista
"""

lista = []  #armazena os itens

while True:
    print("Selecione uma opção: ")
    opcao = input("[i]nserir  [a]pagar  [l]istar  [s]air: ").lower()

    if opcao == "i":
        item = input("Digite o item que deseja inserir: ")
        lista.append(item)  #adiciona item

    elif opcao == "a":
        apagar = input("Qual índice deseja apagar?: ")
        try:
            apagar_int = int(apagar)
            del lista[apagar_int]   #delete item
        except:
            print("Digite um índice válido!")
    
    elif opcao == "l":
        for a, b in enumerate(lista):   #enumera a lista
            print(a, b)     #mostra a lista

    elif opcao == "s":
        break       #sai do programa

    else:
        print("Digite uma opção válida!")   