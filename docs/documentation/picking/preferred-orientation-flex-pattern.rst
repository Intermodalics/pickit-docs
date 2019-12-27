.. _preferred-orientation-flex-pattern:

Preferred pick point orientation in Pickit Flex and Pattern
===========================================================

When specifying the :ref:`pick point <pick-points-flex-pattern>` for a :ref:`Flex <Flex>` or :ref:`Pattern <Pattern>` shape, there can be some freedom in how the pick point is oriented.
For instance, when a rectangle is detected, it's X-axis points along the longest rectangle dimension, but there are two possible solutions, shown below.

.. image:: /assets/images/Documentation/picking/rectangle_flexibility.png
    :scale: 80%
    :align: center

The **preferred pick point orientation** allows to align an axis of the pick point as close as possible to one of the :ref:`reference frame <reference-frame>` axes.
Shape symmetries are used to determine to which extent the pick point can be flipped or rotated to best align the requested axes.

The pictures below show examples of how the preferred pick point orientation is resolved for rectangular and circular shapes.

.. image:: /assets/images/Documentation/Object-to-reference-frame-alignment.png
