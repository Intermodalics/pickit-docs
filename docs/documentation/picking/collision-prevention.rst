.. _collision-prevention:

Collision prevention
====================

In constrained picking scenarios like bin picking, it is important to prevent the :ref:`robot tool <robot-tool-model>` from colliding with the bin or other objects, such that the application runs without interruption.

In the :ref:`Picking page <Picking>`, under **Prevent collision with tool**, one can check whether reaching a pick point with a specific robot tool would result in collision.
If picking an object would lead to a collision, the object is labeled as unpickable and is not sent to the robot.
In the Pickit web interface, unpickable objects are displayed in orange in the :ref:`Objects view <objects-view>` and :ref:`detection-grid`.

.. note::
  Pickit collision-checks the **pick point**, not the robot trajectory that would lead to it.

Collision checks: Bin and other objects
---------------------------------------

For collision prevention to take place, the user needs to define a :ref:`robot tool model <robot-tool-model>`, and specify whether to check for collisions with the **bin** and/or **other objects** in the scene.

The examples below show a pick point being rejected due to collisions that would result between the robot tool and the bin (left), and between the robot tool and another object (right).

.. image:: /assets/images/documentation/picking/example_tool_collision.png
  :scale: 40%
  :align: center


.. tip::
  When collisions checks with the bin are enabled, it's important to have a correctly defined :ref:`bin box <bin-box>`.

  When using Pickit :ref:`Teach <teach>`, having :ref:`multiple pick points <multiple-pick-points>` and/or :ref:`flexible pick orientations <flexible-pick-orientation>` increases the likelihood of finding collision-free pick points.
