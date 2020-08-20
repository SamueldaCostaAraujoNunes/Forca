class Leitor_de_arquivo:
    def __init__(self, path: str):
        self.__path = path
    
    def ler_arquivo(self) -> list:
        "Dado o endereço de um arquivo, será retornado uma lista de palavras"
        with open(self.__path, 'r') as arquivo:
            texto = arquivo.read().strip()
            vetor = texto.split("\n") 
            return vetor
    