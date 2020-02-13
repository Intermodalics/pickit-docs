Yaskawa example picking program
===============================

Example program: TEST_SIMPLEPICK
--------------------------------

This example program can be found in :guilabel:`JOB` → :guilabel:`SELECT JOB`.

The idea of the program is the following:

- First, a detection is triggered.
- If an object is found, its model and pick point ID are retrieved.
  According to these ID's the robot moves to the object to pick it.
  Next, the robot moves to a fixed drop off position, and finally it moves to a corrected drop off position.
  The corrected position is based on the pick offset and the fixed drop off position.
  During these motions when the robot is out the field of view of the camera, a new Pickit detection is triggered immediately.
- If the ROI is empty, the program stops.
- If no object is found but ROI is not empty, the robot moves outside the field of view of the camera and a new detection is triggered.
  If three times no object is found, a snapshot is saved on the Pickit system and the robot program stops. 

Define the tool for calibration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a tool frame with the actual TCP values.
Again it is important that **tool0** is not changed. Any other tool can be used.

Set PIT_CFG
~~~~~~~~~~~

In this command the following values have to be set:

- **Setup**: Pickit setup file ID.
- **Product**: Pickit product file ID.
- **User Frame**: User frame that was created in TEST_CALIB. By default, this is **5**.
- **Tool**: Number of the tool frame defined in the previous step.

.. note:: If something is wrong here, you can expect the following message: Undefined user frame.
   The example program by default uses frame 5 and tool 1, but these might not exist.

Variables used in TEST_SIMPLEPICK 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below you find an overview of the variables used in this example program.
The Pickit variables, in the 40 range, can't be changed by the user.
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
| P023      | Above pick area            | Position that is defined above the pick area                                                      | Yes         |
+-----------+----------------------------+---------------------------------------------------------------------------------------------------+-------------+
| P025      | Detect position            | Position not blocking the field of view of the camera when triggering detections                  | Yes         |
+-----------+----------------------------+---------------------------------------------------------------------------------------------------+-------------+
| P029      | Drop off position          | Position where the part is dropped off                                                            | Yes         |
+-----------+----------------------------+---------------------------------------------------------------------------------------------------+-------------+
| P047      | Pickit object offset       | Offset of the pick point                                                                          | No          |
+-----------+----------------------------+---------------------------------------------------------------------------------------------------+-------------+
| P049      | Pickit object pose         | Position of the object                                                                            | No          |
+-----------+----------------------------+---------------------------------------------------------------------------------------------------+-------------+
| LP000     | Pre pick position          | Position the robot moves to before picking the object                                             | No          |
+-----------+----------------------------+---------------------------------------------------------------------------------------------------+-------------+
| LP001     | Post pick position         | Position the robot moves to after picking the object                                              | No          |
+-----------+----------------------------+---------------------------------------------------------------------------------------------------+-------------+
| LP002     | Corrected drop off positon | Drop off position corrected with offset of the pick point                                         | No          |
+-----------+----------------------------+---------------------------------------------------------------------------------------------------+-------------+
| C000      | Home position              | Position where the robot starts his program                                                       | Yes         |
+-----------+----------------------------+---------------------------------------------------------------------------------------------------+-------------+
| I040      | Pickit status              | Contains a response to previously received robot commands: object found/empty roi/no object found | No          |
+-----------+----------------------------+---------------------------------------------------------------------------------------------------+-------------+
| I041      | Pickit object type         | Contains the model id of the current found object                                                 | No          |
+-----------+----------------------------+---------------------------------------------------------------------------------------------------+-------------+
| I042      | Pickit pick point id       | Contains the pick point id of the current found object                                            | No          |
+-----------+----------------------------+---------------------------------------------------------------------------------------------------+-------------+

.. tip:: The positions P021-P029 can be changed in the position variable menu.

Add grasping/releasing logic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At the **Pick** and **Dropoff** positions, grasping and releasing logic needs to be added, respectively.

Execute the picking program
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To run this program either do **Play + Start**, **Interlock + FWD** or **Interlock + Test**.
Happy picking!
