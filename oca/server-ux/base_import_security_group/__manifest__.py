# Copyright 2015 Anubía, soluciones en la nube,SL (http://www.anubia.es)
# Copyright 2017 Onestein (http://www.onestein.eu)
# Copyright (C) 2019-Today: Druidoo (<https://www.druidoo.io>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Optional CSV import",
    "version": "15.0.1.0.1",
    "category": "Server tools",
    "summary": "Group-based permissions for importing CSV files",
    "license": "AGPL-3",
    "author": "Odoo Community Association (OCA), "
    "Alejandro Santana <alejandrosantana@anubia.es>, "
    "Onestein",
    "maintainer": "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/server-ux",
    "depends": [
        "web",
        "web_tour",
        "base_import",
    ],
    "data": [
        "security/base_import_security_group_security.xml",
    ],
    "assets": {
        "web.assets_backend": ["base_import_security_group/static/src/js/import.js"],
        "web.assets_tests": [
            "base_import_security_group/static/src/js/tour_import.js",
        ],
    },
    "installable": True,
}
