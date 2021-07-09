from mochila import Mochila, mochila
from governo import Governo, governo
from relogio import Relogio, tempo
from craft import Foguete, craft


# variavel instanciada para chamar atributo desconfianca da classe Governo



class Personagem(): 
    def __init__(self) -> None:
        self.__nome = str
        self.__paranoia = 0
        self.__fome = 40
        self.__energia = 100


    def cacar(self):
        '''
        1 - Peixe
        2 - Galinha
        3 - Javali
        4 - Bufalo
        '''
        print(f'Você possui :\n{mochila}\n')
        animal = int(input('Escolha um para caçar:\n\n[ 1 ] Peixe\n[ 2 ] Galinha\n[ 3 ] Javali\n[ 4 ] Bufalo\n'))

        if animal == 1:
            self.alterarEnergia('diminuir', 10)
            tempo.avancaTempo(0, 5)
            self.__paranoia += 0
            mochila.peixe += 1
           
        elif animal == 2:
            tempo.avancaTempo(0, 15)
            self.__paranoia += 0
            mochila.galinha += 1
           
        elif animal == 3:
            self.alterarEnergia('diminuir', 5)
            tempo.avancaTempo(0, 30)
            self.__paranoia += 25
            mochila.javali += 1


        elif animal == 4 :
            self.alterarEnergia('diminuir', 25)
            tempo.avancaTempo(0, 30)
            self.__paranoia += 25
            mochila.bufalo += 1


    def alterarEnergia(self, tipo, valor) :
        '''
        Para o tipo, escolher 'aumentar' ou 'diminuir'
        para o valor, escolher a quantidade
        '''
        if tipo == 'aumentar' :
            self.__energia += valor
            if (self.__energia + valor) >= 100 :
                self.__energia = 100

            print(f'Sua energua aumentou para {self.__energia}')

        elif tipo == 'diminuir' :
            self.__energia -= valor
            if (self.__energia - valor) == 0 :
                self.__energia = 0
            print(f'Sua energia diminuiu para {self.__energia}')


    def comer(self):
        print(f'Você possui :\n{mochila}')
        comer = int(input('Escolha um para comer:\n\n[ 1 ] Peixe\n[ 2 ] Galinha\n[ 3 ] Javali\n[ 4 ] Bufalo\n'))
        
        if comer == 1:
            if mochila.comerPeixe() == False:
                return
            else:
                self.alterarFome('diminuir', 10)

        elif comer == 2:
            if mochila.comerGalinha() == False:
                return
            else:
                self.alterarFome('diminuir', 20)

        elif comer == 3:
            if mochila.comerJavali() == False:
                return
            else:
                self.alterarFome('diminuir', 25)

        elif comer == 4:
            if mochila.comerBufalo() == False:
                return
            else:
                self.alterarFome('diminuir', 50)
    

    def alterarFome(self, tipo, valor) :
        '''
        Para o tipo, escolher 'aumentar' ou 'diminuir'
        para o valor, escolher a quantidade
        '''
        if tipo == 'aumentar':
            self.__fome += valor
            if (self.__fome + valor) >= 100:
                self.__fome = 100
            print(f'Sua fome aumentou para {self.__fome}')

        elif tipo == 'diminuir':
            self.__fome -= valor
            if (self.__fome - valor) <= 0:
                self.__fome = 0
            print(f'Sua fome diminuiu para {self.__fome}')

            if self.__fome == 0 :
                print('Você está satisfeito.')


    def inventario():
        print(mochila)


    def status(self) :

        print(f'''Status
        💈 {self.__paranoia} 
        🍴 {self.__fome} 
        ⚡ {self.__energia} 
        🏛  {governo} ''')

 
    def dormir(self) :
        self.alterarEnergia('aumentar', 80)
        self.alterarFome('diminuir', 30)
        self.__paranoia += 40
        tempo.avancaTempo(8)



