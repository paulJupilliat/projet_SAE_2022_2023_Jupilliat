class QCM:
    def __init__(self, idQCM, nomQCM, urlQCM, idmatiere):
        self._idQCM = idQCM
        self._nomQCM = nomQCM
        self._urlQCM = urlQCM
        self._idmatiere = idmatiere
    
    def __repr__(self):
        return f"QCM({self._idQCM}, {self._nomQCM}, {self._urlQCM})"
    
    #getters and setters
    
    def get_idQCM(self):
        return self._idQCM
    def get_nomQCM(self):
        return self._nomQCM
    def get_urlQCM(self):
        return self._urlQCM
    def get_matiere(self):
        return self._idmatiere
    def set_idQCM(self, idQCM):
        self._idQCM = idQCM
    def set_nomQCM(self, nomQCM):
        self._nomQCM = nomQCM
    def set_urlQCM(self, urlQCM):
        self._urlQCM = urlQCM
    def set_matiere(self,idmatiere):
        self._idmatiere = idmatiere
        
