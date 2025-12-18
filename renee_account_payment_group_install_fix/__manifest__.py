# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Renee Account Payment Group Install Fix',
    'version': '15.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Fix payment group names using first payment name',
    'author': 'Renee',
    'license': 'AGPL-3',
    'depends': [
        'base',
    ],
    'data': [
        'data/ir_actions_server.xml',
    ],
    'installable': True,
    'auto_install': False,
}
