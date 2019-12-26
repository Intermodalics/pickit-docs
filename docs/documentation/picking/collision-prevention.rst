.. _collision-prevention:

Collision prevention
====================

In constrained picking scenarios like bin picking, it is important to prevent the robot tool from colliding with the bin or other objects, such that the application runs without interruption.

In the :ref:`Picking page <Picking>`, under **Prevent collision with tool**, one can check whether reaching a pick point with a specific robot tool would result in collision.
If picking an object would lead to a collision, the object is labeled as unpickable and is not sent to the robot.
In the Pickit web interface, unpickable objects are displayed in orange in the :ref:`Objects view <objects-view>` and :ref:`detection-grid`.

.. note::
  Pickit collision-checks the **pick point**, not the robot trajectory that would lead to it.

Collision checks: Bin and other objects
---------------------------------------

For collision prevention to take place, the user needs to define a :ref:`robot tool model <robot-tool-model>`, and specify whether to check for collisions with the **bin** and/or **other objects** in the scene.

The examples below show a pick point being rejected due to collisions that would result between the robot tool and the bin (left), and between the robot tool and another object (right).

.. image:: /assets/images/Documentation/picking/example_tool_collision.png
  :scale: 40%
  :align: center


.. tip::
  When collisions checks with the bin are enabled, it's important to have a correctly defined :ref:`bin box <bin-box>`.

  When using Pickit :ref:`Teach <teach>`, having :ref:`multiple pick points <multiple-pick-points>` and/or :ref:`flexible pick orientations <flexible-pick-orientation>` increases the likelihood of finding collision-free pick points.

.. _robot-tool-model:

Robot tool model
----------------

.. note::
  The robot tool model is only used for collision checks, and does not influence how the robot picks an object.
  To modify the how the robot picks an object, refer to the :ref:`pick point <pick-points>` documentation.

Pickit allows modeling robot tools that closely resemble commonly used end-effectors.
Currently, three different models are supported:

.. image:: /assets/images/Documentation/picking/tool_models.png
  :scale: 50%
  :align: center

It is possible to modify a tool's characteristic dimensions, as well as adapt its relative distance and orientation with respect to an object’s pick point.
The image below shows the tool model editor for the **Box-shaped tool**.

.. image:: /assets/images/Documentation/picking/tool_model_box_ui_22.png
  :scale: 60%
  :align: center

.. note:: The tool model editor is hidden when collision checks are disabled (Neither ``Bin`` or ``Other objects`` are selected).

Some tool models have optional geometries that can be enabled or disabled.
Two common ones are the **Base sphere**, which typically contains (part of) the robot wrist, and the **Camera box**, which represents the camera volume in robot-mounted camera setups.

The example below compares the actual robot tool with the model used by Pickit.
It shows a tool model consisting of a gripper attached to a long extension cylinder, a robot-mounted camera and a sphere around the robot wrist.

.. image:: /assets/images/Documentation/picking/tool_model_real_vs_model.png
    :scale: 80%
    :align: center

.. tip::
  It is recommended that the robot tool model is *slightly* larger than the actual tool, to have a safety margin when performing robot motions.
  If the model is too large (too conservative), objects will be labeled as unpickabe even if they could be picked without collision.
  Conversely, if the model is smaller than the actual tool, unpickable objects might be labeled as pickable and the robot will collide when picking them.
