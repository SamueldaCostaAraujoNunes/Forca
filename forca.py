import sys
from random import choice
import unidecode
from boneco import Boneco
from leitor_de_arquivo import LeitorDeArquivo

def mostrar_palavra(palavra: str, acertos: list) -> None:
    "Dada uma palavra e uma lista de caracteres, será impresso um texto, contendo traços para as letras que não existem na lista, e as letras correspondentes para as que existem."
    senha = ""
    for letra in palavra:
        senha += (letra + " ") if letra in acertos else "_ "
    print(senha)

def receber_letra() -> int:
    "Função responsável por receber carácter!"
    while True:
        try:
            tentativa = input("\nDigite uma letra:").upper().strip()
            if len(tentativa) != 1:
                raise NameError('erroLetra')
            else:
                return tentativa
        except NameError:
            print("Insira apenas uma letra!")
        except:
            print("Insira uma letra válida!!")

def imprimir_letras_tentadas(digitadas: list) -> str:
    "Imprime uma lista de caracteres"
    texto = ''
    for letra in digitadas:
        texto += letra + ","
    return texto

def verificar_se_ja_acertou(acertadas: list, palavra: str) -> bool:
    "Verifica se todos os caracteres da palavra, estão contidos na lista dos acertos!"
    for letra in palavra:
        if letra not in acertadas:
            return False
    return True

def mostrar_resultado(resultado: str, palavra: str) -> None:
    "Mostra o resultado final pro usuário!"
    print("Você "+resultado+"!!!!!")
    print("A palavra era: ", palavra)

# --------------Declaração de Variaveis-----------------
path:str = 'palavras.txt'  # Endereço do arquivo
currentGame:bool = True
letrasComAcento:dict = {
    'A': ['Á', 'À', 'Â', 'Ã'],
    'E': ['É', 'È', 'Ê'],
    'I': ['Í', 'Ì', 'Î'],
    'O': ['Ó', 'Ò', 'Ô', 'Õ'],
    'U': ['Ú', 'Ù', 'Û'],
    'C': ['Ç']}  # Dicionário de letras com acento

boneco:Boneco = Boneco()
arquivo:LeitorDeArquivo = LeitorDeArquivo(path)

# -----------------Programa Principal-------------------

while currentGame: #Enquanto, houver um jogo
    palavra:str = ''  # Palavra chave da forca
    erros:int = 0  # Quantidade de erros do jogador
    digitadas:list = []  # Letras já digitadas
    acertos:list = []  # Letras digitadas que pertencem a palavra chave
    boneco.reset() # Inicializa o boneco com 0 erros 
    ganhou:bool = False
    enforcou:bool = False
    
    #palavra = input("Digite a palavra secreta:")#Recebe uma palavra por input
    #palavra = 'python'#Recebe palavra especifica, exemplo: A palavra 'python'
    palavra = choice(arquivo.ler_arquivo())# Recebe uma palavra por sorteio

    palavra = palavra.upper().strip()#Faz um tratamento na palavra
    palavraSemAcentos = unidecode.unidecode(palavra)

    while not enforcou and not ganhou:
        mostrar_palavra(palavra, acertos)  # Mostra as casas da palavra
        tentativa = receber_letra()  # Recebe a letra que o usuário quer tentar
        if tentativa in digitadas:  # Se a letra já foi escrita
            print("Você já tentou esta letra!")
        else:
            # Ele adiciona a letra na lista de letras já tentadas
            digitadas.append(tentativa)
            if tentativa in palavraSemAcentos:  # Se a letra existir dentro da palavra
                # Se a tentativa for uma das chaves do dicionários de acento.
                if tentativa in letrasComAcento.keys():
                    # Ele percorre pela lista de letras acentuadas.
                    for letrasAcentuadas in letrasComAcento[tentativa]:
                        if letrasAcentuadas in palavra:  # E verifica se esta letra se encontra na palavra.
                            acertos.append(letrasAcentuadas)# Se sim, ela adiciona tal letra na lista de acertos.
                acertos.append(tentativa)# ele entra na lista das letras já acertadas
                print("Você acertou!")
            else:  # Se não existir, na palavra
                boneco.add_erro()
                print("Você errou!")
        print("As letras que já foram tentadas são:", imprimir_letras_tentadas(digitadas))  # Imprime as letras já sorteadas
        print(boneco)  # Desenha o boneco

        enforcou = boneco.ja_enforcou() #Verifica se o boneco já foi enforcado
        ganhou = verificar_se_ja_acertou(acertos, palavra)

    if not enforcou and ganhou:# Verifica se o jogador já acertou a palavra! 
        mostrar_resultado("GANHOU", palavra)  # Mostra o resultado
    else:
        mostrar_resultado("PERDEU", palavra)  # Mostra o resultado
    currentGame = input("Deseja jogar novamente?(y/n):").upper().strip() == 'Y'
