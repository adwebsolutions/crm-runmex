# -*- coding: utf-8 -*-

from datetime import datetime, date, time
from openerp import api, fields, models

class CrmCustomFields(models.Model):

  _inherit = "crm.lead"
  
  runmex_fecha_de_cita  = fields.Date('Fecha de Cita')
  
  runmex_viaticos  = fields.Integer(string="Viáticos", help="Costo real del viaje")

  runmex_canal = fields.Selection(
                                    (('formulario','Formulario'),
                                    ('telefono', 'Teléfono'),
									('email', 'Email'),
									('facebook', 'Facebook'),
                                    ('linkedin', 'Linkedin')), 'Canal',  help="Canal por el cual llego la oportunidad")
									
  runmex_soluciones    = fields.Many2one(comodel_name = 'runmex.soluciones', string ='Soluciones',  help="Soluciones de productos")
  runmex_origen    = fields.Many2one(comodel_name = 'runmex.origen', string ='Origen',  help="Origen de la oportunidad")
  
class RunmexSoluciones(models.Model):
	_name = 'runmex.soluciones'
	name  = fields.Char('Soluciones', required=True)
	
class RunmexOrigen(models.Model):
	_name = 'runmex.origen'
	name  = fields.Char('Origen', required=True)
	
#crm_custom_fields()
