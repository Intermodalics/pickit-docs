.. _fanuc-pickit-interface:

Fanuc Pickit interface
======================

This article documents the interface of the Fanuc Pickit integration.
For installation instructions, please refer to the :ref:`fanuc_installation_and_setup` article.

Pickit macros
-------------

Below you find an overview of the macros defined by Pickit. 

+---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Macro name                | Comment                                                                                                                                                                         |
+===========================+=================================================================================================================================================================================+
| PI_BUILD_BACKGROUND       | Build the background cloud used in :ref:`advanced-roi-filters`.                                                                                                                 |
+---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PI_CALIBRATE              | Trigger a detection of the robot-camera calibration plate.                                                                                                                      |
+---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PI_CAPTURE_IMAGE          | Trigger Pickit to capture a camera image to be used by a following PI_PROCESS_IMAGE command.                                                                                    |
+---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PI_CONFIGURE              | Load the specified setup and product :ref:`Configuration`.                                                                                                                      |
+---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PI_DETECTION_WITH_RETRIES | Trigger a Pickit object detection, if nothing is found and ROI is not empty Pickit will automatically retry a new detection.                                                    |
+---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PI_GET_PICK_POINT_DATA    | Request the pick point ID and pick point offset of the last requested object.                                                                                                   |
+---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PI_LOOK_FOR_OBJECT        | Trigger a Pickit object detection using the currently active setup and product :ref:`Configuration`.                                                                            |
+---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PI_NEXT_OBJECT            | Request the next detected object.                                                                                                                                               |
+---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PI_OPEN_COMMUNICATION     | Starts the socket communication with Pickit.                                                                                                                                    |
+---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PI_PROCESS_IMAGE          | Trigger an object detection on the camera image that was previously captured via PI_CAPTURE_IMAGE command (or PI_LOOK_FOR_OBJECT).                                              |
+---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PI_RUN                    | Check the current mode of Pickit.                                                                                                                                               |
+---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PI_SAVE_SCENE             | Save a :ref:`Snapshots` with the latest detection results.                                                                                                                      |
+---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PI_SET_PICK_POSE          | Get the current configuration of the robot. This is used as base configuration for calculated pick positions.                                                                   |
+---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PI_WAIT                   | Wait for Pickit reply with detection results. PI_WAIT should always be the next Pickit command after a PI_LOOK_FOR_OBJECT, PI_NEXT_OBJECT or PI_DETECTION_WITH_RETRIES request. |
+---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. tip:: The macros can be assigned to hotkeys on the teach pendant.
  This is done in :guilabel:`MENU` > :guilabel:`SETUP` > :guilabel:`Macro`.

Following macros have input arguments that need to be filled in when you call them.

.. _pi_configure:

PI_CONFIGURE
~~~~~~~~~~~~

- **Setup**: Pickit setup file ID.
- **Product**: Pickit product file ID.

.. _pi_detection_with_retries:

PI_DETECTION_WITH_RETRIES
~~~~~~~~~~~~~~~~~~~~~~~~~

- **Retries**: maximum number of retries before Pickit stops looking for objects.

Pickit registers
----------------

Below you find an overview of the variables used by Pickit.
When using Pickit these variables cannot be used for anything else.
More information about the variables can be found in :ref:`socket-communication`.

+---------------+---------------+---------------------------------------------------------------------------------------+----------+
| Variable      | Field name    | Comment                                                                               | Type     |
+===============+===============+=======================================================================================+==========+
| R[141]        | command       | command from robot to Pickit                                                          | Output   |
+---------------+---------------+---------------------------------------------------------------------------------------+----------+
| R[142]        | setup         | setup file ID known by the Pickit system                                              | Output   |
+---------------+---------------+---------------------------------------------------------------------------------------+----------+
| R[143]        | product       | product file ID known by the Pickit system                                            | Output   |
+---------------+---------------+---------------------------------------------------------------------------------------+----------+
| R[144]        | retries       | maximum number of retries for a Pickit detection                                      | Output   |
+---------------+---------------+---------------------------------------------------------------------------------------+----------+
| R[150]        | comm bit      | used to check if socket communication is running                                      | Input    |
+---------------+---------------+---------------------------------------------------------------------------------------+----------+
| R[151]        | object status | Pickit status of the object: OBJECT_FOUND, NO_OBJECTS, NO_IMAGE_CAPTURED or EMPTY_ROI | Input    |
+---------------+---------------+---------------------------------------------------------------------------------------+----------+
| R[152]        | status        | Pickit response to previously received robot commands                                 | Input    |
+---------------+---------------+---------------------------------------------------------------------------------------+----------+
| R[153]        | obj remaining | number of remaining objects that can be sent in next messages to the robot            | Input    |
+---------------+---------------+---------------------------------------------------------------------------------------+----------+
| R[154]-R[156] | obj dim 1-3   | [0]: length or diameter (m) [1]: width or diameter (m) [2]: height (m)                | Input    |
+---------------+---------------+---------------------------------------------------------------------------------------+----------+
| R[157]        | model id      | ID type of the detected object                                                        | Input    |
+---------------+---------------+---------------------------------------------------------------------------------------+----------+
| R[158]        | pick id       | ID of the pick point that was selected for the given object                           | Input    |
+---------------+---------------+---------------------------------------------------------------------------------------+----------+
| R[159]        | pick ref id   | ID of the selected pick point’s reference pick point                                  | Input    |
+---------------+---------------+---------------------------------------------------------------------------------------+----------+
| PR[51]        | pose          | object pose expressed relatively to the robot base frame                              | Input    |
+---------------+---------------+---------------------------------------------------------------------------------------+----------+
| PR[52]        | pick offset   | pick point offset of the last requested object                                        | Input    |
+---------------+---------------+---------------------------------------------------------------------------------------+----------+
| PR[53]        | x rot         | helper pose to calculate a correct offset pose                                        | Internal |
+---------------+---------------+---------------------------------------------------------------------------------------+----------+

.. tip:: If these registers are already used on your robot, please contact us at `support@pickit3d.com <mailto:support@pickit3d.com>`__, and we will assist you in finding a solution.