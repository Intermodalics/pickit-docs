.. _universal-robots-urcap-installation:

URCap installation and setup
============================

Pickit integrates seamlessly with **Universal Robots** by means of a **URCap plugin**.
This plugin allows to perform vision-guided pick and place with *minimal* programming effort.
It offers functionality to:

- Connect to a Pickit system.
- Perform robot-camera calibration.
- Create pick and place robot programs.

This article explains how to install the Pickit URCap plugin.

Pre-requisites
--------------

Verify that you meet the :ref:`minimum required versions <downloads_ur>` for Pickit and Polyscope.

The **Pickit version** can be verified in the :ref:`top bar <web-interface-top-bar>`
of the web interface.

.. image:: /assets/images/robot-integrations/ur/urcap-installation-pickit-version.png
  :align: center

.. include:: ../../upgrade_pickit_tip.rst

The **Polyscope version** can be verified by opening the **hamburger menu** at the upper-right corner and selecting :guilabel:`About`.

.. image:: /assets/images/robot-integrations/ur/urcap-installation-polyscope-version.png
  :scale: 80%
  :align: center

Installing the Pickit URCap plugin
----------------------------------

.. toctree::
  :glob:
  :maxdepth: 1
  :hidden:

  installation_polyscope_3.rst

.. note::
  This article contains the installation instructions for **Polyscope 5**.
  If using **Polyscope 3**, you can refer to :ref:`this article <universal-robots-urcap-installation-polyscope-3>`.

To install the Pickit URCap plugin, follow these steps:

#. :ref:`Download the Pickit URCap archive <downloads_ur>`.
#. Unzip the archive and copy its contents to an **empty** USB drive.
#. Insert the drive into the USB port of either the robot controller or the teach pendant while it is turned on.
#. On the hamburger menu, select :guilabel:`Settings`, then :guilabel:`System` > :guilabel:`URCaps` on the left panel.

.. image:: /assets/images/robot-integrations/ur/urcap-installation-settings.png
  :scale: 80%
  :align: center

#. If there's a previous installation of the Pickit URCap plugin (appears listed under ``Active UCaps``), it should be removed by selecting it and pressing :guilabel:`-`. Polyscope will indicate that a restart is needed, but there is no need to do it yet.

#. Press :guilabel:`+` to install a new URCap: navigate to the USB drive, and select the ``pickit_urcap-[version].urcap`` file.

#. Polyscope will indicate that a restart is needed for the changes to take effect. Press the :guilabel:`Restart` button to continue.

    .. image:: /assets/images/robot-integrations/ur/urcap-installation-add-urcap.png
      :align: center

#. Once Polyscope restarts, the plugin will be deployed and ready to use. Make sure your Pickit system is running and connected to the robot’s network to continue.

Using the Pickit URCap plugin
------------------------------

To use the Pickit URCap plugin, three steps must be taken:

.. _universal-robots-urcap-connect:

1. Connect to a Pickit system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On the header bar, go to :guilabel:`Installation`, then :guilabel:`URCaps` > :guilabel:`Pickit` on the left panel.

.. image:: /assets/images/robot-integrations/ur/urcap-installation-connect-to-pickit.png
  :align: center

#. Make sure that ``Enable Pickit plugin`` is checked.
#. Set the :ref:`IP address <settings-network>` and **hostname** of the Pickit system if you know them. Otherwise leave the default values.
#. Click :guilabel:`Find connected Pickit systems`. If the supplied IP and hostname are not correct, the URCap will search for a running Pickit systems in the network and populate the fields for you.

As long as the connection to Pickit has not been established, the status indicator at the lower left looks like this:

.. image:: /assets/images/robot-integrations/ur/urcap-installation-status-disconnected.png

Establishing the connection to Pickit can take a few seconds, and while this takes place, the status indicator displays:

.. image:: /assets/images/robot-integrations/ur/urcap-installation-status-connecting.png

When the connection to the Pickit system is successful, the status indicator at the lower left should look like this:

.. image:: /assets/images/robot-integrations/ur/urcap-installation-status-connected.png

If you plan to run robot programs that don't use Pickit, you should **disable** (not uninstall) the Pickit URCap plugin, by unchecking the ``Enable Pickit plugin`` checkbox in the plugin's installation screen.

.. _universal-robots-urcap-perform-calibration:

2. Perform robot-camera calibration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to perform :ref:`robot-camera calibration <robot-camera-calibration>` once or infrequently, you can teach the calibration poses manually using free-drive and the :ref:`Collect current pose <multi-poses-calibration-collect-current-pose>` button of the calibration wizard.

If, on the other hand, you expect to run calibration multiple times, you can use the :ref:`example calibration program <universal-robots-urcap-calibration>`, which stores the calibration poses.
This would be useful in the case when, for instance, the relative position of the camera with respect to the robot is not yet fully decided for your application.

.. _universal-robots-urcap-write-program:

3. Create pick and place robot programs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Writing a robot program with vision-guided pick and place is straightforward with the Pickit :ref:`pick and place template <urcap-pick-and-place-template>`.
Take a look at the :ref:`example program <urcap-pick-and-place-program>` to learn more about the easy and intuitive user experience it offers.

Example programs are installed in the ``/programs/pickit_examples`` folder of the robot.
