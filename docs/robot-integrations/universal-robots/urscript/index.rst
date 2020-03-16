.. _universal-robots-scripts:

URScript legacy interface
=========================

.. attention::
   This article describes the legacy way of using Pickit with a Universal Robots. For new systems, please use the :ref:`universal-robots-urcap` plugin instead.

The setup of **Pickit** with a **Universal** **robot** consists of **3 steps**:

.. contents::
    :backlinks: top
    :local:
    :depth: 1

Setup the network connection
----------------------------

Hardware connection
~~~~~~~~~~~~~~~~~~~

The Pickit processor has to be connected to the Universal Robots controller using an Ethernet cable. 

This Ethernet cable should be plugged in:

- The **ROBOT** port of the **Pickit processor**; 
- The **Internet & MODBUS** port of the **UR controller**.

IP configuration
~~~~~~~~~~~~~~~~

To allow communication between Pickit and the Universal Robots controller both must have an IP address in the same subnet.

By default, the Ethernet port on the Pickit processor labeled **ROBOT** is configured to have the following static IP address: **169.254.5.180** with a subnet mask of **255.255.0.0**.

If this setting is kept, the following has to be done on the Universal Robots controller via :guilabel:`Setup Robot` > :guilabel:`Setup Network`: 

- **Disable DHCP** to obtain a static IP
- Set the IP address of the robot to **169.254.5.182** which is an IP address in the same subnet as the Pickit IP
- Set the subnet mask to **255.255.0.0**;
- Click :guilabel:`Apply`.

The IP address of the robot **can not** be the same as the IP address of Pickit.

.. image:: /assets/images/robot-integrations/ur/urscript-step-1.png

.. note:: Default gateway and DNS servers can stay untouched. 

Test robot connection
~~~~~~~~~~~~~~~~~~~~~

Details on testing this connection can be found on: :ref:`test-robot-connection`.

Load the program files
---------------------------

Loading the program files for a Universal Robots consists of the following steps:

.. contents::
    :backlinks: top
    :local:
    :depth: 1

Download the right files
~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`Download the URScript files <downloads_ur>`

Once unpacked, the UR_Pickit folder contains the following files:

- ``pickit_communication``: This program is responsible for the low level communication between Pickit and the robot.
- ``pickit_functions``: This program defines basic Pickit functions that allow taking Pickit actions via the robot controller.
- ``pickit_transformations``: This program is responsible for computing the transform of the robot’s end-effector with respect to the reference frame.
- ``urmagic_upload_programs.sh``: This program takes care of the automatic uploading of all Pickit related files to the UR controller.

The UR_Pickit folder also contains a few folders, each one corresponding to a different **Polyscope** software version, containing robot programs that use the mentioned ASCII files.
A list of available functions can be found here:

.. toctree::
    :maxdepth: 1
    :glob:

    the_pickit_functions_cheat_sheet

.. warning::
    Modifying **pickit\_communication**, **pickit\_functions** or **Pickit\_transformations** should only be considered after talking to a **Pickit support engineer**. 

Upload the files to the robot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to upload these files onto the robot controller, a USB pendrive containing these files has to be used.

#. **Copy all files** inside the UR_Pickit folder to the root of the
   USB pendrive
#. **Insert the USB pendrive** into the USB port of the robot controller
   screen
#. A red **“USB”** sign appears in the interface, indicating that **the upload is in progress**. At this moment, all files with extension ``.urp``, ``.txt``, ``.script``, ``.installation`` and ``.variables`` are copied to the /programs folder in the original subfolders. 
#. After the upload is complete, **a green “USB” sign shows up**.

Start and verify communication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Starting and verifying communication consists of 3 steps:

.. contents::
    :backlinks: top
    :local:
    :depth: 1

Start communication
~~~~~~~~~~~~~~~~~~~

To start the communication, on the robot you have to select a Pickit example program which contains the Script instructions for Pickit in the **BeforeStart** section. You can see an example in the Robot_camera_calibration program:

.. image:: /assets/images/robot-integrations/ur/urscript-step-2.png

Press :guilabel:`Play` on the Universal Robots interface, and communication will start. Communication will stop again once the current robot program stops.

Verify on the Pickit interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To verify the data packages are received by Pickit: Check for the **V** icon next to 'Robot' in the top bar of the Pickit interface.

Test robot connection on Pickit
--------------------------------

Details on testing this connection can be found on: :ref:`test-robot-connection`

Example program
---------------

.. toctree::
    :hidden:
    :maxdepth: 1
    :glob:

    universal_robots_example_program

A :ref:`Universal Robots example program <universal-robots-scripts-example-program>` article provides a detailed description of a robto program using the Pickit scripting commands.
