class QCM:
    def __init__(self, idQCM, nomQCM, urlQCM):
        self.idQCM = idQCM
        self.nomQCM = nomQCM
        self.urlQCM = urlQCM
    
    def __repr__(self):
        return f"QCM({self.idQCM}, {self.nomQCM}, {self.urlQCM})"
    
    #getters and setters
    
    def get_idQCM(self):
        return self.idQCM
    def get_nomQCM(self):
        return self.nomQCM
    def get_urlQCM(self):
        return self.urlQCM
    def set_idQCM(self, idQCM):
        self.idQCM = idQCM
    def set_nomQCM(self, nomQCM):
        self.nomQCM = nomQCM
    def set_urlQCM(self, urlQCM):
        self.urlQCM = urlQCM