.. _release-notes:

Software release 2.3
====================

The new features of the 2.3 release revolve around improving flat object detection and robot tool definition.

1. Flat object detection
------------------------

Pickit :ref:`Teach <teach>` is great for detecting objects with a distinctive 3D shape.
Flat objects are different from other 3D shapes in the sense that edges are the main source of shape information.

This release enables Pickit Teach to :ref:`detect flat objects <teach-flat-objects-note>` more reliably by focusing on shape edges.

.. image:: /assets/images/documentation/detection/teach/flat_objects.png
  :align: center
  :scale: 70%

2. Define your tool model from a CAD file
-----------------------------------------

In the previous 2.2 release, we added support for :ref:`teaching part models from CAD <teach-from-cad>`.
In this release, we extend this so you can also :ref:`define your tool model from a CAD file <cad-tool>`.

.. image:: /assets/images/documentation/picking/define_tool.png
  :align: center

.. image:: /assets/images/documentation/picking/tool_model_cad_ui.png
  :align: center

Alternatively, if a CAD file for your tool is not readily available, you can still define your tool using the existing :ref:`generic tool models <generic-tool>`.

3. Assign different tools to different pick points
--------------------------------------------------

It's now possible to create multiple :ref:`tool models <robot-tool-model>`, and assign different tools to different pick points.
A common example would be a two-finger gripper used with different opening distances depending on the selected pick point.

.. image:: /assets/images/documentation/picking/different_gripper_openings.png
  :align: center

Get the update now
------------------

If you have an older Pickit version and would like to try 2.3, check out :ref:`how you can upgrade your system <Pickit-system-software-upgrade>`.
