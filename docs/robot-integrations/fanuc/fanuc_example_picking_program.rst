.. _fanuc-example-picking-program:

Fanuc example picking program
=============================

This example program requires that Pickit is installed and set up with your robot.
For installation instructions, please refer to the :ref:`yaskawa_installation_and_setup` article.

Before you can start picking, make sure that :ref:`robot-camera-calibration` is done.
This can be done by running the :ref:`yaskawa_calibration_program`.

Example program: PICKIT_SIMPLE_PICKING
--------------------------------------

This example program can be found in :guilabel:`Select`.

::

      1:  CALL PI_OPEN_COMMUNICATION    ;
      2:  UFRAME_NUM=0 ;
      3:  UTOOL_NUM=1 ;
      4:  R[1:setup]=5    ;
      5:  R[2:product]=2    ;
      6:  R[3:retries]=5    ;
      7:J PR[1:home pose] 100% CNT100    ;
      8:  CALL PI_CONFIGURE(R[1:setup],R[2:product]) ;
      9:J PR[2:detect pose] 100% CNT100    ;
     10:  CALL PI_DETECTION_WITH_RETRIES(R[3:retries]) ;
     11:  CALL PI_WAIT    ;
     12:  LBL[1] ;
     13:  !Object found ;
     14:  IF (R[150:pi object status]=20) THEN ;
     15:    CALL PI_GET_PICK_POINT_DATA    ;
     16:J   PR[3:above bin pose] 100% CNT100    ;
     17:L   PR[51:pi pose] 100mm/sec CNT100 Offset,PR[5:before pick]    ;
     18:L   PR[51:pi pose] 100mm/sec FINE    ;
     19:    !Add grasping logic ;
     20:L   PR[51:pi pose] 100mm/sec CNT100 Tool_Offset,PR[6:after pick]    ;
     21:L   PR[3:above bin pose] 100mm/sec CNT100    ;
     22:J   PR[2:detect pose] 100% CNT100    ;
     23:    CALL PI_DETECTION_WITH_RETRIES(R[3:retries]) ;
     24:L   PR[4:drop off pose] 100mm/sec FINE    ;
     25:    !Add release logic ;
     26:J   PR[2:detect pose] 100% CNT100    ;
     27:    CALL PI_WAIT    ;
     28:  ELSE ;
     29:  !Empty ROI ;
     30:  IF (R[150:pi object status]=23) THEN ;
     31:    MESSAGE[ROI is empty] ;
     32:    JMP LBL[2] ;
     33:  !No object found ;
     34:  ELSE ;
     35:    MESSAGE[No object found] ;
     36:    CALL PI_SAVE_SCENE    ;
     37:    JMP LBL[2] ;
     38:  ENDIF ;
     39:  ENDIF ;
     40:  JMP LBL[1] ;
     41:  LBL[2] ;

The idea of the program is the following:

- If an object is found, its model and pick point ID are retrieved.
  The robot moves to the object to pick it.
  Next, the robot moves to a fixed drop off position.
  During these motions when the robot is out the field of view of the camera, a new Pickit detection is triggered immediately.
- If the ROI is empty, the program stops.
- If no object is found but ROI is not empty, a snapshot is saved on the Pickit system and the robot program stops. 

Define the tool for picking
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a tool frame with the actual TCP values.
In this example **UTOOL1** is used.

Set PI_CONFIGURE
~~~~~~~~~~~~~~~~

In this command the input arguments have to be set.
See :ref:`pi_configure` for more information on how to do this.
In this example R[1] and R[2] are reserved for this and by default set to 5 and 2.

Set PI_DETECTION_WITH_RETRIES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this command the input argument have to be set.
See :ref:`pi_detection_with_retries` for more information on how to do this.
In this example R[3] is reserved for this and by default set to 5.

Variables used in PICKIT_SIMPLE_PICKING 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below you find an overview of the variables used in this example program.
The Pickit registers, in the 140-160 range, and the Pickit pose registers, in the 50 range, can't be changed by the user, an overview of these can be found in the :ref:`fanuc-pickit-interface` article.
All other variables can be adapted according the changes you want to apply to this example program.

+-----------+------------------------+---------------------------------------------------------------------------------------------------+-------------+
| Variable  | Field name             | Comment                                                                                           | Set by user |
+===========+========================+===================================================================================================+=============+
| R[1]      | Setup                  | Requested Pickit setup ID                                                                         | Yes         |
+-----------+------------------------+---------------------------------------------------------------------------------------------------+-------------+
| R[2]      | Product                | Requested Pickit product ID                                                                       | Yes         |
+-----------+------------------------+---------------------------------------------------------------------------------------------------+-------------+
| R[3]      | Retries                | Maximum number of detection retries                                                               | Yes         |
+-----------+------------------------+---------------------------------------------------------------------------------------------------+-------------+
| PR[1]     | Home pose              | Start position of the robot program                                                               | Yes         |
+-----------+------------------------+---------------------------------------------------------------------------------------------------+-------------+
| PR[2]     | Detect pose            | Position not blocking the field of view of the camera when triggering detections                  | Yes         |
+-----------+------------------------+---------------------------------------------------------------------------------------------------+-------------+
| PR[3]     | Above bin pose         | Position above the picking area                                                                   | Yes         |
+-----------+------------------------+---------------------------------------------------------------------------------------------------+-------------+
| PR[4]     | Drop off pose          | Position where the object is dropped off                                                          | Yes         |
+-----------+------------------------+---------------------------------------------------------------------------------------------------+-------------+
| PR[5]     | Before pick            | Position offset the robot moves to before picking the object                                      | Yes         |
+-----------+------------------------+---------------------------------------------------------------------------------------------------+-------------+
| PR[6]     | After pick             | Position offset the robot moves to after picking the object                                       | Yes         |
+-----------+------------------------+---------------------------------------------------------------------------------------------------+-------------+

Add grasping/releasing logic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At the **pi pose** and **drop off pose** positions, grasping and releasing logic needs to be added, respectively.

Run PI_SET_PICK_POSE
--------------------

Before executing the picking program we first need to define the robot joint configuration for picking.
This is done by jogging the robot to the center of the picking area and manually run the PI_SET_PICK_POSE macro.
The macro will read out the current joint configuration of the robot and this will be used as seed for all calculated pick poses. 

Execute the picking program
---------------------------

Now you can run the program.
Happy picking!