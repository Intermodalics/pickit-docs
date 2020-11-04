
.. _smart-picking-examples:

Smart picking examples
----------------------

This article provides some example applications on how to smartly **pick** objects with Pickit.
It presents in a practical way how to make good use of :ref:`multiple pick points <multiple-pick-points>`, :ref:`symmetry axes <pick-point-symmetry-axis>`, and robot tool :ref:`flexible pick orientation <flexible-pick-orientation>` to increase the likelihood that an object is pickable.

To learn more about how to smartly **place** objects with Pickit, please take a look at the :ref:`smart placing examples <smart-place-examples>`.
There, you will learn how to place objects in a consistent way, while keeping the robot program as simple as possible.

.. _example-pick-ring-gripper:

Pick a ring object with a two-finger gripper
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This part has a symmetry axis and it's possible to pick it from the top, bottom, or side.
The picking configuration is as follows:

- **Three pick points**, as it's possible to pick the part from the top, bottom or side.

  - All pick points are **symmetric** about the part's axis.

  - The top and bottom pick points are internal grasps on a circular hole, which are self-centering. Since the side pick is not self-centering, it's given a **lower priority**.

- **Two-finger gripper** :ref:`tool model <robot-tool-model>`, with a flexible pick orientation that allows a **Y-axis tilt**.


.. image:: /assets/images/documentation/picking/example_ring_gripper.png
    :scale: 70%
    :align: center

.. note::
  A similar example can be interactively explored by opening the ``examples/cad/red_rings.snapshot`` :ref:`snapshot <Snapshots>`.

.. _example-pick-socket-gripper:

Pick sockets with a two-finger gripper
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This part has distinct top and bottom sides, and has the following picking configuration:

- **Four pick points**, two on each side.
  The two pick points of each side have a 180° offset in Z to represent the lateral symmetry of the gripper.
  Representing this discrete symmetry allows Pickit to choose the one that is closest to the :ref:`preferred pick point orientation <preferred-orientation>`, and potentially minimize robot motions.

- **Two-finger gripper** :ref:`tool model <robot-tool-model>`, with a flexible pick orientation that allows a **Y-axis tilt**.

.. image:: /assets/images/documentation/picking/example_socket_gripper.png
    :scale: 70%
    :align: center

.. note::
  A similar example can be interactively explored by opening the ``examples/cad/white_sockets_gripper.snapshot`` :ref:`snapshot <Snapshots>`.

  .. _example-pick-socket-suction:

Pick sockets with a suction gripper
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the same part as in the :ref:`previous example <example-pick-socket-gripper>`, the only difference being that it's now picked by a suction gripper, instead of a two-finger gripper.
It has the following picking configuration:

- **Four pick points**, two on each side.

- **Cylinder-shaped** :ref:`tool model <robot-tool-model>`, with a flexible pick orientation that allows:

  - **XY axes tilt:** The flexible bellows at the tip of the suction cup allow tilting in any direction.

  - **Full rotation about Z-axis:** The tool is free to rotate about its axis.

.. image:: /assets/images/documentation/picking/example_socket_suction.png
    :scale: 75%
    :align: center

.. note::
  Notice the impact of gripper choice on the number of pickable objects: all **12 detected objects** are pickable with the suction gripper, while **only 10** are with the :ref:`two-finger gripper <example-pick-socket-gripper>`.

.. note::
  A similar example can be interactively explored by opening the ``examples/cad/white_sockets_suction.snapshot`` :ref:`snapshot <Snapshots>`.
