.. _connecting-the-cables:

Connecting the cables
=====================

.. contents::
    :backlinks: top
    :local:
    :depth: 1

Connect the power cable
~~~~~~~~~~~~~~~~~~~~~~~

The **Pickit processor** has a built-in power supply and needs to be
connected to the power outlet with the provided cable. The Pickit
processor will automatically boot once it's powered.

The Pickit processor can be shut down by pressing the power button
once. The power button is positioned behind the front lid. Powering it
again can be done by pressing the same power button once.

.. note::
  In case the Pickit processor is on and there is a power failure, it
  will restart automatically when power is restored. Pickit will start
  with robot mode enabled.

Connect the camera
~~~~~~~~~~~~~~~~~~

While the M and L cameras do not require a power supply, the M-HD camera
does. The connection steps for both types of cameras are indicated below.

M or L camera
^^^^^^^^^^^^^

Connect the Pickit M or L camera with the 10 m USB cable (CBL-USB-CAM-10) that
is provided with Pickit and plug it into the **CAMERA** labeled USB
port at the back side of the Pickit processor.

When the Pickit camera is connected correctly, there will be a
continuous green light on the front of the Pickit camera. This
indicates that the Pickit camera is operational.

M-HD camera
^^^^^^^^^^^

Connect the power and data cables to the M-HD camera, in the corresponding
connectors. Ensure that all connections are screwed tightly in. Plug the USB cable to the Pickit processor, in the **CAMERA** port.
To power the camera, connect the power chord to the power supply, and plug
the other end to a power outlet. The camera fan should immediately start
spinning.

.. important::
   A USB hub is not allowed between the Pickit processor and any of the Pickit
   cameras.

.. warning::
   When using the optical extension cables provided by Pickit, make sure that these are paired with the provided shorter, 0.5m, copper cable (blue).

.. _connect-computer:

Connect a computer
~~~~~~~~~~~~~~~~~~

Interaction with Pickit is done by accessing its
:ref:`web interface <web-interface>` from an external computer.
This is required only during the setup and configuration of your application.
Once Pickit is in :Ref:`Robot Mode <web-interface-top-bar>`, the connection
with an external computer is no longer required.

There are two ways to connect your Pickit processor to a computer and access the
web interface:
You can connect the two systems directly with an Ethernet cable, or connect them
through your network. You can use the provided gray/black 5 m UTP network cable
(CBL-CAT6-GRAY-5 / CBL-CAT6-BLACK-5) for this.
The following describes each alternative in detail.

.. _connect-computer-directly:

Connecting a computer directly
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is the most common way to connect to Pickit.
Connect a computer to the **YOUR PC** labeled RJ45 port on the Pickit
processor. Your computer will be assigned an IP address by the Pickit
processor. Once connected you can access the Pickit web interface by pointing
a :ref:`supported web browser <supported-browsers>` to the following URL:

`http://192.168.66.1 <http://192.168.66.1/>`__

.. _connect-computer-network:

Connecting a computer using a network
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Connect the Pickit processor to a network with the **LAN** labeled RJ45
port and connect it to your router or switch. An IP address will be
assigned using the DHCP server of your network. You can now connect to
the Pickit web interface by navigating to this IP address.

Alternatively, you can assign a fixed IP to the Pickit processor. For this, you
first need to :ref:`connect a computer directly <connect-computer-directly>` to
configure the fixed IP (see :ref:`here <pickit-port-lan>` for more details).

Connect the robot or machine controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using the provided green 5 m UTP network cable (CBL-CAT6-GREEN-5) connect
your robot or machine controller with the **ROBOT** labeled RJ45 port at
the back side of the Pickit processor.

Instructions on the network configuration can be found on the robot
brand specific instruction pages:

-  :ref:`abb`
-  :ref:`fanuc`
-  :ref:`kuka`
-  :ref:`staubli`
-  :ref:`universal-robots`
-  :ref:`yaskawa`

.. tip:: This step is not necessary to already start testing the Pickit system.
