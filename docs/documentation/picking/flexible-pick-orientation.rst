.. _flexible-pick-orientation:

Flexible pick orientation
-------------------------

In practice, many applications can tolerate some variation with respect to the nominal pick orientation without compromising pick success.
Taking advantage of this can increase the likelihood that individual pick points are pickable by the robot.
This flexibility is typically due to shape symmetries (e.g. a circular object, below left), robot tool compliance (e.g. suction cup bellows, below center), or application-specific considerations (e.g. clearance between the tool and object at a specific pickpoint, below right). It is represented in Pickit by a pick point's :guilabel:`Flexible pick orientation`.

.. image:: /assets/images/documentation/picking/flexibility_real_examples.png
  :scale: 60%
  :align: center

Pickit allows the pick point orientation to tilt around the X and/or Y axes, as well as to rotate around the Z-axis (below, left).
Flexibility around each axis is represented in the 3D model view as a circular sector as wide as the specified interval size (below, right).

.. image:: /assets/images/documentation/picking/flexible_pick_orientation_ui_with_3d.png
  :scale: 80%
  :align: center

The following three examples show, from left to right:

- A picture of the real application.
- The 3D visualization of the :ref:`object model <teach>`, :ref:`robot tool model <robot-tool-model>`, pick point and flexible pick orientation.
- The flexible pick orientation specification.

.. image:: /assets/images/documentation/picking/flexibility_real_examples_full.png
  :align: center

The image below highlights the beneficial effect of flexible pick orientations on increasing the likelihood of finding pickable objects.
Without it, the shown objects would be labeled as unpickable by Pickit due to :ref:`collisions <collision-prevention>` between the tool and the bin or other objects.
The :ref:`example applications <pick-points-teach-examples>` section describes further scenarios where flexible pick orientations can be used.

.. image:: /assets/images/documentation/picking/flexible_pick_orientation_comparison.png
  :scale: 55%
  :align: center

.. note::
  Apart from the robot tool model :ref:`flexible pick orientation <flexible-pick-orientation>`, :ref:`multiple pick points <multiple-pick-points>` and pick point :ref:`symmetry axes <pick-point-symmetry-axis>` are other strategies for increasing the likelihood of an object being pickable.

.. tip::
  Flexible pick orientations, in combination with the :ref:`preferred pick point orientation <preferred-orientation-teach>` can be used to favor picks that are easier and faster to reach by the robot (e.g. less wrist motion, lower occurrence of unreachable points).

In some applications, you may want to drop-off the object in the same location independently of how it was picked (which pick point and how orientation flexibility was used).
:ref:`This article <smart-place-pick-point-offset>` shows two different examples where this goal is achieved.
