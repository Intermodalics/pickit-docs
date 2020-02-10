.. _yaskawa:

Setting up Pickit with a Yaskawa robot
======================================

This setup manual helps you setup Pickit with a Yaskawa robot. The
setup of Pickit with a Yaskawa robot consists of 4 steps:

.. contents::
    :backlinks: top
    :local:
    :depth: 1

Check controller and software compatibility
-------------------------------------------

Pickit is compatible with controllers **DX200**, **YRC1000** and **YRC1000 micro**.
Also Pickit can be used with the **HC10** human-collaborative robot.

.. note:: Pickit is not yet compatible with the **Smart Pendant**.

The parameters listed below must be declared on the controller to allow the correct operation of the application.
Ask your local Yaskawa affiliate to check this.

-  **LAN INTERFACE SETTING** function set to **MANUAL SETTING**
-  **MotoPlus** function set to **USED**
-  **MACRO INST.** function set to **USED**
-  **MotoPlus - Number of files** set to **1** (Default setting)
-  **MotoPlus - Number of tasks** set to **5** (Default setting)

Setup the network connection
----------------------------

Hardware connection
~~~~~~~~~~~~~~~~~~~

The connection between the Yaskawa controller and Pickit is done over ethernet. You connect your robot controller to the **ROBOT** port on the Pickit processor as shown in the diagram below:

.. image:: /assets/images/robot-integrations/yaskawa/yaskawa.png

- For **DX200** controllers you need to connect the Pickit processor to the **CN104** port.
- For **YRC1000 (Micro)** controllers you need to connect the Pickit processor to the **CN106** or **CN107** port.

IP configuration
~~~~~~~~~~~~~~~~

.. warning::
  Before making these changes, the robot controller should be in **maintenance mode**, and the security mode should be **management mode**.

Setting the IP address of the robot controller should be done in **maintenance mode**.
Go to :guilabel:`SYSTEM` → :guilabel:`SETUP` → :guilabel:`OPTION FUNCTION` → :guilabel:`LAN interface setting` (or :guilabel:`Network` for the DX200) and set the following values:

  - **IP ADDRESS SETTING**: MANUAL SETTING
  - **IP ADDRESS:** 169.254.5.182
  - **SUBNET MASK:** 255.255.0.0
  - **DEFAULT GATEWAY:** 0.0.0.0

Press :guilabel:`ENTER` and :guilabel:`CONFIRM` to modify the values.

Load the program files
----------------------

Before starting, :ref:`Download the Pickit Yaskawa files here <downloads:Yaskawa>`.
The Pickit folder should be copied to a USB pen drive.

The robot controller should still be in **maintenance mode** and the security mode set to **management mode** before making these changes.

#. Insert the USB pen drive in the robot pendant.
#. Load the correct USB device under :guilabel:`MotoPlus APL` → :guilabel:`DEVICE`.
#. Select the folder **Pickit** > **MotoPlus** on the USB device under :guilabel:`MotoPlus APL` → :guilabel:`FOLDER`.
#. Load the MotoPlus application under :guilabel:`MotoPlus APL` → :guilabel:`LOAD(USER APPLICATION)`. 

.. warning:: In the next step, uploading the system data file **MACRO INST DEF DATA, MACRO.DAT** will remove all existing macro files on your controller, before pushing in the Pickit macros.
   If this is unwanted, do not upload the file.
   In that case, you should upload all other files as described below, and then :ref:`manually define the macros. <manually-define_macros>`

Press :guilabel:`Select`, :guilabel:`Enter` and confirm.
Now reboot the controller in **normal mode** with the USB device still attached.
After rebooting, set security to **management mode**.

#. Load the correct USB device under :guilabel:`EX. MEMORY` → :guilabel:`DEVICE`.
#. Select the folder **Pickit** > **Program** on the USB device under :guilabel:`EX. MEMORY` → :guilabel:`FOLDER`.
#. Load the **I/O DATA**, **SYSTEM DATA** and  **JOB** files under :guilabel:`EX. MEMORY` → :guilabel:`LOAD` (the order of loading the files is important).

Load the Pickit example jobs
----------------------------

In the Pickit folder there are two example jobs available.
These can be uploaded to the controller so you can easily get started with picking.

#. Select the folder **Pickit** > **Program** > **Examples** on the USB device under :guilabel:`EX. MEMORY` → :guilabel:`FOLDER`.
#. Load the **JOB** files under :guilabel:`EX. MEMORY` → :guilabel:`LOAD`.

Setting the Pickit IP address on the robot controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Still in **normal mode**, the IP address of Pickit needs to be entered in a **String**. To do this:

  #. Go to :guilabel:`Main menu` → :guilabel:`VARIABLE` → :guilabel:`STRING` → :guilabel:`S099`.
  #. Set **S099** to value **169.254.5.180**.

.. note:: There is no communication yet between the Pickit and the robot.
  So don't worry if the connection is not shown in the Pickit web interface :ref:`web-interface-top-bar`.
  The robot can be pinged from the Pickit web interface to check the IP settings.
  Details on testing this connection can be found on: :ref:`test-robot-connection`.

Test the robot connection
-------------------------

To start the communication, you can run **PIT_RUN** on the robot.
This job can be found in :guilabel:`JOB` → :guilabel:`SELECT MACRO JOB`.

While the program is running, an indicator in the Pickit web interface :ref:`web-interface-top-bar` should confirm that the robot is connected .

Example program: TEST_CALIB
---------------------------

This example program can be found in :guilabel:`JOB` → :guilabel:`SELECT JOB`, and allows executing robot camera :ref:`robot-camera-calibration`.

Define the tool for picking
~~~~~~~~~~~~~~~~~~~~~~~~~~~

When using Pickit it is important that **tool0** is set equal to the robot flange.
This is done by setting all the values of **tool0** to 0.

Set user frame
~~~~~~~~~~~~~~

To help us set the user frame we are going to use a **Position** variable, by default **P008**.
Set following values in :guilabel:`VARIABLE` → :guilabel:`POSITION(ROBOT)`:

- Select **BASE**.
- Make sure that **X**, **Y**, **Z**, **Rx**, **Ry** and **Rz** are all equal to **0**.

Here it is assumed that **P008** is not yet being used anywhere else in the robot program.
You can also use any other variable, as long as it is free.
In that case, make sure to fill this variable in, in the command **MFRAME UF#(5) P008 BF**.

After running the program, a new user frame **(5)** will be created that will be used both for calibration and picking.

Teach calibration points
~~~~~~~~~~~~~~~~~~~~~~~~

The calibration program requires five points to be defined.
For more information on how to define these points, see the article on :ref:`multi-poses-calibration`.

Execute the calibration program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before running the calibration program, make sure that the Pickit web interface is in the :guilabel:`Calibration` page, which provides feedback on calibration plate visibility and progress of the calibration process (:ref:`more <multi-poses-calibration-calibrating>`).
To run this program either do **Play + Start**, **Interlock + FWD** or **Interlock + Test**.

Example program: TEST_SIMPLEPICK
--------------------------------

This example program can be found in :guilabel:`JOB` → :guilabel:`SELECT JOB`.

The idea of the program is the following:

- First, a detection is triggered.
- If an object is found, the model and pick point ID is checked to know to where the robot will be guided to.
  According these ID's the robot moves to the object to pick it.
  Next he moves to a fixed drop off position, and finally he moves to a corrected drop off position.
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

Set variables used in TEST_SIMPLEPICK 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Variables used by the Pickit system
-----------------------------------

Below you find an overview of the variables used by Pickit.
When using Pickit these variables cannot be used for anything else.

+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Variable | Field name        | Comment                                                                                                                                  |
+==========+===================+==========================================================================================================================================+
| I049     | command           | A single command from robot to Pickit.                                                                                                   |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| I048     | setup             | A number matching to a setup file known by the Pickit system.                                                                            |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| I047     | product           | A number matching to a product file known by the Pickit system.                                                                          |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| I046     | Frame ID          | A number matching the frame ID used during calibration and picking.                                                                      |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| I045     | Tool ID           | A number matching the tool ID used for picking                                                                                           |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| I044     | Timeout           | Value of the timeout used for communication with Pickit                                                                                  |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| I041     | object_type       | The type of detected object.                                                                                                             |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| I040     | status            | Contains the Pickit status or a response to previously received robot commands.                                                          |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| I030-039 | status of cycles  | Used for keeping track of the communication cycle with Pickit.                                                                           |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| S049     | IP Pickit         | IP address of Pickit, by default 169.254.5.180.                                                                                          |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| P049     | object_pose       | An object pose expressed relatively to the robot base frame.                                                                             |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| P048     | object_dimension  | [0]: length or diameter (m) [1]: width or diameter (m) [2]: height (m)                                                                   |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| P047     | object_offset     | pick point offset of the last requested object                                                                                           |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| P046     | rx_flip           | A helper pose to calculate a correct offset pose                                                                                         |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| D042     | pick_ref_id       | ID of the selected pick point’s reference pick point                                                                                     |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| D041     | object_remaining  | If this field is non-zero, it contains the number of remaining objects that can be sent in next messages to the robot.                   |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| D040     | object_age        | The amount of time that has passed between the capturing of the camera data and the moment the object information is sent to the robot.  |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+

.. tip:: If these registers are already used on your robot, please contact us at `support@pickit3d.com <mailto:support@pickit3d.com>`__, and we will assist you in finding a solution.

.. toctree::
  :maxdepth: 1
  :hidden:

  manually-define-the-pickit-macros