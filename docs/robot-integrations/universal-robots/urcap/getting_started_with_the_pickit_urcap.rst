.. _universal-robots-urcap-installation:

URCap installation and setup
============================

Pickit integrates seamlessly with Universal Robots by means of a URCap plugin. This plugin exposes a set of Pickit specific command blocks that make the creation of vision-guided programs simple and easy. This document explains how to install the Pickit URCap plugin and introduces the functionality it provides.

Some of the benefits of using the Pickit URCap plugin:

-  Less typing and less code.
-  Graphical command interface with in-place documentation.
-  Pickit :ref:`2D view <2d-view>` available from the UR Teach Pendant.

Pre-requisites
--------------

Pickit
~~~~~~~

Verify that the installed **Pickit version is 1.8.2 or greater**. The software version can be verified in the :ref:`top bar <web-interface-top-bar>`
of the web interface. When the version is not displayed at the top left of the web interface you are running an older version of Pickit which needs to be updated first.

.. image:: /assets/images/robot-integrations/ur/urcap-installation-1.png

.. tip::
    Still having an older Pickit version installed? Contact our support team to have your Pickit system updated: support@pickit3d.com.

Robot
~~~~~

Verify that you have a supported **Polyscope version**. The Polyscope versions supported by the Pickit URCap plugin are listed on our :ref:`downloads page <downloads:Universal Robots>`. To check the Polyscope version currently installed in your robot, click the :guilabel:`About` button on the home screen.

.. image:: /assets/images/robot-integrations/ur/urcap-installation-2.png

Installing the Pickit URCap plugin
----------------------------------

To install the Pickit URCap plugin, follow these steps:

#. :ref:`Download the Pickit URCap files <downloads:Universal Robots>` the Pickit URCap plugin archive containing the latest version of the URCap.
#. Unzip the archive and copy its contents to an **empty** USB drive.
#. Insert the drive into the USB port of either the robot controller or teach pendant while it is turned on.
#. On the Polyscope home screen, press :guilabel:`Setup Robot` > :guilabel:`URCaps` to entery the **URCaps** section.

   .. image:: /assets/images/robot-integrations/ur/urcap-installation-3.png

#. If there's a previous installation of the Pickit URCap plugin (appears listed under Active), it should be removed by selecting it and pressing :guilabel:`-`. Polyscope will indicate that a restart is needed to apply the changes. Press the :guilabel:`Restart` button to continue, and after restart head back to :guilabel:`Setup Robot` > :guilabel:`URCaps`, and make sure that Pickit is not listed in the Active URCaps.

   .. image:: /assets/images/robot-integrations/ur/urcap-installation-4.png

#. Press :guilabel:`+` to install a new URCap.

   .. image:: /assets/images/robot-integrations/ur/urcap-installation-5.png

#. Navigate to the USB drive, and select the ``pickit_urcap-[version].urcap`` file.
#. Polyscope will indicate that a restart is needed to apply the changes. Press the restart button to continue.

   .. image:: /assets/images/robot-integrations/ur/urcap-installation-6.png

#. Once Polyscope restarts, the plugin will be deployed and ready to use. Make sure your Pickit system is running and connected to the robot’s network to continue.

Using the Pickit URCap plugin
------------------------------

To use the Pickit URCap plugin two things must be done: Connect to a running Pickit system, and write a program that uses Pickit specific commands.

Connect to a running Pickit system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From the main screen, go to **Program Robot** and select the **Installation** tab. The configuration screen of the Pickit plugin is accessible by selecting **Pickit** on the left panel.

.. image:: /assets/images/robot-integrations/ur/urcap-installation-7.png

.. image:: /assets/images/robot-integrations/ur/urcap-installation-8.png

#. Make sure that **Enable Pickit plugin** is checked.
#. Set the **IP address** and **hostname** of the Pickit system. The hostname of the Pickit system can be found on the top-left of the Pickit web interface next to the Pickit logo.
#. Click :guilabel:`Connect to Pickit`.

As long as the connection to Pickit has not been established, the status indicator at the lower left looks like this:

.. image:: /assets/images/robot-integrations/ur/urcap-installation-9.png

Establishing the connection to Pickit can take a few seconds, and while this takes place, the status indicator displays:

.. image:: /assets/images/robot-integrations/ur/urcap-installation-10.png

When the connection to the Pickit system is successful, the status indicator at the lower left should look like this:

.. image:: /assets/images/robot-integrations/ur/urcap-installation-11.png

If you plan to run robot programs that don't use Pickit, you should disable (not uninstall) the Pickit URCap plugin, by unchecking the **Enable Pickit plugin** checkbox in the plugin's installation screen.

Example programs
----------------

The Pickit URCap plugin installation makes available a few example programs under the ``/programs/pickit_samples`` folder of the robot. They can also be downloaded independently of the URCap \ `here <https://drive.google.com/uc?export=download&id=1Gf63Y35NaVxbP4mwc5YUC5SU8u8RYvyO>`__. These programs are a great way to get familiar with the Pickit URCap plugin, and can serve as a template to build your own applications. The following articles provide detailed descriptions of example programs:

-  :ref:`universal-robots-urcap-example`

-  :ref:`universal-robots-urcap-calibration`

Running URScript programs
-------------------------

If you have robot programs written for Pickit 1.7 or older, before the URCap plugin existed, and want to run them without porting them to the new URCap syntax, please refer to the :ref:`faq-how-to-run-urscript-urcap` article.
