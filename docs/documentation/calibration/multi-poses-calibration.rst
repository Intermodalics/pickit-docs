.. _multi-poses-calibration:

Multi poses calibration
=======================

This article goes through the main steps in the multi poses calibration process:

.. contents::
    :backlinks: top
    :local:
    :depth: 1

Fixing the calibration plate
----------------------------

Fixed camera
~~~~~~~~~~~~

If the camera is fixed to a static structure, the calibration plate must be mounted on the robot
flange. For multi poses calibration it does not matter how the plate is mounted, as long as it's
fixed rigidly to the flange.

Refer to :ref:`installing-calibration-plate` for the standard way to mount the plate.

.. image:: /assets/images/Documentation/calibration_multi_pose_fixed_camera_plate_attachment.png
   :scale: 50 %
   :align: center

Robot mounted camera
~~~~~~~~~~~~~~~~~~~~

If the camera is mounted on the robot flange, place the calibration plate on a surface, at a
comfortable distance from the robot. The location of the plate should correspond to the picking
area.

.. image:: /assets/images/Documentation/calibration_multi_pose_plate_in_view.png
   :scale: 50 %
   :align: center

Building the robot program
--------------------------

In the robot interface, open the multi poses calibration template program, or create one your own.
This program repeats five times the following sequence: move to a waypoint and request Pickit to
find the calibration plate. Each of the five waypoints should be defined such that:

- The calibration plate is shown to the robot approximately in the center if the Pickit 2D view.
- The calibration plate is presented to the camera at different angles around the X, Y and Z axes
  of the plate. The angles should be large enough (for instance 30 degrees), while still making
  sure that the plate is clearly visible in the Pickit 2D viewer.

.. image:: /assets/images/Documentation/Calibration-plate-visible-viewer.png
   :align: center
.. image:: /assets/images/Documentation/Calibration-plate-visible.png
   :align: center

Program for fixed camera
~~~~~~~~~~~~~~~~~~~~~~~~

Move the robot such that the plate is in the middle of the field of view of the camera. Move the
flange to five different angle combinations around the X, Y and Z axes.

.. image:: /assets/images/Documentation/calibration_multi_pose_fixed_camera.png

Program for robot mounted camera
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Teach the five waypoints such that the plate always appears approximately in the center of the
image, but tilted in different directions.

.. image:: /assets/images/Documentation/calibration_multi_pose_camera_on_robot.png


.. _multi-poses-calibration-calibrating:

Calibrating
-----------

#. Click on the :guilabel:`Calibration` button, located on top of the Pickit web interface.
#. Choose the camera mount: whether the camera is fixed to a **stationary** place or **robot mounted**.
#. Select the correct robot type: **6 DOF** or **4 DOF**, depending on the number of
   degrees-of-freedom of your robot.
#. Choose the **multi poses** robot camera calibration method.
#. Follow the indicated steps, and run the robot program when instructed. Alternatively, you can also
   move your robot into the positions and press :guilabel:`Collect current pose` in the calibration wizard.
   Notice that the latter is only possible if the robot is periodically sending its pose to Pickit.
   The Pickit web interface shows the progress of the calibration process.
#. In the next step, you will see a 3D viewer showing the robot and camera models. Here you can confirm
   whether the calibration is correct.

.. image:: /assets/images/Documentation/Calibration-progress-multi-poses.png

4 DoF robots
~~~~~~~~~~~~

If your robot has 4 degrees-of-freedom, in the last step of the calibration wizard you will also find
a field for inputing:
- The distance between the robot flange and the camera, if the camera is mounted on the robot. Notice
  that, if the camera is mounted at a higher location than the robot flange, this value should be
  negative.
- The distance between the robot base and the camera, if the camera is fixed.

Looking at the camera location in the 3D viewer will help you obtaining the correct value.

.. important::
  After finishing robot camera calibration, don't forget to check the calibration result. Go to
  :ref:`checking-robot-camera-calibration` to know how.

.. warning::
  If after calibration the Pickit camera has been relocated or rotated relatively to the robot base,
  a new robot camera calibration is required before picking, even if the motion was small.
