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
   The robot controller should be in **maintenance mode** and the security mode to **management mode** before making these changes.

Setting the IP address of the robot controller happens in **maintenance mode** and can be done under :guilabel:`SYSTEM` → :guilabel:`SETUP` → :guilabel:`OPTION FUNCTION` → :guilabel:`LAN interface setting` and set the following values:

  - **IP ADDRESS SETTING**: MANUAL SETTING
  - **IP ADDRESS:** 169.254.5.182
  - **SUBNET MASK:** 255.255.0.0
  - **DEFAULT GATEWAY:** 0.0.0.0

Press :guilabel:`ENTER` and :guilabel:`CONFIRM` to modify the values before rebooting the controller.

Setting the Pickit IP address on the robot controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After rebooting the address of Pickit needs to be entered in a **String**. To do this:

  #. Start the robot controller in **normal mode**
  #. Go to :guilabel:`Main menu` → :guilabel:`VARIABLE` → :guilabel:`STRING` → :guilabel:`S099`.
  #. Set **S099** to value **169.254.5.180**

.. note:: There is no communication yet between the Pickit and the robot.
  So don't worry if the connection is not shown in the Pickit web interface :ref:`web-interface-top-bar`.
  The robot be pinged from the Pickit web interface to check the IP settings. 
  Details on testing this connection can be found on: :ref:`test-robot-connection`.

Load the program files
----------------------

The robot controller should be maintenance mode and the security mode to management mode before making these changes.

Before starting, the Pickit folder should be placed on a USB dongle. 
:ref:`Download the Pickit Yaskawa files here <downloads:Yaskawa>`.

#. Load the **JOB**, **I/O DATA** and **SYSTEM DATA** files under :guilabel:`EX. MEMORY` → :guilabel:`LOAD`.
#. Load the correct USB device under :guilabel:`MotoPlus APL` → :guilabel:`DEVICE`.
#. Open the correct folder where the MotoPlus application is stored
   under :guilabel:`MotoPlus APL` → :guilabel:`FOLDER`.
#. Load the MotoPlus application under :guilabel:`MotoPlus APL` → :guilabel:`LOAD(USER APPLICATION)`. 

Test robot connection
---------------------

To start the communication, on the robot you can run the **PIT_RUN JOB**.
When running the program, connection should be shown in the Pickit web interface :ref:`web-interface-top-bar`.