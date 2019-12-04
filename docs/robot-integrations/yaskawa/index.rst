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

Pickit is compatible with controllers **FS100,** **DX200** and **YRC1000(Micro)**.

The following parameters must be declared on the controller to allow the correct operation of the application.
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
- For **FS100** controllers you need to connect the Pickit processor to the **CN2** port.
- For **YRC1000** controllers you need to connect the Pickit processor to the **CN106** or **CN107** port.

IP configuration
~~~~~~~~~~~~~~~~

.. warning::
  Before making these changes, the robot controller should be in **maintenance mode**, and the security mode should be **management mode**.

Setting the IP address of the robot controller should be done in **maintenance mode**.
Go to :guilabel:`SYSTEM` → :guilabel:`SETUP` → :guilabel:`OPTION FUNCTION` → :guilabel:`LAN interface setting` (or :guilabel:`Network` for DX200 and FS100) and set the following values:

  - **IP ADDRESS SETTING**: MANUAL SETTING
  - **IP ADDRESS:** 169.254.5.182
  - **SUBNET MASK:** 255.255.0.0
  - **DEFAULT GATEWAY:** 0.0.0.0

Press :guilabel:`ENTER` and :guilabel:`CONFIRM` to modify the values.

Load the program files
----------------------

Before starting, the Pickit folder should be copied to a USB pen drive. 
:ref:`Download the Pickit Yaskawa files here <downloads:Yaskawa>`.

The robot controller should still be in **maintenance mode** and the security mode set to **management mode** before making these changes.

#. Insert USB device in the robot pendant.
#. Load the correct USB device under :guilabel:`MotoPlus APL` → :guilabel:`DEVICE`.
#. Select the folder **Pickit** > **MotoPlus** on the USB device under :guilabel:`MotoPlus APL` → :guilabel:`FOLDER`.
#. Load the MotoPlus application under :guilabel:`MotoPlus APL` → :guilabel:`LOAD(USER APPLICATION)`. 

Press :guilabel:`Select`, :guilabel:`Enter` and confirm.
Now reboot the controller in **Normal mode** with USB device still attached.
After rebooting set security to **management mode**.

#. Load the correct USB device under :guilabel:`EX. MEMORY` → :guilabel:`DEVICE`.
#. Select the folder **Pickit** > **Program** on the USB device under :guilabel:`EX. MEMORY` → :guilabel:`FOLDER`.
#. Load the **I/O DATA**, **SYSTEM DATA** and  **JOB** files under :guilabel:`EX. MEMORY` → :guilabel:`LOAD` (the order of loading the files is important).

Define the Pickit macros
------------------------

Still in **normal mode**, the macros should be defined manually.
To do this go to :guilabel:`SYSTEM` → :guilabel:`SETUP` → :guilabel:`MACRO INST.`.

.. note:: In order to use the example Pickit files the macros should be defined in the exact same order as shown in the image below.

.. image:: /assets/images/robot-integrations/yaskawa/yaskawa-macro.jpg

Load the Pickit example jobs
----------------------------

In the Pickit folder there are two example jobs available.
These can be uploaded to the controller so you can get easily started with picking.

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

Test robot connection
---------------------

To start the communication, you can run **PIT_RUN** on the robot.
This job can be found in :guilabel:`JOB` → :guilabel:`SELECT MACRO JOB`.

When running the program, there should be an indication that the robot is connected in the Pickit web interface :ref:`web-interface-top-bar`.

Example program: TEST_CALIB
---------------------------

This example program can be found in :guilabel:`JOB` → :guilabel:`SELECT JOB`.

The program helps you by executing robot camera :ref:`robot-camera-calibration`.

Define tool
~~~~~~~~~~~

When using Pickit it is important that **tool0** is set equal to the robot flange.
This is done by setting all the values of **tool0** to 0.

Set user frame
~~~~~~~~~~~~~~

To help us set the user frame we are going to use a **Position** variable, by default **P008**.
Set following values in :guilabel:`VARIABLE` → :guilabel:`POSITION(ROBOT)`:

- Select **BASE**.
- Make sure that **X**, **Y**, **Z**, **Rx**, **Ry** and **Rz** are all equal to **0**.

Here it is assumed that **P008** is not yet being used somewhere else in the robot program.
Any other variable that is free should also be fine. 
If another variable is used make sure to fill it in, in the command **MFRAME UF#(5) P008 BF**.

After unning the program a new user frame **(5)** will be created that will be both be used for calibration and picking.

Teach calibration positions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the program 5 positions needs to be defined.
For more information on where to define the positions see the following article, :ref:`multi-poses-calibration`.

Execute robot program
~~~~~~~~~~~~~~~~~~~~~

After defining the positions, the Pickit must be set in calibration mode and the robot program can be executed.
To run this program either do **Play + Start**, **Interlock + FWD** or **Interlock + Test**.

Example program: TEST_SIMPLEPICK
--------------------------------

This example program can be found in :guilabel:`JOB` → :guilabel:`SELECT JOB`.

The idea of this program is the following.
First a detection is triggered.
If an object is found, the robot moves to the object to pick it and drop it off at a fixed position.
Once the robot is out the field of view of the robot, immediately a new Pickit detection is triggered.
If the ROI is empty the program stops.

Define tool
~~~~~~~~~~~

Create a tool frame with the actual TCP values.
Again it is important that **tool0** is not changed, any other tool can be used.

Set PIT_CFG
~~~~~~~~~~~

In this command following values have to be set:

- **Setup**: Pickit setup file number.
- **Product**: Pickit product file number.
- **User Frame**: User frame that was created in TEST_CALIB, by default this is **5**.
- **Tool**: Number of tool frame defined in previous step.

.. note:: If something is wrong here, you can expect the following message: Undefined user frame.
   The example program by default uses frame 5 and tool 1, but these might not exist. 

Set robot positions
~~~~~~~~~~~~~~~~~~~

- **C00000**: **Home position** starting position of the robot, this position needs to be defined by the user.
- **P025**: **Detect position** a position not blocking the camera to trigger a detection, this position needs to be defined by the user.
- **P023**: **Above pick area position** a transition position to enter the pick area, this position needs to be defined by the user.
- **LP000**: **Pre Picking position**, this position does not need to be defined.
- **P099**: **Picking position**, this position does not need to be defined.
- **LP001**: **Post pick position**, this position does not need to be defined.
- **P029**: **Drop off position** a position where the parts will be dropped, this position needs to be defined by the user.

Add grasping/releasing logic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At the **Picking position** and **Drop off position** grasping and releasing logic needs to be added.

Execute robot program
~~~~~~~~~~~~~~~~~~~~~

To run this program either do **Play + Start**, **Interlock + FWD** or **Interlock + Test**.
Enjoy your pickings!

Variables used by the Pickit system
-----------------------------------

+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Variable | Field name        | Comment                                                                                                                                  |
+==========+===================+==========================================================================================================================================+
| I099     | command           | A single command from robot to Pickit.                                                                                                   |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| I098     | setup             | A number matching to a setup file known by the Pickit system.                                                                            |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| I097     | product           | A number matching to a product file known by the Pickit system.                                                                          |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| I096     | Frame ID          | A number matching to the frame ID used during calibration and picking.                                                                   |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| I095     | Tool ID           | A number matching to the tool ID used for picking                                                                                        |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| I094     | Timeout           | Value of timeout that is used for communication with Pickit                                                                              |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| I091     | object_type       | The type of detected object.                                                                                                             |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| I090     | status            | Contains the Pickit status or a response to previously received robot commands.                                                          |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| I080-089 | status of cycles  | Used for keeping track of communication cycle with Pickit.                                                                               |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| S099     | IP Pickit         | IP address of Pickit, by default 169.254.5.180.                                                                                          |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| P099     | object_pose       | An object pose expressed relatively to the robot base frame.                                                                             |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| P098     | object_dimension  | [0]: length or diameter (m) [1]: width or diameter (m) [2]: height (m)                                                                   |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| D091     | object_remaining  |  If this field is non-zero, it contains the number of remaining objects that can be sent in next messages to the robot.                  |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| D090     | object_age        | The amount of time that has passed between the capturing of the camera data and the moment the object information is sent to the robot.  |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+

.. tip:: If these registers are already used on your robot. Please contact us at `support@pickit3d.com <mailto:support@pickit3d.com>`__ and we will assist you in finding a solution.
