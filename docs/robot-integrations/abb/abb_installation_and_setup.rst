.. _abb-installation-and-setup:

ABB installation and setup
==========================

The setup of Pickit with an ABB robot consists of 4 steps:

.. contents::
    :backlinks: top
    :local:
    :depth: 1

Check controller and software compatibility
-------------------------------------------

Pickit is compatible with controllers as of version IRC5 with RobotWare 5 or 6 and furthermore. To communicate with Pickit, the following controller modules need to be installed:

- 616 PC interface
- 623-1 Multitasking

To check this compatibility, open RobotStudio and follow the next steps:

.. image:: /assets/images/robot-integrations/abb/abb-check-compatibility-step-1.jpg
    :width: 550

.. image:: /assets/images/robot-integrations/abb/abb-check-compatibility-step-2.jpg
    :width: 550

.. image:: /assets/images/robot-integrations/abb/abb-check-compatibility-step-3.jpg
    :width: 550

If you don't have the right software version or module please contact
your local ABB distributor.

Setup the network connection
----------------------------

Hardware connection
~~~~~~~~~~~~~~~~~~~

The Pickit processor has to be connected to the robot controller using
an Ethernet cable. 

This Ethernet cable should be plugged in:

- The **ROBOT** port of the Pickit processor; 
- The **WAN** port of the robot controller.

IP configuration
~~~~~~~~~~~~~~~~

Open RobotStudio and follow the next steps:

.. image:: /assets/images/robot-integrations/abb/abb-ip-configuration-step-1.jpg
    :width: 550

.. image:: /assets/images/robot-integrations/abb/abb-ip-configuration-step-2.jpg

Set the IP address of the controller preferably to **169.254.5.182** which is an IP address in the same subnet as the Pickit IP and set the subnet mask to **255.255.0.0**.

The IP address of the robot can not be the same as the IP address of Pickit.

After these steps restart from the Flex pendant (assuming you have no write access yet).

.. image:: /assets/images/robot-integrations/abb/abb-ip-configuration-step-3.jpg
    :width: 550

Load the program files
----------------------

Download the right files
~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`Download the Pickit ABB files <downloads_abb>`

Upload the files to the robot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Upload these files using File Transfer.

.. image:: /assets/images/robot-integrations/abb/abb-load-program-files-step-1.jpg
    :width: 550
    :alt: Request write access

-  Manual mode: press 'Grant' on the Flex pendant
-  Automatic mode: not necessary

.. image:: /assets/images/robot-integrations/abb/abb-load-program-files-step-2.jpg
    :width: 550
    :alt: Grant write access on the Flex pendant

Load parameters from controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /assets/images/robot-integrations/abb/abb-load-program-files-step-3.jpg
    :width: 550
    :alt: Load parameters from controller

-  For an ABB controller with RobotWare 5 select the **Pickit SYS RW5.cfg** file.
-  For an ABB controller with RobotWare 6 select the **Pickit SYS RW6.cfg** file.
-  For the ABB YuMi, select the **Pickit SYS YuMi.cfg** file.

This will load the required system modules in corresponding tasks.

.. image:: /assets/images/robot-integrations/abb/abb-load-program-files-step-4.jpg
    :width: 550
    :alt: Select Pickit SYS.cfg

Restart the controller.

.. image:: /assets/images/robot-integrations/abb/abb-load-program-files-step-5.jpg
    :alt: Restart the controller

Test robot connection with Pickit
---------------------------------

Details on testing this connection can be found on: :ref:`test-robot-connection`