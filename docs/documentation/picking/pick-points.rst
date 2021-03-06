.. _pick-points-detail:

Pick points
===========

Once a :ref:`part to detect <detection>` has been defined, pick points need to be associated to it.
A pick point represents where an object can be picked by the robot.
It is specified as a position and orientation relative to the object, where the robot Tool Center Point (TCP) should move to perform a pick.
What constitutes a good pick point depends on both the gripping device and the object to be picked.

This article focuses on how pick points are created and managed in the generic :ref:`Pickit Teach <teach>` workflow.
Pickit also provides convenient wizards for creating pick points for the following particular cases:

- :ref:`Pick points for cylinders <cylinder-pick-points-wizard>` of known size with :ref:`Pickit Teach <teach-cylinder>`.
- :ref:`Pick points for 2D or 3D shapes <pick-points-flex-pattern>` with :ref:`Flex <Flex>` or :ref:`Pattern <Pattern>`.

.. _multiple-pick-points:

Multiple pick points per model
------------------------------

A single object can often be picked from more than one point. Having multiple pick points associated to a single Teach model has a two-fold advantage:

- Increase the likelihood that objects are pickable even if they overlap or are close to bin walls. Below, two possible pick points for picking a socket with a suction gripper are shown: the left one (in orange) is unpickabe due to collisions with the bin, while the right one (in green) is pickable.

.. image:: /assets/images/documentation/picking/pick_point_bin_collision.png
  :scale: 60%
  :align: center

- Specify pick points for models where only one part is visible at a time. This is the case for full object models :ref:`taught from CAD <teach-from-cad>`. Below, pick points for the top (left) and bottom (right) sides of a socket are shown.

.. image:: /assets/images/documentation/picking/socket_top_bottom_pick_points.png
  :scale: 50%
  :align: center

.. tip::
  Apart from :ref:`multiple pick points <multiple-pick-points>`, other strategies that, if applicable, can increase the likelihood of an object being pickable, are :ref:`pick point symmetry axes <pick-point-symmetry-axis>`, and :ref:`flexible robot tool orientation <flexible-pick-orientation>`.

.. _pick-point-creation-management:

Pick point creation and management
----------------------------------

The **Define pick points** section of the :ref:`picking <Picking>` page allows to create and manage the pick points of Teach models:

- **Add pick point** creates a new pick point.
  Once created, a pick point can be enabled/disabled and its visibility can be toggled.
- :guilabel:`⋮` **button**, provides access to duplicating or deleting an existing pick point.
- :ref:`Select tool <robot-tool-model>`, sets the tool model to use for this pick point.
- :ref:`Point position and orientation <pick-point-location>`, sets the pick point location with respect to the object origin, or optionally with respect to an existing point by changing the :ref:`Reference point <pick-point-reference>`.
- :ref:`Priority <pick-point-priority>`, can be optionally set such that pick points with lower priority are considered only if higher priority ones are unpickable.
- :ref:`Symmetry axis <pick-point-symmetry-axis>`, can be optionally associated to the pick point. This is especially relevant for parts with axial symmetry.

.. image:: /assets/images/documentation/picking/pick_point_ui.png
  :align: center

.. tip::
  The way in which an object is picked can also determine how to correctly place it at a drop-off location.
  To learn more about how to make the best use of pick points in real application scenarios, take a look at the
  :ref:`smart picking <smart-picking-examples>` and :ref:`smart placing <smart-place-examples>` examples companion articles.

.. _pick-point-selection:

Pick point selection
--------------------

When an object has multiple ways of being picked, Pickit smartly selects the best one to use.
It does so by following these steps:

1. **Sort the pick points**

  a. If a pick point tolerates variations, because it either has a :ref:`symmetry axis <pick-point-symmetry-axis>` or the robot tool has a :ref:`flexible pick orientation <flexible-orientation-at-pick-point>`, prefer orientations that are closer to the :ref:`preferred pick point orientation <preferred-orientation>`.

  b. If :ref:`multiple pick points <multiple-pick-points>` exist, prefer pick points that are higher.
  For pick points at the same height, prefer pick points that are closer to the :ref:`preferred pick point orientation <preferred-orientation>`.

2. **Find a pickable point**

  a. Select a pick point from the sorted list.

  b. If the initial configuration is unpickable (e.g. it's too tilted or collides with the bin or other objects) but the pick point tolerates variations, search for a pickable configuration that deviates as little as possible from the preferred orientation.

  c. If a pickable configuration is found, use it to pick the object, else continue with the next pick point.

3. **No pickable points?** If no pickable point is found, the object is labeled as unpickable.

.. tip::
  If you click on a particular detection in the :ref:`detection grid <detection-grid>`, you can learn which pick point was selected for picking. Also, if an object is unpickable, you can learn the reason why its pick points were not considered pickable.

.. These entries are included last to not show in the left panel toc.

.. toctree::
    :hidden:
    :maxdepth: 1
    :glob:

    cylinder-pick-points-wizard
    pick-point-location
    pick-point-priority
    pick-point-symmetry-axis
    pick-points-flex-pattern
    smart-pick-examples
    smart-place-examples