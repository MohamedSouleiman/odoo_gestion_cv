#coding: utf-8

from odoo import models, fields

class Personne(models.Model): 
	_name= 'cv.personne'
	_rec_name= 'nom'

	nom = fields.Char(
		string = 'Nom'
	)
	prenom = fields.Char(
		sting = 'Prenom'
	)