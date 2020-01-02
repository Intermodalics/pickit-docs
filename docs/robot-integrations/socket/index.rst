.. _socket-communication:

The low-level communication structures between a robot and Pickit on the TCP/IP socket level
=============================================================================================

This article documents the low-level communication structures between a robot and Pickit on the TCP/IP socket level. This information is only required to interface a new robot brand to Pickit.

Protocol
--------

The robot Pickit communication is based on TCP/IP socket communication. Pickit is the server (slave) and the robot is the client (master). Hence, the robot is responsible for opening the socket communication and needs to know:

-  The **IP address** of the Pickit port labelled ROBOT,
-  The **port number** which is **5001** by default.
-  Pickit communicates data packages using the **network byte order** convention (Big Endian).

.. image:: /assets/images/robot-integrations/socket/socket-1.png

Above you can find an example of the different behaviour between network byte order and host byte order.

.. warning::
    The robot client sends requests using the `command message <#command-message>`__, and the Pickit server answers with the `response message <#response-message>`__. These messages **have a static size**, and **don’t have a begin and/or end character**. While the TCP/IP protocol prevents data loss, the robot client implementation is responsible for keeping track of the boundary between messages by counting the number of sent/received bytes and comparing with the expected message size.

    There is **no explicit coupling between a command and a response** in the communication. Therefore, the robot client should not send a second command before having confirmed that a response to the first command has been received. It is the responsibility of the client implementation or the robot program to prevent this from happening.

The Pickit server only sends `response messages <#response-message>`__ after having received an explicit request from the robot client in a `command message <#command-message>`__. Apart from this request-response exchange, Pickit also expects to receive periodic **robot flange** pose updates from the client. The rate of these periodic updates depends on the robot brand, but is typically in the range of 10 to 50 messages per second. Note that both command requests and robot flange pose updates use the same message structure, ``robot_to_pickit_data``, described in more detail in the `command message <#command-message>`__ section. The structure of the response messages, ``pickit_to_robot_data``, is described in the `response message <#response-message>`__ section.

.. image:: /assets/images/robot-integrations/socket/socket-2.png

A Pickit data package consists of a number of **int32s** in network byte order. As such, floating-point data like distances and angles are multiplied by a factor MULT before being sent as an int32, and are divided by MULT after being received. This integer conversion factor **MULT** has the value of **10000**.

For **position** information Pickit sends and expects to receive values in **meter** before/after compensating with the MULT factor. For the **orientation** information it depends on the robot type. For UR **radians** are used, for ABB **unit quaternions** are used and for the other brands **degrees** are used. Also here, this is the unit before/after compensating with the MULT factor. 

.. _command-message:

Command message from robot to Pickit
------------------------------------

The data package communicated to Pickit contains the actual robot pose, an (optional) robot command and the desired configuration. The latter allows to request Pickit to configure according to an existing setup and product type. To find out the number associated to a setup or product file, go to the **Setup** page (for setup file) or **Detection** or **Picking** page (for product file) and press the :guilabel:`Open` button on top of the page. The number appears next to the file name.

In summary, the robot is required to send this structure to the Pickit Socket Interface:

::

    struct robot_to_pickit_data {
        int32 actual_pose[7];
        int32 command;
        int32 setup;
        int32 product;
        meta_data meta;
    };

Metadata fields are documented in the  `Message metadata <#message-metadata>`__ section of this article. The remaining fields are explained below.

+--------------------+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field name         | Type / units                     | Comment                                                                                                                                                                                                                          |
+====================+==================================+==================================================================================================================================================================================================================================+
| **actual\_pose**   | **int32[7]**                     | | Actual robot flange pose in robot base frame consisting of position in Cartesian space and orientation in axis angle, quaternion or Euler angles convention. The orientation convention and units depend on the robot brand.   |
|                    | [0-2] : position (m)             | | To populate array elements, each value has to be multiplied by the  **MULT** factor before being sent.                                                                                                                         |
|                    | [3-6] : orientation (rad,o,/)    |                                                                                                                                                                                                                                  |
+--------------------+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **command**        | **int32**                        | A single command from robot to Pickit.                                                                                                                                                                                           |
+--------------------+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                    | RC\_PICKIT\_NO\_COMMAND          | Use when sending a periodic pose update. Pickit does not reply to these requests.                                                                                                                                                |
+--------------------+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                    | RC\_PICKIT\_CHECK\_MODE          | Check the current mode of Pickit (RUNNING, IDLE or CALIBRATION)                                                                                                                                                                  |
+--------------------+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                    | RC\_PICKIT\_FIND\_CALIB\_PLATE   | Trigger the localisation of the Pickit camera-to-robot calibration plate.                                                                                                                                                        |
+--------------------+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                    | RC\_PICKIT\_LOOK\_FOR\_OBJECTS   | Trigger camera to look for new objects in its current workspace. Pickit will respond with the amount of objects currently found in the workspace, which may be zero, as well as the pose of the first object if one was detected.|
+--------------------+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                    | RC\_PICKIT\_NEXT\_OBJECT         | Request camera to return next localised object stored in the Pickit buffer and which was found with RC\_PICKIT\_LOOK\_FOR\_OBJECTS. Please note that the RC\_PICKIT\_LOOK\_FOR\_OBJECTS command already returns the first object,|
|                    |                                  | if one was detected.                                                                                                                                                                                                             |
+--------------------+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                    | RC\_PICKIT\_CONFIGURE            | Request Pickit to load a specific setup and product type.                                                                                                                                                                        |
+--------------------+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                    | RC\_PICKIT\_SAVE\_SCENE          | Request Pickit to save a :ref:`snapshot <Saving-a-snapshot>`. This is useful when your application is not behaving as you expect (for example, no objects detected in a non-empty bin). If you don't want to stop your application everytime such a situation occurs, you can instead save a snapshot from the robot program, and use it later to understand the problem and possibly improve the settings. |
+--------------------+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **setup**          | **int32**                        | A number matching to a setup known by the Pickit system.                                                                                                                                                                         |
|                    |                                  | Used only when the command type is RC\_PICKIT\_CONFIGURE.                                                                                                                                                                        |
+--------------------+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **product**        | **int32**                        | A number matching to a product type known by the Pickit system.                                                                                                                                                                  |
|                    |                                  | Used only when the command type is RC\_PICKIT\_CONFIGURE.                                                                                                                                                                        |
+--------------------+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Below are the values for the robot command constants expected by Pickit:

::

        #define RC_PICKIT_NO_COMMAND         -1
        #define RC_PICKIT_CHECK_MODE         0
        #define RC_PICKIT_FIND_CALIB_PLATE   10
        #define RC_PICKIT_LOOK_FOR_OBJECTS   20
        #define RC_PICKIT_NEXT_OBJECT        30
        #define RC_PICKIT_CONFIGURE          40
        #define RC_PICKIT_SAVE_SCENE         50

All command messages (not just periodic pose updates) should contain a valid ``actual_pose`` field.

.. _response-message:

Response message from Pickit to robot
-------------------------------------

Except for the ``RC_PICKIT_NO_COMMAND`` command, each robot command sent to Pickit will result in one response message from Pickit. These messages contain a Pickit status value as well as the actual object data for one object.

The robot receives this structure from the Pickit interface:

::

         struct pickit_to_robot_data {
              int32 object_pose[7];
              int32 object_age;
              int32 object_type;
              int32 object_dimensions[3];
              int32 objects_remaining;
              int32 status;
              meta_data meta;
         };

Metadata fields are documented in the `Message metadata <#metadata>`__ section of this article. The remaining fields are explained below.

+--------------------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field name               | Type / units                       | Comment                                                                                                                                                                                                                                     |
+==========================+====================================+=============================================================================================================================================================================================================================================+
| **object\_pose**         | **int32[7]**                       | An object pose expressed relative to the robot base frame consisting of position in cartesian space and orientation in axis angle, quaternion or Euler angles convention. This convention as well as the units depend on the robot brand.   |
|                          | [0-2] : position (m)               | When reading array elements, each value has to be divided by the  **MULT** factor.                                                                                                                                                          |
|                          | [3-6] : orientation (rad, o,/)     |                                                                                                                                                                                                                                             |
+--------------------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **object\_age**          | **int32**                          | The amount of time that has passed between the capturing of the camera data and the moment the object information is sent to the robot.                                                                                                     |
|                          | (seconds)                          | This value has to be divided by the  **MULT** factor.                                                                                                                                                                                       |
+--------------------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **object\_type**         | **int32**                          | The type of object detected at object\_pose                                                                                                                                                                                                 |
+--------------------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_TYPE\_SQUARE               | A square has been detected with center at object\_pose                                                                                                                                                                                      |
+--------------------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_TYPE\_RECTANGLE            | A rectangle has been detected with center at object\_pose                                                                                                                                                                                   |
+--------------------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_TYPE\_CIRCLE               | A circle has been detected with center at object\_pose                                                                                                                                                                                      |
+--------------------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_TYPE\_ELLIPSE              | An ellipse has been detected with center at object\_pose                                                                                                                                                                                    |
+--------------------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_TYPE\_CYLINDER             | A cylinder has been detected with center at object\_pose                                                                                                                                                                                    |
+--------------------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_TYPE\_SPHERE               | A sphere has been detected with center at object\_pose                                                                                                                                                                                      |
+--------------------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_TYPE\_POINT\_CLOUD         | A Pickit Teach model has been detected                                                                                                                                                                                                      |
+--------------------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_TYPE\_BLOB                 | An object without a specified shape has been detected                                                                                                                                                                                       |
+--------------------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **object\_dimensions**   | **int32[3]**                       | | **PICKIT_TYPE_SQUARE**                                                                                                                                                                                                                    |
|                          | [0]: length or diameter (m)        | | [0] and [1] contain the side length of the square                                                                                                                                                                                         |
|                          | [1]: width or diameter (m)         |                                                                                                                                                                                                                                             |
|                          | [2]: height (m)                    | | **PICKIT\_TYPE\_RECTANGLE**                                                                                                                                                                                                               |
|                          |                                    | | [0] and [1] respectively contain the length and width of the rectangle                                                                                                                                                                    |
|                          |                                    |                                                                                                                                                                                                                                             |
|                          |                                    | | **PICKIT\_TYPE\_CIRCLE**                                                                                                                                                                                                                  |
|                          |                                    | | [0] and [1] contain the diameter of the circle                                                                                                                                                                                            |
|                          |                                    |                                                                                                                                                                                                                                             |
|                          |                                    | | **PICKIT\_TYPE\_ELLIPSE**                                                                                                                                                                                                                 |
|                          |                                    | | [0] and [1] respectively contain the length and width of the ellipse                                                                                                                                                                      |
|                          |                                    |                                                                                                                                                                                                                                             |
|                          |                                    | | **PICKIT\_TYPE\_CYLINDER**                                                                                                                                                                                                                |
|                          |                                    | | [0] and [1] respectively contain cylinder length and diameter                                                                                                                                                                             |
|                          |                                    |                                                                                                                                                                                                                                             |
|                          |                                    | | **PICKIT\_TYPE\_SPHERE**                                                                                                                                                                                                                  |
|                          |                                    | | [0] and [1] contain the diameter of the sphere                                                                                                                                                                                            |
|                          |                                    |                                                                                                                                                                                                                                             |
|                          |                                    | | **PICKIT\_TYPE\_POINT\_CLOUD**                                                                                                                                                                                                            |
|                          |                                    | | [0], [1] and [2] respectively contain the length, width and height of the point cloud bounding box                                                                                                                                        |
|                          |                                    |                                                                                                                                                                                                                                             |
|                          |                                    | | **PICKIT\_TYPE\_BLOB**                                                                                                                                                                                                                    |
|                          |                                    | | [0], [1] and [2] respectively contain the length, width and height of the blob bounding box                                                                                                                                               |
|                          |                                    |                                                                                                                                                                                                                                             |
|                          |                                    | When reading array elements, each value has to be divided by the  **MULT** factor.                                                                                                                                                          |
+--------------------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **objects\_remaining**   | **int32**                          | Only one object per pickit\_to\_robot\_data message can be communicated. If this field is non-zero, it contains the number of remaining objects that can be sent in next messages to the robot.                                             |
+--------------------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **status**               | **int32**                          | Contains the Pickit status or a response to previously received robot commands.                                                                                                                                                             |
+--------------------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_UNKNOWN\_COMMAND           | Pickit received an unknown command.                                                                                                                                                                                                         |
+--------------------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_RUNNING\_MODE              | Pickit is in running mode.                                                                                                                                                                                                                  |
+--------------------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_IDLE\_MODE                 | Pickit is in idle mode.                                                                                                                                                                                                                     |
+--------------------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_CALIBRATION\_MODE          | Pickit is in calibration mode.                                                                                                                                                                                                              |
+--------------------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_FIND\_CALIB\_PLATE\_OK     | The calibration plate has been successfully detected.                                                                                                                                                                                       |
+--------------------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_FIND\_CALIB\_PLATE\_FAILED | The calibration plate has not been detected.                                                                                                                                                                                                |
+--------------------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_OBJECT\_FOUND              | A pickable object has been detected.                                                                                                                                                                                                        |
+--------------------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_NO\_OBJECTS                | No pickable objects were detected.                                                                                                                                                                                                          |
+--------------------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_NO\_IMAGE\_CAPTURED        | Pickit failed to capture a camera image, most possibly due to a hardware failure (e.g. disconnected camera).                                                                                                                                |
+--------------------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_EMPTY\_ROI                 | An empty Region of Interest (ROI) has been detected.                                                                                                                                                                                        |
+--------------------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_CONFIG\_OK                 | Loading the requested Pickit configuration suceeded.                                                                                                                                                                                        |
+--------------------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_CONFIG\_FAILED             | Loading the requested Pickit configuration failed.                                                                                                                                                                                          |
+--------------------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_SAVE\_SCENE\_OK            | Pickit snapshot saving succeeded.                                                                                                                                                                                                           |
+--------------------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_SAVE\_SCENE\_FAILED        | Pickit snapshot saving failed.                                                                                                                                                                                                              |
+--------------------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Below are the values of the Pickit status constants communicated by Pickit:

::

         #define PICKIT_UNKNOWN_COMMAND           -99
         #define PICKIT_RUNNING_MODE                0
         #define PICKIT_IDLE_MODE                   1
         #define PICKIT_CALIBRATION_MODE            2

         #define PICKIT_FIND_CALIB_PLATE_OK        10
         #define PICKIT_FIND_CALIB_PLATE_FAILED    11
         #define PICKIT_OBJECT_FOUND               20
         #define PICKIT_NO_OBJECTS                 21
         #define PICKIT_NO_IMAGE_CAPTURED          22
         #define PICKIT_EMPTY_ROI                  23

         #define PICKIT_CONFIG_OK                  40
         #define PICKIT_CONFIG_FAILED              41
         #define PICKIT_SAVE_SCENE_OK              50
         #define PICKIT_SAVE_SCENE_FAILED          51

Below are the values of the object type constants communicated by Pickit:

::

        #define PICKIT_TYPE_SQUARE               21
        #define PICKIT_TYPE_RECTANGLE            22
        #define PICKIT_TYPE_CIRCLE               23
        #define PICKIT_TYPE_ELLIPSE              24
        #define PICKIT_TYPE_CYLINDER             32
        #define PICKIT_TYPE_SPHERE               33
        #define PICKIT_TYPE_POINT_CLOUD          35 // See remark below for Teach on 1.9+ versions.
        #define PICKIT_TYPE_BLOB                 50

.. warning::
    From version 1.9+, ``PICKIT_TYPE_POINT_CLOUD`` is no longer 35 with the Pickit Teach detection engine, but representing the ID Teach model the object was detected from.

.. _message-metadata:

Message metadata
----------------

To guarantee correct interpretation of the data on both the robot and the Pickit side, the following metadata is always sent along with the structures:

::

        struct meta_data {
            int32 robot_type;
            int32 interface_version;
        };

Each field is explained below. All **int32** are expressed in Network Byte Format.

+--------------------------+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field name               | Type / units   | Comment                                                                                                                                                |
+==========================+================+========================================================================================================================================================+
| **robot\_type**          | **int32**      | The type of robot Pickit is connected to:                                                                                                              |
|                          |                |                                                                                                                                                        |
|                          |                |   #. UNIVERSAL ROBOT → Angle-axis                                                                                                                      |
|                          |                |   #. ABB, **GENERIC** → Quaternions (w,x,y,z)                                                                                                          |
|                          |                |   #. STAUBLI → Euler Angles (x-y’-z”)                                                                                                                  |
|                          |                |   #. FANUC, YASKAWA → Fixed Angles (x-y-z)                                                                                                             |
|                          |                |   #. KUKA → Euler Angles (z-y’-x”)                                                                                                                     |
|                          |                |   #. COMAU → Euler Angles (z-y’-z”)                                                                                                                    |
+--------------------------+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **interface\_version**   | **int32**      | | The version of the robot-Pickit communication.                                                                                                       |
|                          |                | | To get this number, all dots are removed from the actual version number.                                                                             |
|                          |                | | The current version is ``1.1``, so the communicated value is ``11``.                                                                                 |
+--------------------------+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+

To add support for a robot type not adhering to one of the above conventions, it's recommended to use the **GENERIC** (quaternions) convention above. The robot-side interface would then take the responsibility of converting back and forth between the representation used by Pickit and the robot.
