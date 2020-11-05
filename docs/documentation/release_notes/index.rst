.. _release-notes:

Software release 2.4
====================

Pickit 2.4 has been created with one main goal in mind: Improving the experience of ramping up bin-picking applications into production.
Special attention was given to cylindrical shaped objects, such as billets, which is a commonly observed application in the forging industry.

Teach cylinder model
--------------------

The Teach engine has been upgraded to support :ref:`cylinder models<teach-cylinder>`, which is ideal for detecting billets.
Whereas before you had to teach a cylindrical part by placing it under the camera or uploading a CAD file, now you only need to specify a length and diameter.
Choose how you intend to pick the cylinders, and Pickit takes care of the pick point definition for you.
Furthermore, by letting Pickit exploit the cylindrical geometry, both detection speed and accuracy are optimized.

.. image:: /assets/images/documentation/detection/teach/teach_cylinder_wizard_and_model.png
  :align: center

.. image:: /assets/images/documentation/detection/teach/billets_example.png
  :scale: 80%
  :align: center

Are you picking several types of billets, but don't want to open the web interface to teach a new model everytime?
Now you can optionally :ref:`set the cylinder dimensions directly from the robot program <RC_PICKIT_SET_CYLINDER_DIM>`, speeding up the setup of different production settings.

Shape symmetry
--------------

If you want to pick a symmetric part like a billet, a ring or a shaft, you can now specify its :ref:`symmetry axis<pick-point-symmetry-axis>` and make pick points aware of it.
Pickit exploits the motion freedom introduced by this symmetry to increase the likelihood of the part being pickable.

.. image:: /assets/images/documentation/picking/symmetry_axis.png
  :align: center

Flexible tools instead of flexible pick points
----------------------------------------------

In Pickit 2.2, we introduced the concept of flexible pick orientation, which allows pick points to tolerate some orientation variability without compromising pick success.
This can, in fact, increase the likelihood that a part is pickable.

In Pickit 2.4, we moved the specification of this flexibility from the pick point to the :ref:`robot tool definition <flexible-pick-orientation>`.
Don't worry! Your existing product files will be automatically converted to this new specification.

.. image:: /assets/images/documentation/picking/tool_flexibility.png
  :scale: 80%
  :align: center

Minimum distance between robot flange and bin
---------------------------------------------

It is sometimes desired that the robot flange, when picking objects, does not deviate too much laterally above the :ref:`ROI <region-of-interest>` or bin.
This is particularly relevant when there are collision obstacles close to the bin like poles, fences or other tall structures, as shown below.
It is now possible to limit how much the :ref:`robot flange is allowed to deviate away from the bin walls <flange-filter>`.

.. image:: /assets/images/documentation/picking/flange_filter.png

Temporarily avoid unpicked objects
----------------------------------

The success of many applications, like forging, relies on a steady flow of picked objects, which in practice can be hindered by various reasons.
A typical example is when the gripper is not strong enough to establish a firm pick on an object that is locked in place by neighboring parts.
In these situations, it is important to :ref:`temporarily avoid unpicked objects <temporarily-avoid-unpicked-objects>`, and prevent the robot from repeatedly going to the same hard-to-pick object, and potentially get stuck in an endless loop.

.. image:: /assets/images/documentation/picking/blacklist_object_table.png

Picking experience in Flex
--------------------------

Pickit Flex now benefits from all the picking improvements that have been added to Pickit Teach since version 2.2, like :ref:`flexible pick orientation <flexible-pick-orientation>`, :ref:`symmetry axes<pick-point-symmetry-axis>`, and the different :ref:`pick strategy <pick-strategy>` options.

If you are picking basic shaped-objects with mixed dimensions, Pickit will find more pickable parts with potentially less robot motions.

.. image:: /assets/images/documentation/picking/flex_pick_flexibility.png

Get the update now
------------------

If you have an older Pickit version and would like to try 2.4, check out :ref:`how you can upgrade your system <Pickit-system-software-upgrade>`.
