.. _preferred-orientation-teach:

Preferred pick point orientation in Pickit Teach
================================================

When a Pickit Teach model has :ref:`multiple pick points <multiple-pick-points>`, optionally with :ref:`flexible pick orientation <flexible-pick-orientation>`, there can be some freedom in how the pick point is oriented.
The **preferred pick point orientation** allows to choose a pick point with an axis that aligns as close as possible to one of the :ref:`reference frame <reference-frame>` axes.

Consider the following example. The part in the image below has a single pick point with no flexible pick orientation, hence has no freedom to reorient the pick point.
As a consequence, pick points are randomly oriented with respect to the reference frame (lower left, dashed axes).

.. image:: /assets/images/Documentation/picking/preferred_orientation_rigid.png
    :scale: 70%
    :align: center

Because the part has circular symmetry, a flexible pick orientation that represents it can be added; that is, allow the pick point to fully rotate about the object's Z-axis.
It can be seen below that this flexibility is now exploited to fully align the objects with the requested reference frame axis.

.. image:: /assets/images/Documentation/picking/preferred_orientation_full.png
    :align: center

Finally, if this is a bin picking scenario, we are also interested in :ref:`preventing collisions <collision-prevention>` between the robot tool and the bin.
As a result, it can be seen that the preferred orientation is used *as long as* it's collision free.
Only for a few objects the pick point diverges from the preferred orientation, and it can be clearly seen that it's for collision prevention purposes.

.. image:: /assets/images/Documentation/picking/preferred_orientation_with_collision_avoidance.png
    :align: center