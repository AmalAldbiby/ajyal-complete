{
    'name': 'Educational Behavior Management',
    'version': '17.0.1.0.0',
    'category': 'Industries',
    'summary': """"Openerp to Student Attendance Management System for 
     Educational ERP""",
    'description': """Students behavior and Discipline""",
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "http://www.educationalerp.com",
    'depends': ['base',
    'education_core'],
    'data': [
        'security/ir.model.access.csv',
        'data/education_behavior_sequence.xml',
        'views/education_behavior_view.xml',
        'views/base_menu.xml',
        'views/education_student_inherit_view.xml',
    ],
    'application': True,
}