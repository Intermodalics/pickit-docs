.. _kuka-krc4-calibration-program:

KUKA calibration program
========================

This example program requires that Pickit is installed and set up with your robot.
For installation instructions, please refer to the :ref:`kuka-krc4-installation-and-setup` article.

Before following these KUKA specific instructions in this article, make sure you first understand the process of executing a robot camera calibration as explained on :ref:`robot-camera-calibration`.

.. note::
  If you want to perform calibration once or infrequently, you don't need to use this example program.
  You can teach the calibration poses manually using the pendant and the :ref:`Collect current pose <multi-poses-calibration-collect-current-pose>` in the calibration wizard of the Pickit web interface.

Example program: PickitMultiPoseCal
-----------------------------------

This example program can be found in **R1** > **Program** > **Pickit**.

::

    DEF PickitMultiPoseCal( )
        FOLD INI;%{PE}

        PTP home

        PTP P1
        WAIT SEC 0.5
        Pickit_do_calibration()

        PTP P2
        WAIT SEC 0.5
        Pickit_do_calibration()

        PTP P3
        WAIT SEC 0.5
        Pickit_do_calibration()

        PTP P4
        WAIT SEC 0.5
        Pickit_do_calibration()

        PTP P5
        WAIT SEC 0.5
        Pickit_do_calibration()

        PTP home

    END

Below, each step of the program is explained.

Teach calibration points
~~~~~~~~~~~~~~~~~~~~~~~~

The calibration program requires five points to be defined (P1 - P5).
For more information on how to define these points, see the article on :ref:`multi-poses-calibration`.

Execute the calibration program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before running the calibration program, make sure that the Pickit web interface is in the :guilabel:`Calibration` page, which provides feedback on calibration plate visibility and progress of the calibration process (:ref:`more <multi-poses-calibration-calibrating>`).