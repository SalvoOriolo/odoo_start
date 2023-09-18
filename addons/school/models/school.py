from odoo import fields,models,api

class SchoolProfile(models.Model):
    _name="school.profile"

    name=fields.Char(string="Nome",required="True")
    email=fields.Char(string="Email",required="True")
    phone=fields.Char(string="Telefono",required="True")
    address=fields.Text(string="Indirizzo",required="True")
    school_type=fields.Selection([("public","Public School"),("private","Private School")],string="Tipologia")
    school_image=fields.Image(string="Logo",max_width=100,max_heigt=100)
    school_description=fields.Html(string="Descrizione")