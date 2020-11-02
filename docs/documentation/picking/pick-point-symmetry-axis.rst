.. _pick-point-symmetry-axis:

Pick point symmetry axis
------------------------

It is quite common to encounter applications where the parts to pick are symmetric about an axis.
Consider the example of a pick point on the surface of a cylinder.
Any point along the highlighted circle (below left) is equally valid, and this motion freedom can be exploited to increase the likelihood of the object being pickable.
Below right, although we prefer to pick from the top of the cylinder, the pick point is tilting away from the bin to prevent a collision with it.

.. image:: /assets/images/documentation/picking/pick_point_symmetry_axis.png
  :align: center

Pickit allows to individually make pick points symmetric about an axis.
The location of the axis is specified in a similar way as is done for :ref:`pick points <pick-point-location>` (below left), and it's visually displayed in the 3D pick points view as a dashed magenta line for the axis, and a magenta circle where the pick point is allowed to move (below right).

.. image:: /assets/images/documentation/picking/pick_point_symmetry_axis_specification.png
  :scale: 60%
  :align: center

Typical applications where this feature is useful include picking billets, pipes, shafts, discs and rings.

.. image:: /assets/images/documentation/picking/pick_point_symmetry_axis_examples.png
  :align: center

.. note::
  A symmetry axis is automatically added to all pick points created using the wizards for:

  - :ref:`Cylinders of known size <cylinder-pick-points-wizard>` with :ref:`Pickit Teach <teach-cylinder>`.
  - :ref:`Cylinders of unknown size <pick-points-flex-pattern>` with :ref:`Pickit Flex <Flex>`.

.. tip::
  Apart from a pick point's :ref:`symmetry axes <pick-point-symmetry-axis>`, :ref:`multiple pick points <multiple-pick-points>` and :ref:`flexible pick orientation <flexible-pick-orientation>` of the robot tool model are other strategies for increasing the likelihood of an object being pickable.