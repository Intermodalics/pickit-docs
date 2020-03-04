.. _hanwha_pickit_interface:

Hanwha Pickit interface
=======================

This article documents the interface of the Hanwha Pickit integration.
For installation instructions, please refer to the :ref:`hanwha_installation_and_setup` article.

Pickit variables
----------------

Following variables need to be defined before you can use the Pickit functions.
To do this go to :guilabel:`Programming` → :guilabel:`Variables` → :guilabel:`Add`.
Once a variable is created the name can be changed according the table below.

+---------------+----------+------------------------------------------------------------------------------------------------------------------------------------+
| Variable name | Type     | Comment                                                                                                                            |
+===============+==========+====================================================================================================================================+
| piAge         | number   | amount of time that has passed between the capturing of the camera data and the moment the object information is sent to the robot |
+---------------+----------+------------------------------------------------------------------------------------------------------------------------------------+
| piDim1        | number   | length or diameter (mm)                                                                                                            |
+---------------+----------+------------------------------------------------------------------------------------------------------------------------------------+
| piDim2        | number   | width or diameter (mm)                                                                                                             |
+---------------+----------+------------------------------------------------------------------------------------------------------------------------------------+
| piDim3        | number   | height (mm)                                                                                                                        |
+---------------+----------+------------------------------------------------------------------------------------------------------------------------------------+
| piPickId      | number   | ID of the pick point that was selected for the given object                                                                        |
+---------------+----------+------------------------------------------------------------------------------------------------------------------------------------+
| piPose        | position | object pose expressed relatively to the robot base frame                                                                           |
+---------------+----------+------------------------------------------------------------------------------------------------------------------------------------+
| piPrePose     | joint    | joint pose relatively to the piPose, used to approach the piPose                                                                   |
+---------------+----------+------------------------------------------------------------------------------------------------------------------------------------+
| piRefId       | number   | ID of the selected pick point’s reference pick point                                                                               |
+---------------+----------+------------------------------------------------------------------------------------------------------------------------------------+
| piRefJoint    | joint    | joint position used for robot joint configuration, typically defined in the middle of the picking area                             |
+---------------+----------+------------------------------------------------------------------------------------------------------------------------------------+
| piRemain      | number   | number of remaining objects that can be sent in next messages to the robot                                                         |
+---------------+----------+------------------------------------------------------------------------------------------------------------------------------------+
| piStatus      | number   | Pickit status or a response to previously received robot commands                                                                  |
+---------------+----------+------------------------------------------------------------------------------------------------------------------------------------+
| piType        | number   | ID type of the detected object                                                                                                     |
+---------------+----------+------------------------------------------------------------------------------------------------------------------------------------+

Define piRefJoint
~~~~~~~~~~~~~~~~~

To prevent strange movements of the robot we need to define the robot joint configuration for picking.
This is done by jogging the robot to the center of the picking area and manually set the joint position values of **piRefJoint**.
This will be used as seed for all calculated pick poses. 

Pickit functions
----------------

First download the integration files :ref:`here <downloads:Hanwha>`.
To add a Pickit function in your robot program do :guilabel:`Commands` → :guilabel:`script`.
Now a new **script** node will be created.
Press this node and :guilabel:`edit` → :guilabel:`file` → :guilabel:`load`.
Now you can select the **.script** function that you want to add.

+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| Variable | Field name       | Comment                                                                                                                                 | Type     |
+==========+==================+=========================================================================================================================================+==========+
| I049     | command          | command from robot to Pickit                                                                                                            | Input    |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| I048     | setup            | setup file ID known by the Pickit system                                                                                                | Input    |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| I047     | product          | product file ID known by the Pickit system                                                                                              | Input    |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| I046     | Frame ID         | frame ID used during calibration and picking                                                                                            | Input    |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| I045     | Tool ID          | tool ID used for picking                                                                                                                | Input    |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| I044     | Timeout          | timeout used for communication with Pickit [ms]                                                                                         | Input    |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| I042     | pick_id          | ID of the pick point that was selected for the given object                                                                             | Output   |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| I041     | object_type      | ID type of the detected object                                                                                                          | Output   |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| I040     | status           | Pickit status or a response to previously received robot commands                                                                       | Output   |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| I030-039 | status of cycles | used for keeping track of the communication cycle with Pickit                                                                           | Internal |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| S049     | IP Pickit        | IP address of Pickit, by default 169.254.5.180                                                                                          | Input    |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| P049     | object_pose      | object pose expressed relatively to the robot base frame                                                                                | Output   |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| P048     | object_dimension | [0]: length or diameter (m) [1]: width or diameter (m) [2]: height (m)                                                                  | Output   |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| P047     | object_offset    | pick point offset of the last requested object                                                                                          | Output   |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| P046     | rx_flip          | helper pose to calculate a correct offset pose                                                                                          | Internal |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| D042     | pick_ref_id      | ID of the selected pick point’s reference pick point                                                                                    | Output   |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| D041     | object_remaining | number of remaining objects that can be sent in next messages to the robot                                                              | Output   |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| D040     | object_age       | amount of time that has passed between the capturing of the camera data and the moment the object information is sent to the robot      | Output   |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+

.. tip:: If these registers are already used on your robot, please contact us at `support@pickit3d.com <mailto:support@pickit3d.com>`__, and we will assist you in finding a solution.