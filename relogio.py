class Relogio:
    def __init__(self):
        self.__horas = 6
        self.__minutos = 0
        self.__dia = 1
    def __str__(self): 
        return f"{self.horas:02d}:{self.minutos:02d}"
    
    def avancaTempo(self, horas,minutos=0):
        self.__horas+= horas
        self.__minutos += minutos
        while(self.__minutos >= 60):
            self.__minutos -= 60
            self.__horas += 1
        while(self.__horas)>24:
            self.__horas-=24
            self.__dia+=1
        print(self.__dia,self.__horas,self.__minutos)

    