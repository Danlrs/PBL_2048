"""/***************************************************************************************
Autor: Daniel Lucas Rios da Silva
Componente Curricular: Algoritmos I
Concluido em: 04/10/2023
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
***************************************************************************************/"""
import random
import msvcrt
import os

# Declaração da grade do jogo, da lista temporária e das variáveis
tabuleiro = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
listaTemp = [0, 0, 0, 0]
score = 0   # Pontuação atual
contador = 2    # Contador e quantas peças precisam ser geradas no tabuleiro
recorde = 0     # Pontuação recorde
recorde_jogadas = 0     # Menor quantidade de jogadas para a maior pontuação
movimentos = 0      # Quantidade de movimentos atual
movimento_possivel = True   # Verificador de possibilidade de movimento
seguir_jogo = False    # Permite que o jogo prossiga após um movimento válido
jogada = 0   # Jogada atual
move = True     # Verifica se houve movimento para gerar novo bloco

def imprimir_tabuleiro(): # Função que imprime a grade do jogo
    print("2048 -  Recorde: ", recorde, ": ", recorde_jogadas, " movimentos\n")
    for i in range(4):
        print("| ", end="")
        for j in range(4):
            print(tabuleiro[i][j], end=" ")
        print("|")
    print("\nScore: ", score, ": ", movimentos , "movimentos")


def gerador_aleatorio(cont): # Função que gera os números aleatórios        
    while(cont!=0):
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        h = [2, 4]
        if(tabuleiro[x][y]==0):
            tabuleiro[x][y] = random.choice(h)
            cont-=1       


def mover_esquerda(pontuacao):  # Função que movimenta para esquerda
    soma = 0
    movimenta = False
    for i in range(4): 
        for j in range(4):
            if (listaTemp[j]==0):
                listaTemp[j] = tabuleiro[i][j] 
            for t in [2, 1, 0]:
                if(listaTemp[t]!=0 and listaTemp[t] == listaTemp[t+1] and soma != 2):
                    if(soma == 1 and tabuleiro[i][1] != tabuleiro[i][2]):
                        break
                    else:
                        listaTemp[t] *= 2
                        listaTemp[t+1] = 0
                        pontuacao += listaTemp[t]
                        soma += 1
                        movimenta = True
                elif(listaTemp[t] == 0 and listaTemp[t+1] != 0):                             
                    listaTemp[t] = listaTemp[t+1]
                    listaTemp[t+1] = 0
                    movimenta = True
        soma = 0
        for l in range(4):
            tabuleiro[i][l] = listaTemp[l]
            listaTemp[l]=0
    return pontuacao, movimenta


def mover_direita(pontuacao): # Função que movimenta para direita
    soma = 0
    movimenta = False
    for i in [3, 2, 1, 0]:
        for j in [3, 2, 1, 0]:
            if (listaTemp[j]==0):
                listaTemp[j] = tabuleiro[i][j]
            for t in [1, 2, 3]:
                if(listaTemp[t]!=0 and listaTemp[t] == listaTemp[t-1] and soma != 2):
                    if(soma == 1 and tabuleiro[i][2] != tabuleiro[i][1]):
                        break
                    else:
                        listaTemp[t] *= 2
                        listaTemp[t-1] = 0
                        pontuacao += listaTemp[t]
                        soma +=1
                        movimenta = True
                elif(listaTemp[t] == 0 and listaTemp[t-1] != 0):
                    listaTemp[t] = listaTemp[t-1]
                    listaTemp[t-1] = 0
                    movimenta = True
        soma = 0
        for l in range(4):
            tabuleiro[i][l] = listaTemp[l]
            listaTemp[l]=0
    return pontuacao, movimenta


def mover_cima(pontuacao): # Função que movimenta para cima
    soma = 0
    movimenta = False
    for j in range(4):
        for i in range(4):
            if (listaTemp[i]==0):
                listaTemp[i] = tabuleiro[i][j]
            for t in [2, 1, 0]:
                if(listaTemp[t]!=0 and listaTemp[t] == listaTemp[t+1] and soma != 2):
                    if(soma == 1 and tabuleiro[1][j] != tabuleiro[2][j]):
                        break
                    else:
                        listaTemp[t] *= 2
                        listaTemp[t+1] = 0
                        pontuacao += listaTemp[t]
                        soma += 1
                        movimenta = True
                elif(listaTemp[t] == 0 and listaTemp[t+1] != 0):
                    listaTemp[t] = listaTemp[t+1]
                    listaTemp[t+1] = 0
                    movimenta = True
        soma = 0
        for l in range(4):
            tabuleiro[l][j] = listaTemp[l]
            listaTemp[l]=0
    return pontuacao, movimenta


def mover_baixo(pontuacao): # Função que movimenta para baixo
    soma = 0
    movimenta = False
    for j in [3, 2, 1, 0]:
        for i in [3, 2, 1, 0]:
            if (listaTemp[i]==0):
                listaTemp[i] = tabuleiro[i][j]
            for t in [1, 2, 3]:
                if(listaTemp[t]!=0 and listaTemp[t] == listaTemp[t-1] and soma != 2):
                    if(soma == 1 and tabuleiro[1][j] != tabuleiro[2][j]):
                        break
                    else:
                        listaTemp[t] *= 2                                   
                        listaTemp[t-1] = 0
                        pontuacao += listaTemp[t]
                        soma +=1
                        movimenta = True
                elif(listaTemp[t] == 0 and listaTemp[t-1] != 0):
                    listaTemp[t] = listaTemp[t-1]
                    listaTemp[t-1] = 0
                    movimenta = True
        soma = 0
        for l in range(4):
            tabuleiro[l][j] = listaTemp[l]
            listaTemp[l]=0
    return pontuacao, movimenta


def verificar_vitoria(): # Verificando se o usuário ganhou
    for i in range(4):
        for j in range(4):
            if(tabuleiro[i][j] == 2048):
                print("Voce ganhou!!")
                return True
    return False


def verificar_derrota(): # Verificando se todas as casas estão preenchidas
    verificador = 0
    for i in range(4):
        for j in range(4):
            if(tabuleiro[i][j] !=0):
                verificador+=1
    if(verificador == 16):
        return(True)
    return(False)


def jogar_novamente(): # Perguntando se o usuário deseja jogar novamente
    continuar = '2'
    while(continuar != '1' and continuar != '0'):
        continuar = input("Deseja jogar novamente? (1)Sim, (0)Não\n")
        if(continuar == '0'):
            print("Obrigado por usar o programa!")
            return False
        elif(continuar != '1' and continuar != '0'):
            print("Opcao inexistente!")
        elif(continuar == '1'):
            return True  


def verificar_movimentos(movimento): # Função que verifica se o movimento é possível
    jogada_acontece = False
    if(movimento == 0):
        for i in range(4):
            for j in range(4):
                if (listaTemp[j]==0):
                    listaTemp[j] = tabuleiro[i][j]
                for t in [2, 1, 0]:                                                    
                    if(listaTemp[t]!=0 and listaTemp[t] == listaTemp[t+1]):             
                        jogada_acontece = True                                          
            for l in range(4):                                                          
                listaTemp[l]=0
    elif(movimento == 1):
        for i in [3, 2, 1, 0]:
            for j in [3, 2, 1, 0]:
                if (listaTemp[j]==0):
                    listaTemp[j] = tabuleiro[i][j]
                for t in [1, 2, 3]:
                    if(listaTemp[t]!=0 and listaTemp[t] == listaTemp[t-1]):
                        jogada_acontece = True
            for l in range(4):
                listaTemp[l]=0
    elif(movimento == 2):
        for j in range(4):
            for i in range(4):
                if (listaTemp[i]==0):
                    listaTemp[i] = tabuleiro[i][j]
                for t in [2, 1, 0]:
                    if(listaTemp[t]!=0 and listaTemp[t] == listaTemp[t+1]):
                        jogada_acontece = True
            for l in range(4):
                listaTemp[l]=0
    elif(movimento == 3):
        for j in [3, 2, 1, 0]:
            for i in [3, 2, 1, 0]:
                if (listaTemp[i]==0):
                    listaTemp[i] = tabuleiro[i][j]
                for t in [1, 2, 3]:
                    if(listaTemp[t]!=0 and listaTemp[t] == listaTemp[t-1]):
                        jogada_acontece = True
            for l in range(4):
                listaTemp[l]=0
    return jogada_acontece


# Parte principal do jogo (main)                                              
while(True):
    if(move == True and contador != 0):                                                                                            
        gerador_aleatorio(cont=contador)  
        contador = 1                                                                   
    imprimir_tabuleiro()
    while(seguir_jogo == False):
        tecla = msvcrt.getch()     # Verifica qual tecla foi pressionada                                                                   
        if(tecla == b'\xe0'):  # Tecla especial (setas)
            seta = msvcrt.getch()  # Obtém o código da tecla especial
            if(seta == b'K'):  # Tecla de seta para a esquerda
                score, move = mover_esquerda(score)
            elif(seta == b'M'):  # Tecla de seta para a direita
                score, move = mover_direita(score)             
            elif(seta == b'H'):  # Tecla de seta para cima
                score, move = mover_cima(score)
            elif(seta == b'P'):  # Tecla de seta para baixo
                score, move = mover_baixo(score)
            movimentos += 1
            seguir_jogo = True
        else:
            print("Não existe esse movimento.")
        for i in range(4):
            movimento_possivel = verificar_movimentos(i)
            if(movimento_possivel == True):
                break
        if(movimento_possivel == False and verificar_derrota() == True):
            print("Voce perdeu!")
        elif(movimento_possivel == True and verificar_derrota() == True or move == False):
            print("Movimento inválido!")
            movimentos -= 1
            seguir_jogo = False
        if(score >= recorde):
            recorde = score
            recorde_jogadas = movimentos
            if(movimentos <= recorde_jogadas):
                recorde_jogadas = movimentos
    if(verificar_derrota() == True or verificar_vitoria() == True):
        if(jogar_novamente() == False):
            break
        else:
            tabuleiro = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
            score = 0
            contador = 2
            vitoria = False
            derrota = False
            movimentos = 0
            move = True
    seguir_jogo = False         
    os.system('cls') # Limpa o terminal