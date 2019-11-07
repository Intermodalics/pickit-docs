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

Pickit is compatible with controllers **FS100,** **DX200** and **YRC1000**.

The following parameters must be declared on the controller to allow the correct operation of the application. These settings must be enabled by Yaskawa:

-  **Ethernet** function set to **1**
-  **MotoPlus** function set to **1**
-  **Macro** function set to **1**
-  **MotoPlus - Number of files** set to **1**
-  **MotoPlus - Number of tasks** set to **5**

Please contact your local Yaskawa affiliate if you need to connect multiple devices to the Ethernet port to check compatibility of all this equipment.

Setup the network connection
----------------------------

Hardware connection
~~~~~~~~~~~~~~~~~~~

The connection between the Yaskawa controller and Pickit is done over ethernet. You connect your robot controller to the **ROBOT** port on the Pickit processor as shown in the diagram below:

.. image:: /assets/images/robot-integrations/yaskawa/yaskawa.png

- For **DX200** controllers you need to connect the Pickit processor to the **CN104** port.
- For **FS100** controllers you need to connect the Pickit processor to the **CN2** port.

IP configuration
~~~~~~~~~~~~~~~~

.. warning::
  Before making these changes, the robot controller should be in **maintenance mode**, and the security mode should be **management mode**.

Setting the IP address of the robot controller should be done in **maintenance mode**.
Go to :guilabel:`SYSTEM` → :guilabel:`SETUP` → :guilabel:`OPTION FUNCTION` → :guilabel:`LAN interface setting` and set the following values:

  - **IP ADDRESS SETTING**: MANUAL SETTING
  - **IP ADDRESS:** 169.254.5.182
  - **SUBNET MASK:** 255.255.0.0
  - **DEFAULT GATEWAY:** 0.0.0.0

Press :guilabel:`ENTER` and :guilabel:`CONFIRM` to modify the values before rebooting the controller.

Setting the Pickit IP address on the robot controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After rebooting, the address of Pickit needs to be entered in a **String**. To do this:

  #. Start the robot controller in **normal mode**.
  #. Go to :guilabel:`Main menu` → :guilabel:`VARIABLE` → :guilabel:`STRING` → :guilabel:`S099`.
  #. Set **S099** to value **169.254.5.180**.

.. note:: There is no communication yet between the Pickit and the robot.
  So don't worry if the connection is not shown in the Pickit web interface :ref:`web-interface-top-bar`.
  The robot can be pinged from the Pickit web interface to check the IP settings. 
  Details on testing this connection can be found on: :ref:`test-robot-connection`.

Load the program files
----------------------

The robot controller should be in **maintenance mode** and the security mode set to **management mode** before making these changes.

Before starting, the Pickit folder should be copied to a USB pen drive. 
:ref:`Download the Pickit Yaskawa files here <downloads:Yaskawa>`.

#. Load the **JOB**, **I/O DATA** and **SYSTEM DATA** files under :guilabel:`EX. MEMORY` → :guilabel:`LOAD`.
#. Load the correct USB device under :guilabel:`MotoPlus APL` → :guilabel:`DEVICE`.
#. Open the folder where the MotoPlus application is stored
   under :guilabel:`MotoPlus APL` → :guilabel:`FOLDER`.
#. Load the MotoPlus application under :guilabel:`MotoPlus APL` → :guilabel:`LOAD(USER APPLICATION)`. 

Test robot connection
---------------------

To start the communication, you can run the **PIT_RUN JOB** on the robot.
When running the program, there should be an indication that the robot is connected in the Pickit web interface :ref:`web-interface-top-bar`.

Example program: TEST_PICKING
-----------------------------

Before running the program:

-  Create a user frame with the following coordinates: 0.0.0.0.0.0. This user frame corresponds to the robot frame.
-  Create a tool frame with the actual TCP values.

Use both these frames on line 3 of the Test_picking example file, i.e. change the values 5 and 1 to the numbers of the user frame and tool that you defined. 

.. note:: If something is wrong here, you can expect the following message: Undefined user frame.
   The example program by default uses frame 5 and tool 1, but these might not exist. 

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
| S099     | IP Pickit         | IP address of Pickit, by default 169.254.5.180.                                                                                          |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| P099     | object_pose       | An object pose expressed relatively to the robot base frame.                                                                             |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| D090     | object_age        | The amount of time that has passed between the capturing of the camera data and the moment the object information is sent to the robot.  |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| I091     | object_type       | The type of detected object.                                                                                                             |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| P098     | object_dimension  | [0]: length or diameter (m) [1]: width or diameter (m) [2]: height (m)                                                                   |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| D091     | object_remaining  |  If this field is non-zero, it contains the number of remaining objects that can be sent in next messages to the robot.                  |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| I090     | status            | Contains the Pickit status or a response to previously received robot commands.                                                          |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+