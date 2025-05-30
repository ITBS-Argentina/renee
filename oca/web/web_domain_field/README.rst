================
Web Domain Field
================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:3f7d060f86b7af93de337bbdfe21db684a89efd18249d2a4b1e5f23167597704
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fweb-lightgray.png?logo=github
    :target: https://github.com/OCA/web/tree/15.0/web_domain_field
    :alt: OCA/web
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/web-15-0/web-15-0-web_domain_field
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/web&target_branch=15.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

When you define a view you can specify on the relational fields a domain
attribute. This attribute is evaluated as filter to apply when displaying
existing records for selection.

**Table of contents**

.. contents::
   :local:

Usage
=====

When you define a view you can specify on the relational fields a domain
attribute. This attribute is evaluated as filter to apply when displaying
existing records for selection.

.. code-block:: xml

   <field name="product_id" domain="[('type','=','product')]"/>

The value provided for the domain attribute must be a string representing a
valid Odoo domain. This string is evaluated on the client side in a
restricted context where we can reference as right operand the values of
fields present into the form and a limited set of functions.

In this context it's hard to build complex domain and we are facing to some
limitations as:

 * The syntax to include in your domain a criteria involving values from a
   x2many field is complex.
 * The right side of domain in case of x2many can involve huge amount of ids
   (performance problem).
 * Domains computed by an onchange on an other field are not recomputed when
   you modify the form and don't modify the field triggering the onchange.
 * It's not possible to extend an existing domain. You must completely redefine
   the domain in your specialized addon
 * etc...

In order to mitigate these limitations this new addon allows you to use the
value of a field as domain of an other field in the xml definition of your
view.

.. code-block:: xml

   <field name="product_id_domain" invisible="1"/>
   <field name="product_id" domain="product_id_domain"/>

The field used as domain must provide the domain as a JSON encoded string.

.. code-block:: python

   product_id_domain = fields.Char(
       compute="_compute_product_id_domain",
       readonly=True,
       store=False,
   )

   @api.depends('name')
   def _compute_product_id_domain(self):
       for rec in self:
           rec.product_id_domain = json.dumps(
               [('type', '=', 'product'), ('name', 'like', rec.name)]
           )

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/web/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/web/issues/new?body=module:%20web_domain_field%0Aversion:%2015.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* ACSONE SA/NV

Contributors
~~~~~~~~~~~~

* Laurent Mignon <laurent.mignon@acsone.eu>
* Denis Roussel <denis.roussel@acsone.eu>
* Raf Ven <raf.ven@dynapps.be>

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/web <https://github.com/OCA/web/tree/15.0/web_domain_field>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
