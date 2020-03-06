.. _hanwha_pickit_interface:

Hanwha Pickit interface
=======================

This article documents the interface of the Hanwha Pickit integration.
For installation instructions, please refer to the :ref:`hanwha_installation_and_setup` article.

Pickit variables
----------------

The following variables need to be defined before you can use the Pickit functions.
To do this go to :guilabel:`Programming` → :guilabel:`Variables` → :guilabel:`Add`.
Once a variable is created, its name should be changed according to the table below.

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
| piRemain      | number   | number of remaining objects that can be sent to the robot in the next messages                                                     |
+---------------+----------+------------------------------------------------------------------------------------------------------------------------------------+
| piStatus      | number   | Pickit status or a response to previously received robot commands                                                                  |
+---------------+----------+------------------------------------------------------------------------------------------------------------------------------------+
| piType        | number   | ID type of the detected object                                                                                                     |
+---------------+----------+------------------------------------------------------------------------------------------------------------------------------------+

Define piRefJoint
~~~~~~~~~~~~~~~~~

To prevent strange movements of the robot, we need to define the robot joint configuration for picking.
This is done by jogging the robot to the center of the picking area and manually set the joint position values of **piRefJoint**.
This position will indicate the desired robot configuration, which will be used for all calculated pick poses. 

Pickit functions
----------------

First, download the integration files :ref:`here <downloads:Hanwha>`.
Copy all the .script files to a USB drive and plug it in the teach pendant.
To add a Pickit function in your robot program go to :guilabel:`Commands` → :guilabel:`script`.
A new **script** node will be created.
Press this node and :guilabel:`edit` → :guilabel:`file` → :guilabel:`load`.
This allows you to select the **.script** function that you want to add.

All available functions are briefly explained below.

Defining the IP adress of Pickit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before any of these functions can be used, please make sure to set the correct IP address of the Pickit system.
This is done by pressing on the node and :guilabel:`edit`.
Here you can set the IP address, which is set to **169.254.5.180** by default.

+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| Function name          | Comment                                                                                                                                                  | Input                  |
+========================+==========================================================================================================================================================+========================+
| Build background       | Build the background cloud used in :ref:`advanced-roi-filters`.                                                                                          | /                      |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| Calibration            | Trigger a detection of the robot-camera calibration plate.                                                                                               | /                      |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| Capture image          | Trigger Pickit to capture a camera image to be used by a following **Process image** function.                                                           | /                      |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| Configuration          | Load the specified setup and product :ref:`Configuration`.                                                                                               | setup, product         |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| Detection with retries | Repeatedly trigger a Pickit object detection as long as nothing is found and the ROI is not empty, up to a number of attempts.                           | retries, pickit_offset |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| Detection              | Trigger a Pickit object detection using the currently active setup and product :ref:`Configuration`.                                                     | pickit_offset          |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| Next object            | Request the next detected object.                                                                                                                        | pickit_offset          |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| Process image          | Trigger an object detection on the camera image that was previously captured via the **Capture image** function (or one of the **Detection** functions). | pickit_offset          |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| Save scene             | Save a :ref:`Snapshots` with the latest detection results.                                                                                               | /                      |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+

.. hint:: In some functions, input values have to be set manually.
  This is done by pressing on the node and :guilabel:`edit`.
  The mentioned input variables can be found in the 20 first lines of each function.