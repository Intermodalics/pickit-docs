.. _max-robot-flage-tilt:

Maximum robot flange tilt
=========================

This setting rejects picks where the robot flange would tilt too much. Such picks are more likely to
result in unreachable robot motions.
Tilt is measured between the ROI vertical direction and the :ref:`robot tool flange <robot-tool-model>` Z-axis (or pick point Z-axis, if no tool has been assigned to the pick point).

As seen in the image below, if an object is tilted more than the specified angle, it will be labeled as unpickable.
In the Pickit web interface, unpickable objects
are displayed orange in the :ref:`Objects view <objects-view>` and the :ref:`detection-grid`.

.. image:: /assets/images/documentation/picking/max_robot_flange_tilt.png
