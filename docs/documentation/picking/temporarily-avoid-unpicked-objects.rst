.. _temporarily-avoid-unpicked-objects:

Temporarily avoid unpicked objects
==================================

Unavoidably, Pickit might fail to pick some objects. This is inherent to the unstructured aspect of bin picking.
A typical example is when an object is locked by its neighbors and that the gripper is not strong enough to grasp it.

In these situations, it is important to prevent the robot from repeateadly going to the same "hard to pick" object.
Otherwise, the cycle time of the application can significantly drop and in the worst cases the robot program might be stuck at trying to always pick the same "unpickable" object.

The purpose of the **temporarily avoid unpicked objects** functionality is to avoid exactly that.
If an object that was recently sent to the robot for picking is detected again, it will temporarily be deprioritized for picking.
This article describes this functionality.

How it works
------------

Pickit keeps track of the objects that were recently sent to the robot for picking in the so-called `avoid list`.
If an object of the `avoid list` is detected again, it is considered as an object that failed to be picked.
This object will then be put at the bottom of the object list, i.e. it is deprioritized for picking.
In other words, Pickit will avoid to pick this object, if other objects are pickable they will be preferred.

.. note::
  The list of object to avoid only concerns object sent to the robot. It is therefore only updated when in robot mode.

Objects temporarily put at the bottom of the list are indicated in the :ref:`detection grid <detection-grid>` as shown below.

.. image:: /assets/images/documentation/picking/blacklist_object_table.png

The parameters explained
------------------------

Once enabled, 2 parameters need to be configured for the temporary object rejection.

The **number of run to avoid** is the number of detections an object stays in the avoid list.
For example, if set to 5, a missed object will be pull to the bottom of the list for the 5 next detections.
After that it will not be deprioritized anymore.

The **Proximity tolerance** is the distance used to evaluate if a detected object should be avoided.
If the pick point of a detected object is within this distance to the pick point of an object of the avoid list, it will be deprioritized.

For conveninence, a :guilabel:`Reset` button that clears the avoid list is available.
It can be helpful when setting up an application. 