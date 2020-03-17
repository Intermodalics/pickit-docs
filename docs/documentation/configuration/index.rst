.. _Configuration:

Configuration
=============

Pickit stores the configuration of an object detection scenario in two files:

-  **Setup**: Defines `where` Pickit needs to look. It stores all the parameters
   exposed in the :ref:`setup` page of the :ref:`web interface <web-interface>`.
-  **Product**: Defines `what` Pickit needs to look for. It contains all the
   parameters exposed in the :ref:`detection` and :ref:`picking` pages of the
   :ref:`web interface <web-interface>`.

Loading a setup or product file
-------------------------------

The active (i.e. currently loaded) setup and product files are displayed at all
times in the :ref:`top bar <web-interface-top-bar>` of the web interface.
The active setup file is also indicated on top of the **Setup** page, and the
active product file on top of the **Detection** and **Picking** pages.

To load an existing configuration file and set it to active, you can click on
the name of the active file in any of the above mentioned locations,
or press the :guilabel:`Open` button at the top of the respective page
(**Setup**, **Detection** or **Picking**).
A separate view will show all available files.

From this view you can also create :guilabel:`New` files, or :guilabel:`Rename`,
:guilabel:`Download` or :guilabel:`Delete` selected files.
Active files cannot be renamed or deleted.

.. image:: /assets/images/documentation/product-files-window.png

.. warning::
  Deleted setup and product files cannot be recovered.

Setup and product files can also be loaded from your robot program.
Refer to the documentation of the Pickit robot integrations to learn the exact
commands for your robot brand (:ref:`UR example <command-select>`).

Creating a new setup or product file
------------------------------------

To create a new setup or product file, press :guilabel:`New`, name the file and
press :guilabel:`Continue`. The new file will contain default settings.
After creation, the new file will be automatically set to active.

.. image:: /assets/images/documentation/create-new-product-file.png
   :scale: 80%

Saving a setup or product file
------------------------------

Pressing :guilabel:`Save` saves the current configuration to the active file.
The :guilabel:`Save as` button saves the current configuration to a new file
with a different name.
Pressing :guilabel:`Reset` restores the last saved settings, and all unsaved
changes are lost.

.. image:: /assets/images/documentation/save-saveas-reset.png
