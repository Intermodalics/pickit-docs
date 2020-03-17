.. _robot-independent-calibration:

Calibration program
===================

If you want to perform :ref:`robot-camera calibration <robot-camera-calibration>` once or infrequently, you can teach the calibration poses manually using the :ref:`Collect current pose <multi-poses-calibration-collect-current-pose>` button of the calibration wizard.
No robot programming is required.

If, on the other hand, you expect to run calibration multiple times, you can use the program below, which stores the calibration poses.
This would be useful in the case when, for instance, the relative position of the camera with respect to the robot is not yet fully decided for your application.

Performing :ref:`robot-camera calibration <robot-camera-calibration>` programmatically is a simple task.
It consists of teaching a number of calibration poses and iterating through them as Pickit detects the calibration plate.

.. note::
  Before running the program, the user must have the :guilabel:`Calibration` page of the Pickit web interface open.

The following is an example :ref:`multi-poses calibration<multi-poses-calibration>` robot program.

.. literalinclude:: code/calibration-example.py
  :language: python
  :linenos:

