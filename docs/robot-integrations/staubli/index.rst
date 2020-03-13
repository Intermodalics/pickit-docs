.. _staubli:

Setting up Pickit with Stäubli
===============================

The setup of **Pickit** with a **Stäubli** consists of **4 steps**:

.. contents::
    :backlinks: top
    :local:
    :depth: 1

Check Stäubli software version
------------------------------

The software version should be at least 7.

To verify this go to :guilabel:`MENU` > :guilabel:`CONTROL PANEL` > :guilabel:`CONTROLLER CONFIGURATION` > :guilabel:`VERSION`.

.. image:: /assets/images/robot-integrations/staubli/staubli-step-1.png

.. image:: /assets/images/robot-integrations/staubli/staubli-step-2.png

Setup the network connection
----------------------------

Hardware connection
~~~~~~~~~~~~~~~~~~~

The Pickit processor has to be connected to the robot controller using an Ethernet cable. 

This Ethernet cable should be plugged in:

- The **ROBOT** port of the **Pickit processor**; 
- The **robot controller**.

IP configuration
^^^^^^^^^^^^^^^^

To allow communication between Pickit and the robot controller both must have a different IP address in the same subnet.

By default, the Ethernet port on the Pickit processor labeled ROBOT is configured to have the following static IP address: **169.254.5.180** with a subnet mask of **255.255.0.0**.

If this setting is kept, the following has to be done on the robot controller:

For the **CS8 controller**, go to :guilabel:`MENU` > :guilabel:`CONTROL PANEL` > :guilabel:`CONTROLLER CONFIGURATION` > :guilabel:`NETWORK` > :guilabel:`J204 or J205`.

For the **CS9 controller** this can be found in :guilabel:`HOME` > :guilabel:`SETTINGS` > :guilabel:`NETWORK` > :guilabel:`J204 or J205`.

- Set the IP address of the robot to **169.254.5.182** which is an IP address in the same subnet as the Pickit IP address.
- Set the subnet mask to **255.255.0.0**.

Push Enter to edit. Push :guilabel:`F8` OK.

The IP address of the robot can of course not be the same as the IP address of the Pickit processor.

.. image:: /assets/images/robot-integrations/staubli/staubli-step-3.png

Setup socket
^^^^^^^^^^^^

For the **CS8 controller**, go to :guilabel:`MENU` > :guilabel:`CONTROL PANEL` > :guilabel:`IO` > :guilabel:`SOCKETS` > :guilabel:`TCP CLIENTS` > :guilabel:`NEW`.

For the **CS9 controller** this can be found in :guilabel:`HOME` > :guilabel:`IO` > :guilabel:`SOCKETS` > :guilabel:`TCP CLIENTS` > :guilabel:`+`.

- Choose Type: Client
- Add name: **pickit**
- Add the Pickit IP address

  - IP: **169.254.5.180**
  - Port: **5001**

.. image:: /assets/images/robot-integrations/staubli/staubli-step-4.png

.. image:: /assets/images/robot-integrations/staubli/staubli-step-5.png

You can test the new socket connection by pushing the :guilabel:`Test` button.

Load the program files
----------------------

Loading the program files consists of 4 steps:

.. contents::
    :backlinks: top
    :local:
    :depth: 1

Download the right files
~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`Download the Pickit Stäubli files <downloads_staubli>`

Upload the files to the robot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Upload these files using SRS.

.. image:: /assets/images/robot-integrations/staubli/staubli-step-6.png

Start and verify communication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Starting and verifying communication consists of 2 steps:

.. contents::
    :backlinks: top
    :local:
    :depth: 1

Start communication
^^^^^^^^^^^^^^^^^^^

To start the communication, on the robot you have to select a Pickit example program. You can test this by using the *OpenComm* program. 

Verify on the Pickit interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To verify the data packages are received by Pickit: Check for the 
**V** icon next to 'Robot' in the top bar of the Pickit interface.

Test robot connection on Pickit
--------------------------------

Details on testing this connection can be found on: :ref:`test-robot-connection`
