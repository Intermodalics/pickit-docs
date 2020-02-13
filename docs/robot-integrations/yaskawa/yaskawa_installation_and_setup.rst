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

.. toctree::
  :maxdepth: 1
  :hidden:

  manually-define-the-pickit-macros