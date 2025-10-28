from odoo import api, fields, models
from odoo.exceptions import UserError
from datetime import datetime

class EducationBehavior(models.Model):
	_name = 'education.behavior'
	_inherit = ['mail.thread', 'mail.activity.mixin']
	_description = 'Students behavior and Discipline'
	_order = 'date desc, id desc' #To arrange data display

	#serial number YY-Sequence (Ex: 25-001)
	@api.model
	def create (self, vals):
		sequence = self.env['ir.sequence'].next_by_code('education.behavior') or ''
		current_year = str(datetime.now().year)[-2:]
		vals['name'] = f"{current_year}/{sequence}"
		res = super(EducationBehavior, self).create(vals)
		return res

	name = fields.Char(string='Sequence', help="Ex: 25-001")
	#One student have Many behavior report
	student_id = fields.Many2one('education.student', string='Student Id', required=True, Tracking=True)
	class_id = fields.Char(string='Class Id', required=True)
	date = fields.Date(required=True)

	category = fields.Selection([
		('behavior','Behavior'),
		('attendance','Attendance')
		], default= 'behavior', Tracking=True)

	level = fields.Selection([
		('level one','Level One'), ('level two','Level Two'),
		('level three','Level Three'), ('level four','Level Four'),
		('level five','Level Five')], default='level one', Tracking=True)

	description = fields.Char(string='behavior description',required=True)
	action_taken = fields.Text(string='Action Taken', required=True)
	responsible_id = fields.Selection([
		('teacher','Teacher'),('guide','Guide'),
		('agent','Agent')], default='teacher', Tracking=True)

	state = fields.Selection([
		('new','New'),('certified','Certified'),
		('closed','Closed')], default='new', Tracking=True)

	attachment_ids = fields.Many2many('ir.attachment', string='Attachment', required=True)

	def action_certified(self):
		self.ensure_one()
		self.state = 'certified'

	def action_new(self):
		self.ensure_one()
		self.state = 'new'

	def action_closed(self):
		self.ensure_one()
		self.state = 'closed'