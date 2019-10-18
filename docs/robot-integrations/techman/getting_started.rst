.. _techman-installation:

Component installation and setup
================================

Pickit integrates seamlessly with **Omron TM** cobots by means of a a set of **TMflow components**.
Each component is a building block for creating vision-guided applications with Pickit.
This document explains how to install the Pickit components as well as example robot programs.

Pre-requisites
--------------

Pickit
~~~~~~~

Verify that the installed **Pickit version is 2.1 or greater**.
The software version can be verified in the :ref:`top bar <web-interface-top-bar>` of the web interface.

.. tip::
    Still having an older Pickit version installed? Contact our support team to have your Pickit system updated: support@pickit3d.com.

Robot
~~~~~

The **TMflow** versions supported by the Pickit components are listed on our :ref:`downloads page <downloads_omron_tm>`.

Installing the Pickit TM integration files
------------------------------------------

To install the Pickit TM integration files, follow these steps:

#. :ref:`Download the Pickit TM integration files <downloads_omron_tm>`.
#. Unzip the archive and copy its contents to a USB drive.

   .. note::
     TMflow requires USB drives to adhere to a specific directory structure for importing contents into the robot. The files contained in the above archive respect this layout and should not be altered.

#. From a Windows PC, open the TMflow application and **Get control** of your TM robot.
#. Click the `hamburger icon <https://en.wikipedia.org/wiki/Hamburger_button>`__ on the top-left corner of the user interface to display a panel on the left side of the screen.

#. Click on **System** on the left panel, to display the **System setting screen**.

    .. image:: /assets/images/robot-integrations/techman/tm-installation-left-panel-system.png
       :scale: 50%
       :align: center

#. Click on the **Import/Export** icon.

    .. image:: /assets/images/robot-integrations/techman/tm-installation-system-settings-import-export.png
       :scale: 50%
       :align: center

#. Select **Import** on the top-left corner.

    .. image:: /assets/images/robot-integrations/techman/tm-installation-import-export.png
       :scale: 60%
       :align: center

#. Select **Component** on the left panel. Browse the contents of the USB drive and select all the listed Pickit components. These are the building blocks for Pickit-based applications.

    .. image:: /assets/images/robot-integrations/techman/tm-installation-import-component.png

#. Select **Project** on the left panel. Browse again the contents of the USB drive and select all listed projects. These are example programs that can get you started with little effort.

    .. image:: /assets/images/robot-integrations/techman/tm-installation-projects.png
       :scale: 50%
       :align: center

#. The Pickit components are now imported, but they also need to be enabled to make them accessible to projects. To do this, click the `hamburger icon <https://en.wikipedia.org/wiki/Hamburger_button>`__, then **Setting**.

    .. image:: /assets/images/robot-integrations/techman/tm-installation-left-panel-setting.png
       :scale: 50%
       :align: center

#. Click on the **Component** icon.

    .. image:: /assets/images/robot-integrations/techman/tm-installation-robot-settings-component.png
       :scale: 60%
       :align: center

#. On the component list, select all imported Pickit components, enable them and save.

    .. image:: /assets/images/robot-integrations/techman/tm-installation-component-list-cropped.png


Using the Pickit TMflow components
----------------------------------

The available Pickit TMflow components are documented in detail in :ref:`techman-interface`.

There are two main usecases for a robot program that uses the Pickit TMflow components:

- Perform :ref:`robot-camera calibration <robot-camera-calibration>`, which is explained in the :ref:`techman-calibration-program`.
- Perform a pick and place task, which is explained in the :ref:`techman-pick-and-place-program`.

As long as your application is similar to the above examples, it is recommended to use the above examples as templates, and modify them according to the particularities of your application.

Happy picking!
