.. _universal-robots-urcap-calibration:

URCap robot camera calibration program
======================================

This example program requires the **Pickit URCap** plugin to be installed in your robot.  For installation instructions of both the URCap plugin and the example programs, please refer to the :ref:`universal-robots-urcap-installation` article.

Before following these URCap specific instructions in this article, make sure you first understand the process of executing a robot camera calibration as explained on :ref:`robot-camera-calibration`.

Multi poses calibration
-----------------------

.. image:: /assets/images/robot-integrations/ur/urcap-calibration-1.png

The program starts by opening a pop-up message, informing that multi-poses calibration will be carried out. Before running the program, the user must have the :guilabel:`Calibration` page of the Pickit web interface open. If this is not the case, it is notified by a pop-up message. Otherwise, the following sequence is repeated five times:

#. Moves the robot to a waypoint.

   .. image:: /assets/images/robot-integrations/ur/urcap-calibration-2.png
      :scale: 50 %

   All ``MoveJ`` commands are specified with respect to the **tool flange** (as opposed to the TCP).

   While teaching the waypoints, it is recommended to have the :guilabel:`Calibration` page open in the Pickit web interface, where the user can verify whether the calibration plate is visible.

   .. note::
      This program is a template, and the waypoints are not set. They must be taught by the user since they depend on the physical environment and location of the calibration plate.
      Refer to the :ref:`multi-poses calibration <multi-poses-calibration>` article for guidelines on how the five waypoints should be taught.

#. Sends Pickit a calibration request, through the command ``Find calibration plate``.

   .. image:: /assets/images/robot-integrations/ur/urcap-calibration-3.png
      :scale: 50 %


In the :guilabel:`Calibration` page, the user can follow the progress of calibration. 

Single pose calibration
-----------------------

For single pose calibration, the program consists of one single calibration request.

.. image:: /assets/images/robot-integrations/ur/urcap-calibration-4.png
