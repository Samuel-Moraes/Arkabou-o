class Hero:
    def __init__(self, vitalidade = 0, mana = 0, dano = 0, rf = 0, 
                 rm = 0, rv = 0, rs = 0, ra = 0, acerto = 0, 
                 tCrit = 0, rMana = 0, rVit = 0, iniciativa = 0, drein = 0,
                 
                 classe = 0, raca = 0, esquiva = 0):
        
        self.vitalidade = vitalidade # Número Inteiro 
        self.mana = mana             # Número Inteiro  
        self.dano = dano             # Número Inteiro  
        self.rf = rf                 # Porcentagem Inteira
        self.rm = rm                 # Porcentagem Inteira
        self.rv = rv                 # Porcentagem Inteira
        self.rs = rs                 # Porcentagem Inteira
        self.ra = ra                 # Porcentagem Inteira
        self.acerto = acerto         # Porcentagem Inteira
        self.tCrit = tCrit           # Porcentagem Inteira
        self.rMana = rMana           # Número Inteiro  
        self.rVit = rVit             # Número Inteiro 
        self.iniciativa = iniciativa # Número Inteiro (0 ~ 100)
        self.drein = drein           # Porcentagem Inteira

        # Status não documentados 
        self.classe = classe
        self.raca = raca
        self.esquiva = esquiva


    def setVitalidade(self, vitalidade):
        self.vitalidade = vitalidade
    
    def setMana(self, mana):
        self.mana = mana

    def setDano(self, dano):
        self.dano = dano
    
    def setRf(self, rf):
        self.rf = rf 
    
    def setRm(self, rm):
        self.rm = rm
    
    def setRv(self,rv):
        self.rv = rv

    def setRs(self, rs):
        self.rs = rs

    def setRa(self, ra):
        self.ra = ra

    def setAcerto(self, acerto):
        self.acerto = acerto

    def setTcrit(self, tCrit):
        self.tCrit = tCrit

    def setRmana(self, rMana):
        self.rMana = rMana
    
    def setRvit(self, rVit):
        self.rVit = rVit

    def setIniciativa(self, iniciativa):
        self.iniciativa = iniciativa

    def setDrein(self, drein):
        self.drain = drein

    def getVitalidade(self):
        return self.vitalidade
    
    def getMana(self):
        return self.mana

    def getDano(self):
        return self.dano
    
    def getRf(self):
        return self.rf 
    
    def getRm(self):
        return self.rm
    
    def getRv(self):
        return self.rv

    def getRs(self):
        return self.rs

    def getRa(self):
        return self.ra

    def getAcerto(self):
        return self.acerto

    def getTcrit(self):
        return self.tCrit

    def getRmana(self):
        return self.rMana
    
    def getRvit(self):
        return self.rVit

    def getIniciativa(self):
        return self.iniciativa

    def getDrein(self):
        return self.drein
    
    def getEsquiva(self):
        return self.esquiva

    def printDosDados(self):
        print(f'''
Vitalidade:  {self.vitalidade}
Mana:        {self.mana}
Dano:        {self.dano}
Res. Fisica: {self.rf}
Res. Magica: {self.rm}
Res. Veneno: {self.rv}
Res. Sang:   {self.rs}
Res. Atord:  {self.ra}
Acerto:      {self.acerto}
Taxa Crit:   {self.tCrit}
Reg. Mana:   {self.rMana}
Reg. Vit:    {self.rVit}
Iniciativa:  {self.iniciativa}
Drenagem HP: {self.drein}

Raça:        {self.raca}
Classe:      {self.classe}
Esquiva:     {self.esquiva}
               
               ''')