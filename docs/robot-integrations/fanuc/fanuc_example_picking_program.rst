.. _fanuc-example-picking-program:

Fanuc example picking program
=============================

This article describes the Fanuc example picking program. 
Then, it explains how to adapt the program to start running it.
It is ideal to get started with Pickit.

PICKIT_SIMPLE_PICKING: program overview
---------------------------------------

The program follows the :ref:`generic Pickit example program <pick-and-place-simple-logic>` logic.

- First check if Pickit is in :ref:`Robot mode <web-interface-top-bar>`.
- If so, the robot moves to its detect pose and a detection is triggered.
- If an object is found and if it is reachable, its model and pick point ID are retrieved.
  The robot moves to the object to pick it.
  Next, the robot moves to a fixed drop off position.
  During these motions when the robot is out the field of view of the camera, a new Pickit detection is triggered immediately.
- If the ROI is empty, the program stops.
- If no object is found but ROI is not empty, a :ref:`Snapshots` is saved on the Pickit system and the robot program stops. 

This program can be found in :guilabel:`Select`.

::

   1:  !Program settings ;
   2:  !Fill in settings below ;
   3:  UFRAME_NUM=0 ;
   4:  UTOOL_NUM=1 ;
   5:  R[1:setup id]=3    ;
   6:  R[2:product id]=2    ;
   7:  R[3:max detect]=5    ;
   8:  R[4:pre offset]=(-100)    ;
   9:  R[5:post offset]=(-100)    ;
  10:   ;
  11:   ;
  12:  !Init ;
  13:  CALL PI_OPEN_COMMUNICATION    ;
  14:  CALL PI_RUN    ;
  15:  IF (R[151:pi status]<>0) THEN ;
  16:  MESSAGE[Not in robot mode] ;
  17:  JMP LBL[2] ;
  18:  ENDIF ;
  19:  CALL PI_CONFIGURE(R[1:setup id],R[2:product id]) ;
  20:  CALL PI_SET_OFFSET(R[4:pre offset],1) ;
  21:  CALL PI_SET_OFFSET(R[5:post offset],2) ;
  22:   ;
  23:  !First detection ;
  24:J P[1:detect] 100% CNT100    ;
  25:  CALL PI_DETECTION_WITH_RETRIES(R[3:max detect]) ;
  26:  CALL PI_WAIT    ;
  27:   ;
  28:   ;
  29:  !Main Loop ;
  30:  LBL[1] ;
  31:   ;
  32:  !If object found ;
  33:  IF (R[150:pi obj status]=20) THEN ;
  34:   ;
  35:  !If reachable ;
  36:  CALL PI_REACH    ;
  37:  IF (R[160:pi reach status]=0) THEN ;
  38:   ;
  39:  CALL PI_GET_PICK_POINT_DATA    ;
  40:   ;
  41:  !Picking ;
  42:J P[2:above bin] 100% CNT100    ;
  43:  !Move to pre pick pose ;
  44:L PR[51:pi pick pose] 100mm/sec CNT100 Tool_Offset,PR[1:pre offset]    ;
  45:  !Move to pick pose ;
  46:L PR[51:pi pick pose] 100mm/sec FINE    ;
  47:  !Add grasping logic ;
  48:  !Move to post pick pose ;
  49:L PR[51:pi pick pose] 100mm/sec CNT100 Tool_Offset,PR[2:post offset]    ;
  50:L P[2:above bin] 100mm/sec CNT100    ;
  51:  !Detection ;
  52:J P[1:detect] 100% CNT100    ;
  53:  CALL PI_CAPTURE_IMAGE    ;
  54:  CALL PI_PROCESS_IMAGE    ;
  55:   ;
  56:  !Drop off ;
  57:J P[3:drop off] 100% FINE    ;
  58:  !Add release logic ;
  59:J P[1:detect] 100% CNT100    ;
  60:   ;
  61:  !Get detection results ;
  62:  CALL PI_WAIT    ;
  63:   ;
  64:  !Not reachable ;
  65:  ELSE ;
  66:  !Try next object ;
  67:  CALL PI_NEXT_OBJECT    ;
  68:  CALL PI_WAIT    ;
  69:  ENDIF ;
  70:   ;
  71:  !No object found ;
  72:  ELSE ;
  73:  !Empty ROI ;
  74:  IF (R[150:pi obj status]=23) THEN ;
  75:  MESSAGE[ROI is empty] ;
  76:  JMP LBL[2] ;
  77:  !No object found ;
  78:  ELSE ;
  79:  MESSAGE[No object found] ;
  80:  CALL PI_SAVE_SCENE    ;
  81:  JMP LBL[2] ;
  82:  ENDIF ;
  83:  ENDIF ;
  84:  JMP LBL[1] ;
  85:  LBL[2] ;
     END

See :ref:`fanuc-pickit-macros` for more information about the Pickit rountines available.

Before running the program
--------------------------

This example program requires Pickit to be installed and set up with your robot.
For installation instructions, please refer to the :ref:`fanuc_installation_and_setup` article.

Make sure that :ref:`robot-camera-calibration` is done.
This can be done by running the :ref:`fanuc-calibration-program`.

Run PI_SET_PICK_POSE
~~~~~~~~~~~~~~~~~~~~

Before executing the picking program we first need to define the robot joint configuration for picking.
This is done by jogging the robot to the center of the picking area and manually run the PI_SET_PICK_POSE macro.
The macro will read out the current joint configuration of the robot and this will be used as seed for all calculated pick poses. 

Define the tool for picking
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a tool frame with the actual TCP values.
In this example **UTOOL1** is used.

Adapt the registers used in PICKIT_SIMPLE_PICKING 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below you find an overview of the registers used in this example program.
They should be adapted according the changes you want to apply to this example program.

.. note::
  The Pickit registers, in the 140-160 range, and the Pickit pose registers, in the 50 range, can't be changed by the user.
  An overview of these can be found in the :ref:`fanuc-pickit-interface` article.

+-----------+------------------------+---------------------------------------------------------------------------------------------------+
| Variable  | Field name             | Comment                                                                                           |
+===========+========================+===================================================================================================+
| R[1]      | Setup                  | Requested Pickit setup ID                                                                         |
+-----------+------------------------+---------------------------------------------------------------------------------------------------+
| R[2]      | Product                | Requested Pickit product ID                                                                       |
+-----------+------------------------+---------------------------------------------------------------------------------------------------+
| R[3]      | Retries                | Maximum number of detection retries                                                               |
+-----------+------------------------+---------------------------------------------------------------------------------------------------+
| R[4]      | Pre pick offset        | Z offset used to defined the pre pick pose offset (use a negative value).                         |
+-----------+------------------------+---------------------------------------------------------------------------------------------------+
| R[5]      | Post pick offset       | Z offset used to defined the post pick pose offset (use a negative value).                        |
+-----------+------------------------+---------------------------------------------------------------------------------------------------+
| P[1]      | Detect pose            | Position not blocking the field of view of the camera when triggering detections                  |
+-----------+------------------------+---------------------------------------------------------------------------------------------------+
| P[2]      | Above bin pose         | Position above the picking area                                                                   |
+-----------+------------------------+---------------------------------------------------------------------------------------------------+
| P[3]      | Drop off pose          | Position where the object is dropped off                                                          |
+-----------+------------------------+---------------------------------------------------------------------------------------------------+
| PR[1]     | Pre pick pose          | Position offset the robot moves to before picking the object (relative to tool frame)             |
+-----------+------------------------+---------------------------------------------------------------------------------------------------+
| PR[2]     | Post pick pose         | Position offset the robot moves to after picking the object (relative to tool frame)              |
+-----------+------------------------+---------------------------------------------------------------------------------------------------+

Add grasping/releasing logic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At the **pi pose** and **drop off pose** positions, grasping and releasing logic needs to be added, respectively.

Execute the picking program
---------------------------

Now you can run the program.
Happy picking!