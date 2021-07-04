
def craft(self, construcao) :

    if construcao == 'plataformaCombustivel' :
        self.__nivelPlataforma += 20 
        self.__desconfianca += 20
        self.__tempo += 8*60

    elif construcao == 'servidor' :
        self.__nivelServidor += 50 
        self.__desconfianca += 5
        self.__tempo += 8*60

    elif construcao == 'usinaFotovotaica' :
        self.__nivelUsina += 50 
        self.__desconfianca += 5
        self.__tempo += 4*60

    elif construcao == 'altoForno' :
        self.__nivelAltoForno += 25 
        self.__desconfianca += 15
        self.__tempo += 8*60

    elif construcao == 'estufaBiologica' :
        self.__nivelEstufa += 50 
        self.__desconfianca += 10
        self.__tempo += 4*60
        

    if self.__nivelEstufa >= 100 :  # caso corresponda aos requisitos, sobe de nível
        self.estufaPronta = "Uffa, a Estufa Biológica está completa!"
        self.__foguete = 20  # aumenta o nivel construção do foguete.

    elif self.__nivelAltoForno >= 100 :  # caso corresponda aos requisitos, sobe de nível
        self.altoFornoPronto = "Uffa, o Alto forno está completo!"
        self.__foguete = 20  # aumenta o nivel construção do foguete.

    elif self.__usinaFotovoltaica >= 100 :  # caso corresponda aos requisitos, sobe de nível
        self.usinaFotovoltaicaPronto = "Uffa, a Usina Fotovoltaica está completa!"
        self.__foguete = 20  # aumenta o nivel construção do foguete.

    elif self.__nivelServidor >= 100 :  # caso corresponda aos requisitos, sobe de nível
        self.servidorPronto = "Uffa, o servidor está completo!"
        self.__foguete = 20  # aumenta o nivel construção do foguete.

    elif self.__nivelPlataformaCombustivel >= 100 :  # caso corresponda aos requisitos, sobe de nível
        self.plataformaCombustivelPronto = "Uffa, a plataforma de combustível está completa!"
        self.__foguete = 20  # aumenta o nivel construção do foguete.