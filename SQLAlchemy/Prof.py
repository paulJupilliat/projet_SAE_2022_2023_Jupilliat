class Prof:
    def __init__(self, idProf, nomProf, prenomProf, emailProf):
        self.idProf = idProf
        self.nomProf = nomProf
        self.prenomProf = prenomProf
        self.emailProf = emailProf
        
    def __repr__(self):
        return f"Prof({self.idProf}, {self.nomProf}, {self.prenomProf}, {self.emailProf})"
    
    # getters and setters
    
    def get_idProf(self):
        return self.idProf
    def get_nomProf(self):
        return self.nomProf
    def get_prenomProf(self):
        return self.prenomProf
    def get_emailProf(self):
        return self.emailProf
    def set_idProf(self, idProf):
        self.idProf = idProf
    def set_nomProf(self, nomProf):
        self.nomProf = nomProf
    def set_prenomProf(self, prenomProf):
        self.prenomProf = prenomProf
    def set_emailProf(self, emailProf):
        self.emailProf = emailProf