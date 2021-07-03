from inventario import Inventario

class Personagem(Inventario): ## Motivo de ter feito assim: SIM
    def __init__(self) -> None:
        super().__init__()
        self.__nome = str()
        self.__genero = str()
        self.__paranoia = 0
        self.__fome = 100
        self.__energia = 100
        self.__tempo = 1440

    def cacar(self, animal):
        if animal == 'Galinha':
            self.__energia -= 5
            self.__tempo -= 15
            self.__paranoia += 0
            self.guardarAlimentoCru(1)
        elif animal == 'javali':
            self.__energia -= 10
            self.__tempo -= 30
            self.__paranoia += 25
            self.guardarAlimentoCru(2)
        elif animal == 'peixe':
            self.__energia -= 0
            self.__tempo -= 5
            self.__paranoia += 0
            self.guardarAlimentoCru(1)
        else: # animal == bufalo
            self.__energia -= 10
            self.__tempo -= 30
            self.__paranoia += 25
            self.guardarAlimentoCru(3)

    def comer(self):
        if self.__temAlmentoCuzido():
            self.__fome += int() # Definir valor padrão

    def cozinhar(self):
        if self.__temAlimentoCru():
            self.alimentoCru -+ 1
            self.alimentoCuzido += 1
