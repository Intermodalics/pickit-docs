.. _pick-points-flex-pattern:

Pick points in Pickit Flex and Pattern
======================================

2D shapes
---------

For 2D shapes (circles, squares, rectangles and ellipses), the pick point is located in the shape center, with the Z-axis perpendicular to the surface.
Additionally, the following considerations apply:

- **Circle:** The pick point has a symmetry axis about the circle center.
- **Square:** The X-axis points toward one of the sides.
- **Rectangle and ellipse:** The X-axis is parallel to the longest side (any of the two directions).

.. image:: /assets/images/documentation/picking/flex_2d_shape_pick_points.png
    :scale: 80%
    :align: center

3D shapes
---------

For 3D shapes (cylinders and spheres), the pick point can be in one of the following locations, which can be selected from the wizard in the **Define pick points** section.

.. image:: /assets/images/documentation/picking/flex_3d_shape_pick_points.png
    :align: center

Blobs
-----

Blobs have the pick point in the centroid of the visible points. Its orientation is such that the Z-axis points towards the visible points and the X-axis points along the longest blob direction.