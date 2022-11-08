#CREATE TABLE SONDAGE (
  #  idSondage INT,
   # urlSondage VARCHAR(255),
    #Primary Key (idSondage)
class Sondage:
    def __init__(self, idSondage, urlSondage):
        self.idSondage = idSondage
        self.urlSondage = urlSondage
        
    def __repr__(self):
        return f"Sondage({self.idSondage}, {self.urlSondage})"
    
    def get_idSondage(self):
        return self.idSondage
    def get_urlSondage(self):
        return self.urlSondage
    def set_idSondage(self, idSondage):
        self.idSondage = idSondage
    def set_urlSondage(self, urlSondage):
        self.urlSondage = urlSondage
    