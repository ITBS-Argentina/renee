You need to define a view with the tag <timeline> as base element. These are
the possible attributes for the tag:

+--------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Attribute          | Required? | Description                                                                                                                                                                                                                                                                         |
+====================+===========+=====================================================================================================================================================================================================================================================================================+
| date_start         | **Yes**   | Defines the name of the field of type date that contains the start of the event.                                                                                                                                                                                                    |
+--------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| date_stop          | No        | Defines the name of the field of type date that contains the end of the event. The date_stop can be equal to the attribute date_start to display events has 'point' on the Timeline (instantaneous event).                                                                          |
+--------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| date_delay         | No        | Defines the name of the field of type float/integer that contain the duration in hours of the event, default = 1.                                                                                                                                                                   |
+--------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| default_group_by   | **Yes**   | Defines the name of the field that will be taken as default group by when accessing the view or when no other group by is selected.                                                                                                                                                 |
+--------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zoomKey            | No        | Specifies whether the Timeline is only zoomed when an additional key is down. Available values are '' (does not apply), 'altKey', 'ctrlKey', or 'metaKey'. Set this option if you want to be able to use the scroll to navigate vertically on views with a lot of events.           |
+--------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| horizontalScroll   | No        | This option allows you to scroll horizontally to move backwards and forwards in the time range. Only applicable when option zoomKey is defined or zoomable is false.                                                                                                                |
+--------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| verticalScroll     | No        | Show a vertical scroll on the side of the group list and link it to the scroll event when zoom is not triggered. Notice that defining this option as true will NOT override horizontalScroll. The scroll event will be vertically ignored, but a vertical scrollbar will be visible |
+--------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| mode               | No        | Specifies the initial visible window. Available values are: 'day' to display the current day, 'week', 'month' and 'fit'. Default value is 'fit' to adjust the visible window such that it fits all items.                                                                           |
+--------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| margin             | No        | Specifies the margins around the items. It should respect the JSON format. For example '{"item":{"horizontal":-10}}'. Available values are: '{"axis":<number>}' (The minimal margin in pixels between items and the time axis)                                                      |
|                    |           | '{"item":<number>}' (The minimal margin in pixels between items in both horizontal and vertical direction), '{"item":{"horizontal":<number>}}' (The minimal horizontal margin in pixels between items),                                                                             |
|                    |           | '{"item":{"vertical":<number>}}' (The minimal vertical margin in pixels between items), '{"item":{"horizontal":<number>,"vertical":<number>}}' (Combination between horizontal and vertical margins in pixels between items).                                                       |
+--------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| event_open_popup   | No        | When set to true, it allows to edit the events in a popup. If not (default value), the record is edited changing to form view.                                                                                                                                                      |
+--------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| stack              | No        | When set to false, items will not be stacked on top of each other such that they do overlap.                                                                                                                                                                                        |
+--------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| colors             | No        | Allows to set certain specific colors if the expressed condition (JS syntax) is met.                                                                                                                                                                                                |
+--------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dependency_arrow   | No        | Set this attribute to a x2many field to draw arrows between the records referenced in the x2many field.                                                                                                                                                                             |
+--------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Optionally you can declare a custom template, which will be used to render the
timeline items. You have to name the template 'timeline-item'.
These are the variables available in template rendering:

* ``record``: to access the fields values selected in the timeline definition.
* ``field_utils``: used to format and parse values (see available functions in ``web.field_utils``).

You also need to declare the view in an action window of the involved model.

Example:

.. code-block:: xml

    <?xml version="1.0" encoding="utf-8"?>
    <odoo>
        <record id="view_task_timeline" model="ir.ui.view">
            <field name="model">project.task</field>
            <field name="type">timeline</field>
            <field name="arch" type="xml">
                <timeline date_start="date_assign"
                          date_stop="date_end"
                          string="Tasks"
                          default_group_by="user_id"
                          event_open_popup="true"
                          zoomKey="ctrlKey"
                          colors="#ec7063:user_id == false;#2ecb71:kanban_state=='done';"
                          dependency_arrow="task_dependency_ids">
                    <field name="user_id"/>
                    <templates>
                        <div t-name="timeline-item">
                            <div t-esc="record.display_name"/>
                            Assigned to:
                            <span t-esc="record.user_id[1]"/>
                        </div>
                    </templates>
                </timeline>
            </field>
        </record>

        <record id="project.action_view_task" model="ir.actions.act_window">
            <field name="view_mode">kanban,tree,form,calendar,gantt,timeline,graph</field>
        </record>
    </odoo>
