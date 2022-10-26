class Reponse_sondage(models.Model):
    _name = 'reponse.sondage'
    _description = 'Reponse_sondage'

    name = fields.Char(string='Nom', required=True)
    reponse = fields.Char(string='Reponse', required=True)
    sondage_id = fields.Many2one('sondage', string='Sondage')