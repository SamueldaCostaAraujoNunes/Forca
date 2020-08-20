from boneco import Boneco
from leitor_de_arquivo import Leitor_de_arquivo
from random import choice

class Game:
    def __init__(self):
        self.path = 'palavras.txt'  # Endereço do arquivo
        self.currentGame = True
        self.letrasComAcento = {
            'A': ['Á', 'À', 'Â', 'Ã'],
            'E': ['É', 'È', 'Ê'],
            'I': ['Í', 'Ì', 'Î'],
            'O': ['Ó', 'Ò', 'Ô', 'Õ'],
            'U': ['Ú', 'Ù', 'Û'],
            'C': ['Ç']}  # Dicionário de letras com acento

        self.boneco = Boneco()
        self.arquivo = Leitor_de_arquivo(self.path)
    
    def setup(self):
        self.palavra = ''  # Palavra chave da forca
        self.erros = 0  # Quantidade de erros do jogador
        self.digitadas = []  # Letras já digitadas
        self.acertos = []  # Letras digitadas que pertencem a palavra chave
        self.boneco.reset() # Inicializa o boneco com 0 erros 
        self.ganhou = False
        self.enforcou = False

    def choice_palavra(self):
        #self.palavra = input("Digite a palavra secreta:")#Recebe uma palavra por input
        #self.palavra = 'python'#Recebe palavra especifica, exemplo: A palavra 'python'
        self.palavra = choice(self.arquivo.ler_arquivo())# Recebe uma palavra por sorteio

    def format_palavra(self):    
        self.palavra = self.palavra.upper().strip()#Faz um tratamento na palavra
        self.palavraSemAcentos = unidecode.unidecode(self.palavra)

    def isGame(self):
        return not self.enforcou and not self.ganhou