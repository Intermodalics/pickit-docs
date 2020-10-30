.. _Picking:

Picking
=======

Pickit is not only about detecting objects, but also about being able to pick them.
While the :ref:`Detection <detection>` page is concerned with *what* to detect, the **Picking** page is concerned with everything that revolves around *how* to pick a detected object:
From which points can it be picked? With which tool? Is the pick collision-free?

.. tip::
  You can learn about the main ideas behind *how to pick* by watching this :ref:`video tutorial <video-tutorials-how-to-pick>`.

.. _Picking-tool-model:

Robot tool model
----------------

Pickit allows to :ref:`model the robot tool <robot-tool-model>` that is used for picking.
The tool model is useful for visually confirming the correct location of a pick point, and can also be used to :ref:`prevent collisions <collision-prevention>` between the tool and a bin or other objects.

.. toctree::
    :hidden:
    :maxdepth: 1
    :glob:

    robot-tool-model

.. _pick-points:

Pick points
-----------

A :ref:`pick point <pick-points-detail>` represents where an object can be picked by the robot.
It is specified as a position and orientation relative to the object, where the robot Tool Center Point (TCP) should move to perform a pick.
What constitutes a good pick point depends on both the gripping device and the object to be picked.

.. toctree::
    :hidden:
    :maxdepth: 1
    :glob:

    pick-points

.. _pick-strategy:

Pick strategy
-------------

.. toctree::
    :hidden:
    :maxdepth: 1
    :glob:

    object-ordering
    preferred-orientation
    max-robot-flange-tilt
    enforce-alignment-of-pick-frame-orientation
    flange-filter
    temporarily-avoid-unpicked-objects

Once pick points are specified, there are a number of options that influence how objects are picked.

  - :ref:`Object ordering: <object-ordering>` When multiple objects are detected, object ordering determines the order in which they should be picked.
  - :ref:`Preferred pick point orientation: <preferred-orientation>` Pick points can have flexibility in how they are oriented.
    This flexibility can be used to favor pick orientations that are easier and faster to reach by the robot (e.g. less wrist motion):

  - :ref:`Maximum robot flange tilt: <max_angle_pick_z_ref_z>` When the robot flange tilts too much to pick an object, it is more likely that picking it will result in unreachable robot motions.
    This option allows to label objects that are too tilted as unpickable.

  - :ref:`Minimum distance between robot flange and ROI: <flange-filter>` This allows limiting lateral deviations of the robot flange away from the bin walls, at the pick point.

  - :ref:`Temporarily avoid unpicked objects: <temporarily-avoid-unpicked-objects>` This prevents repeatedly failing to pick the same object, and contributes to more consistent cycle times.

Collision prevention
--------------------

.. toctree::
    :hidden:
    :maxdepth: 1
    :glob:

    collision-prevention

In constrained picking scenarios like bin picking, it is important to prevent the robot tool from colliding with the bin or other objects.
Pickit allows to model the robot tool and to perform :ref:`collision checks with the bin and other objects <collision-prevention>`.
