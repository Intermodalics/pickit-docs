
.. _pick-points-teach-examples:

Pick points in Pickit Teach: Example applications
-------------------------------------------------

This article provides some example applications of how :ref:`pick points <pick-points-teach>` are defined for a Pickit Teach model.
It presents in a practical way how to make good use of **multiple pick points** and **flexible pick orientations**.

.. _example-pick-ring-gripper:

Pick a ring object with a two-finger gripper
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This part has circular symmetry and distinct top and bottom sides. It has two pick points, one for each side.
The gripper performs a centered, internal grasp, and each pick point has the following flexible pick orientations:

- **Y-axis tilt:** The gripper can tilt in one direction and still successfully pick the object.
- **Full rotation about Z-axis:** The circular symmetry of the object allows the gripper to freely rotate about the symmetry axis.

.. image:: /assets/images/Documentation/picking/example_ring_gripper.png
    :scale: 75 %
    :align: center

.. note::
  In a real deployment of the application, it would be valuable to add an additional pick point for picking parts lying on their side. This has been omitted from the example for brevity's sake.

.. note::
  This example can be interactively explored by opening the ``examples/cad/red_rings.snapshot`` :ref:`snapshot <Snapshots>`.

.. _example-pick-socket-gripper:

Pick sockets with a two-finger gripper
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This part has distinct top and bottom sides, and a total of four pick points. Each side has two pick points with a 180° offset in Z to represent the bilateral symmetry of the gripper.
Representing this discrete symmetry allows Pickit to chose the one that is closest to the :ref:`preferred pick point orientation <preferred-orientation-teach>`, and potentially minimize robot motions.


Each pick point has a single flexible pick orientation:

 - **Y-axis tilt:** The gripper can tilt in one direction and still successfully pick the object.

.. image:: /assets/images/Documentation/picking/example_socket_gripper.png
    :scale: 80%
    :align: center


.. note::
  This example can be interactively explored by opening the ``examples/cad/white_sockets_gripper.snapshot`` :ref:`snapshot <Snapshots>`.

  .. _example-pick-socket-suction:

Pick sockets with a suction gripper
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the same part as in the :ref:`previous example <example-pick-socket-gripper>`, the only difference being that it's now picked by a suction gripper, instead of by a two-finger gripper.
It has two pick points per side (total four pick points).
Each pick point has the following flexible pick orientations:

 - **XY axes tilt:** The flexible bellows at the tip of the suction cup allow tilting in any direction.
 - **Full rotation about Z-axis:** The tool is free to rotate about its axis.

.. image:: /assets/images/Documentation/picking/example_socket_suction.png
    :scale: 75%
    :align: center

.. note::
  Notice the impact of gripper choice on the number of pickable objects: all **12 detected objects** are pickable with the suction gripper, while **only 9** are with the :ref:`two-finger gripper <example-pick-socket-gripper>`.

.. note::
  This example can be interactively explored by opening the ``examples/cad/white_sockets_suction.snapshot`` :ref:`snapshot <Snapshots>`.

This article covers concrete examples on how to benefit from multiple pick points and pick orientation flexibility to pick more objects from the bin, or to optimize robot motions.
In some cases, however, you may want to drop the picked objects in a consistent way, without any offsets, while keeping the robot program as simple as possible.
Check out :ref:`this article` <smart-place-examples> with examples of different objects being smartly placed, after being picked with the techniques mentioned above.
