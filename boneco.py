class Boneco:
    def __init__(self, erros):
        self.__erros = erros
    
    def criar_boneco(self):
        str_boneco = ''
        str_boneco += "X==:==\nX  :   \n"
        str_boneco += "X  O   \n" if self.__erros >= 1 else "X\n"
        linha = ""
        if self.__erros == 2:
            linha = "  |   "
        elif self.__erros == 3:
            linha = " \|   "
        elif self.__erros >= 4:
            linha = " \|/ "

        str_boneco += f"X{linha}\n"

        linha= ""
        if self.__erros >= 5:
            linha = "  |   "

        str_boneco += f"X{linha}\n"

        linha = ""
        if self.__erros == 6:
            linha += " /     "
        elif self.__erros >= 7:
            linha += " / \ "

        str_boneco += f"X{linha}\n"
        str_boneco += "X\n==========="

        return str_boneco

    def __str__(self):
        return self.criar_boneco()

    def set_erro(self, n_erro):
        self.__erros = n_erro
    
   