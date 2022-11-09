class Eleve:
    def __init__(self, numEtu, nom, prenom, groupeS1,groupeS2):
        self._numEtu = numEtu
        self._nom = nom
        self._prenom = prenom
        self._groupeS1 = groupeS1
        self._groupeS2 = groupeS2
    
    def __repr__(self):
        return f"Eleve({self._nom}, {self._prenom}, {self._groupeS1}, {self._groupeS2})"
    
    def get_numEtu(self):
        return self._numEtu
    
    def get_nom(self):
        return self._nom
    
    def get_prenom(self):
        return self._prenom
    
    def get_groupeS1(self):
        return self._groupeS1

    def get_groupeS2(self):
        return self._groupeS2
    
    def set_groupeS1(self, groupeS1):
        self._groupeS1 = groupeS1
    
    def set_prenom(self, prenom):
        self._prenom = prenom

    def set_groupeS2(self, groupeS2):
        self._groupeS2 = groupeS2