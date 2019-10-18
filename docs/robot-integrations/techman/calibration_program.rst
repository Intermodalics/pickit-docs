.. _techman-calibration-program:

Example robot camera calibration program
========================================

Loading the program
-------------------

This example program requires the **Pickit TMflow components** to be installed in your robot. For installation instructions of both the TMflow components and the example programs, please refer to the :ref:`techman-installation` article.

Click the `hamburger icon <https://en.wikipedia.org/wiki/Hamburger_button>`__ on the top-left corner of the user interface, and select **Project**.

    .. image:: /assets/images/robot-integrations/techman/tm-installation-left-panel-project.png
       :scale: 50%
       :align: center

Open the project called ``pickit_calibration``. This program is a template for performing :ref:`multi-poses calibration <multi-poses-calibration>`.


Multi poses calibration
-----------------------

The program starts by initializing pickit with the :ref:`init <tm-init>` component.
Note that since robot mode doesn't need to be enabled to perform calibration, both exit states of the component map to the nominal program flow.

  .. note::
    If your Pickit system is not using the default 169.254.5.180 IP address, you should set it in the configuration of the :ref:`init <tm-init>` component.

  .. image:: /assets/images/robot-integrations/techman/tm-init-3.png
       :scale: 50%
       :align: center

Then, the following sequence is repreated five times:

#. Move the robot to a waypoint where the calibration plate is visible.

    When teaching the waypoints, it is recommended to have the :guilabel:`Calibration` page open in the Pickit web interface, where the user can verify whether the calibration plate is visible.

    .. note::
      This program is a template, and the waypoints need to be retaught by the user since they depend on the physical environment and location of the calibration plate.
      Refer to the :ref:`multi-poses calibration <multi-poses-calibration>` article for guidelines on how the five waypoints should be taught.

#. Send a request to find the calibration plate by means of the :ref:`tm-find-calibration-plate` component.

    .. image:: /assets/images/robot-integrations/techman/tm-findcalibrationplate-1.png
       :scale: 50%
       :align: center

It is possible to follow the progress of the calibration procedure from the :guilabel:`Calibration` page.

Single pose calibration
-----------------------

For :ref:`single pose calibration <single-pose-calibration>`, the program is similar, but only performs a single calibration request.
