# -*- coding: utf-8 -*-

from openerp import models, fields, api
from datetime import date, datetime, timedelta

class venex_stock_picking(models.Model):
	_name = 'stock.picking'
	_inherit = 'stock.picking'

	move_type = fields.Selection([('direct', 'Partial'), ('one', 'All at once')], 'Delivery Method', default='one')
	
	correlativo_anterior = fields.Char('Correlativo ant.', help="Correlativo Anterior")
	estado_id = fields.Many2one('res.country.state','Estado')
	municipio_id = fields.Many2one('municipio','Municipio')
	parroquia_id = fields.Many2one('parroquia','Parroquia')
	direccion_entrega = fields.Char('Dirección de Entrega')
	punto_referencia = fields.Char('Punto de Referencia')
	nombre_contacto = fields.Char('Nombre Contacto')
	telefono_contacto = fields.Char('Teléfono Contacto')
	vehiculo_id = fields.Many2one('fleet.vehicle','Vehículo')
	conductor_id = fields.Many2one('fleet.conductor','Conductor')
	observaciones = fields.Text('Observaciones')
	eventos_ids = fields.One2many('stock.picking.eventos','stock_picking_id','Eventos')
	
class venex_stock_eventos(models.Model):
	_name = 'stock.picking.eventos'
	fecha = fields.Date('Fecha', default=datetime.today())
	titulo = fields.Char('Título')
	descripcion = fields.Text('Descripción')
	usuario_id = fields.Many2one('res.users','Usuario')
	stock_picking_id = fields.Many2one ('stock.picking','Transferencia')

	_defaults = {'usuario_id': lambda self, cr, uid, ctx=None: uid}