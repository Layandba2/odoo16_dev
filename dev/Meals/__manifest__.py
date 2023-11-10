{
    'name' : 'Meals',
    'license': 'LGPL-3',
    'version' : '1.0',
    'author' : 'DSI IT',
    'summary': 'Meals Ordering Capture',
    'depends': ['mail'],
    'data' : [
        'security/ir.model.access.csv',
        'views/meal_menu.xml',
        'views/meal_supplier_view.xml',
        'views/meal_rotation_settings_view.xml',
        'views/meal_loc_view.xml',
        'views/meal_order_machine.xml',
        'views/meal_order_view.xml',
        'views/meal_product_view.xml',
        'views/breakfast_order_view.xml',
        'views/breakfast_invoice_view.xml',
        'reports/breakfast_invoice.xml',
        'reports/report.xml',

    ]

}