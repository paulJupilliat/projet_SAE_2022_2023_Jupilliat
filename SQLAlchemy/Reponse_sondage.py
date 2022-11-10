import Oraux
import Eleve
class Reponse_sondage:
    def __init__(self, participation, matiere, commentaire, dateSondage, Eleve, idSondage):
        self.participation = participation
        self.matiere = matiere
        self.commentaire = commentaire
        self.dateSondage = dateSondage
        self.Eleve = Eleve
        self.idSondage = idSondage
        
    def __repr__(self) -> str:
        return "Participation : "+str(self.participation)+" Matiere : "+str(self.matiere)+" Commentaire : "+str(self.commentaire)+" Date : "+str(self.dateSondage)+" Eleve : "+str(self.Eleve)+" idSondage : "+str(self.idSondage)
    
    def getParticipation(self):
        return self.participation
    
    def getMatiere(self):
        return self.matiere
    def getCommentaire(self):
        return self.commentaire
    def getDateSondage(self):
        return self.dateSondage
    def getEleve(self):
        return self.Eleve
    def getIdSondage(self):
        return self.idSondage
    def setParticipation(self,participation):
        self.participation=participation
    def setMatiere(self,matiere):
        self.matiere=matiere
    def setCommentaire(self,commentaire):
        self.commentaire=commentaire
    def setDateSondage(self,dateSondage):
        self.dateSondage=dateSondage
    def setEleve(self,eleve):
        self.Eleve=eleve
    def setIdSondage(self,idSondage):
        self.idSondage=idSondage
    