.. _Picking:

Picking
=======

Pickit is not only about detecting objects, but also about being able to pick them.
While the :ref:`Detection <detection>` page is concerned with *what* to detect, the **Picking** page is concerned with everything that revolves around *how* to pick a detected object:
From which points can it be picked? With which tool? Is the pick collision-free?


.. _pick-points:

Pick points
-----------

A pick point represents where an object can be picked by the robot.
It is specified as a position and orientation relative to the object, where the robot Tool Center Point (TCP) should move to perform a pick.
What constitutes a good pick point depends on both the gripping device and the object to be picked.
The following articles detail how pick points are managed by the different detection engines:

.. toctree::
    :maxdepth: 1
    :glob:

    pick-points-teach
    pick-points-flex-pattern


.. _pick-strategy:

Pick strategy
-------------

.. toctree::
    :hidden:
    :maxdepth: 1
    :glob:

    object-ordering
    preferred-orientation-teach
    preferred-orientation-flex-pattern
    maximum-angle-between-pick-and-reference-frame-zaxis
    enforce-alignment-of-pick-frame-orientation

Once pick points are specified, there are a number of options that influence how objects are picked.

  - **Object ordering:** When multiple objects are detected, object ordering determines the order in which they should be picked (:ref:`more <object-ordering>`).
  - **Preferred pick point orientation:** Pick points can have flexibility in how they are oriented.
    This flexibility can be used to favor pick orientations that are easier and faster to reach by the robot (e.g. less wrist motion):

      - :ref:`Preferred pick point orientation in Pickit Teach <preferred-orientation-teach>`
      - :ref:`Preferred pick point orientation in Pickit Flex and Pattern <preferred-orientation-flex-pattern>`

  - **Maximum tilt from reference frame Z-axis:** When a pick point is too tilted, it is more likely that picking it will result in unreachable robot motions. This option allows to label objects that are too tilted as unpickable (:ref:`more <max_angle_pick_z_ref_z>`).

  - **Enforce pick point alignment** This applies only to the :ref:`Flex <Flex>` and :ref:`Pattern <Pattern>` detection engines, and is explained in detail in :ref:`this article <enforce-alignment-of-pick-point-orientation>`. If using Pickit :ref:`Teach <teach>`, refer to the more powerful :ref:`flexible pick orientation <flexible-pick-orientation>` feature.


Collision prevention
--------------------

.. toctree::
    :hidden:
    :maxdepth: 1
    :glob:

    collision-prevention

In constrained picking scenarios like bin picking, it is important to prevent the robot tool from colliding with the bin or other objects.
Pickit allows to model the robot tool and to perform :ref:`collision checks with the bin and other objects <collision-prevention>`.
