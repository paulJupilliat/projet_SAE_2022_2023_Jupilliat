import Oraux
import Eleve
class Reponse_sondage:
    def __init__(self, participation, matiere
    , commentaire, dateSondage, eleve, idSondage, oraux):
        self.participation = participation
        self.matiere = matiere
        self.commentaire = commentaire
        self.dateSondage = dateSondage
        self.eleve = eleve
        self.idSondage = idSondage
        self.oraux = oraux

        
    def __repr__(self) -> str:
        return "Participation : "+str(self.participation)+" Matiere : "+str(self.matiere)+" Commentaire : "+str(self.commentaire)+" Date : "+str(self.dateSondage)+" Eleve : "+str(self.eleve)+" idSondage : "+str(self.idSondage)+" Oraux : "+str(self.oraux)
    
    def getParticipation(self):
        return self.participation
    
    def getMatiere(self):
        return self.matiere
    def getCommentaire(self):
        return self.commentaire
    def getDateSondage(self):
        return self.dateSondage
    def getEleve(self):
        return self.eleve
    def getIdSondage(self):
        return self.idSondage
    def getOraux(self):
        return self.oraux
    def setParticipation(self,participation):
        self.participation=participation
    def setMatiere(self,matiere):
        self.matiere=matiere
    def setCommentaire(self,commentaire):
        self.commentaire=commentaire
    def setDateSondage(self,dateSondage):
        self.dateSondage=dateSondage
    def setEleve(self,eleve):
        self.eleve=eleve
    def setIdSondage(self,idSondage):
        self.idSondage=idSondage
    def setOraux(self,oraux):
        self.oraux=oraux
    