import random

class Spel:
    
    def __init__(self, status):
        """
        tegel = (rij, kol)
        """
        self.vlek = status['vlek']
        self.score = status['score']
        self.rooster = status['board']
        self.druppeltegel = (0, 0)
                
    def __str__(self):
        """
        geeft een stringweergave van het bord terug
        """
        string = ''
        for rindex, rij in enumerate(self.rooster):
            for kindex, kleur in enumerate(rij):
                string += kleur + ' ' * (kindex < len(rij)-1)
            string += '\n' * (rindex < len(self.rooster)-1)
        return string
    
    def updateVlek(self, kleur):
        """
        geeft lijst terug van de coordinaten van de huidige vlek
        """
        for rij, kolom in self.vlek:
            Buren = self.buren(rij, kolom) 
            for buur in Buren:
                buurrij = buur[0]
                buurkolom = buur[1]
                if (self.rooster[buurrij][buurkolom] == kleur and
                    buur not in self.vlek):
                    self.vlek.append(buur)
        
        
    def buren(self, rij, kolom):
        """
        geeft een lijst terug van alle buren van een tegel
        """
        linker = rij, kolom -1*(kolom > 0)
        rechter = rij, kolom +1*(kolom < len(self.rooster[0])-1)
        boven = rij -1*(rij > 0), kolom
        onder = rij +1*(rij < len(self.rooster)-1), kolom
        return linker, boven, rechter, onder
        
    def druppel(self, kleur):
        """
        laat een druppel vallen op de druppeltegel
        """
        if len(self.vlek) == 0:
            self.vlek.append(tegel)
        self.updateVlek(kleur)
        for rij, kolom in self.vlek:
            self.rooster[rij][kolom] = kleur
        self.score += 1
        self.moves = zetten(self.rooster)
        return self
    
    def gewonnen(self):
        """
        kijkt na of alle tegels dezelfde kleur hebben
        """
        doelkleur = self.rooster[0][0]
        for rij in self.rooster:
            for kleur in rij:
                if (kleur.upper() != doelkleur.upper()):
                    return False
        return True
    
    def status(self):
        """
        geeft JSON object trug met de huidige status
        """
        state = {
                    'vlek': self.vlek,
                    'board': self.rooster,
                    'moves': self.moves,
                    'score': self.score,
                    'message': ('Proficiat! Je hebt de puzzel opgelost in %d stappen'%(self.score))*self.gewonnen()
                }
        return state
    
def maakRooster(size):
    """
    maakt een randomm rooster aan met het aantal kolommen
    """
    rooster = []
    kleuren = ["orange", "red", "blue", "green", "purple"]
    for i in range(size):
        rij = []
        for j in range(size):
            rij.append(random.choice(kleuren))
        rooster.append(rij)
    return rooster

def zetten(rooster):
    """
    geeft lijst van mogelijke zetten terug
    """
    moves = []
    druppel = rooster[0][0]
    for rij in rooster:
        for kleur in rij:
            if kleur not in moves and kleur != druppel: 
                moves.append(kleur)
    return moves