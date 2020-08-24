.. _siemens_pickit_interface:

Siemens Pickit interface
========================

This article gives an overview of the prgram blocks provided by Pickit. Both the communication function block (required) and robot commands function (optional) are covered in this article.

.. _function_block_detailed:

The communication function block
--------------------------------

This section describes the Pickit communication Function Block **(FB)** in detail. Using the block in OB1 gives a clear overview of the imputs and outputs, as shown below.

.. image:: ../../assets/images/robot-integrations/siemens/network_pi_comm.PNG

The block inputs, ouputs, their corresponding datatype and default values are summarized in the two tables below. The default values can be overwritten in the data block. The *robot_to_pickit_data*, *socket_params* and *pickit_to_robot_data* are structures containing different data fields and are elaborated in detail in the subsections below.

.. table:: Inputs

   +----------------------------+-----------+----------------+---------------------------------------------------------------------------------------------------+
   | Input                      | Datatype  | Default value  | Comment                                                                                           |
   +============================+===========+================+===================================================================================================+
   | *robot_to_pickit_data*     | Struct    |                | Structure containing the data being sent from the robot to the Pickit system.                     |
   +----------------------------+-----------+----------------+---------------------------------------------------------------------------------------------------+
   | *socket_params*            | Struct    |                | Structure containing the TCP/IP V4 connection parameters.                                         |
   +----------------------------+-----------+----------------+---------------------------------------------------------------------------------------------------+
   | enable                     | Bool      | ``true``       | Bit that enables the block for commication, this bit has to remain high during runtime.           |
   +----------------------------+-----------+----------------+---------------------------------------------------------------------------------------------------+
   | request                    | Bool      | ``false``      | Bit that initiates a communcation request on **a rising edge signal**.                            |
   +----------------------------+-----------+----------------+---------------------------------------------------------------------------------------------------+
   | clear                      | Bool      | ``false``      | Bit that clears the *pickit_to_robot_data* outputs on **a rising edge signal**.                   |
   +----------------------------+-----------+----------------+---------------------------------------------------------------------------------------------------+
   | reset                      | Bool      | ``false``      | Bit that resets the block on **a rising edge signal**. Established connections will be terminated.|
   +----------------------------+-----------+----------------+---------------------------------------------------------------------------------------------------+

Similarly, an overview of the block outputs and their datatypes.

.. table:: Outputs

   +----------------------------+-----------+-------------------------------------------------------------------------------------------------------------------+
   | Output                     | Datatype  | Comment                                                                                                           |
   +============================+===========+===================================================================================================================+
   | *pickit_to_robot_data*     | Struct    | Structure containing the data being received from Pickit.                                                         |
   +----------------------------+-----------+-------------------------------------------------------------------------------------------------------------------+
   | pickit_connected           | Bool      | Bit that states if a connection with the Pickit is successfully established.                                      |
   +----------------------------+-----------+-------------------------------------------------------------------------------------------------------------------+
   | pickit_success             | Bool      | Bit that states if the previous request had a succesful response.                                                 |
   +----------------------------+-----------+-------------------------------------------------------------------------------------------------------------------+
   | pickit_mode                | SInt      | Integer that holds the Pickit mode.                                                                               |
   +----------------------------+-----------+-------------------------------------------------------------------------------------------------------------------+
   | done                       | Bool      | Communication job finished successfully. The bit remains high until a new job is triggered.                       |
   +----------------------------+-----------+-------------------------------------------------------------------------------------------------------------------+
   | busy                       | Bool      | Active communication job. This bit will either move to done or busy.                                              |
   +----------------------------+-----------+-------------------------------------------------------------------------------------------------------------------+
   | error                      | Bool      | This bit is set to high when a fatal block error occured.                                                         |
   +----------------------------+-----------+-------------------------------------------------------------------------------------------------------------------+
   | status                     | Byte      | This byte gives concrete information on block status and fatal block errors/faults.                               |
   +----------------------------+-----------+-------------------------------------------------------------------------------------------------------------------+

The different status output values and their meaning are summarized below.
All of the status variables marked as *error* are considered fatal, i.e. leading to block fault and subsequently terminating the connection.
These error types require a block reset by the reset input or a memory reset ``MRES`` of the CPU (cold start).

.. table:: Function block status output overview

   +------------+-----------+-----------------------------------------------------------------------------------------------------------------+
   | status     | error     | Description                                                                                                     |
   +============+===========+=================================================================================================================+
   | ``16#00``  | 0         | No active connection.                                                                                           |
   +------------+-----------+-----------------------------------------------------------------------------------------------------------------+
   | ``16#10``  | 0         | The connection is successfully established.                                                                     |
   +------------+-----------+-----------------------------------------------------------------------------------------------------------------+
   | ``16#11``  | 1         | The established connection is lost.                                                                             |
   +------------+-----------+-----------------------------------------------------------------------------------------------------------------+
   | ``16#12``  | 1         | The received data is invalid.                                                                                   |
   +------------+-----------+-----------------------------------------------------------------------------------------------------------------+
   | ``16#1A``  | 1         | The command input number is undefined.                                                                          |
   +------------+-----------+-----------------------------------------------------------------------------------------------------------------+
   | ``16#1B``  | 1         | Pickit is not in robot mode.                                                                                    |
   +------------+-----------+-----------------------------------------------------------------------------------------------------------------+
   | ``16#1C``  | 0         | Pickit is not in calibration mode.                                                                              |
   +------------+-----------+-----------------------------------------------------------------------------------------------------------------+
   | ``16#1D``  | 1         | Pickit returned a *failure* status number.                                                                      |
   +------------+-----------+-----------------------------------------------------------------------------------------------------------------+
   | ``16#40``  | 1         | Timeout error, cannot establish a connection.                                                                   |
   +------------+-----------+-----------------------------------------------------------------------------------------------------------------+
   | ``16#41``  | 1         | Timeout error, the connection was established but the initial handshake failed.                                 |
   +------------+-----------+-----------------------------------------------------------------------------------------------------------------+
   | ``16#42``  | 1         | Timeout error, the connection was established but there was no data received as a response to the send request. |
   +------------+-----------+-----------------------------------------------------------------------------------------------------------------+

The communication is internally set up with the ``TSEND_C`` and ``TRCV_C`` standard function blocks.
For detailed status information on the connection itself, these blocks can be monitored inside the Pickit data block.
Detailed information can be found in the `Siemens S7-1200 Programmable controller System Manual <https://drive.google.com/file/d/1yu0xbqCDkAdQDNX_uxTlV8zeeYXEIkpU/view?usp=sharing>`__.

.. _siemens_robot_to_pickit_data:

Robot to Pickit data
^^^^^^^^^^^^^^^^^^^^
The *robot_to_pickit_data* structure contains all parameters that make up the send message of 48 bytes.
Detailed information about the message structure can be found in the :ref:`socket communication article <socket-communication>`.

.. table:: robot_to_pickit_data

   +----------------------------+-----------+----------------+-------------------------------------------------------------------------------------------------------+
   | robot_to_pickit_data       | Datatype  | Default value  | Comment                                                                                               |
   +============================+===========+================+=======================================================================================================+
   | RobotPose.X                | Real      | ``0.0``        | Registers containing the robot pose X translation in m.                                               |
   +----------------------------+-----------+----------------+-------------------------------------------------------------------------------------------------------+
   | RobotPose.Y                | Real      | ``0.0``        | Registers containing the robot pose Y translation in m.                                               |
   +----------------------------+-----------+----------------+-------------------------------------------------------------------------------------------------------+
   | RobotPose.Z                | Real      | ``0.0``        | Registers containing the robot pose Z translation in m.                                               |
   +----------------------------+-----------+----------------+-------------------------------------------------------------------------------------------------------+
   | RobotPose.A                | Real      | ``0.0``        | Registers containing the robot pose A rotation.                                                       |
   +----------------------------+-----------+----------------+-------------------------------------------------------------------------------------------------------+
   | RobotPose.B                | Real      | ``0.0``        | Registers containing the robot pose B rotation.                                                       |
   +----------------------------+-----------+----------------+-------------------------------------------------------------------------------------------------------+
   | RobotPose.C                | Real      | ``0.0``        | Registers containing the robot pose C rotation.                                                       |
   +----------------------------+-----------+----------------+-------------------------------------------------------------------------------------------------------+
   | RobotPose.D                | Real      | ``0.0``        | Registers containing the robot pose D rotation.                                                       |
   +----------------------------+-----------+----------------+-------------------------------------------------------------------------------------------------------+
   | Payload.SetupId            | DInt      | ``1``          | ID of the setup configuration when requesting ``rc_pickit_configure()``.                              |
   +----------------------------+-----------+----------------+-------------------------------------------------------------------------------------------------------+
   | Payload.ProductId          | DInt      | ``1``          | ID of the product configuration when requesting ``rc_pickit_configure()``.                            |
   +----------------------------+-----------+----------------+-------------------------------------------------------------------------------------------------------+
   | Payload.DetectionRetries   | DInt      | ``0``          | Maximum number of detection retries when requesting ``rc_pickit_look_for_objects_with_retries()``.    |
   +----------------------------+-----------+----------------+-------------------------------------------------------------------------------------------------------+
   | Command                    | DInt      | ``0``          | Pickit robot command number.                                                                          |
   +----------------------------+-----------+----------------+-------------------------------------------------------------------------------------------------------+
   | MetaData.RobotType         | DInt      | ``5``          | Orientation convention dependent on robot brand. The default value corresponds to KUKA.               |
   +----------------------------+-----------+----------------+-------------------------------------------------------------------------------------------------------+
   | MetaData.InterfaceVersion  | DInt      | ``11``         | Pickit socket interface version ``1.1``.                                                              |
   +----------------------------+-----------+----------------+-------------------------------------------------------------------------------------------------------+

Pickit expects to receive the robot pose continuously.
For that reason does the block send the ``robot_to_pickit_data.RobotPose`` input values each 100 ms, also referred to as the heartbeat.
This implies the robot pose **must be sent to** the PLC from the robot controller in a real-time data stream.

The convention in which the orientation part of the pose is expressed depends on the robot brand being used.
This convention is specified in the ``MetaData.RobotType`` input.
The supported brands and their corresponding convention can be found in the socket communication article under :ref:`Meta Data<meta-msg>`.

Each request from the PLC contains a command number.
This number has to be filled in inside the ``robot_to_pickit_data.Command`` variable.
An overview of all possible Pickit commands can be found in the list below.
More information on the exact meaning of each command can be found in :ref:`socket communication article <socket-communication>`.

 .. _siemens_request-cmds:
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
    RC_PICKIT_SAVE_SCENE                    = 50
    RC_PICKIT_BUILD_BACKGROUND              = 60
    RC_PICKIT_GET_PICK_POINT_DATA           = 70


.. warning:: Sending undefined command numbers will lead to block fault, which is considered a fatal error and terminating the connection.

On startup the connection is automatically being established.
To confirm there is a connection, an initial *rc_pickit_check_mode()* command is sent for verification.
This initial handhake sets the pickit_mode output.
During runtime, this output is only reliable when consiquently requesting the *rc_pickit_check_mode()* command.
The possible values for this parameter are listed below.

 .. _pickit-mode:
 .. code-block:: python
    :caption: The Pickit mode output values

    UNDEFINED                               = -1
    ROBOT MODE                              = 0
    CALIBRATION MODE                        = 1
    IDLE                                    = 2

Certain command numbers require Pickit to be in the correct mode.
The *rc_pickit_find_calib_plate()* command requires calibration mode.
The commands from *rc_pickit_look_for_objects()* and up require robot mode.

.. warning:: When Pickit is not set to the correct mode, the communication block faults and terminates the connection.

.. _socket_params:

Socket parameters
^^^^^^^^^^^^^^^^^

The *socket_params* structure contains all parameters to set up the TCP/IP V4 connection.
The tabel below gives an overview of all the parameters that have to be filled in.

.. table:: socket_params

   +----------------------------+-----------+----------------+---------------------------------------------------------------------------------------------------+
   | socket_params              | Datatype  | Default value  | Comment                                                                                           |
   +============================+===========+================+===================================================================================================+
   | ConnectionId               | Word      | ``16#0001``    | Connection identifier in TIA. When having multiple connections, use the next free id.             |
   +----------------------------+-----------+----------------+---------------------------------------------------------------------------------------------------+
   | RemoteAddress[0]           | USInt     | ``169``        | First octet of the Pickit IP address.                                                             |
   +----------------------------+-----------+----------------+---------------------------------------------------------------------------------------------------+
   | RemoteAddress[1]           | USInt     | ``254``        | Second octet of the Pickit IP address.                                                            |
   +----------------------------+-----------+----------------+---------------------------------------------------------------------------------------------------+
   | RemoteAddress[2]           | USInt     | ``5``          | Third octet of the Pickit IP address.                                                             |
   +----------------------------+-----------+----------------+---------------------------------------------------------------------------------------------------+
   | RemoteAddress[3]           | USInt     | ``182``        | Fourth octet of the Pickit IP address.                                                            |
   +----------------------------+-----------+----------------+---------------------------------------------------------------------------------------------------+
   | RemotePort[0]              | USInt     | ``16#13``      | First octet of the Pickit port number (fixed ``5001``).                                           |
   +----------------------------+-----------+----------------+---------------------------------------------------------------------------------------------------+
   | RemotePort[1]              | USInt     | ``16#89``      | Second octet of the Pickit port number (fixed ``5001``).                                          |
   +----------------------------+-----------+----------------+---------------------------------------------------------------------------------------------------+
   | Timeout                    | IEC time  | ``T#4s``       | Communication timeout value.                                                                      |
   +----------------------------+-----------+----------------+---------------------------------------------------------------------------------------------------+
   | Heartbeat                  | IEC time  | ``T#100ms``    | Specifies the time between each ``rc_pickit_no_command()``, default 100 ms.                       |
   +----------------------------+-----------+----------------+---------------------------------------------------------------------------------------------------+

The default value for the connection identifier within TIA Portal is set to ``1``.
However with multiple connections, this number might already be in use.
The ids that are still free to use can be found in device proporties under *Device settings*.

The ``socket_params.Timeout`` input specifies the timeframe the PLC has for receiving messages back from Pickit.
When this timeframe is exceeded, the block faults.

The ``socket_params.Heartbeat`` input specifies the timestamp Pickit will receive the robot pose update.
This information is necessary for the visualisation of the robot pose within the Pickit UI.
Setting this value to ``T#0s`` will not update the robot pose and Pickit might appear to not be connected.

.. _pickit_to_robot_data:

Pickit to robot data
^^^^^^^^^^^^^^^^^^^^

The *pickit_to_robot_data* structure contains all the output parameters that make up the receive message of 64 bytes.
Detailed information of the receive message can be found in the :ref:`socket communication article <socket-communication>`.

.. table:: pickit_to_robot_data

   +---------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------+
   | pickit_to_robot_data            | Datatype  | Comment                                                                                                                                           |
   +=================================+===========+===================================================================================================================================================+
   | RobotPose.X                     | Real      | Object translation X in m.                                                                                                                        |
   +---------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------+
   | RobotPose.Y                     | Real      | Object translation Y in m.                                                                                                                        |
   +---------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------+
   | RobotPose.Z                     | Real      | Object translation Z in m.                                                                                                                        |
   +---------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------+
   | RobotPose.A                     | Real      | Object rotation A.                                                                                                                                |
   +---------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------+
   | RobotPose.B                     | Real      | Object rotation B.                                                                                                                                |
   +---------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------+
   | RobotPose.C                     | Real      | Object rotation C.                                                                                                                                |
   +---------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------+
   | RobotPose.D                     | Real      | Object rotation D.                                                                                                                                |
   +---------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------+
   | PickPointOffset.X               | Real      | Pick point offset translation X in m.                                                                                                             |
   +---------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------+
   | PickPointOffset.Y               | Real      | Pick point offset translation Y in m.                                                                                                             |
   +---------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------+
   | PickPointOffset.Z               | Real      | Pick point offset translation Z in m.                                                                                                             |
   +---------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------+
   | PickPointOffset.A               | Real      | Pick point offset rotation A.                                                                                                                     |
   +---------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------+
   | PickPointOffset.B               | Real      | Pick point offset rotation B.                                                                                                                     |
   +---------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------+
   | PickPointOffset.C               | Real      | Pick point offset rotation C.                                                                                                                     |
   +---------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------+
   | PickPointOffset.D               | Real      | Pick point offset rotation D.                                                                                                                     |
   +---------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------+
   | Payload.ObjectAge               | Real      | The duration (in seconds) elapsed between the capturing of the camera image and the moment the object information is sent to the robot.           |
   +---------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------+
   | Payload.ObjectType              | UDInt     | For a Teach detection, this field contains the model ID of the current object. For a Flex/Pattern detection, this field contains the object type. |
   +---------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------+
   | Payload.ObjectDimensions.Length | Real      | Object length (SQUARE, RECTANGLE, ELLIPSE, CYLINDER, POINTCLOUD, BLOB) or diameter (CIRCLE, SPHERE) in meters.                                    |
   +---------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------+
   | Payload.ObjectDimensions.Width  | Real      | Object width (RECTANGLE, ELLIPSE, POINTCLOUD, BLOB) or diameter (CYLINDER) in meters.                                                             |
   +---------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------+
   | Payload.ObjectDimensions.Height | Real      | Object height (POINTCLOUD, BLOB) in meters.                                                                                                       |
   +---------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------+
   | Payload.ObjectsRemaining        | UDInt     | If this field is non-zero, it contains the number of remaining objects that can be retrieved via consecutive RC_PICKIT_NEXT_OBJECT requests.      |
   +---------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------+
   | Payload.ReferencePickPointID    | UDInt     | ID of the selected pick point’s reference pick point.                                                                                             |
   +---------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------+
   | Payload.SelectedPickPointID     | UDInt     | ID of the pick point that was selected for the given object.                                                                                      |
   +---------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------+
   | Status                          | DInt      | The Pickit response status number.                                                                                                                |
   +---------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------+
   | MetaData.RobotType              | DInt      | The confirmed orientation convention dependent on robot brand.                                                                                    |
   +---------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------+
   | MetaData.InterfaceVersion       | DInt      | The confirmed Pickit socket interface version.                                                                                                    |
   +---------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------+

The ``pickit_to_robot_data.ObjectPose`` holds the object pose expressed to robot base frame.
The orientation convention is determined by the ``robot_to_pickit_data.MetaData.RobotType`` parameter in the input section.

The ``robot_to_pickit_data.PickPointOffset`` contains the offset transformation w.r.t. the reference pick point set inside the Pickit system.
To obtain both the object pose and the pick point offset you need to subsequently request a *rc_pickit_find_objects()* and *rc_pickit_get_pick_point_data()* in correct order.

.. note:: The orientation of the object pose is expressed in compliance with the Pickit *Objects view*. More specifically, the object pose z-axis points outwards from the model. Dependent on your TCP configurtion on the robot side, it will be necessary to apply an additional 180 degrees rotation around the object x-axis. This to ensure the robot approaches the object correctly.

.. warning:: The object pose from Pickit is not validated on reachability. It is **strongly advised** to validate this position on the robot controller before moving to the position. The supported robot brands by Pickit have these validations built into the robot interface. When using any of these brands, contact support for more information.

The response message from Pickit contains a status number, found in the ``pickit_to_robot_data.Status`` output. The possible constants are shown in the list below.

 .. _siemens_response-status:
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

The robot commands function
---------------------------

This section describes the Pickit robot commands function in detail.
The use of this block is optional.

.. image:: ../../assets/images/robot-integrations/siemens/network_pi_rc.PNG

This function calculates the Pickit command number from separate command inputs.
The inputs for the block are all Booleans that can be linked to user-defined memory.
The output is a double integer DInt containing the command number.
This output is intented to be linked directly to the ``robot_to_pickit_data.Command`` input parameter as shown in the image.

.. warning:: Note that if two or more inputs are set to ``True``, the block outputs an undefined command number which results in block fault. Therefore it is mandatory to **set only one input** each time.
