.. _fanuc-calibration-program:

Fanuc calibration program
=========================

This example program requires that Pickit is installed and set up with your robot.
For installation instructions, please refer to the :ref:`fanuc_installation_and_setup` article.

Before following these Fanuc specific instructions in this article, make sure you first understand the process of executing a robot camera calibration as explained on :ref:`robot-camera-calibration`.

.. note::
  If you want to perform calibration once or infrequently, you don't need to use this example program.
  You can teach the calibration poses manually using the pendant and the :guilabel:`Collect current pose` in the calibration wizard of the Pickit web interface.

Example program: PICKIT_MP_CALIBRATE
------------------------------------

This example program can be found in :guilabel:`Select`.

::

   1:  UTOOL_NUM=9 ;
   2:  UFRAME_NUM=0 ;
   3:L P[1] 100mm/sec FINE    ;
   4:  CALL PI_CALIBRATE    ;
   5:L P[2] 100mm/sec FINE    ;
   6:  CALL PI_CALIBRATE    ;
   7:L P[3] 100mm/sec FINE    ;
   8:  CALL PI_CALIBRATE    ;
   9:L P[4] 100mm/sec FINE    ;
  10:  CALL PI_CALIBRATE    ;
  11:L P[5] 100mm/sec FINE    ;
  12:  CALL PI_CALIBRATE    ;

Below, each step of the program is explained.

Define the tool for calibration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the calibration program the plate can be mounted to flange of the robot or clamped tightly with a gripper.
The tool settings for the calibration program can be set to anything that suits best your setup.
In the example program by default **UTOOL9** is used.

Set user frame
~~~~~~~~~~~~~~

Calibration is done relative to the base frame of the robot, hence **UFRAME0** is selected.

Teach calibration points
~~~~~~~~~~~~~~~~~~~~~~~~

The calibration program requires five points to be defined.
For more information on how to define these points, see the article on :ref:`multi-poses-calibration`.

Execute the calibration program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before running the calibration program, make sure that the Pickit web interface is in the :guilabel:`Calibration` page, which provides feedback on calibration plate visibility and progress of the calibration process (:ref:`more <multi-poses-calibration-calibrating>`).