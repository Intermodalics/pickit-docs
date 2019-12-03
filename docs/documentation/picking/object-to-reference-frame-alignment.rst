Object to reference frame alignment
-----------------------------------

.. note:: This setting is only available with the Flex and Pattern
   engine.


This setting aligns the object frame axis with a reference frame axis.
The newly created aligned frame is the pick point that will be sent to
the robot. The setting smartly makes use of the symmetry of an object to
decide if object axes can be flipped so they point to the same direction
as the selected reference frame axes.

Two settings need to be provided to make this work:

-  The **axis of the object frame** to align. The provided options are X
   or Y.
-  And the **axis of the reference frame** to align the object axis
   with. The provided options are X, -X, Y, -Y, Z or -Z.

The pictures below show examples of the object to reference frame
alignment setting for rectangular and circular shapes respectively:

.. image:: /assets/images/Documentation/Object-to-reference-frame-alignment.png