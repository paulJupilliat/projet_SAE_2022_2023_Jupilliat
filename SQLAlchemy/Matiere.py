class Matiere:
    def __init__(self, idMatiere, nomMatiere):
        self.idMatiere = idMatiere
        self.nomMatiere = nomMatiere
        
    def __repr__(self):
        return f"Matiere({self.idMatiere}, {self.nomMatiere})"
    
    # fais les getters et setters
    def get_idMatiere(self):
        return self.idMatiere
    
    def get_nomMatiere(self):
        return self.nomMatiere
    
    def set_idMatiere(self, idMatiere):
        self.idMatiere = idMatiere
        
    def set_nomMatiere(self, nomMatiere):
        self.nomMatiere = nomMatiere
        
    