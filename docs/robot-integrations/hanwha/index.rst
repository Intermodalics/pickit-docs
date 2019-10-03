.. _hanwha:

Setting up Pickit with a Hanwha HCR robot
=========================================

The setup of Pickit with a Hanwha HCR robot consists of 4 steps:

.. contents::
    :backlinks: top
    :local:
    :depth: 1

Check controller and software compatibility
-------------------------------------------

Pickit is compatible with controllers as of version **2.001** and **Rodi 2.001 for socket communication** is required.

.. note::
   Socket communication is supported by Rodi 1.3 or higher versions but verified in Rodi 2.001.

Setup the network connection
----------------------------

Hardware connection
~~~~~~~~~~~~~~~~~~~

The Pickit processor has to be connected to the robot controller using
an Ethernet cable. 

This Ethernet cable should be plugged in:

- The **ROBOT** port of the Pickit processor; 
- The **EPC** network port of the HCR robot controller. The location of this port is shown in the pictures below.

.. image:: /assets/images/robot-integrations/hanwha/network-port-1.png

.. image:: /assets/images/robot-integrations/hanwha/network-port-2.png

.. warning::
    The Ethernet cable must be fastened by a cable clamp to prevent tension being applied to the RJ-45 connector, in case the Ethernet cable is pulled directly. This clamp is also used to ground the cable shield.

IP configuration
~~~~~~~~~~~~~~~~

To allow communication between Pickit and the HCR controller both must have an IP address in the same subnet.

By default, the Pickit ROBOT connection (the Ethernet port on the Pickit processor labeled ROBOT) is configured to have the following static IP address:  **169.254.5.180** with a subnet mask of **255.255.0.0**. 

Set the IP address of the controller preferably to **169.254.5.182** which is an IP address in the same subnet as the Pickit IP and set the subnet mask to **255.255.255.0** via :guilabel:`SW Configuration` → :guilabel:`Network Setting`:

.. image:: /assets/images/robot-integrations/hanwha/network-settings-1.png

.. image:: /assets/images/robot-integrations/hanwha/network-settings-2.png

 
Load example program
--------------------

Loading the example program file called `HCR_Pickit_Example.file` for a HCR robot consists calibration step and detection test. The example program contains calibration step and detection step. 

:ref:`Download the Pickit Hanwha HCR files <downloads:Hanwha>`

Define data
~~~~~~~~~~~

The command message from robot to Pickit is below. Details on the low-level socket communication can be found on: :ref:`socket-communication`.


+----------------------------+------------------------------------------------+
| **robot_to_pickit_data**   | **HCR data**                                   |
+----------------------------+------------------------------------------------+
| actual_pose[7]             | x, y, z, rz, ry, rx, 0                         |
+----------------------------+------------------------------------------------+
| command                    | Following Pickit command (RC_PICKIT_XXXX)      |
+----------------------------+------------------------------------------------+
| setup                      | 15                                             |
+----------------------------+------------------------------------------------+
| product                    | 22                                             |
+----------------------------+------------------------------------------------+
| meta.robot_type            | 5                                              |
+----------------------------+------------------------------------------------+
| meta.interface_version     | 11                                             |
+----------------------------+------------------------------------------------+

Calibration step
~~~~~~~~~~~~~~~~

In calibration step, following steps are included.

    1. Set calibration count: `calCount` is number for calibration pose 1 ~ 5.
    2. Move to calibration pose: Define 5 position for calibration. Details on defining calibration pose can be found on : :ref:`multi-poses-calibration`
    3. Send current pose to Pickit server. In this script, socket communication is used. Define Pickit server information to SERVER_INFO, and send the message using ‘socketSendInteger’ function. See details in `HCR_Pickit_Calibration.script`.

Detection step
~~~~~~~~~~~~~~

In detection step, connection is same with calibration step, just change the command to Pickit as RC_PICKIT_LOOK_FOR_OBJECTS. See details in `HCR_Pickit_Detection.script`.

Test robot connection on Pickit
--------------------------------

Details on testing this connection can be found on: :ref:`test-robot-connection`