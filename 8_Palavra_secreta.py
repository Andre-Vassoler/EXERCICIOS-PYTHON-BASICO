# JOGO DA PALAVRA SECRETA
"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    - se a letra digitada estiver vna palavra secreta; exiba a letra
    - Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do usuário
"""
print("JOGO DA PALAVRA SECRETA".center(40, "!"))
palavra_secreta = "Programador".lower()
letras_acertadas = "" #guarda as letras acertadas
repeticoes = 0

#loop infinito
while True:
    letra = input(f"Digite uma letra({repeticoes}°): ").lower()
    repeticoes += 1

    if len(letra) != 1:
        print("Digite apenas um letra")
        continue
    
    #se a letra digitada existir dentro da palavra secreta...
    if letra in palavra_secreta:
        letras_acertadas += letra
        #"guardamos" essa letra na nossa memória de acertos

    #string vazia para construila a cada rodada
    palavra_formada = ""
    for letra_secreta in palavra_secreta:       #verificamos cada letra da palavra original, uma por uma
        if letra_secreta in letras_acertadas:   #se a letra da palavra original já foi acertada antes...
            palavra_formada += letra_secreta    #...adicionamos a letra real na palavra_formada
        else:
            palavra_formada += "*"              #...se não, escondemos com um asterisco
    print(palavra_formada)                      #exibe como está a palavra no momento (ex: p*****a**)

    if palavra_formada == palavra_secreta:
        print(f"\nPARABÉNS! Você acertou a Palavra em {repeticoes} tentativas")
        break


    


