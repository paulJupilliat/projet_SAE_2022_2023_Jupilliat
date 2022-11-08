class Eleve:
    def __init__(self, numEtu, nom, prenom, groupeS1,groupeS2):
        self.numEtu = numEtu
        self.nom = nom
        self.prenom = prenom
        self.groupeS1 = groupeS1
        self.groupeS2 = groupeS2
    
    def __repr__(self):
        return f"Eleve({self.nom}, {self.prenom}, {self.groupeS1}, {self.groupeS2})"
    
    def get_nom(self):
        return self.nom
    
    def get_prenom(self):
        return self.prenom
    
    def get_groupeS1(self):
        return self.groupeS1

    def get_groupeS2(self):
        return self.groupeS2
    
    def set_groupeS1(self, groupeS1):
        self.groupeS1 = groupeS1
    
    def set_prenom(self, prenom):
        self.prenom = prenom

    def set_groupeS2(self, groupeS2):
        self.groupeS2 = groupeS2