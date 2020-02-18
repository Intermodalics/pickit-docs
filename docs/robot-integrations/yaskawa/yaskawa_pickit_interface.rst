.. _yaskawa_pickit_interface:

Yaskawa Pickit interface
========================

This article documents the interface of the Yaskawa Pickit integration.
For installation instructions, please refer to the :ref:`yaskawa_installation_and_setup` article.

Pickit macros
-------------

Below you find an overview of the macros defined by Pickit. 

+---------+------------+---------------------------------------------------------------------------------------------------------+
| MACRO   | Field name | Comment                                                                                                 |
+=========+============+=========================================================================================================+
| MACRO1  | PI_CALIB   | Trigger detection of the robot-camera calibration plate.                                                |
+---------+------------+---------------------------------------------------------------------------------------------------------+
| MACRO2  | PI_LOOK    | Trigger a Pickit object detection using the currently active setup and product configuration.           |
+---------+------------+---------------------------------------------------------------------------------------------------------+
| MACRO3  | PI_WAIT    | Wait for Pickit reply with detection results. PI_WAIT should always be the next Pickit command after a  |
|         |            | PI_LOOK or PI_NEXT request.                                                                             |
+---------+------------+---------------------------------------------------------------------------------------------------------+
| MACRO4  | PI_NEXT    | Request the next detected object.                                                                       |
+---------+------------+---------------------------------------------------------------------------------------------------------+
| MACRO5  | PI_CFG     | Loads the specified setup and product :ref:`Configuration`.                                             |
+---------+------------+---------------------------------------------------------------------------------------------------------+
| MACRO6  | PI_SAVE    | Save a :ref:`Snapshots` with the latest detection results.                                              |
+---------+------------+---------------------------------------------------------------------------------------------------------+
| MACRO7  | PI_RUN     | Check the current mode of Pickit.                                                                       |
+---------+------------+---------------------------------------------------------------------------------------------------------+
| MACRO8  | PI_GPPD    | Requests the pick point ID and pick point offset of the last requested object.                          |
+---------+------------+---------------------------------------------------------------------------------------------------------+
| MACRO9  | PI_CAPTU   | Trigger Pickit to capture a camera image to be used by a following PI_PROCE command.                    |
+---------+------------+---------------------------------------------------------------------------------------------------------+
| MACRO10 | PI_PROCE   | Trigger an object detection on the camera image that was previously captured via PI_CAPTU command.      |
+---------+------------+---------------------------------------------------------------------------------------------------------+
| MACRO11 | PI_BUILD   | Build the background cloud used in :ref:`advanced-roi-filters`.                                         |
+---------+------------+---------------------------------------------------------------------------------------------------------+

.. tip:: The ID's of the macros can be changed by :ref:`manually defining the Pickit macros <manually-define_macros>`.
  Note if the ID's are changed the provided example programs by Pickit need to be altered accordingly.

Following macros have input arguments that need to be filled in when you call them.

PI_CALIB
~~~~~~~~

- **USER FRAME**: User frame created at start of TEST_CALIB. By default, this is **5**.

.. _pi_cfg:

PI_CFG
~~~~~~

- **SETUP**: Pickit setup file ID.
- **PRODUCT**: Pickit product file ID.
- **USER FRAME**: User frame that was created in TEST_CALIB. By default, this is **5**.
- **TOOL**: Tool frame ID that is used by robot for picking.
- **TIMEOUT**: Value of the timeout used for communication with Pickit.

.. note:: If something is wrong here, you can expect the following message: Undefined user frame.
   The example program by default uses frame 5 and tool 1, but these might not exist.

Pickit registers
----------------

Below you find an overview of the variables used by Pickit.
When using Pickit these variables cannot be used for anything else.

+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| Variable | Field name       | Comment                                                                                                                                 | Type     |
+==========+==================+=========================================================================================================================================+==========+
| I049     | command          | A single command from robot to Pickit.                                                                                                  | Input    |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| I048     | setup            | A number matching to a setup file known by the Pickit system.                                                                           | Input    |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| I047     | product          | A number matching to a product file known by the Pickit system.                                                                         | Input    |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| I046     | Frame ID         | A number matching the frame ID used during calibration and picking.                                                                     | Input    |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| I045     | Tool ID          | A number matching the tool ID used for picking.                                                                                         | Input    |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| I044     | Timeout          | Value of the timeout used for communication with Pickit.                                                                                | Input    |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| I042     | pick_id          | ID of the pick point that was selected for the given object.                                                                            | Output   |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| I041     | object_type      | The type of detected object.                                                                                                            | Output   |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| I040     | status           | Contains the Pickit status or a response to previously received robot commands.                                                         | Output   |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| I030-039 | status of cycles | Used for keeping track of the communication cycle with Pickit.                                                                          | Internal |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| S049     | IP Pickit        | IP address of Pickit, by default 169.254.5.180.                                                                                         | Input    |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| P049     | object_pose      | An object pose expressed relatively to the robot base frame.                                                                            | Output   |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| P048     | object_dimension | [0]: length or diameter (m) [1]: width or diameter (m) [2]: height (m).                                                                 | Output   |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| P047     | object_offset    | pick point offset of the last requested object.                                                                                         | Output   |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| P046     | rx_flip          | A helper pose to calculate a correct offset pose.                                                                                       | Internal |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| D042     | pick_ref_id      | ID of the selected pick point’s reference pick point.                                                                                   | Output   |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| D041     | object_remaining | If this field is non-zero, it contains the number of remaining objects that can be sent in next messages to the robot.                  | Output   |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+
| D040     | object_age       | The amount of time that has passed between the capturing of the camera data and the moment the object information is sent to the robot. | Output   |
+----------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------+

.. tip:: If these registers are already used on your robot, please contact us at `support@pickit3d.com <mailto:support@pickit3d.com>`__, and we will assist you in finding a solution.