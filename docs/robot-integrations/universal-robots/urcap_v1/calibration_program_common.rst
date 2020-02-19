.. note::
  If you want to perform calibration once or infrequently, you don't need to use this example program.
  You can teach the calibration poses manually using free-drive and the :ref:`Collect current pose <multi-poses-calibration-collect-current-pose>` button in the calibration wizard of the Pickit web interface.

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
