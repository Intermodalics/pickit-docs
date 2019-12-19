.. _pick-points-flex-pattern:

Pick points in Pickit Flex and Pattern
======================================

The primitive shapes detected by the :ref:`Flex <Flex>` and :ref:`Pattern <Pattern>` detection engines have a *single* pick point.

2D shapes
---------

For 2D shapes (circles, squares, rectangles and ellipses), the pick point is located in the shape center, with the X-axis parallel to the longest direction, and the Z-axis perpendicular to the surface.

.. image:: /assets/images/Documentation/picking/flex_2d_shape_pick_points.png
    :scale: 80%
    :align: center

3D shapes
---------

For 3D shapes (cylinders and spheres), the pick point can be in one of the following locations, which can be selected from the **Define pick points** section.

.. image:: /assets/images/Documentation/picking/flex_3d_shape_pick_points.png
    :align: center

Blobs
-----

Blobs have the pick point in the centroid of the visible points. Its orientation is such that the Z-axis points towards the visible points and the X-axis points along the longest blob direction.