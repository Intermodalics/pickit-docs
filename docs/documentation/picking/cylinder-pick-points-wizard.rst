.. _cylinder-pick-points-wizard:

Cylinder pick points wizard
===========================

Cylinder pick points wizard can be selected by clicking the `pick points wizard` tab, in `Define Pick points`.
It smartly creates pick points in a few clicks that fully exploit the symmetries of cylinders.

3 different pick point location can be selected:

- `Cylinder surface`: to pick cylinders from their surface. Ideal for suction or magnetic grippers. 
- `Cylinder axis`: to pick cylinders around their central axis: Ideal for 2 finger gripper.
- `Circular caps`: to pick cylinders from their caps. Ideal to pick cylinders standing vertically.

.. image:: /assets/images/documentation/picking/cylinder_pick_points_wizard.png
   :scale: 70 %
   :align: center

.. tip::
  `Circular cap` is best used together with `cylinder surface` or `circular cap`.
  That way, both vertically standing and horizontally lying cylinders can be picked.
  In that case, a :ref:`smart placing <smart-place-pick-point-id>` of the picked cylinder might be needed.

In order to maximize the number of pickable objects, the cylinder symmetries are fully exploited.
First, all the pick points created by the wizard use a 360 deg rotational symmetry around the cylinder central axis.
Additionaly, for every pick point created a mirrored version is created to represent the mirror symmetry of the cylinder.
