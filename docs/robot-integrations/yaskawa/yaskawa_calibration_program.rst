.. _yaskawa_calibration_program:

Yaskawa calibration program
===========================

This example program requires that Pickit is installed and set up with your robot.
For installation instructions, please refer to the :ref:`yaskawa_installation_and_setup` article.

Before following these Yaskawa specific instructions in this article, make sure you first understand the process of executing a robot camera calibration as explained on :ref:`robot-camera-calibration`.

.. note::
  If you want to perform calibration once or infrequently, you don't need to use this example program.
  You can teach the calibration poses manually using free-drive and the :guilabel:`Collect current pose` in the calibration wizard of the Pickit web interface.

Example program: TEST_CALIB
---------------------------

This example program can be found in :guilabel:`JOB` → :guilabel:`SELECT JOB`.

::

    NOP
    MFRAME UF#(5) P008 BF
    MOVJ C00000 VJ=10.00 PL=0
    PI_CALIB
    MOVJ C00001 VJ=10.00 PL=0
    PI_CALIB
    MOVJ C00002 VJ=10.00 PL=0
    PI_CALIB
    MOVJ C00003 VJ=10.00 PL=0
    PI_CALIB
    MOVJ C00004 VJ=10.00 PL=0
    PI_CALIB
    END

Below, each step of the program is explained.

Define the tool for picking
~~~~~~~~~~~~~~~~~~~~~~~~~~~

When using Pickit it is important that **tool0** is set equal to the robot flange.
This is done by setting all the values of **tool0** to 0.

Set user frame
~~~~~~~~~~~~~~

To help us set the user frame we are going to use a **Position** variable, by default **P008**.
Set following values in :guilabel:`VARIABLE` → :guilabel:`POSITION(ROBOT)`:

- Select **BASE**.
- Make sure that **X**, **Y**, **Z**, **Rx**, **Ry** and **Rz** are all equal to **0**.

Here it is assumed that **P008** is not yet being used anywhere else in the robot program.
You can also use any other variable, as long as it is free.
In that case, make sure to fill this variable in, in the command **MFRAME UF#(5) P008 BF**.

After running the program, a new user frame **(5)** will be created that will be used both for calibration and picking.

Teach calibration points
~~~~~~~~~~~~~~~~~~~~~~~~

The calibration program requires five points to be defined.
For more information on how to define these points, see the article on :ref:`multi-poses-calibration`.

Execute the calibration program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before running the calibration program, make sure that the Pickit web interface is in the :guilabel:`Calibration` page, which provides feedback on calibration plate visibility and progress of the calibration process (:ref:`more <multi-poses-calibration-calibrating>`).
To run the program either do **Play + Start**, **Interlock + FWD** or **Interlock + Test**.