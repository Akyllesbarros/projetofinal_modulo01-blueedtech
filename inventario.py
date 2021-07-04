class Inventario:
    def __init__(self) -> None:
        self.__alimentoCru = 0
        self.__alimentoCuzido = 0

        # Ainda definir isso direito
        self.__ferramentas = list() # lsta de materias de contrução ['martelo', 'chave de boca', ...]
        self.__componentes = list() # componentes para montagem de algo do foguete
        

    @property
    def alimentoCru(self):
        return self.__temAlimentoCru
    
    @alimentoCru.setter
    def alimentoCru(self, quantidade):
        self.__alimentoCru = quantidade

    @property
    def alimentoCuzido(self):
        return self.__alimentoCuzido

    @alimentoCuzido.setter
    def alimentoCuzido(self, quantidade):
        self.__alimentoCuzido = quantidade

    def guardarAlimentoCru(self, quantidade):
            self.__alimentoCru += quantidade

    def guardarAlimentoCuzido(self, quantidade):
        self.__alimentoCuzido += quantidade

    def __temAlmentoCuzido(self):
        return self.alimentoCuzido > 0
    
    def __temAlimentoCru(self):
        return self.alimentoCuzido > 0
