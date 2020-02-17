.. _universal-robots-urcap-installation-polyscope-3:

URCap installation and setup - Polyscope 3
==========================================

This article explains how to install the Pickit URCap plugin in **Polyscope verison 3**.
The main installation and setup article, based on **Polyscope 5** can be found :ref:`here <universal-robots-urcap-installation>`.

Installing the Pickit URCap plugin
----------------------------------

To install the Pickit URCap plugin, follow these steps:

#. :ref:`Download the Pickit URCap archive <downloads_ur>`.
#. Unzip the archive and copy its contents to an **empty** USB drive.
#. Insert the drive into the USB port of either the robot controller or the teach pendant while it is turned on.
#. On the Polyscope home screen, press :guilabel:`Setup Robot` > :guilabel:`URCaps` to entery the **URCaps** section.

   .. image:: /assets/images/robot-integrations/ur/urcap-installation-3.png
    :align: center

#. If there's a previous installation of the Pickit URCap plugin (appears listed under ``Active UCaps``), it should be removed by selecting it and pressing :guilabel:`-`. Polyscope will indicate that a restart is needed, but there is no need to do it yet.

#. Press :guilabel:`+` to install a new URCap: navigate to the USB drive, and select the ``pickit_urcap-[version].urcap`` file.

#. Polyscope will indicate that a restart is needed for the changes to take effect. Press the :guilabel:`Restart` button to continue.

    .. image:: /assets/images/robot-integrations/ur/urcap-installation-6.png
      :align: center

#. Once Polyscope restarts, the plugin will be deployed and ready to use. Make sure your Pickit system is running and connected to the robot’s network to continue.

Connect to a running Pickit system
----------------------------------

From the main screen, go to :guilabel:`Program Robot` and select the :guilabel:`Installation` tab. The configuration screen of the Pickit plugin is accessible by selecting **Pickit** on the left panel.

.. image:: /assets/images/robot-integrations/ur/urcap-installation-7.png

.. image:: /assets/images/robot-integrations/ur/urcap-installation-8.png

#. Make sure that ``Enable Pickit plugin`` is checked.
#. Set the **IP address** and **hostname** of the Pickit system if you know them. Otherwise leave the default values.
#. Click :guilabel:`Find connected Pickit systems`. If the supplied IP and hostname are not correct, the URCap will search for a running Pickit systems in the network and populate the fields for you.

As long as the connection to Pickit has not been established, the status indicator at the lower left looks like this:

.. image:: /assets/images/robot-integrations/ur/urcap-installation-status-disconnected.png

Establishing the connection to Pickit can take a few seconds, and while this takes place, the status indicator displays:

.. image:: /assets/images/robot-integrations/ur/urcap-installation-status-connecting.png

When the connection to the Pickit system is successful, the status indicator at the lower left should look like this:

.. image:: /assets/images/robot-integrations/ur/urcap-installation-status-connected.png

If you plan to run robot programs that don't use Pickit, you should **disable** (not uninstall) the Pickit URCap plugin, by unchecking the ``Enable Pickit plugin`` checkbox in the plugin's installation screen.

You can now continue with the main :ref:`URCap installation and setup article <universal-robots-urcap-perform-calibration>`.