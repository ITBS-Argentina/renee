# Copyright 2022 Tecnativa - Sergio Teruel
# Copyright 2023 Tecnativa - Carolina Fernandez
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Stock Picking Import Serial Numbers",
    "summary": "Import S/N from excel file for incoming pickings",
    "version": "15.0.2.0.0",
    "development_status": "Production/Stable",
    "category": "stock",
    "website": "https://github.com/OCA/stock-logistics-workflow",
    "author": "Tecnativa, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "installable": True,
    "depends": ["stock"],
    "data": [
        "wizard/import_serial_number_view.xml",
        "views/res_config_settings_views.xml",
        "views/stock_picking.xml",
        "security/ir.model.access.csv",
    ],
    "external_dependencies": {"python": ["xlrd"]},
    "maintainers": ["sergio-teruel"],
}
