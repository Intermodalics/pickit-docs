.. _flange-filter:

Minimum distance between robot flange and ROI
=============================================

It is sometimes desired that the robot flange, when picking objects, does not deviate too much laterally above the :ref:`ROI <region-of-interest>` (or bin).
This is particularly relevant when there are collision obstacles close to the bin like poles, fences or other tall structures, as shown below.
Note that Pickit can :ref:`prevent collisions <collision-prevention>` between the robot tool and the bin or other objects inside it. This feature minimizes the risk of collisions occurring *beyond* the bin.

.. image:: /assets/images/documentation/picking/flange_filter_fence.png
  :scale: 70%
  :align: center

It is possible to limit how much the robot flange is allowed to deviate away from the bin walls.

.. image:: /assets/images/documentation/picking/flange_filter_ui.png

The following image shows three possible ways to pick a billet.

.. image:: /assets/images/documentation/picking/flange_filter_off_neg_pos.png

**Left:** no limit is imposed on the robot flange position.

**Middle:** We are limiting the flange position with a **negative distance**, such that at the pick point, its position is constrained to not go *beyond* the bin walls more than the specified distance.

**Right:** We are limiting the flange position with a **positive distance**, such that at the pick point, its position is constrained to be *within* the bin walls, by at least the specified distance.

:ref:`Multiple pick points <multiple-pick-points>`, :ref:`symmetry axes <pick-point-symmetry-axis>` and a :ref:`tool model's flexible pick orientation <flexible-pick-orientation>` are explored to find a pick point that satisfies this constraint.
If this is not possible, the pick point is labeled as unpickable.

Limiting how much the robot flange is allowed to deviate away from the bin walls can also have the effect of reducing the required robot workspace, resulting in potentially more reachable and faster robot motions.
