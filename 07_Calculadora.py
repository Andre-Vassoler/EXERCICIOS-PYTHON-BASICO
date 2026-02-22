# CALCULADORA COM WHILE

while True: #calculadora infinita (loop)
    numero1 = input("Digite um número: ")
    numero2 = input("Digite outro número: ")
    operador = input("Digite o operador desejado(+-*/): ")

    numeros_validos = None  #bandeira (flag)

    try:
        num1_float = float(numero1)
        num2_float = float(numero2)
        numeros_validos = True
    except: #Exception as error:
        #print(error) para saber qual erro deu
        numeros_validos = None
    
    if numeros_validos is None:
        print("Um ou ambos os números inseridos são inválidos")
        continue #pois se os dados n estão certos, ele para e volta pro inicio
    
    operadores_permitidos = "+-*/"
    if operadores_permitidos not in operadores_permitidos:
        print("Operador inválido")
        continue
    if len(operador) > 1:
        print("Digite apenas um operador!")
        continue

    if operador == "+":
        soma = num1_float + num2_float
        print(f"A soma dos números {numero1} e {numero2} = {soma}")
    elif operador == "-":
        subtracao = num1_float - num2_float
        print(f"A subtração dos números {numero1} e {numero2} = {subtracao}")
    elif operador == "*":
        multiplicacao = num1_float * num2_float
        print(f"A multiplicação dos números {numero1} e {numero2} = {multiplicacao}")
    elif operador == "/":
        divisao = num1_float / num2_float
        print(f"A divisão dos números {numero1} e {numero2} = {divisao}")
    else:
        print("Digite um operador válido")

    sair = input("Quer sair? [s]im ").lower().startswith("s")
    # .lower() - retorna sempre em letra minuscula
    # .startwith("s) - se começa com "s" (True)
    if sair is True:
        break 
    
