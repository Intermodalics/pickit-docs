.. _socket-communication:

Pickit socket interface
=======================

Pickit offers a low-level interface based on a TCP/IP socket communication which can be used to connect
your robot (or PLC) with Pickit. Using the socket interface, the robot can for instance trigger detections,
retrieve object poses and change the Pickit configuration.

The following article describes the technical details of the socket interface. This is relevant if you
are planning to interface a new robot brand with Pickit.

.. note::
   Before starting, make sure that the robot integration
   does not already exist and confirm with support@pickit3d.com that the integration is not under development.

Overview
--------

The robot and Pickit exchange information in a request-response pattern, where the robot acts as the client
and Pickit as the server. The robot sends a request, such as e.g. an object detection, to Pickit, which replies
with a corresponding response. All requests are implemented in a purely synchronous fashion, and it is up to
the client to ensure that no new requests are sent before having received a response for the previous request.

Next to this request-response exchange, Pickit also expects to receive periodic **robot flange** pose
updates from the client. Note that the robot pose update is the only request for which the Pickit
system does not reply with a matching response message.

.. figure:: /assets/images/robot-integrations/socket/socket-2.png
   :align: center
   :width: 500


Connection details
------------------

+----------------+--------------------------------+
| **Type**       | TCP/IP socket                  |
+----------------+--------------------------------+
| **Port**       | 5001 (TCP)                     |
+----------------+--------------------------------+
| **Byte order** | Network order (big endian)     |
+----------------+--------------------------------+

Once a Pickit system is started, it listens to TCP port ``5001`` and waits until the robot initiates
a connection. This is done on the robot side by opening a TCP socket targeting the IP address of the Pickit system
and the given port.

The IP address of the Pickit system can be found and changed in the Pickit :ref:`network settings <settings-network-robot>`.
The default IP for the Ethernet port labeled `ROBOT` is ``169.254.5.180``.

Protocol
--------

Request and response messages that are exchanged between a robot and Pickit have a fixed size. A fixed-size message
protocol has the advantage that it is easy to implement on the robot side, even with limited programming features.

.. note::
   Request and response messages have a fixed size and do not have a begin and/or end character. While the TCP/IP protocol
   prevents data loss, the robot client implementation is responsible for keeping track of the boundary between messages by
   counting the number of sent/received bytes and comparing with the expected message size.

.. _MULT:

Request and response messages consist of a number of fields, each represented by an ``int32`` (4 bytes). Floating-point data, such
as distances and angles, are multiplied by a constant factor ``MULT = 10000`` and truncated, before being sent as an ``int32``. The receiving side
then decodes this field by dividing the received value by ``MULT`` again. Negative numbers are encoded using
`two's complement <https://en.wikipedia.org/wiki/Two%27s_complement>`_.

Request message
~~~~~~~~~~~~~~~

The request message that is sent from the robot to Pickit is ``48 bytes`` long and consists of the following fields:

.. table:: Request message structure

   +-------------+----------+---------+-------------------------------------------------------------------------------+
   | Field       | Type     | Length  | Description                                                                   |
   +=============+==========+=========+===============================================================================+
   | position    | int32[3] | 12 bytes| Robot flange position (XYZ, in meters) expressed in the right-handed robot    |
   |             |          |         | base frame. Each field has to be multiplied by the MULT_ factor.              |
   +-------------+----------+---------+-------------------------------------------------------------------------------+
   | orientation | int32[4] | 16 bytes| Robot flange orientation expressed in the right-handed robot base frame.      |
   |             |          |         | The orientation encoding and units depend on the chosen                       |
   |             |          |         | :ref:`orientation convention <meta-msg>`. Each field has to be                |
   |             |          |         | multiplied by the MULT_ factor.                                               |
   +-------------+----------+---------+-------------------------------------------------------------------------------+
   | command     | int32    | 4 bytes | One of the possible :ref:`request commands <request-cmds>`.                   |
   +-------------+----------+---------+-------------------------------------------------------------------------------+
   | payload     | int32[2] | 8 bytes | Optional payload fields.                                                      |
   +-------------+----------+---------+-------------------------------------------------------------------------------+
   | meta        | int32[2] | 8 bytes | Orientation convention and protocol version. See the                          |
   |             |          |         | :ref:`detailed meta field explanation <meta-msg>`.                            |
   +-------------+----------+---------+-------------------------------------------------------------------------------+

Except for the optional ``payload`` fields, all fields are mandatory, and have to be set to sane values for every request.
The payload fields are only required for certain commands, and are otherwise not used by Pickit.

The ``command`` field indicates which operation Pickit should execute. Possible commands and their
corresponding response messages are explained in more detail :ref:`below <request-response-pairs>`.

Response message
~~~~~~~~~~~~~~~~

Except for the pose-update request, all requests are answered with a ``64 byte`` long response message
with the following structure:

.. table:: Response message structure

   +-------------+----------+---------+-------------------------------------------------------------------------------+
   | Field       | Type     | Length  | Description                                                                   |
   +=============+==========+=========+===============================================================================+
   | position    | int32[3] | 12 bytes| Object position or pick point offset translation (XYZ, in meters), depending  |
   |             |          |         | on the response status. See also the                                          |
   |             |          |         | :ref:`detailed command explanation<request-response-pairs>`. Each value       |
   |             |          |         | has to be divided by MULT_.                                                   |
   +-------------+----------+---------+-------------------------------------------------------------------------------+
   | orientation | int32[4] | 16 bytes| Object orientation or pick point offset rotation, depending on the            |
   |             |          |         | response status. See also the                                                 |
   |             |          |         | :ref:`detailed command explanation<request-response-pairs>`. Encoding and     |
   |             |          |         | units depend on the chosen :ref:`orientation convention<meta-msg>` and have   |
   |             |          |         | to be divided by MULT_.                                                       |
   +-------------+----------+---------+-------------------------------------------------------------------------------+
   | payload     | int32[6] | 24 bytes| Optional payload fields.                                                      |
   +-------------+----------+---------+-------------------------------------------------------------------------------+
   | status      | int32    | 4 bytes | One of the defined :ref:`status values <response-status>`.                    |
   +-------------+----------+---------+-------------------------------------------------------------------------------+
   | meta        | int32[2] | 8 bytes | Orientation convention and protocol version. See the                          |
   |             |          |         | :ref:`detailed meta field explanation <meta-msg>`.                            |
   +-------------+----------+---------+-------------------------------------------------------------------------------+

Not every command response conveys pose information or additional payload. The ``status`` field determines if (and how)
``position``, ``orientation`` and ``payload`` fields have to be interpreted. In the following sections, the individual
commands and their corresponding responses are explained in more detail.

.. _request-response-pairs:

Available commands
~~~~~~~~~~~~~~~~~~

.. _RC_PICKIT_NO_COMMAND:

RC_PICKIT_NO_COMMAND (Robot pose update)
________________________________________

Send the current robot flange pose to Pickit. This information is used by Pickit to determine if the robot is
still connected, as well as to update the 3D views in the Pickit web interface.

Robot pose updates should be sent periodically to Pickit, typically in the range of 10 messages per second. This
command does not trigger a response, so it can be sent also while waiting for a response for a different command.

.. _RC_PICKIT_CHECK_MODE:

RC_PICKIT_CHECK_MODE
____________________

Check the current mode of Pickit. Pickit can be in the following modes: ``ROBOT``, ``CALIBRATION`` or ``IDLE``.

**Response**

+--------+--------------------------------------------------+---------------------------------------------------------+
| Field  | Value                                            | Description                                             |
+========+==================================================+=========================================================+
| status | :ref:`PICKIT_ROBOT_MODE <response-status>`       | Pickit is in robot mode and able to send object poses to|
|        |                                                  | the robot. After booting, the Pickit system is in robot |
|        |                                                  | mode, which can be disabled and re-enabled via the      |
|        |                                                  | :ref:`web interface <web-interface-top-bar>`.           |
|        +--------------------------------------------------+---------------------------------------------------------+
|        | :ref:`PICKIT_CALIBRATION_MODE <response-status>` | Pickit is in calibration mode and able to localize the  |
|        |                                                  | calibration plate. The system is in calibration mode    |
|        |                                                  | while the calibration wizard in the web interface is    |
|        |                                                  | open.                                                   |
|        +--------------------------------------------------+---------------------------------------------------------+
|        | :ref:`PICKIT_IDLE_MODE <response-status>`        | When not in robot or calibration mode, Pickit is in idle|
|        |                                                  | mode, and can be configured via the web interface.      |
+--------+--------------------------------------------------+---------------------------------------------------------+

.. _RC_PICKIT_FIND_CALIB_PLATE:

RC_PICKIT_FIND_CALIB_PLATE
__________________________

Trigger Pickit to localize the calibration plate. If sufficient calibration poses have been collected,
Pickit will additionally trigger the computation of the :ref:`robot-camera calibration<robot-camera-calibration>`.
Note that Pickit has to be in calibration mode when this command is sent.

**Response**

+--------+---------------------------------------------------------+--------------------------------------------------+
| Field  | Value                                                   | Description                                      |
+========+=========================================================+==================================================+
| status | :ref:`PICKIT_FIND_CALIB_PLATE_OK <response-status>`     | Successfully localized calibration plate.        |
|        +---------------------------------------------------------+--------------------------------------------------+
|        | :ref:`PICKIT_FIND_CALIB_PLATE_FAILED <response-status>` | Failed to localize calibration plate.            |
+--------+---------------------------------------------------------+--------------------------------------------------+

.. _RC_PICKIT_LOOK_FOR_OBJECTS:

RC_PICKIT_LOOK_FOR_OBJECTS
__________________________

Request Pickit to find objects in the current scene. This command performs an image capture and image processing in a single request.

.. _RC_PICKIT_LOOK_FOR_OBJECTS_response:

**Response**

Due to the fixed-size structure of the response message, only one object can be transmitted
at a time. If more than one object has been detected, the information of the first object is
communicated in the response message of a detection request, and the remaining objects can be obtained using the
:ref:`RC_PICKIT_NEXT_OBJECT` request, one at a time.

+-------------+-------------------------------------------------------------------------------------------------------+
| Field       | Value / Description                                                                                   |
+=============+=======================================================================================================+
| position    | Object position (XYZ, in meters) expressed in the robot base frame. Each field has to be divided by   |
|             | MULT_.                                                                                                |
+-------------+-------------------------------------------------------------------------------------------------------+
| orientation | Object orientation expressed in the robot base frame. The orientation encoding and units depend on    |
|             | the chosen :ref:`orientation convention <meta-msg>`. Each field has to be divided by MULT_.           |
+-------------+-------------------------------------------------------------------------------------------------------+
| payload[0]  | The duration (in seconds) elapsed between the capturing of the camera                                 |
|             | image and the moment the object information is sent to the robot. This value has to be                |
|             | divided by MULT_.                                                                                     |
+-------------+-------------------------------------------------------------------------------------------------------+
| payload[1]  | - For a Teach detection, this field contains the model ID of the current object.                      |
|             | - For a Flex/Pattern detection, this field contains the :ref:`object type <response-object-type>`.    |
+-------------+-------------------------------------------------------------------------------------------------------+
| payload[2]  | Object length (:ref:`SQUARE, RECTANGLE, ELLIPSE, CYLINDER, POINTCLOUD, BLOB <response-object-type>`)  |
|             | or diameter (:ref:`CIRCLE, SPHERE <response-object-type>`) in meters. Needs to be divided by MULT_.   |
+-------------+-------------------------------------------------------------------------------------------------------+
| payload[3]  | Object width (:ref:`RECTANGLE, ELLIPSE, POINTCLOUD, BLOB <response-object-type>`)                     |
|             | or diameter (:ref:`CYLINDER <response-object-type>`) in meters. Needs to be divided by MULT_.         |
+-------------+-------------------------------------------------------------------------------------------------------+
| payload[4]  | Object height (:ref:`POINTCLOUD, BLOB <response-object-type>`) in meters.                             |
|             | Needs to be divided by MULT_.                                                                         |
+-------------+-------------------------------------------------------------------------------------------------------+
| payload[5]  | If this field is non-zero, it contains the number of remaining                                        |
|             | objects that can be retrieved via consecutive RC_PICKIT_NEXT_OBJECT_ requests.                        |
+-------------+---------------------------------------------------+---------------------------------------------------+
| status      | :ref:`PICKIT_OBJECT_FOUND <response-status>`      | At least one object has been detected.            |
|             +---------------------------------------------------+---------------------------------------------------+
|             | :ref:`PICKIT_NO_OBJECTS <response-status>`        | No objects have been detected, but the ROI is not |
|             |                                                   | empty.                                            |
|             +---------------------------------------------------+---------------------------------------------------+
|             | :ref:`PICKIT_NO_IMAGE_CAPTURED <response-status>` | No camera image has been captured.                |
|             +---------------------------------------------------+---------------------------------------------------+
|             | :ref:`PICKIT_EMPTY_ROI <response-status>`         | An :ref:`empty ROI <detecting-an-empty-roi>` has  |
|             |                                                   | been detected.                                    |
+-------------+---------------------------------------------------+---------------------------------------------------+

.. _pose-flipping:

.. attention::
   Object poses communicated by Pickit, via the ``position`` and ``orientation`` fields,
   have their Z-axis pointing upwards. Depending on the orientation of your robot's flange frame, it might be necessary
   to flip the received poses by 180 degrees around the X-axis, such that the tool correctly aligns with the object at the moment of picking.

.. _RC_PICKIT_LOOK_FOR_OBJECTS_WITH_RETRIES:

RC_PICKIT_LOOK_FOR_OBJECTS_WITH_RETRIES
_______________________________________

Request Pickit to find objects in the current scene *with retries*.
This command is similar to RC_PICKIT_LOOK_FOR_OBJECTS_, but when no objects are found (but the :ref:`Region of Interest (ROI) <region-of-interest>` is not empty), Pickit will retry up to *n* times to find objects before giving up.

**Request**

+-------------+-----------------------------------------------------------+
| Field       | Value /  Description                                      |
+=============+===========================================================+
| payload[0]  | Maximum number of detection retries.                      |
+-------------+-----------------------------------------------------------+

**Response**

See response message of RC_PICKIT_LOOK_FOR_OBJECTS_.


.. _RC_PICKIT_NEXT_OBJECT:

RC_PICKIT_NEXT_OBJECT
_____________________

Request to return the next detected (valid *and* pickable) object in the :ref:`detection grid<detection-grid>`. Use this command when a single object detection run yields
multiple detected objects. Note that the RC_PICKIT_LOOK_FOR_OBJECTS_ (or RC_PICKIT_PROCESS_IMAGE_) command already returns
the first object, if at least one was detected.

**Response**

See response message of RC_PICKIT_LOOK_FOR_OBJECTS_.

If RC_PICKIT_NEXT_OBJECT_ is called after the last detected object has been sent to the robot, Pickit replies with a
:ref:`PICKIT_NO_OBJECTS <response-status>` status.


.. _RC_PICKIT_CAPTURE_IMAGE:

RC_PICKIT_CAPTURE_IMAGE
_______________________

Trigger Pickit to capture a camera image to be used by a following RC_PICKIT_PROCESS_IMAGE_ request. This command allows
to wait until image capture is done and afterwards parallelize image processing with robot motion. This is especially relevant
for robot-mounted cameras where the robot has to stand still during image capture.

However, in most cases, it is sufficient and more convenient to call RC_PICKIT_LOOK_FOR_OBJECTS_, which performs image capture and
processing in a single request.

**Response**

+--------+---------------------------------------------------------+--------------------------------------------------+
| Field  | Value                                                   | Description                                      |
+========+=========================================================+==================================================+
| status | :ref:`PICKIT_IMAGE_CAPTURED <response-status>`          | Successfully captured camera image.              |
|        +---------------------------------------------------------+--------------------------------------------------+
|        | :ref:`PICKIT_NO_IMAGE_CAPTURED <response-status>`       | Failed to capture camera image.                  |
+--------+---------------------------------------------------------+--------------------------------------------------+

.. _RC_PICKIT_PROCESS_IMAGE:

RC_PICKIT_PROCESS_IMAGE
_______________________

Trigger an object detection on the camera image that was previously captured via RC_PICKIT_CAPTURE_IMAGE_ (or RC_PICKIT_LOOK_FOR_OBJECTS_).

**Response**

See response message of RC_PICKIT_LOOK_FOR_OBJECTS_.

.. _RC_PICKIT_CONFIGURE:

RC_PICKIT_CONFIGURE
___________________

Request Pickit to load a specific setup and product :ref:`configuration<Configuration>`. Each setup and product configuration
have a unique ID assigned, which is shown in the web interface, next to the configuration name.

**Request**

+-------------+-----------------------------------------------------------+
| Field       | Value /  Description                                      |
+=============+===========================================================+
| payload[0]  | ID of the setup configuration.                            |
+-------------+-----------------------------------------------------------+
| payload[1]  | ID of the product configuration.                          |
+-------------+-----------------------------------------------------------+

**Response**

+--------+---------------------------------------------------+--------------------------------------------------+
| Field  | Value                                             | Description                                      |
+========+===================================================+==================================================+
| status | :ref:`PICKIT_CONFIG_OK <response-status>`         | Successfully loaded the specified configurations.|
|        +---------------------------------------------------+--------------------------------------------------+
|        | :ref:`PICKIT_CONFIG_FAILED <response-status>`     | Failed to load the specified configurations.     |
+--------+---------------------------------------------------+--------------------------------------------------+

.. _RC_PICKIT_SET_CYLINDER_DIM:

RC_PICKIT_SET_CYLINDER_DIM
__________________________

Request Pickit to set the cylinder dimensions when using the :ref:`teach-cylinder`.
For the command to succeed, there can be only one Teach model, it must be of type cylinder, and it must be enabled.

**Request**

+-------------+-----------------------------------------------------------+
| Field       | Value /  Description                                      |
+=============+===========================================================+
| payload[0]  | Length of the cylinder.                                   |
+-------------+-----------------------------------------------------------+
| payload[1]  | Diameter of the cylinder.                                 |
+-------------+-----------------------------------------------------------+

**Response**

+--------+---------------------------------------------------+--------------------------------------------------+
| Field  | Value                                             | Description                                      |
+========+===================================================+==================================================+
| status | :ref:`PICKIT_CONFIG_OK <response-status>`         | Successfully set the cylinder dimensions.        |
|        +---------------------------------------------------+--------------------------------------------------+
|        | :ref:`PICKIT_CONFIG_FAILED <response-status>`     | Failed to set the cylinder dimensions.           |
+--------+---------------------------------------------------+--------------------------------------------------+

.. _RC_SAVE_ACTIVE_SETUP:

RC_SAVE_ACTIVE_SETUP
____________________

Request Pickit to save the currently loaded setup.

**Response**

+--------+---------------------------------------------------+--------------------------------------------------+
| Field  | Value                                             | Description                                      |
+========+===================================================+==================================================+
| status | :ref:`PICKIT_CONFIG_OK <response-status>`         | Successfully saved the active setup.             |
|        +---------------------------------------------------+--------------------------------------------------+
|        | :ref:`PICKIT_CONFIG_FAILED <response-status>`     | Failed to save the active setup.                 |
+--------+---------------------------------------------------+--------------------------------------------------+

.. _RC_SAVE_ACTIVE_PRODUCT:

RC_SAVE_ACTIVE_PRODUCT
____________________

Request Pickit to save the currently loaded product.

**Response**

+--------+---------------------------------------------------+--------------------------------------------------+
| Field  | Value                                             | Description                                      |
+========+===================================================+==================================================+
| status | :ref:`PICKIT_CONFIG_OK <response-status>`         | Successfully saved the active product.           |
|        +---------------------------------------------------+--------------------------------------------------+
|        | :ref:`PICKIT_CONFIG_FAILED <response-status>`     | Failed to save the active product.               |
+--------+---------------------------------------------------+--------------------------------------------------+

.. _RC_PICKIT_SAVE_SNAPSHOT:

RC_PICKIT_SAVE_SNAPSHOT
_______________________

Request Pickit to save a :ref:`snapshot<Snapshots>` with the last captured scene and the current configuration.
Snapshots will be saved in the ``robot`` subfolder, which can be accessed from the web interface.
If the user wishes to distinguish snapshots of different situations (ex. mispicks and no detected objects), it is possible to specify a subfolder inside the ``robot`` folder.

**Request**

+-------------+--------------------------------------------------------------------------+
| Field       | Value /  Description                                                     |
+=============+==========================================================================+
| payload[0]  | Subfolder (inside ``robot``) in which the snapshot should be saved.      |
|             | The subfolder is identified and named by a number smaller than 256.      |
|             | If zero (0), the snapshot is saved directly inside the ``robot`` folder. |
+-------------+--------------------------------------------------------------------------+

**Response**

+--------+------------------------------------------------------+--------------------------------------------------+
| Field  | Value                                                | Description                                      |
+========+======================================================+==================================================+
| status | :ref:`PICKIT_SAVE_SNAPSHOT_OK <response-status>`     | Successfully saved a snapshot.                   |
|        +------------------------------------------------------+--------------------------------------------------+
|        | :ref:`PICKIT_SAVE_SNAPSHOT_FAILED <response-status>` | Failed to save a snapshot.                       |
+--------+------------------------------------------------------+--------------------------------------------------+

.. _RC_PICKIT_BUILD_BACKGROUND:

RC_PICKIT_BUILD_BACKGROUND
__________________________

Request Pickit to capture the current scene as background for :ref:`background removal <Point-based-roi-filter>`.

**Response**

+--------+-------------------------------------------------------+-------------------------------------------------+
| Field  | Value                                                 | Description                                     |
+========+=======================================================+=================================================+
| status | :ref:`PICKIT_BUILD_BKG_CLOUD_OK <response-status>`    | Successfully built background scene.            |
|        +-------------------------------------------------------+-------------------------------------------------+
|        | :ref:`PICKIT_BUILD_BKG_CLOUD_FAILED <response-status>`| Failed to built background scene.               |
+--------+-------------------------------------------------------+-------------------------------------------------+

.. _RC_PICKIT_GET_PICK_POINT_DATA:

RC_PICKIT_GET_PICK_POINT_DATA
_____________________________

With multiple or flexible :ref:`pick points <pick-points-teach>`, the robot needs to know how an object is being picked in order to drop it off
at a fixed position. This information can be retrieved via RC_PICKIT_GET_PICK_POINT_DATA_, which requests the
pick point ID and pick point offset of the last requested object.

In the simplest case, the pick point ID is sufficient to know how an object was picked and how it should be dropped off.
For applications with multiple pick points and/or pick points with flexible orientations, it is advised to make use of
the pick point offset as well. Using the pick point offset, you don't need to define a drop off point for every pick point.
Instead, you only have to define a drop off point for every pick point reference, and apply the inverse pick point offset to this point.

Note that, due to the :ref:`flipping of object poses<pose-flipping>`, it is necessary to correct the communicated pick point offset on the robot side.
This corrected offset is computed by ``pick_offset_to_apply = Rx × inv(offset_from_pickit) × Rx``, where ``Rx`` denotes a rotation of 180 degrees
around the X-axis. The pick point offset ``fpp_T_ppr`` is the transform between the final pick point and the pick point's
reference.

.. _RC_PICKIT_GET_PICK_POINT_DATA_response:

**Response**

+-------------+-------------------------------------------------------------------------------------------------------+
| Field       | Value / Description                                                                                   |
+=============+=======================================================================================================+
| position    | Pick point offset position (XYZ, in meters) expressed in the final pick point frame.                  |
|             | Values have to be divided by MULT_.                                                                   |
+-------------+-------------------------------------------------------------------------------------------------------+
| orientation | Pick point offset orientation expressed in the final pick point frame. The encoding and units depend  |
|             | on the chosen :ref:`orientation convention <meta-msg>`. Values have to be divided by MULT_.           |
+-------------+-------------------------------------------------------------------------------------------------------+
| payload[0]  | ID of the selected pick point's reference pick point.                                                 |
+-------------+-------------------------------------------------------------------------------------------------------+
| payload[1]  | ID of the pick point that was selected for the given object.                                          |
+-------------+------------------------------------------------------------+------------------------------------------+
| status      | :ref:`PICKIT_GET_PICK_POINT_DATA_OK <response-status>`     | Successfully retrieved pick point data.  |
|             +------------------------------------------------------------+------------------------------------------+
|             | :ref:`PICKIT_GET_PICK_POINT_DATA_FAILED <response-status>` | Failed to retrieve pick point data.      |
+-------------+------------------------------------------------------------+------------------------------------------+

Constants
---------

.. _request-cmds:
.. code-block:: python
   :caption: Request command constants

   RC_PICKIT_NO_COMMAND                    = -1
   RC_PICKIT_CHECK_MODE                    = 0
   RC_PICKIT_FIND_CALIB_PLATE              = 10
   RC_PICKIT_LOOK_FOR_OBJECTS              = 20
   RC_PICKIT_LOOK_FOR_OBJECTS_WITH_RETRIES = 21
   RC_PICKIT_CAPTURE_IMAGE                 = 22
   RC_PICKIT_PROCESS_IMAGE                 = 23
   RC_PICKIT_NEXT_OBJECT                   = 30
   RC_PICKIT_CONFIGURE                     = 40
   RC_PICKIT_SET_CYLINDER_DIM              = 41
   RC_SAVE_ACTIVE_SETUP                    = 42
   RC_SAVE_ACTIVE_PRODUCT                  = 43
   RC_PICKIT_SAVE_SCENE                    = 50
   RC_PICKIT_BUILD_BACKGROUND              = 60
   RC_PICKIT_GET_PICK_POINT_DATA           = 70

.. _response-status:
.. code-block:: python
   :caption: Response status constants

   PICKIT_UNKNOWN_COMMAND                  = -99
   PICKIT_ROBOT_MODE                       =   0
   PICKIT_IDLE_MODE                        =   1
   PICKIT_CALIBRATION_MODE                 =   2
   PICKIT_FIND_CALIB_PLATE_OK              =  10
   PICKIT_FIND_CALIB_PLATE_FAILED          =  11
   PICKIT_OBJECT_FOUND                     =  20
   PICKIT_NO_OBJECTS                       =  21
   PICKIT_NO_IMAGE_CAPTURED                =  22
   PICKIT_EMPTY_ROI                        =  23
   PICKIT_IMAGE_CAPTURED                   =  26
   PICKIT_CONFIG_OK                        =  40
   PICKIT_CONFIG_FAILED                    =  41
   PICKIT_SAVE_SNAPSHOT_OK                 =  50
   PICKIT_SAVE_SNAPSHOT_FAILED             =  51
   PICKIT_BUILD_BKG_CLOUD_OK               =  60
   PICKIT_BUILD_BKG_CLOUD_FAILED           =  61
   PICKIT_GET_PICK_POINT_DATA_OK           =  70
   PICKIT_GET_PICK_POINT_DATA_FAILED       =  71

.. _response-object-type:
.. code-block:: python
   :caption: Object type constants

   PICKIT_TYPE_SQUARE                =  21
   PICKIT_TYPE_RECTANGLE             =  22
   PICKIT_TYPE_CIRCLE                =  23
   PICKIT_TYPE_ELLIPSE               =  24
   PICKIT_TYPE_CYLINDER              =  32
   PICKIT_TYPE_SPHERE                =  33
   PICKIT_YTPE_POINTCLOUD            =  35
   PICKIT_TYPE_BLOB                  =  50

.. _meta-msg:

Message metadata
----------------

To guarantee correct interpretation of the data on both the robot and the Pickit side,
the following metadata is always sent along with both request and response messages:

.. table:: Metadata message

   +------------------------+------------------------------------------------------------------------------------------+
   | Field                  | Value / Description                                                                      |
   +========================+==========================================================================================+
   | orientation convention | Convention that is being used to encode object or robot flange orientations.             |
   |                        | The following conventions are supported:                                                 |
   |                        |                                                                                          |
   |                        | 1. Angle-axis (3D vector consisting of the unit axis multiplied by the angle in radians) |
   |                        |    → UNIVERSAL ROBOTS                                                                    |
   |                        | 2. Quaternions (w,x,y,z) → **GENERIC**, ABB                                              |
   |                        | 3. Euler Angles (x-y’-z”, in degrees) → STÄUBLI                                          |
   |                        | 4. Fixed Angles (x-y-z, in degrees) → FANUC, NACHI, OMRON TM, YASKAWA                    |
   |                        | 5. Euler Angles (z-y’-x”, in degrees) → HANWHA, KUKA                                     |
   |                        | 6. Euler Angles (z-y’-z”, in degrees) → COMAU, DOOSAN, OMRON                             |
   +------------------------+------------------------------------------------------------------------------------------+
   | protocol version       | The version of the robot-Pickit communication. The current version number is ``11`` and  |
   |                        | is not expected to change in the near future.                                            |
   +------------------------+------------------------------------------------------------------------------------------+

If your robot does not adhere to any of the above orientation conventions, it is recommended to use the **GENERIC** (quaternions)
convention. The robot-side interface would then take the responsibility of converting back and forth between quaternions and
the representation used by the robot.

Communication flow
------------------

An example communication flow is as follows:

#. The robot checks the Pickit mode using RC_PICKIT_CHECK_MODE_.
#. After confirming that Pickit is in robot mode, the robot initiates a background thread that periodically sends
   robot pose updates (RC_PICKIT_NO_COMMAND_) to Pickit.
#. To configure Pickit for the given product and workspace, the robot loads the desired product and setup configurations
   via RC_PICKIT_CONFIGURE_.
#. The robot requests an object detection with RC_PICKIT_LOOK_FOR_OBJECTS_. For this example, Pickit
   responds that two objects were found, of which the first object is part of the response message.
#. The robot requests specific pick point data for the first object with RC_PICKIT_GET_PICK_POINT_DATA_.
#. After the first object has been picked, the robot requests the second and final object with RC_PICKIT_NEXT_OBJECT_. This
   is again followed by RC_PICKIT_GET_PICK_POINT_DATA_, to retrieve the pick point data of the last requested object.

.. figure:: /assets/images/robot-integrations/socket/socket-1.png
   :align: center
   :width: 500
   :alt: Socket communication flow

   Example communication flow between robot and Pickit.
