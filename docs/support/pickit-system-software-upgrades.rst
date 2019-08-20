.. _Pickit-system-software-upgrade:

Pickit system software upgrades
================================

Upgrading the Pickit software can be done by the user, without Pickit
support engineers’ intervention. This guide will take you through the upgrade
procedure.

Overview
--------

To upgrade your system follow these steps:

- Before proceeding with the upgrade, make sure your setup and product files are saved.

- Download the latest version of Pickit here_.
- Press the **Settings** button in the top bar of Pickit's web interface.

     .. image:: /assets/images/Documentation/settings-button-21.png

- In the **Network settings** section of the left menu, select the **Upgrade
  Pickit version** drawer, and press the **Upload and
  Install Upgrades** button to upload and select the downloaded
  file.

  .. note:: **For version < 2.1.2** :

    You first need to enable the option **I prefer downloading and
    uploading the new version myself** before pressing the **Upload and
    Install Upgrades** button.

- While the upgrade is in progress you should see the following:

   .. image:: /assets/images/Documentation/pickit-upgrading.png

.. _here: https://client.pickit3d.com/upgrade/v2/

.. warning:: Note that for Pickit versions < 2.1.2, the web interface can show
  the error message **ERROR: Something went wrong during upgrading**, even though the
  upgrade process is still running without problems.

  If you see this message, **DO NOT REBOOT THE PICKIT SYSTEM YOURSELF**. Instead
  **WAIT FOR IT TO REBOOT AUTOMATICALLY**. After the reboot, the web
  interface will refresh automatically and show the newest version.

  In the exceptional case where the Pickit system does not reboot within
  15 minutes after starting the upgrade, please contact **support@pickit3d.com**.
