.. _temporarily-avoid-unpicked-objects:

Temporarily avoid unpicked objects
==================================

On occasions, it happens that an object detected by Pickit cannot be picked by the robot. A typical example is when the gripper is not strong enough to establish a firm pick on an object that is locked in place by neighboring parts.

In these situations, it is important to prevent the robot from repeatedly going to the same hard to pick object, and potentially get stuck in an endless loop.
By reaching out to other pickable objects instead of insisting on a hard pick, the application moves forward, cycle time becomes more consistent, and the hard to pick object eventually can become pickable.

This is the purpose of the **temporarily avoid unpicked objects** functionality.
If an object that was recently sent to the robot for picking is detected again, it will temporarily be deprioritized for picking.

How it works
------------

Pickit keeps track of the objects that were recently sent to the robot for picking in the so-called `avoid list`.
If an object of the `avoid list` is detected again, it is considered as an object that failed to be picked.
This object will then be deprioritized and put at the bottom of the `pickable` object list.
In other words, Pickit will avoid to pick this object, as long as there are other objects to be picked.

.. note::
  The list of objects to avoid only operates when robot mode is enabled. It is updated from objects sent to the robot, and not from detections triggered from the :ref:`Pickit web interface <web-interface>`.
  
  Pickit :ref:`snapshots <Snapshots>` preserve the list of objects to avoid that was active at the time of saving.

Objects temporarily put at the bottom of the list are indicated in the :ref:`detection grid <detection-grid>` as shown below.

.. image:: /assets/images/documentation/picking/blacklist_object_table.png

The parameters explained
------------------------

Once enabled, two parameters need to be configured:

The **number of runs to avoid** is the number of detection runs an object stays in the avoid list.
For example, when set to 5, an initially unpicked object will be pushed to the bottom of the pickable objects list for the 5 next detections (if detected again).
After that, the object will no longer be deprioritized.

The **Proximity tolerance** is the distance used for matching a detection against the avoid list.
If the pick point of a detected object is within this distance to a pick point stored in the avoid list, it will be deprioritized.

For convenience, a :guilabel:`Reset` button that clears the avoid list is available.
It can be helpful when setting up an application. 
