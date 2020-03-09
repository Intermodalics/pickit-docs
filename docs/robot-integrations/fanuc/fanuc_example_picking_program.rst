.. _fanuc-example-picking-program:

Fanuc example picking program
=============================

This example program requires that Pickit is installed and set up with your robot.
For installation instructions, please refer to the :ref:`fanuc_installation_and_setup` article.

Make sure that :ref:`robot-camera-calibration` is done.
This can be done by running the :ref:`fanuc-calibration-program`.

Run PI_SET_PICK_POSE
--------------------

Before executing the picking program we first need to define the robot joint configuration for picking.
This is done by jogging the robot to the center of the picking area and manually run the PI_SET_PICK_POSE macro.
The macro will read out the current joint configuration of the robot and this will be used as seed for all calculated pick poses. 

Example program: PICKIT_SIMPLE_PICKING
--------------------------------------

This example program can be found in :guilabel:`Select`.

::

      1:  CALL PI_OPEN_COMMUNICATION    ;
      2:  CALL PI_RUN    ;
      3:  IF (R[151:pi status]<>0) THEN ;
      4:    MESSAGE[Not in robot mode] ;
      5:    JMP LBL[2] ;
      6:  ENDIF ;
      7:  UFRAME_NUM=0 ;
      8:  UTOOL_NUM=1 ;
      9:  !Fill in correct setup id ;
     10:  R[1:setup]=3    ;
     11:  !Fill in correct product id ;
     12:  R[2:product]=2    ;
     13:  !Fill in max detection retries ;
     14:  R[3:retries]=5    ;
     15:  CALL PI_CONFIGURE(R[1:setup],R[2:product]) ;
     16:J P[1:detect] 100% CNT100    ;
     17:  CALL PI_DETECTION_WITH_RETRIES(R[3:retries]) ;
     18:  CALL PI_WAIT    ;
     19:  LBL[1] ;
     20:  !Object found ;
     21:  IF (R[150:pi object status]=20) THEN ;
     22:    CALL PI_GET_PICK_POINT_DATA    ;
     23:J   P[2:above bin] 100% CNT100    ;
     24:    !Move to pre pick pose ;
     25:L   PR[51:pi pose] 100mm/sec CNT100 Tool_Offset,PR[1:pre pick offset]    ;
     26:    !Move to pick pose ;
     27:L   PR[51:pi pose] 100mm/sec FINE    ;
     28:    !Add grasping logic ;
     29:    !Move to post pick pose ;
     30:L   PR[51:pi pose] 100mm/sec CNT100 Offset,PR[2:post pick offset]    ;
     31:L   P[2:above bin] 100mm/sec CNT100    ;
     32:J   P[1:detect] 100% CNT100    ;
     33:    CALL PI_DETECTION_WITH_RETRIES(R[3:retries]) ;
     34:J   P[3:drop off] 100% FINE    ;
     35:    !Add release logic ;
     36:J   P[1:detect] 100% CNT100    ;
     37:    CALL PI_WAIT    ;
     38:  ELSE ;
     39:  !Empty ROI ;
     40:  IF (R[150:pi object status]=23) THEN ;
     41:    MESSAGE[ROI is empty] ;
     42:    JMP LBL[2] ;
     43:  !No object found ;
     44:  ELSE ;
     45:    MESSAGE[No object found] ;
     46:    CALL PI_SAVE_SCENE    ;
     47:    JMP LBL[2] ;
     48:  ENDIF ;
     49:  ENDIF ;
     50:  JMP LBL[1] ;
     51:  LBL[2] ;
     END

The idea of the program is the following:

- First it is checked if Pickit is set to :ref:`Robot mode <web-interface-top-bar>`.
- If so, the robot moves to its detect pose and a detection is triggered.
- If an object is found, its model and pick point ID are retrieved.
  The robot moves to the object to pick it.
  Next, the robot moves to a fixed drop off position.
  During these motions when the robot is out the field of view of the camera, a new Pickit detection is triggered immediately.
- If the ROI is empty, the program stops.
- If no object is found but ROI is not empty, a :ref:`Snapshots` is saved on the Pickit system and the robot program stops. 

Define the tool for picking
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a tool frame with the actual TCP values.
In this example **UTOOL1** is used.

Set correct input arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The commands PI_CONFIGURE and PI_DETECTION_WITH_RETRIES need input arguments.
In this example R[1], R[2] and R[3] are reserved for this and by default set to 5, 2 and 5.
See :ref:`fanuc-pickit-macros` for more information about these arguments.

Variables used in PICKIT_SIMPLE_PICKING 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below you find an overview of the variables used in this example program.
The Pickit registers, in the 140-160 range, and the Pickit pose registers, in the 50 range, can't be changed by the user, an overview of these can be found in the :ref:`fanuc-pickit-interface` article.
All other variables should be adapted according the changes you want to apply to this example program.

+-----------+------------------------+---------------------------------------------------------------------------------------------------+
| Variable  | Field name             | Comment                                                                                           |
+===========+========================+===================================================================================================+
| R[1]      | Setup                  | Requested Pickit setup ID                                                                         |
+-----------+------------------------+---------------------------------------------------------------------------------------------------+
| R[2]      | Product                | Requested Pickit product ID                                                                       |
+-----------+------------------------+---------------------------------------------------------------------------------------------------+
| R[3]      | Retries                | Maximum number of detection retries                                                               |
+-----------+------------------------+---------------------------------------------------------------------------------------------------+
| P[1]      | Detect pose            | Position not blocking the field of view of the camera when triggering detections                  |
+-----------+------------------------+---------------------------------------------------------------------------------------------------+
| P[2]      | Above bin pose         | Position above the picking area                                                                   |
+-----------+------------------------+---------------------------------------------------------------------------------------------------+
| P[3]      | Drop off pose          | Position where the object is dropped off                                                          |
+-----------+------------------------+---------------------------------------------------------------------------------------------------+
| PR[1]     | Before pick            | Position offset the robot moves to before picking the object (relative to tool frame)             |
+-----------+------------------------+---------------------------------------------------------------------------------------------------+
| PR[2]     | After pick             | Position offset the robot moves to after picking the object (relative to world frame)             |
+-----------+------------------------+---------------------------------------------------------------------------------------------------+

Add grasping/releasing logic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At the **pi pose** and **drop off pose** positions, grasping and releasing logic needs to be added, respectively.

Execute the picking program
---------------------------

Now you can run the program.
Happy picking!