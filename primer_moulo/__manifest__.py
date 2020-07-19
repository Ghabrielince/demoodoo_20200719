# -*- coding: utf-8 -*-
{
    'name': "Mascotas",

    'summary': """
        Gestión de mascotas del hogar""",

    'description': """
        Con este módulo podremos registrar a cada una de nuestras mascotas y además llevar un control 
        de las veces de necesitamos o hemos llevado a sus diviersos controles de salud.
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/razas_views.xml',
        'views/tipos_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}