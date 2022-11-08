import QCM
import Eleve

class Resultat :
    def __init__(self,note,QCM,Eleve):
        self.note=note
        self.idQCM = QCM
        self.numEtu = Eleve        
    def __repr__(self) -> str:
        return "Note : "+str(self.note)+" idQCM : "+str(self.idQCM)+" numEtu : "+str(self.numEtu)
    
    def getNote(self):
        return self.note
    def getQCM(self):
        return self.idQCM
    def getEleve(self):
        return self.numEtu
    def setNote(self,note):
        self.note=note
    def setQCM(self,idQCM):
        self.idQCM=idQCM
    def setNumEtu(self,numEtu):
        self.numEtu=numEtu
    