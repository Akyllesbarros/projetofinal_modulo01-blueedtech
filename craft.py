from relogio import Relogio, tempo
from governo import Governo, governo
from menu import Menu, menu

class Foguete() :
    def __init__(self):
        self.__nivelPlataforma = 0
        self.__nivelAltoForno = 0
        self.__nivelEstufa = 0
        self.__nivelServidor = 0
        self.__nivelUsina = 0
        self.__foguete = 0

    
    def estufaPronta(self) :
        print("Uffa, a Estufa Biológica está completa!")
    

    def altoFornoPronto(self) :
        print("Uffa, o Alto Forno está completo!")

    
    def usinaFotovoltaicaPronto(self) :
        print("Uffa, a Usina Fotovoltaica completa!")

    
    def servidorPronto(self) :
        print('Uffa, o Servidor está completo!')

    def plataformaCombustivelPronto(self) :
        print('Uffa, o Plataforma de Combustível está completo!')


    def craft(self) :
        construcao = int(input('''Por favor, escolha o que você quer construir: 
        [ 1 ] Plataforma de Combustível
        [ 2 ] Servidor
        [ 3 ] Usina Fotovoltaica
        [ 4 ] Alto forno
        [ 5 ] Estufa Biológica'''))
        
        if construcao == 1 :
            self.__nivelPlataforma += 20 
            governo.diminuiDesconfianca(20)
            tempo.avancaTempo(8)
            print('Você construiu 1/4 da Plataforma!')

        elif construcao == 2 :
            self.__nivelServidor += 50 
            governo.diminuiDesconfianca(5)
            tempo.avancaTempo(8)
            print('Você construiu mais 1/2 do Servidor!')

        elif construcao == 3 :
            self.__nivelUsina += 50 
            governo.diminuiDesconfianca(5)
            tempo.avancaTempo(4)
            print('Você construiu 1/2 da Usina!')

        elif construcao == 4 : 
            self.__nivelAltoForno += 25 
            governo.diminuiDesconfianca(15)
            tempo.avancaTempo(8)
            print('Você construiu 1/4 do Alto forno!')

        elif construcao == 5 :
            self.__nivelEstufa += 50 
            governo.diminuiDesconfianca(10)
            tempo.avancaTempo(4)
            print('Você construiu 1/2 da Estufa!')

        if self.__nivelEstufa >= 100 :  # caso corresponda aos requisitos, sobe de nível
            self.estufaPronta()
            self.__foguete += 20  # aumenta o nivel construção do foguete.

        elif self.__nivelAltoForno >= 100 :  # caso corresponda aos requisitos, sobe de nível
            self.altoFornoPronto()
            self.__foguete += 20  # aumenta o nivel construção do foguete.

        elif self.__nivelUsina >= 100 :  # caso corresponda aos requisitos, sobe de nível
            self.usinaFotovoltaicaPronto()
            self.__foguete += 20  # aumenta o nivel construção do foguete.

        elif self.__nivelServidor >= 100 :  # caso corresponda aos requisitos, sobe de nível
            self.servidorPronto()
            self.__foguete += 20  # aumenta o nivel construção do foguete.

        elif self.__nivelPlataforma >= 100 :  # caso corresponda aos requisitos, sobe de nível
            self.plataformaCombustivelPronto()
            self.__foguete += 20  # aumenta o nivel construção do foguete.
        

