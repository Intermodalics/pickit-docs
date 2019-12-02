.. _check-collisions-with:

Check collisions with the robot tool
------------------------------------

This setting allows you to discard pick points that would result in collision. The pick points can be checked for possible collisions with the bin and/or other objects.

When collision checking yields that a certain object pose will result in
a collision,  the object will be labeled as unpickable and not sent to
the robot. In the Pickit web interface, unpickable objects are
displayed orange in the :ref:`Objects view <objects-view>` and the :ref:`detection-grid`.
When clicking on the unpickable object, the modeled tool will appear in
the :ref:`Objects view <objects-view>` to illustrate why the given object is
unpickable.

Bin
~~~

This option checks if the tool is colliding with the Region of Interest.
If set the tool is not allowed to hit the sides or bottom of the
region of interest box. If the Region of interest box is set to similar
dimensions as the actual bin, this option is checking for collisions
with the actual bin. A rule of thumb for this to work properly is to set
the dimensions of the region of interest box slightly smaller and
slightly higher than the real bin.

.. image:: /assets/images/Documentation/check-collision-with-bin-21.png

Other objects
~~~~~~~~~~~~~

This option checks if the tool is colliding with other objects that are
visible in the Region of Interest. As seen in the image below the object
is not safe to pick because there is another object on top and the tool
would collide with this other object.

.. image:: /assets/images/Documentation/check-collision-with-other-objects-21.png
