from random import choice
from typing import Dict, List
import unidecode
from boneco import Boneco
from leitor_de_arquivo import LeitorDeArquivo

# python -m flake8 forca.py
# python -m mypy forca.py


def mostrar_palavra(palavra: str, acertos: list) -> None:
    """Dada uma palavra e uma lista de caracteres, será impresso um texto,
    contendo traços para as letras que não existem na lista, e as letras
    correspondentes para as que existem."""
    senha = ""
    for letra in palavra:
        senha += (letra + " ") if letra in acertos else "_ "
    print(senha)


def receber_letra() -> str:
    """Função responsável por receber carácter!"""
    while True:
        try:
            tentativa = input("\nDigite uma letra:").upper().strip()
            if len(tentativa) != 1:
                raise NameError('erroLetra')
            elif tentativa.isnumeric():
                raise NameError('erroNumero')
            else:
                return tentativa
        except NameError:
            print("Insira apenas uma letra!")
        except BaseException:
            print("Insira uma letra válida!!")


def imprimir_letras_tentadas(digitadas: list) -> str:
    """Imprime uma lista de caracteres"""
    texto = ''
    for letra in digitadas:
        texto += letra + ","
    return texto


def verificar_se_ja_acertou(acertadas: list, palavra: str) -> bool:
    """Verifica se todos os caracteres da palavra,
    estão contidos na lista dos acertos!"""
    for letra in palavra:
        if letra not in acertadas:
            return False
    return True


def mostrar_resultado(resultado: str, palavra: str) -> None:
    """Mostra o resultado final pro usuário!"""
    print("Você "+resultado+"!!!!!")
    print("A palavra era: ", palavra)

# --------------Declaração de Variaveis-----------------


path: str = 'palavras.txt'  # Endereço do arquivo
current_game: bool = True
letras_com_acento: Dict[str, List[str]] = {
    'A': ['Á', 'À', 'Â', 'Ã'],
    'E': ['É', 'È', 'Ê'],
    'I': ['Í', 'Ì', 'Î'],
    'O': ['Ó', 'Ò', 'Ô', 'Õ'],
    'U': ['Ú', 'Ù', 'Û'],
    'C': ['Ç']}  # Dicionário de letras com acento

boneco: Boneco = Boneco()
arquivo: LeitorDeArquivo = LeitorDeArquivo(path)

# -----------------Programa Principal-------------------

while current_game:  # Enquanto, houver um jogo
    palavra: str = ''  # Palavra chave da forca
    erros: int = 0  # Quantidade de erros do jogador
    digitadas: list = []  # Letras já digitadas
    acertos: list = []  # Letras digitadas que pertencem a palavra chave
    boneco.reset()  # Inicializa o boneco com 0 erros
    ganhou: bool = False
    enforcou: bool = False

    # Recebe uma palavra por input
    # palavra = input("Digite a palavra secreta:")
    # Recebe palavra especifica, exemplo: A palavra 'python'
    # palavra = 'python'
    palavra = choice(arquivo.ler_arquivo())  # Recebe uma palavra por sorteio

    palavra = palavra.upper().strip()  # Faz um tratamento na palavra
    palavra_sem_acentos = unidecode.unidecode(palavra)

    while not enforcou and not ganhou:
        mostrar_palavra(palavra, acertos)  # Mostra as casas da palavra
        tentativa = receber_letra()  # Recebe a letra que o usuário quer tentar
        if tentativa in digitadas:  # Se a letra já foi escrita
            print("Você já tentou esta letra!")
        else:
            # Ele adiciona a letra na lista de letras já tentadas
            digitadas.append(tentativa)
            # Se a letra existir dentro da palavra
            if tentativa in palavra_sem_acentos:
                # Se a tentativa for uma chave do dicionário de acento
                if tentativa in letras_com_acento.keys():
                    # Ele percorre pela lista de letras acentuadas
                    for letrasAcentuadas in letras_com_acento[tentativa]:
                        # E verifica se esta letra se encontra na palavra
                        if letrasAcentuadas in palavra:
                            # Se sim, ela adiciona a letra na lista de acertos
                            acertos.append(letrasAcentuadas)
                # Ele entra na lista das letras já acertadas
                acertos.append(tentativa)
                print("Você acertou!")
            else:  # Se não existir, na palavra
                boneco.add_erro()
                print("Você errou!")
        # Imprime as letras já sorteadas
        print("As letras que já foram tentadas são:",
              imprimir_letras_tentadas(digitadas))
        print(boneco)  # Desenha o boneco

        # Verifica se o boneco já foi enforcado
        enforcou = boneco.ja_enforcou()
        ganhou = verificar_se_ja_acertou(acertos, palavra)

    if not enforcou and ganhou:  # Verifica se o jogador já acertou a palavra!
        mostrar_resultado("GANHOU", palavra)  # Mostra o resultado
    else:
        mostrar_resultado("PERDEU", palavra)  # Mostra o resultado
    current_game = (input("Deseja jogar novamente?(y/n):")
                    .upper().strip() == 'Y')
