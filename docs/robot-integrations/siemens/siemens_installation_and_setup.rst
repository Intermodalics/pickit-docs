.. _siemens_installation_and_setup:

Siemens installation and setup
==================================

This setup manual guides you through the setup between Pickit and a Siemens PLC. The setup consists of the following steps:

.. contents::
    :backlinks: top
    :local:
    :depth: 1

Before starting, :ref:`download the Pickit Siemens source code (.scl) here <downloads_siemens>`.

.. note:: Pickit is compatible with the Siemens **S7-12XX-X PN** and **S7-15XX-X PN** CPUs. The CPUs must have a Profinet interface/network socket onboard (**PN**-notation). The provided source code is built and compiled by **TIA Portal version 15**. This version and upwards are compatible.

Setting up the connection
~~~~~~~~~~~~~~~~~~~~~~~~~

Pickit communcates with other devices over the TCP/IP version 4 protocol. The advised setup connects the PLC directly to Pickit by the designated port. Connect the network cable between the **ROBOT** port on the Pickit processor and the desired **Profinet (PN)** socket on the PLC. It is possible to use a router between the Pickit and PC/PLC for uploading the TIA project onto the PLC. But again, it is advised to use a direct connection in production mode. When using a router for uploading, please enable this setting into the device properties in TIA Portal.

In the Pickit settings, navigate to :ref:`"ROBOT" port settings <settings-network-robot>` and set the desired IP address for the Pickit system. The default value for the IP addess and subnet mask are ``169.254.5.180`` and ``255.255.0.0``.

.. warning:: The **LAN** port on the Pickit system uses the address range ``192.168.XXX.XXX`` by default. That means that the **ROBOT** port can only be configured within this address range when the **LAN** port is set for an alternative range first.

.. _tia_portal_configuration:

The TIA Portal configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In a new or active TIA Portal project under *Project tree*, add the desired CPU by selecting *Add new device*. Navigate in the device tree to *External source files*. Upload the corresponding source file ``pickit_3d_comm_v1.1.scl`` here. Next, right-click on the source file and select *Generate blocks from source*. The Pickit blocks will now be available in the device program under *Program blocks*. In total, two blocks will appear:

1. The Pickit communication **Function Block (FB)** "*Pickit_3D_communication*" (required).
2. The Pickit robot command **Function (FC)** "*Pickit_3D_robot_commands*" (optional).

.. note:: In case TIA portal outputs an error when generating the blocks, please contact support.

Add the communication function block into an empty network in **Main (OB1)**. TIA Portal will request generate an appurtenant **Data Block (DB)**. Next, in the *Device configuration* under the *Ethernet addresses* section, change the IP address and subnet mask of the corresponding Profinet port to the desired values. The default values are respectively ``169.254.5.182`` and ``255.255.0.0``.

.. note:: It is **not** mandatory to add an *unspecified* device into the hardware configuration manually to represent the Pickit system.

Verify the connection
~~~~~~~~~~~~~~~~~~~~~

Once the block is inserted into **OB1** we can verify that the communication is working. Firstly, compile the project and upload it to the CPU such that it has the correct IP address configured. Now inside the Pickit software in settings, navigate to :ref:`"ROBOT" Check robot IP connection` and enter the IP address of the robot. By pressing the *check*-button you are executing a ping from the Pickit processor.

.. note:: If the ping is unsuccessful, validate the IP address settings on both the Pickit and the PLC.

After a successful ping from Pickit to the CPU, we can establish the socket communication. After uploading the entire project to the PLC, it will try to establish a connection immediately based on the IP address entered in the Pickit communication **Data Block (DB)**. The default value is ``169.254.5.180`` and the remote port value is ``5001`` (fixed). Pickit will show the connection checkmark in the UI when there is a connection established. You can also validate the initial handshake request that has been sent out by the PLC which can be seen under :ref:`"LOGS" Log raw data from robot`. This initial handshake is a ``rc_pickit_check_mode()`` command, the actual mode of Pickit is not of importance (robot, idle or calibration mode).

.. note:: When connecting or switching network cables **after** powering on the PLC, the block will fault as no connection could be made. When you need to switch cables when uploading through a router you can memory reset the PLC ``MRES`` (cold start).
