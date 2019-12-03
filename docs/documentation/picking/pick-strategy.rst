Pick strategy
-------------

.. note::
  This setting is only available for **cylinder** and **sphere** detections with the **Flex engine**.

This setting allows you to move the pick point to the real surface of
the detected object instead of the center of the object. The possible
options are:

-  Default: The default object frame will be used, which is a frame in
   the center of the cylinder or sphere. This option does not modify the
   pick point.
-  Surface top: The pick point will move to the center at the top
   surface of the object.
-  Surface visible: The pick point will move to the center of the
   visible part of the object. This setting is useful to avoid
   collisions when the detected object is partially covered by another
   object.
-  End circle: The pick point will be moved to the highest circular end
   of the cylinder.

.. note::
  The resulting pick point axes will not necessarily be parallel to one of the reference frame axes. If you want this, use the **Enforce alignment of pick point orientation** option.

The picture below shows an example of a spherical and cylindrical object
respectively:

.. image:: /assets/images/Documentation/Pick-strategy-example.png