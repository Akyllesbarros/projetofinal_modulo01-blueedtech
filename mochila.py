
class Mochila:
    def __init__(self):
        self.javali = 0
        self.galinha = 0
        self.peixe = 0
        self.bufalo = 0

    def __str__(self):
        return f'Peixe: {self.peixe}\nGalinha: {self.galinha}\nJavali: {self.javali}\nBufalo: {self.bufalo}'

    def comerJavali(self):
        if self.javali == 0:
            print('Você não possui este item no inventario.')
            return False
        else:
            self.javali -= 1
            print(f'Você comeu javali! Agora você possui {self.javali} pedaços. ')

    def comerGalinha(self):
        if self.galinha == 0:
            print('Você não possui este item no inventario.')
            return False
        else:
            self.galinha -= 1
            print(f'Você comeu galinha! Agora você possui {self.galinha} pedaços. ')

    def comerPeixe(self):
        if self.peixe == 0:
            print('Você não possui este item no inventario.')
            return False
        else:
            self.peixe -= 1
            print(f'Você comeu peixe! Agora você possui {self.peixe} pedaços. ')
            
    
    def comerBufalo(self):
        if self.bufalo == 0:
            print('Você não possui este item no inventario.')
            return False
        else:
            self.bufalo -= 1
            print(f'Você comeu bufalo! Agora você possui {self.bufalo} pedaços. ')

