#-*- coding: utf-8 -*-
from odoo import models, fields, api
class PersonalizacionSet(models.Model):
  _name = 'personalizacion.set'
  _inherit = ['personalizacion.set','mail.thread']
  user_id = fields.Many2one('res.user', 'Responsible')
  date_deadline = fields.Date('Deadline')
  name = fields.Char(help="Breve descripcion de latarea.")

  #def do_marcar(self):
  #  if self.user_id != self.env.user:
  #    raise Exception('Solo el responsable ha demarcarla como hecha!')
  #  else:
  #    return super(personalizacion user, self).do_marcar()

  #def do_limpiar(self):
  #  domain = [('is_done', '=', True), '|', ('user_id','=', self.env.uid), ('user_id', '=', False)]
  #  done_recs = self.search(domain)
  #  done_recs.write({'active': False})
  #  return True
