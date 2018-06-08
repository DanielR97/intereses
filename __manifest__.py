# -*- coding: utf-8 -*-
{
    'name': "Intereses",

    'summary': """
        Módulo para llevar un segumiento de los intereses de los usuarios""",

    'description': """
        Este módulo llevará almacenados los datos de intereses y hobbies de los usuarios del mismo,
        ya sean simples usuarios del módulo o posibles compradores de un producto""",

    'author': "Daniel Ramos Fuentes",
    'website': "https://github.com/DanielR97",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
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
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}