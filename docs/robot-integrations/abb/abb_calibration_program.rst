.. _abb-calibration-program:

ABB calibration program
=======================

This example program requires that Pickit is installed and set up with your robot.
For installation instructions, please refer to the :ref:`abb-installation-and-setup` article.

Before following these ABB specific instructions in this article, make sure you first understand the process of executing a robot-camera calibration as explained on :ref:`robot-camera-calibration`.

.. note::
  If you want to perform calibration once or infrequently, you don't need to use this example program.
  You can teach the calibration poses manually using the pendant and the :ref:`Collect current pose <multi-poses-calibration-collect-current-pose>` in the calibration wizard of the Pickit web interface.

Example program: MultiPoseCalibration
-------------------------------------

This example program can be found as a routine in the module Pickit_calibration.
Go to :guilabel:`Program Editor` > :guilabel:`Modules` > :guilabel:`Pickit_calibration` > :guilabel:`MultiPoseCalibration()`.

::

   PROC MultiPoseCalibration()
        !
        MoveToCalPoint pCalibration1;
        WaitTime 0.5;
        pickit_find_calib_plate;
        !
        MoveToCalPoint pCalibration2;
        WaitTime 0.5;
        pickit_find_calib_plate;
        !
        MoveToCalPoint pCalibration3;
        WaitTime 0.5;
        pickit_find_calib_plate;
        !
        MoveToCalPoint pCalibration4;
        WaitTime 0.5;
        pickit_find_calib_plate;
        !
        MoveToCalPoint pCalibration5;
        WaitTime 0.5;
        pickit_find_calib_plate;
        !
        Stop;
    ENDPROC

Below, each step of the program is explained.

Teach calibration points
~~~~~~~~~~~~~~~~~~~~~~~~

The calibration program requires five points to be defined.
For more information on how to define these points, see the article on :ref:`multi-poses-calibration`.

Execute the calibration program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before running the calibration program, make sure that the Pickit web interface is in the :guilabel:`Calibration` page, which provides feedback on calibration plate visibility and progress of the calibration process (:ref:`more <multi-poses-calibration-calibrating>`).

.. note::
  By default the robot flange (**tool0**) and the robot base (**wobj0**) are used to move to these points.