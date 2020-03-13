.. _smart-place-examples:

Smart placing using pick point data
-----------------------------------

Having multiple and/or flexible pick points increases the likelihood that an object is pickable, which significantly :ref:`benefits bin picking applications <pick-points-teach-examples>`.
However, after picking an object, the robot usually needs to know something about the way the object was picked, in order to place it appropriately.

Concrete examples of such situations are listed below, as well as a brief explanation of how :ref:`pick point data <RC_PICKIT_GET_PICK_POINT_DATA>` can help to obtain the desired
way to place the objects, while keeping the robot program as simple as possible.

.. contents::
    :backlinks: top
    :local:
    :depth: 1

.. note::
  Each example below contains a **Robot program snippet**, consisting of an implementation of the object placing sequence, ``place()``.
  These snippets are written in robot-agnostic pseudo-code.
  Refer to the :ref:`complete pick and place program <robot-independent-pick-and-place-complete>` to learn more about the logic of a pick and place application.

.. _smart-place-pick-point-id:

Different drop-off based on pick point ID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When using Teach CAD models to detect randomly overlapping objects, :ref:`multiple pick points <multiple-pick-points>` are usually necessary in order to be able to pick the parts from different sides.
For instance, these power sockets can be picked from the top (pick point 1) or from the bottom (pick point 2).

.. image:: /assets/images/documentation/picking/pick_point_data_sockets_multiple_id.png

Depending on which side is picked, the user may want the robot to place the object differently.
Below, the robot program uses the **pick point ID** to drop the object on the left side if picked from the top, and on the right side if picked from the bottom.

.. details:: Robot program snippet (click to expand)

  .. literalinclude:: code/pick-point-id.py
    :language: python

|

.. raw:: html

  <iframe src="https://drive.google.com/file/d/1K79zDj8HftvqvtCRKUUHXb0_4bRO_iz4/preview" frameborder="0" allowfullscreen width="640" height="480"></iframe>
  <br>

|

.. note::
    Similar logic can be written depending not on the pick point ID, but on the detected :ref:`model <robot-independent-pickit-obj-type>`  (if multiple :ref:`Teach <Teach>` models exist) or the detected :ref:`object dimensions <robot-independent-pickit-obj-dim>` (:ref:`Flex <Flex>` engine), for instance.

.. _smart-place-pick-point-offset:

Same drop-off for objects with flexible pick point orientation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are using :ref:`pick points with flexible orientations <flexible-pick-orientation>`, the object can be picked in infinitely many ways.
However, it is usually desired that the object is dropped off in the same way, regardless of how it was picked.
In the two cases below, the robot program compensates the difference between the actual and nominal pick point to always place the object at the same drop-off location.

.. details:: Robot program snippet (click to expand)

  .. literalinclude:: code/pick-point-offset.py
    :language: python

  Where ``Dropoff`` was defined for the nominal pick point, that is, when :ref:`flexible pick orientations <flexible-pick-orientation>` are not used.
  Learn more about ``PickPointOff`` :ref:`here <robot-independent-pickit-pick-off>`.

|

Flexibility around Z
^^^^^^^^^^^^^^^^^^^^

In the example below, we use flexibility around the pick point Z-axis to prevent the robot flange from rotating upon picking the cups.

.. image:: /assets/images/documentation/picking/pick_point_data_cups_flexible_offset.png

The **pick point offset** is used to correct the drop-off pose, such that the cups are always dropped with the same orientation, independently of how they were picked.

.. raw:: html

  <iframe src="https://drive.google.com/file/d/1_DKlv7mdbWH2Szi3mT_JdBp9GLAQpvWu/preview" frameborder="0" allowfullscreen width="640" height="480"></iframe>
  <br>

|

Flexibility around X and/or Y
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The example below shows a similar offset compensation.
This time, the pick point of the blocks has flexibility around the Y-axis, in order to allow being picked by a two-finger gripper as vertically as possible (see, for example, :ref:`example-pick-ring-gripper`).

.. image:: /assets/images/documentation/picking/pick_point_data_blocks_flexible_offset.png

Using the **pick point offset**, the block position is first corrected, and only then dropped on top of the previously picked blocks.

.. raw:: html

  <iframe src="https://drive.google.com/file/d/1Ut1F9RQORHGMIyVTXPl4Dt_uhE48eA0o/preview" frameborder="0" allowfullscreen width="640" height="480"></iframe>
  <br>

|

.. _smart-place-pick-point-reference:

Same drop-off when picking with different pick points
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the following example, the object model contains three pick points.
It is desired that the object is always picked by the highest possible pick point, to minimize the likelihood of collisions.
Since the objects are oriented in different ways, the highest pick point will not always be the same.

.. image:: /assets/images/documentation/picking/pick_point_data_shape_multiple_offset.png

Having multiple pick points increases the chance of an object being pickable.
However, defining the same number of drop-off poses would be time-consuming, error-prone, as well as introduce complex logic in the robot program.
Thanks to the ability to :ref:`define reference pick points <pick-point-reference>`, only one drop-off pose is defined in this example.
Having one pick point as the reference of the other two, the robot program only needs to define the drop-off position of the reference.
The **pick point offset**, which is the offset between the actual pick point and its reference, is used to correct the drop-off position, allowing the object to always be placed in the same way, regardless of which pick point was used to pick it.

.. details:: Robot program snippet (click to expand)

  .. literalinclude:: code/pick-point-offset.py
    :language: python

  Where ``Dropoff`` was defined for the reference pick point.
  Learn more about ``PickPointOff`` :ref:`here <robot-independent-pickit-pick-off>`.

|

.. raw:: html

  <iframe src="https://drive.google.com/file/d/1OUK9VyHi-C_O5IFim4eg1wdEBQp4qqGw/preview" frameborder="0" allowfullscreen width="640" height="480"></iframe>
  <br>

|

.. note:: This article shows examples where the pick point data is used for smart object **placing**.
          However, pick point information can also be used for smart object **picking**, such as:

            - Different gripper settings depending on the pick point (see example below).
            - Different grippers for different pick points.
            - Different approach or retreat motions depending on the pick point.

          .. image:: /assets/images/documentation/picking/pick_point_different_gripper_settings.png
