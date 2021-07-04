class Dormir:
    from .relogio import Relogio
    def __init__(self,energia,paranoia,fome,horas=8,tempo):
        self.energia=energia+(10*horas)
        self.paranoia=paranoia-(5*horas)
        self.fome=fome-(3*horas)
        avancaTempo(horas)

    def embreagar(self,energia,paranoia,fome,horas=0.5,tempo):
        self.energia= -20
        self.paranoia-= -40
        self.tempo=tempo+horas
    
    def cozinhar(self,fome,tempo,minutos=15,tempo)
        avancaTempo(horas)
        #15 min
