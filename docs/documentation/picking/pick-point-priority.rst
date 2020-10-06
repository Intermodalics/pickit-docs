.. _pick-point-priority:

Pick point priority
-------------------

By default, all pick points have the same priority, but in some applications it makes sense to prefer a certain pick point over another, when multiple valid choices exist.
In the below example, we have a part with three pick points, two of which should be preferred.

.. image:: /assets/images/documentation/picking/pick_point_priority.png
  :scale: 60%
  :align: center

By setting pick point priorities, it can be enforced that pick points with lower priority are considered only if higher priority ones are unpickable.

.. image:: /assets/images/documentation/picking/pick_point_priority_preference.png
  :align: center

The below part can be picked from two pick points.
In the absence of different priorities, the side pick would be preferred, as it's higher up (left).
But, if the side pick is given a lower priority, picking from the circular hole is preferred (right).

.. image:: /assets/images/documentation/picking/pick_point_priority_example.png
  :align: center

The typical motivations for using pick point priorities are:

**Likelihood of pick success:** Some pick point locations are more robust to picking errors. For instance, in the below example:

- Pick points 1 and 2 are internal grasps on a circular hole. The fingers have room to accomodate positioning errors during the pick, and the resulting pick will be self-centering along the circle plane.
- Pick point 3 is an external grasp that can accomodate less positioning errors, and lacks the self-centering property. For this reason, this pick is potentially less likely to succeed. When successful, it might result in less accurate picks, which brings us to the second motivation.

**Cycle time:** Some pick points might require a tool recongifuration, or going through an additional repicking station, such that the part can be accurately placed at the dropoff location.



