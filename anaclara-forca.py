import random #Import= importa de uma biblioteca, e gera 0números aleatórios

palavras = [] #As palavras que serão usadas no jogo
letrasErradas = '' #Onde ficará armazenado as letras erradas
letrasCertas = '' #Onde ficará armazenado as letras corretas
    
FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''] #Os desenhos que apareceram na tela de acordo com os erros e os acertos do jogador

def receberpalavras():
    global palavras
    while True:
        p= input('Digite uma palavra: ')
        if p== "":
            break
        palavras.append(p)

def principal(): #(criar funções), no caso a função 'principal' foi criada.
    """
    Função Princial do programa
    """
    print('F O R C A') #Aparece na tela o que foi digitado entre os parenteses.
    receberpalavras()
    palavraSecreta = sortearPalavra() #A palavra secreta tem que ser igual a palavra sorteada
    palpite = '' #Variável onde armazenará as letras digitadas
    desenhaJogo(palavraSecreta,palpite)

    while True: #Repetirá infinitamente
        palpite = receberPalpite() #A variável 'palpite' receberá a variável 'receberPalpite'
        desenhaJogo(palavraSecreta,palpite) #A variável 'desenhaJogo' receberá as variáveis 'palavraSecreta' e 'palpite'
        if perdeuJogo(): #SE o jogador perdeu o jogo, então:
            print('Voce Perdeu!!!') #Aparecerá na tela: Voce Perdeu!!!
            break #Para a repetição
        if ganhouJogo(palavraSecreta): #SE o jogador acertou todas as letras:
            print('Voce Ganhou!!!') #Aparecerá na tela: Voce Ganhou!!!
            break #Para a repetição           
        
def perdeuJogo(): #Criou a função 'perdeuJogo'
    global FORCAIMG #Busca a variável 'FORCAIMG' entre as variáveis globais, que são as que estão fora da função
    if len(letrasErradas) == len(FORCAIMG): #Fala quantas letras tem na variável
        return True #Retorne para o ponto onde a função foi chamada
    else: #Se o que foi comandado antes não der certo, então:
        return False #Retorne para o ponto onde a função foi chamada
    
def ganhouJogo(palavraSecreta): #Definiu a função 'ganhoujogo' e dentro disso criou um paramêtro
    global letrasCertas #O nome da variável não foi qualificado, então é feita uma busca entre as variáveis globais, que são as que estão fora da função 
    ganhou = True #Se o jogador tiver ganhado
    for letra in palavraSecreta: #realiza uma sequência de forma ordenada e acabará alterando os valores que são especificados em variáveis
        if letra not in letrasCertas: #SE a letra não pertencer ao grupo de letrasCertas
            ganhou = False #Se o jogador não tiver ganhado
            
    return ganhou #Encerra a execução da função, e volta exatamente para o ponto onde ela foi chamada.      
        


def receberPalpite(): #Definiu a função 'receberPalpite'
    
    palpite = input("Adivinhe uma letra: ") #Dentro da variável 'palpite' pede para o jogador dizer uma letra
    palpite = palpite.upper() #A variável 'palpite' recebe o comando do 'palpite.upper' que faz com que todas as letras digitadas pelo jogador fiquem em maiúsculo 
    if len(palpite) != 1: #if (se): Verifica se uma condição é verdadeira.
        print('Coloque um unica letra.')
        receberPalpite()
    elif palpite in letrasCertas or palpite in letrasErradas:
        print('Voce ja disse esta letra.') #O elif é usado quando a condição de if e else não foi executada.
        receberPalpite()
    elif not "A" <= palpite <= "Z":
        print('Por favor escolha apenas letras')
        receberPalpite()
    else: #Se a condição do if não for verdadeira, essa condição será executada.
        return palpite #Encerra a execução da função, e volta exatamente para o ponto onde ela foi chamada.    
        
    
def desenhaJogo(palavraSecreta,palpite):
    global letrasCertas
    global letrasErradas  #Global: Se refere à uma variável já existente para se tornar global, ou seja, são as que estão fora da função
    global FORCAIMG

    print(FORCAIMG[len(letrasErradas)]) #Imprime na tela uma parte do bonequinho na forca porque a pessoa errou um palpite.
    
     
    vazio = len(palavraSecreta)*'-'
    
    if palpite in palavraSecreta:
        letrasCertas += palpite
    else:
        letrasErradas += palpite

    for letra in letrasCertas:
        for x in range(len(palavraSecreta)):
            if letra == palavraSecreta[x]:
                vazio = vazio[:x] + letra + vazio[x+1:]
                
    print('Acertos: ',letrasCertas ) #Irá imprimir os acertos que o jogador acertou
    print('Erros: ',letrasErradas)  #Irá imprimir os erros que o jogador errou
    print(vazio)
     

def sortearPalavra():
    global palavras
    return random.choice(palavras).upper() #random.choice: Gera uma amostra aleatória de uma determinada função

    
principal()
