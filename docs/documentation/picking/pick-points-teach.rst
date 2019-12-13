.. _pick-points-teach:

Pick points in Pickit Teach
===========================

Once a Pickit Teach model :ref:`has been taught <teach-a-model>`, pick points need to be associated to it.
A pick point represents where an object can be picked by the robot.
It is specified as a position and orientation relative to the object, where the robot Tool Center Point (TCP) should move to perfrom a pick.
What constitutes a good pick point depends on both the gripping device and the object to be picked.

This article focuses on how pick points are created and managed, and the companion :ref:`example applications <pick-points-teach-examples>` article presents a number of real scenarios and how to make the best use of this feature.

.. toctree::
    :hidden:
    :maxdepth: 1
    :glob:

    pick-points-teach-examples

.. _multiple-pick-points:

Multiple pick points per model
------------------------------

A single object can often be picked from more than one point. Having multiple pick points associated to a single Teach model has a two-fold advantage:

- Increase the likelihood that objects are pickable even if they overlap or are close to bin walls. Below, two possible pick points for picking a socket with a suction gripper are shown: the left one (in orange) is unpickabe due to collisions with the bin, while the right one (in green) is pickable.

.. image:: /assets/images/Documentation/picking/pick_point_bin_collision.png
    :scale: 60%
    :align: center

- Specify pick points for models where only one part is visible at a time. This is the case for full object models :ref:`taught from CAD <teach-from-cad>`. Below, pick points for the top (left) and bottom (right) sides of a socket are shown.

.. image:: /assets/images/Documentation/picking/socket_top_bottom_pick_points.png
    :scale: 50%
    :align: center

The **Define pick points** section of the :ref:`picking <Picking>` page allows to create and manage the pick points of Teach models:

- Create a new pick point by clicking :guilabel:`Add pick point`.
  Once creted, a pick point can be enabled/disabled and its visibility can be toggled.
- Duplicate or delete an existing pick point by clicking on the  :guilabel:`⋮` button.
- Set the :guilabel:`Point position and orientation`, which specifies its location with respect to the object origin, or optionally with respect to an existing point by changing the :guilabel:`Reference point`.
- Optionally, specify a :guilabel:`Flexible pick orientation` (:ref:`more <flexible-pick-orientation>`).

.. image:: /assets/images/Documentation/picking/pick_point_ui_22.png
    :scale: 60%
    :align: center



.. _flexible-pick-orientation:

Flexible pick orientation
-------------------------

In practice, many applications can tolerate some variation with respect to the nominal pick orientation without compromising pick success.
Taking advantage of this can increase the likelihood that individual pick points are pickable by the robot.
This flexibility is typically due to shape symmetries, (e.g. a circular object, below left), or robot tool compliance (e.g. suction cup bellows, below right), and is represented in Pickit by a pick point's :guilabel:`Flexible pick orientation`.

.. image:: /assets/images/Documentation/picking/flexibility_real_pic.png
    :scale: 60%
    :align: center

Pickit allows the pick point orientation to tilt around the X and/or Y axes, as well as to rotate around the Z-axis (below, left).
Flexibility around each axis is represented in the 3D model view as a circular sector as wide as the specified interval size (below, right).

.. image:: /assets/images/Documentation/picking/flexible_pick_orientation_ui_with_3d_22.png
    :scale: 80%
    :align: center

The image below highlights the beneficial effect of flexible pick orientations on increasing the likelihood of finding pickable objects.
Without it, the shown objects would be labeled as unpickable by Pickit due to :ref:`collisions <collision-prevention>` between the tool and the bin or other objects.
The :ref:`example applications <pick-points-teach-examples>` section describes further scenarios where flexible pick orientations can be used.

.. image:: /assets/images/Documentation/picking/flexible_pick_orientation_comparison.png
    :scale: 55%
    :align: center

.. note::
  Both **multiple pick points** and **flexible pick orientations** are complementary strategies for increasing the likelihood that an object is pickable.

.. tip::
  Flexible pick orientations, in combination with the :ref:`preferred pick point orientation <preferred-orientation-teach>` can be used to favor picks that are easier and faster to reach by the robot (e.g. less wrist motion, lower occurrence of unreachable points).


.. _selecting-a-pick-point:

Selecting which pick point to use
---------------------------------

When an object has multiple pick points, Pickit smartly selects the best one to use.
It does so by following these steps:

1. **Sort the pick points** from highest to lowest. Note that this depends on how a particular object is oriented in the scene.
2. **Go over the list of pick points** starting from the highest one.

  a. **Is the preferred orientation pickable?** Determine the orientation that is closest to the :ref:`preferred pick point orientation <preferred-orientation-teach>`. If it's pickable, use it to pick the object, else continue with the next step.
  b. **Is there a pickable configuration?** If the pick point has a :ref:`flexible pick orientation <flexible-pick-orientation>`, search for a pickable configuration. The search will favor configurations that deviate as little as possible from the :ref:`preferred pick point orientation <preferred-orientation-teach>`. If a pickable configuration is found, use it to pick the object, else continue with the next pick point.

3. **No pickable points?** If no pickable point is found, the object is labeled as unpickable.

.. tip::
  If you click on a particular detection in the :ref:`detection grid <detection-grid>`, you can learn which pick point was selected for picking. Also, if an object is unpickable, you can learn the reason why its pick points were not pickable.
