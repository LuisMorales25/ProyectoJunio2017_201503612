class Nodo:
    def __init__(self,dato,oponente,totalTiros,tirosAcertados,tirosFallados,gano,damage):
        self.dato=dato
        self.oponente=oponente
        self.totalTiros=totalTiros
        self.tirosAcertados=tirosAcertados
        self.tirosFallados=tirosFallados
        self.damage=damage
        self.gano=gano
        self.siguiente=None
        self.anterior=None