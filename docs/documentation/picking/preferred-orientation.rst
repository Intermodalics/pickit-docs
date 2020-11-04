.. _preferred-orientation:

Preferred pick point orientation
================================

When an object model has :ref:`multiple pick points <multiple-pick-points>`, a :ref:`symmetry axis <pick-point-symmetry-axis>` or a tool with :ref:`flexible pick orientation <flexible-pick-orientation>`, there can be some freedom in how the pick point is oriented.
The **preferred pick point orientation** allows to point a pick point axis as close as possible to one of the :ref:`reference frame <reference-frame>` axes, or a specific location, like the reference frame origin or the :ref:`ROI <region-of-interest>` center.
This contributes to minimize unnecessary robot motions when picking objects, and can have a favorable effect on cycle time.

Consider the following example.
Because the part in the image below is symmetric, the model can be correctly fit in an infinity of orientations.
If the part has a single pick point without :ref:`symmetry axis <pick-point-symmetry-axis>`, there is no freedom to reorient the pick point.
As a consequence, pick points are randomly oriented with respect to the reference frame (lower left, dashed axes).

.. image:: /assets/images/documentation/picking/preferred_orientation_rigid.png
    :scale: 70%
    :align: center

If a :ref:`symmetry axis <pick-point-symmetry-axis>` is defined, the pick point can now fully rotate about it.
It can be seen below how the symmetry is now exploited to fully align the objects with the requested reference frame axis.

.. image:: /assets/images/documentation/picking/preferred_orientation_full.png
    :align: center

Finally, if this is a bin picking scenario, we are also interested in :ref:`preventing collisions <collision-prevention>` between the robot tool and the bin.
As a result, it can be seen that the preferred orientation is used *as long as* it's collision free.
The pick point diverges from the preferred orientation only for a few objects, for collision prevention purposes.

.. image:: /assets/images/documentation/picking/preferred_orientation_with_collision_avoidance.png
    :align: center