class Oraux:
    def __init__(self, idOral, nomOral, nbEleveMax):
        self.idOral = idOral
        self.nomOral = nomOral
        self.nbEleveMax = nbEleveMax
        
    def __repr__(self):
        return f"Oraux({self.idOral}, {self.nomOral}, {self.nbEleveMax})"
    
    # getters and setters
    
    def get_idOral(self):
        return self.idOral
    def get_nomOral(self):
        return self.nomOral
    def get_nbEleveMax(self):
        return self.nbEleveMax
    def set_idOral(self, idOral):
        self.idOral = idOral
    def set_nomOral(self, nomOral):
        self.nomOral = nomOral
    def set_nbEleveMax(self, nbEleveMax):
        self.nbEleveMax = nbEleveMax
        
    