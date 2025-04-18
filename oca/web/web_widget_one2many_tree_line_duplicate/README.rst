=======================================
Web Widget One2many Tree Line Duplicate
=======================================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:620c16e6d6bd0ad72a9d7eb3c8f243fbbf721898252fea9c26d70b2e0a7822d7
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fweb-lightgray.png?logo=github
    :target: https://github.com/OCA/web/tree/15.0/web_widget_one2many_tree_line_duplicate
    :alt: OCA/web
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/web-15-0/web-15-0-web_widget_one2many_tree_line_duplicate
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/web&target_branch=15.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

Allow to add a icon to clone the line.

**Table of contents**

.. contents::
   :local:

Usage
=====

This module works on all one2many tree views. The cloning process doesn't trigger onchange/default calls.

**Available Options**

- allow_clone > Add the icon to clone the line (default: false)

**Examples**

.. code:: xml

  <field name="order_line" widget="section_and_note_one2many" mode="tree,kanban" options="{'allow_clone': True}" attrs="{'readonly': [('state', 'in', ('done','cancel'))]}">

Known issues / Roadmap
======================

* Add an option to control which columns are copied

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/web/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/web/issues/new?body=module:%20web_widget_one2many_tree_line_duplicate%0Aversion:%2015.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Tecnativa

Contributors
~~~~~~~~~~~~

* `Tecnativa <https://www.tecnativa.com/>`_:

  * Alexandre Díaz

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/web <https://github.com/OCA/web/tree/15.0/web_widget_one2many_tree_line_duplicate>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
