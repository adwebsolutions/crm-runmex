{
    'name': 'RUMEX CRM campos adicionales',
    'category': 'Tools',
    'summary': 'Incluye campos adicionales en el crm de Runmex desarrollados por ADWEB',
    'website': 'https://www.adweb.mx',
    'version': '1.0',
    'description': """
Modulo de ADWEB para RUMEX - CRM
===================================
    Este módulo incluye un grupo de campos nuevos a los modelos res.partners y crm.lead, para cumplir los requerimientos de RUMEX

    
        """,
    'author': 'ADWEB',
    'depends': ['crm'], 
    'external_dependencies': {},
    'data': ['views/crm_custom_fields.xml','views/partner_custom_fields.xml'],
    'installable': True,
    'auto_install':False,
    'active':False,
}
