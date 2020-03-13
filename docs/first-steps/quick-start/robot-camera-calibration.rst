Robot camera calibration
========================

In this step we do a robot camera calibration. In the previous chapter
we saw that the Pickit system is able to detect parts in its field of
view. Now Pickit needs to know where the robot is based so that it can
tell the robot where it needs to move to when an object is detected.
**If you skip this step, the robot will move to a wrong location.**

Follow the steps below to do a robot camera calibration:

-  Mount the robot-to-camera calibration plate to the flange of the
   robot. Make sure it is well fixed.
-  Click on the :guilabel:`Calibration` button on top of the web interface. Select a
   **stationary** camera mount and **Multi Poses Calibration**
   for the calibration method. For the robot type, select **6 DOF** or **4 DOF**
   depending on the number of degrees-of-freedom (DOF) of your robot. If your robot has
   only 4 degrees-of-freedom, fill in the distance between calibration plate and
   robot flange in the field **Flange Z-axis**.
-  On your robot open the example multi-poses calibration program supplied
   by Pickit. Edit the program, defining different waypoints such that the
   robot shows the calibration plate to the camera at different angles. Confirm that
   the plate is visible for all waypoints.

.. image:: /assets/images/Documentation/calibration_multi_pose_fixed_camera.png

-  Run the multi-poses calibration program on the robot. Once all five poses are
   collected, the calibration process is finished.
-  Check in the :ref:`3D view <3d-view>` if the position and orientation of the robot model match
   the actual robot. If that is the case, the calibration plate can be dismounted from
   the robot, and Pickit is ready for picking.

.. tip:: More details about robot camera calibration can be found in
   the :ref:`robot-camera-calibration` article.
