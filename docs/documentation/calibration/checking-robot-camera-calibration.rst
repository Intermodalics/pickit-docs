.. _checking-robot-camera-calibration:

Checking robot camera calibration
=================================

During robot camera calibration, small procedure mistakes can lead to significant calibration errors.
It is therefore important to check the correctness of calibration before starting to pick.

Once Pickit thinks it knows where the robot is, it places two new frames in the 3D environment: the
**robot base** and the **robot flange** frames. Their pose relatively to the camera frame should
correspond to the actual transformations between robot base, flange and camera in the real world.
It is recommended to have a look from different viewpoints to verify that the position and
orientation of the robot base and flange frames look correct.

.. image:: /assets/images/documentation/Verify-calibration.png

.. image:: /assets/images/documentation/Verify-calibration-2.png

Checking robot camera calibration with a UR robot
-------------------------------------------------

If you have a Universal Robots robot, you can additionally visualize a virtual 3D robot, which should
make it easier to verify the correctness of calibration. To do so, follow these steps:

#. Make sure there is communication between Pickit and the robot:

   .. image:: /assets/images/documentation/Communication-robot-2.png

#. Navigate to the 3D view and click on the settings button on the lower right of the viewer.

   .. image:: /assets/images/documentation/Settings-button-2.png


#. Toggle the **Visualize Robot** check box.

   .. image:: /assets/images/documentation/Visualize-robot-2.png

This allows you to intuitively check whether the virtual 3D robot aligns well with the displayed
coordinate frames and captured point cloud. For example, the following images show a fixed-camera
scenario where the robot is inside the camera view volume. It can be seen how, before calibration,
the robot as seen by the camera does not align with the virtual 3D robot. After calibration they
nicely align. Similarly, the attached calibration plate (only visible to the camera, not part of
the virtual 3D robot) is correctly aligned with respect to the robot flange after calibration.

.. image:: /assets/images/documentation/Before-calibration.png
.. image:: /assets/images/documentation/After-calibration.png

Wrong robot camera calibration?
-------------------------------

You have just gone through the calibration process, but the frames appear at wrong places. Here is
what could be wrong:

- The camera mount might have been wrongly selected.
- In case of multi poses calibration, the plate may not be tilted at large enough angles.
  Perhaps the plate is not being tilted at all around one or more directions.
- In case of single pose calibration, perhaps the helper transformation is wrong.
- The calibration plate may have moved during the calibration process.
- If a non-supported robot brand is being used, there might be an incompatability in the way poses
  are communicated between Pickit and the robot.

If you are having trouble figuring out what could be wrong, immediately contact our
support team via `support@pickit3d.com <mailto:mailto://support@pickit3d.com>`__.

.. note::
  The information resulting from robot camera calibration is associated to the Pickit camera used
  in the process. It is not saved in the setup or product files.

.. warning::
  If after calibration the Pickit camera has been relocated or rotated relatively to the robot base,
  a new robot camera calibration is required before picking, even if the motion was small.
