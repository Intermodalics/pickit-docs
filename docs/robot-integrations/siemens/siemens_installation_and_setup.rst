.. _siemens_installation_and_setup:

Siemens installation and setup
==================================

This setup manual guides you through the setup between Pickit and a Siemens PLC. The setup consists of the following steps:

.. contents::
    :backlinks: top
    :local:
    :depth: 1

Before starting, :ref:`download the Pickit Siemens source code (.scl) here <downloads_siemens>`.

.. note:: Pickit is compatible with the Siemens **S7-12XX-X PN** and **S7-15XX-X PN** CPUs with a Profinet interface. The provided source code is supported by **TIA Portal version 15** and higher.

Setting up the connection
~~~~~~~~~~~~~~~~~~~~~~~~~

Pickit communcates with other devices over the TCP/IP version 4 protocol. The advised setup connects the PLC directly to Pickit by the designated port. To do this, connect a network cable between the **ROBOT** port on the Pickit processor and the desired **Profinet (PN)** socket on the PLC. It is possible to use a router between the Pickit and PC/PLC for uploading the project onto the PLC. But again, it is advised to use a direct connection in production mode. When using a router for uploading, please enable this setting into the device properties in TIA Portal.

In the Pickit settings, navigate to *Pickit port labeled "ROBOT"* and set the desired IP address for the Pickit system. The default values for the IP addess and subnet mask are ``169.254.5.180`` and ``255.255.0.0``.

.. warning:: The **LAN** port on the Pickit system uses the address range ``192.168.XXX.XXX`` by default. That means that the **ROBOT** port can only be configured within this address range when the **LAN** port is set for an alternative range.

.. _tia_portal_configuration:

The TIA Portal configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In a new or active TIA Portal project under *Project tree*, add the desired CPU by selecting *Add new device*. Navigate in the device tree to *External source files*. Upload the correcponding source file ``.scl`` here. Now, right-click on the source file and select *Generate blocks from source*. The Pickit blocks will now be available in the device program.

1. The Pickit communication **Function Block (FB)** "*Pickit_3D_communication*" (required).
2. The Pickit robot command **Function (FC)** "*Pickit_3D_robot_commands*" (optional).

Add the communication function block into an empty network in **Main (OB1)**. TIA Portal will immediately allocate memory by generating a coupled **Data Block (DB)**. Now, in the *Device configuration* under the *Ethernet addresses* section, change the IP address and subnet mask of the corresponding Profinet port to the desired values. The default values are respectively ``169.254.5.182`` and ``255.255.0.0``.

.. note:: It is **not** mandatory to add an *unspecified* device into the hardware configuration to represent the Pickit system.

