class Leitor_de_arquivo:
    def __init__(self, path: str):
        self.__path = path
    
    def ler_arquivo() -> list:
        "Dado o endereço de um arquivo, será retornado uma lista de palavras"
        with open(nomeArquivo, 'r') as arquivo:
            texto = arquivo.read().strip()
            vetor = texto.split("\n") 
            return vetor
    