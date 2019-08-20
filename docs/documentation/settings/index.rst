.. _Settings:

Settings
========

.. contents::
    :backlinks: top
    :local:
    :depth: 1

User settings
-------------

Units
~~~~~

.. image:: /assets/images/Documentation/settings-units.png

This setting allows you to select the length unit of choice
(meters, inches, ...) after which length values in the interface
will be converted to the newly selected unit.

Automatic detections
~~~~~~~~~~~~~~~~~~~~

.. image:: /assets/images/Documentation/settings-automatic-detections.png

Share usage statistics
~~~~~~~~~~~~~~~~~~~~~~

.. image:: /assets/images/Documentation/settings-usage-statistics.png

This aggregated data can be used to help create features that
can give you a better understanding of what’s happening across your
entire application.

You benefit when this setting is ON because this data could be used to
help build better tools and provide guidance that can help you analyze
your application. Application data lets you know where you stand in your
application and it’s performance and may uncover important trends or
problems.

Network settings
----------------

Pickit port labeled ROBOT
~~~~~~~~~~~~~~~~~~~~~~~~~~

This port has the purpose of connecting your Pickit processor to the
robot controller or PLC.

.. image:: /assets/images/Documentation/settings-port-your-robot.png

By default, this port is set to Static, which means it's using a fixed IP
configuration.
You can set the following IP Configuration options:

-  IP Address (Default value: 169.254.5.180)
-  Subnet mask (Default value: 255.255.0.0)
-  Gateway

If you prefer to get an IP Address from a DHCP server, you set this port
to Dynamic. 

.. _test-robot-connection:

Testing the Robot to Pickit connection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can check if the IP address of the robot or PLC is reachable from the
Pickit processor by entering its IP address in the **Robot IP** field and
pressing :guilabel:`Check`.

A pop-up message indicating failure or success appears on the lower right corner
of the screen.

.. image:: /assets/images/Documentation/pickit-robot-connection.png
   :scale: 70%

.. note:: In case of failure, check if the cables are
  :ref:`properly connected <connecting-the-cables>` and whether the IP assigned
  to the robot during its IP configuration step matches the tested one.

.. _pickit-port-lan:

Pickit port labeled LAN
~~~~~~~~~~~~~~~~~~~~~~~~

This port has the purpose of connecting your Pickit processor to a
network, to bring the system online for remote support (see article :ref:`support-remote-service`). 

.. image:: /assets/images/Documentation/settings-port-lan.png

By default, this port is set to Dynamic, which means it's
requesting an IP address from the DHCP server in your network.

If you prefer to set a Static IP, you can set the following IP
Configuration options:

-  IP Address
-  Subnet mask
-  Gateway

Test connectivity to the internet by pressing the Check button.

Upgrade Pickit version
~~~~~~~~~~~~~~~~~~~~~~

.. image:: /assets/images/Documentation/upgrade_pickit_2.1.2.png

Here you can upgrade your Pickit system to latest software version.
Refer to the :ref:`Pickit-system-software-upgrade`
for a step-by-step explanation how to upgrade the software on your
system.

System commands
~~~~~~~~~~~~~~~

.. image:: /assets/images/Documentation/settings-system-commands.png

Here you can **reboot** or **power off** the Pickit processor.
