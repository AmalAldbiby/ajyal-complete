from odoo import fields, models

class EducationStudent(models.Model):
	_inherit ='education.student'

	behavior_count = fields.Integer(compute='_compute_behavior_count')

	def _compute_behavior_count(self):
		for student in self:
			student.behavior_count = self.env['education.behavior'].search_count(
				[('student_id', '=', student.id)]
				)