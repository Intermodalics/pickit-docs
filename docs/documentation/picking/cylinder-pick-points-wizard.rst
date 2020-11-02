.. _cylinder-pick-points-wizard:

Pick points for Teach cylinder models
=====================================

Defining pick points for :ref:`Teach cylinder models <teach-cylinder>` is a very simple task.
By default, on teaching a new model, Pickit adds pick points on the surface of the cylinder, in the middle of the shape.
When using suction or magnetic grippers, this is typically enough to start picking.

.. image:: /assets/images/documentation/picking/pick_point_cylinder_surface.png
   :scale: 50 %
   :align: center

The default choice can be overridden by means of the **pick points wizard**, which can be accessed just below the existing pick points.

.. image:: /assets/images/documentation/picking/pick_point_cylinder_wizard.png
   :scale: 80 %
   :align: center


It's possible to select between three different pick point locations:

- `Cylinder surface`: to pick cylinders from their surface. Ideal for suction or magnetic grippers.
- `Cylinder axis`: to pick cylinders around their central axis: Ideal for two-finger grippers.
- `Circular caps`: to pick cylinders from their caps. Ideal to pick cylinders standing (almost) vertically.

All pick points created by the wizard are aware of the cylinder :ref:`symmetry axis <pick-point-symmetry-axis>`, and have a mirrored version to represent the lateral symmetry of the cylinder.

.. image:: /assets/images/documentation/picking/cylinder_pick_points_wizard.png
   :scale: 70 %
   :align: center

.. tip::
  `Circular cap` is best used together with `cylinder surface` or `cylinder axis`.
  That way, both vertically standing and horizontally lying cylinders can be picked.
  In that case, a :ref:`smart placing <smart-place-pick-point-id>` strategy might be needed on the robot program.

  .. image:: /assets/images/documentation/picking/pick_point_cylinder_combos.png
   :align: center

Apart from the convenience of the **pick points wizard**, power users can also modify existing pick points and add new ones using the standard :ref:`pick point editor <pick-point-creation-management>`.