.. _yaskawa_example_picking_program:

Yaskawa example picking program
===============================

This example program requires that Pickit is installed and set up with your robot.
For installation instructions, please refer to the :ref:`yaskawa_installation_and_setup` article.

Before you can start picking, make sure that :ref:`robot-camera-calibration` is done.
This can be done by running the :ref:`yaskawa_calibration_program`.

Example program: TEST_SIMPLEPICK
--------------------------------

This example program can be found in :guilabel:`JOB` → :guilabel:`SELECT JOB`.

::

    NOP
    PI_RUN
    'Initiallization PI count
    SET B021 0
    'Init' reachable check signal
    SET I043 0
    MOVJ VJ=10.00  //Home pose
    'Load config
    PI_CFG SETUP:2 PRODUCT:2 U/FRAME:5 TOOL:1 TIMEOUT:20000
    *LABEL
    'Picking
    IFTHEN I040=20
    	'Prepick pose
    	 MULMAT P043 P049 P022
    	'Postpick pose
    	 MULMAT P045 P049 P021
    	'Check reachable object pose
    	 PI_REACH
    	'GET PICK POINT DATA
    	 PI_GPPD
    	'If reachable
    	 IFTHENEXP I043=0
    		 MOVJ P040 VJ=50.00  //Above pick area
    		 MSG "Moving to object"
    		 MOVJ P043 VJ=10.00  //Prepick pose
    		 MOVL P049 V=800.0 PL=0  //Pick pose
    		'Add grasping logic here
    		 MOVJ P045 VJ=10.00  //Post pick pose
    		 MOVJ P040 VJ=50.00  //Above pick area
    		 MOVJ P025 VJ=50.00  //Detect pose
    		 MSG "Looking for objects"
    		 PI_LOOK
    		'Drop off part
    		 MULMAT LP000 P047 P029
    		 MSG "Moving to dropoff"
    		 MOVL P029 V=23.0  //Dropoff pose
    		 MOVL LP000 V=23.0  //Corr dropoff pose
    		'Add realese logic here
    		 MOVJ P025 VJ=50.00
    		 PI_WAIT
    	 ELSE
    		 MSG "OBJECT OUT OF REACH"
    		 PI_NEXT
    		 PI_WAIT
    	 ENDIF
    ELSEIFEXP I040=23
    	 MSG "ROI is empty"
    	 JUMP *EMPTY
    ELSE
    	 INC B021
    	 IFTHENEXP B021>3
    		 MSG "No objects found after 3 times"
    		 PI_SAVE
    		 JUMP *EMPTY
    	 ENDIF
    	 MOVJ P025 VJ=50.00
    	 PI_LOOK
    	 MSG "Looking for objects"
    	 PI_WAIT
    ENDIF
    JUMP *LABEL
    *EMPTY
    END

The idea of the program is the following:

- If an object is found, and is within reach of the robot arm.
  The robot moves to the object to pick it.
  Next, the robot moves to a fixed drop off position, and finally it moves to a corrected drop off position.
  The corrected position is based on the pick offset and the fixed drop off position.
  During these motions when the robot is out the field of view of the camera, a new Pickit detection is triggered immediately.
- If the ROI is empty, the program stops.
- If no object is found but ROI is not empty, the robot moves outside the field of view of the camera and a new detection is triggered.
  If three times no object is found, a snapshot is saved on the Pickit system and the robot program stops. 

Define the tool for picking
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a tool frame with the actual TCP values.
Again it is important that **tool0** is not changed. Any other tool can be used.

Set PI_CFG
~~~~~~~~~~

In this command the input arguments have to be set. See :ref:`pi_cfg` for more information on how to do this.


Variables used in TEST_SIMPLEPICK 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below you find an overview of the variables used in this example program.
The Pickit variables, in the 40 range, can't be changed by the user, an overview of these can be found in the :ref:`yaskawa_pickit_interface` article.
All other variables can be adapted according the changes you want to apply to this example program.

+-----------+----------------------------+---------------------------------------------------------------------------------------------------+-------------+
| Variable  | Field name                 | Comment                                                                                           | Set by user |
+===========+============================+===================================================================================================+=============+
| B021      | Detection counter          | This variable keeps track of the number of detections that are triggered                          | Yes         |
+-----------+----------------------------+---------------------------------------------------------------------------------------------------+-------------+
| P021      | Post pick offset           | Distance offset to calculate the post pick position                                               | Yes         |
+-----------+----------------------------+---------------------------------------------------------------------------------------------------+-------------+
| P022      | Pre pick offset            | Distance offset to calculate the pre pick position                                                | Yes         |
+-----------+----------------------------+---------------------------------------------------------------------------------------------------+-------------+
| P025      | Detect position            | Position not blocking the field of view of the camera when triggering detections                  | Yes         |
+-----------+----------------------------+---------------------------------------------------------------------------------------------------+-------------+
| P029      | Drop off position          | Position where the part is dropped off                                                            | Yes         |
+-----------+----------------------------+---------------------------------------------------------------------------------------------------+-------------+
| LP000     | Corrected drop off positon | Drop off position corrected with offset of the pick point                                         | No          |
+-----------+----------------------------+---------------------------------------------------------------------------------------------------+-------------+
| C000      | Home position              | Position where the robot starts his program                                                       | Yes         |
+-----------+----------------------------+---------------------------------------------------------------------------------------------------+-------------+

.. tip:: The positions P021-P029 can be changed in the position variable menu.

Add grasping/releasing logic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Grasping and releasing logic need to be added at the **Add grasping logic here** and **Add realese logic here** comments, respectively.

Execute the picking program
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To run this program either do **Play + Start**, **Interlock + FWD** or **Interlock + Test**.
Happy picking!