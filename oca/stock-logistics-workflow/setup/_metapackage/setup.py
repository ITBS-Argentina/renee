import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-stock-logistics-workflow",
    description="Meta package for oca-stock-logistics-workflow Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-delivery_procurement_group_carrier>=15.0dev,<15.1dev',
        'odoo-addon-product_cost_price_avco_sync>=15.0dev,<15.1dev',
        'odoo-addon-product_supplierinfo_for_customer_picking>=15.0dev,<15.1dev',
        'odoo-addon-purchase_stock_picking_invoice_link>=15.0dev,<15.1dev',
        'odoo-addon-sale_line_returned_qty>=15.0dev,<15.1dev',
        'odoo-addon-sale_line_returned_qty_mrp>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_global_stock_route>=15.0dev,<15.1dev',
        'odoo-addon-stock_account_product_run_fifo_hook>=15.0dev,<15.1dev',
        'odoo-addon-stock_auto_move>=15.0dev,<15.1dev',
        'odoo-addon-stock_delivery_note>=15.0dev,<15.1dev',
        'odoo-addon-stock_force_assign_by_type>=15.0dev,<15.1dev',
        'odoo-addon-stock_landed_costs_delivery>=15.0dev,<15.1dev',
        'odoo-addon-stock_landed_costs_priority>=15.0dev,<15.1dev',
        'odoo-addon-stock_landed_costs_purchase_auto>=15.0dev,<15.1dev',
        'odoo-addon-stock_landed_costs_security>=15.0dev,<15.1dev',
        'odoo-addon-stock_lot_on_hand_first>=15.0dev,<15.1dev',
        'odoo-addon-stock_lot_product_qty_search>=15.0dev,<15.1dev',
        'odoo-addon-stock_move_change_source_location>=15.0dev,<15.1dev',
        'odoo-addon-stock_move_consu_location_from_putaway>=15.0dev,<15.1dev',
        'odoo-addon-stock_move_line_auto_fill>=15.0dev,<15.1dev',
        'odoo-addon-stock_move_name_from_sale_line>=15.0dev,<15.1dev',
        'odoo-addon-stock_move_original_date>=15.0dev,<15.1dev',
        'odoo-addon-stock_move_propagate_first_move>=15.0dev,<15.1dev',
        'odoo-addon-stock_move_quick_lot>=15.0dev,<15.1dev',
        'odoo-addon-stock_no_negative>=15.0dev,<15.1dev',
        'odoo-addon-stock_owner_restriction>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_assign_serial_final>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_auto_create_lot>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_back2draft>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_backorder_strategy>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_batch_extended>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_batch_extended_account>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_batch_extended_account_sale_type>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_batch_operation_quick_change>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_batch_outgoing>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_batch_set_quantity>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_customer_ref>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_filter_lot>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_import_serial_number>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_info_lot>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_invoice_link>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_line_sequence>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_mass_action>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_operation_manual_lot_selection>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_operation_quick_change>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_origin_reference>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_origin_reference_purchase>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_origin_reference_sale>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_product_assortment>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_product_assortment_availability_inline>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_product_availability_inline>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_product_availability_search>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_propagate_scheduled_date>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_purchase_order_link>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_return_restricted_qty>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_sale_order_link>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_send_by_mail>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_show_backorder>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_show_lot>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_show_return>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_start>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_warn_message>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_whole_scrap>=15.0dev,<15.1dev',
        'odoo-addon-stock_product_set>=15.0dev,<15.1dev',
        'odoo-addon-stock_production_lot_active>=15.0dev,<15.1dev',
        'odoo-addon-stock_production_lot_traceability>=15.0dev,<15.1dev',
        'odoo-addon-stock_push_delay>=15.0dev,<15.1dev',
        'odoo-addon-stock_putaway_hook>=15.0dev,<15.1dev',
        'odoo-addon-stock_receipt_lot_info>=15.0dev,<15.1dev',
        'odoo-addon-stock_reception_discrepancy_distribution>=15.0dev,<15.1dev',
        'odoo-addon-stock_remote_measure>=15.0dev,<15.1dev',
        'odoo-addon-stock_restrict_lot>=15.0dev,<15.1dev',
        'odoo-addon-stock_return_request>=15.0dev,<15.1dev',
        'odoo-addon-stock_scrap_tier_validation>=15.0dev,<15.1dev',
        'odoo-addon-stock_split_picking>=15.0dev,<15.1dev',
        'odoo-addon-stock_valuation_fifo_lot>=15.0dev,<15.1dev',
        'odoo-addon-stock_valuation_layer_usage>=15.0dev,<15.1dev',
        'odoo-addon-stock_warn_option>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
