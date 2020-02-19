.. _urcap-pick-and-place-template:

Pick and place template
=======================

The Pickit pick and place template is a program node for executing vision-guided pick and place tasks with *minimal programming effort*.
It provides an easy and intuitive interface for specifying relevant application knowledge, and abstracts away the complexity required to robustly execute the task.

This article presents the pick and place template in detail.
Refer to the companion articles for an :ref:`example pick and place program <urcap-pick-and-place-program>` and the :ref:`interface documentation <urcap-interface>`  (exposed variables and additional commands).

.. contents::
    :backlinks: top
    :local:
    :depth: 2

.. image:: /assets/images/robot-integrations/ur/pick-and-place-overview.png
  :align: center

.. note::
  The Pickit Pick and place template is only available for **URCap 2.0** or later and **Pickit 2.2** or later.
  Installation instructions can be found :ref:`here <universal-robots-urcap-installation>`.

  The Pickit Pick and place template supercedes the :ref:`low-level interface <urcap-low-level-interface>` from :ref:`URCap version 1 <universal-robots-urcap-v1>` as the preferred way to set up a pick and place application, although both ways of working are supported.


.. _template-insert:

Inserting the template
----------------------

The pick and place template can be inserted in a robot program by selecting :guilabel:`Program` in the header bar, then :guilabel:`URCaps` → :guilabel:`Pickit: pick and place` on the left panel.

.. image:: /assets/images/robot-integrations/ur/pick-and-place-insert-template.png
  :scale: 70%
  :align: center

On insertion, you need to answer two basic questions about your application on the right panel and click :guilabel:`Done` for the template to initialize.

.. image:: /assets/images/robot-integrations/ur/pick-and-place-basic-configuration.png
  :scale: 70%
  :align: center

Power users can fine-tune pick and place behavior to a much finer degree than what the basic questions allow by entering the :guilabel:`Advanced configuration`.
For instance, pick and place will by default continue until no more pickable objects are found, but it's also possible to stop after a user-specified number of successful picks.

The pick and place template consists of a :ref:`top-level node <template-pick-and-place>`, three main sequences responsible for :ref:`object detection <template-object-detection>`, :ref:`pick <template-pick>` and :ref:`place <template-place>` actions, and :ref:`optional actions <template-optional-actions>` that can be selectively enabled according to the needs of the application.

.. image:: /assets/images/robot-integrations/ur/pick-and-place-tree.png
  :align: center

.. note::
  Lines marked in yellow by Polyscope indicate that they (or their nested commands) have uninitialized input parameters that must be set before running the program.


The template explained
----------------------

The following statechart depicts the execution logic for the default pick and place configuration and a fixed camera mount.
Optional actions are shown in dashed lines, and the places where Pickit is busy performing object detection are shown in green.
Note that in the lower-right, object detection runs in parallel to the :ref:`place <template-place>` sequence, which saves cycle time.
If this parallel execution is not desired, it can be disabled in the :ref:`advanced configuration <template-pick-and-place>`.

.. image:: /assets/images/robot-integrations/ur/pick-and-place-statechart.png
  :scale: 60%
  :align: center

.. _template-waypoints:

The motions involved in pick and place involve a number of waypoints, some of which are :ref:`computed by Pickit <urcap-global-variables-picking>` (prefixed with ``Pickit`` and shown in green below), and three (in blue) which are user-defined:

-  ``Detect`` from where to perform :ref:`object detection <template-object-detection>`. Refer to :ref:`this article <robot-position-during-capture>` for guidelines on how to make a good choice.
-  ``Dropoff`` where to :ref:`place <template-place>` objects.
-  ``AbovePickArea`` a point roughly above the :ref:`pick <template-pick>` area from which the above two can be reached without collision. In simple scenarios, it can be the same as ``Detect``.

.. image:: /assets/images/robot-integrations/ur/pick-and-place-waypoints.png
  :align: center

.. _template-pick-and-place:

Pick and place
--------------

The top-level node is meant for monitoring Pickit by showing a live camera stream overlaid with the ROI and detected objects (the same as the web interface :ref:`2D view <2d-view>`).
It also allows to access and modify the general pick and place :guilabel:`Configuration` (basic and advanced) which was set when :ref:`inserting the template <template-insert>`.

Inputs and configuration that are specific to the :ref:`object detection <template-object-detection>`, :ref:`pick <template-pick>` or :ref:`place <template-place>` actions are specified in the corresponding action.

.. image:: /assets/images/robot-integrations/ur/pick-and-place-top-level-node.png
  :scale: 70%
  :align: center

Note that below the camera stream the connectivity to the Pickit system is displayed.
The following are two examples of the Pickit system being connected and not:

.. image:: /assets/images/robot-integrations/ur/pick-and-place-status-examples.png
  :scale: 80%
  :align: center

.. _template-object-detection:

Object detection
~~~~~~~~~~~~~~~~

This sequence triggers a Pickit object detection.

.. image:: /assets/images/robot-integrations/ur/pick-and-place-object-detection.png
  :align: center

**Required inputs**

- ``Detect`` user-defined :ref:`waypoint <template-waypoints>`.

  .. tip::
    Some applications using a robot-mounted camera benefit from having extra logic that modifies the ``Detect`` point as the program executes. Examples:

    - De-palletizing, where the camera viewpoint lowers after emptying each layer.
    - Multiple viewpoints to cover bins wider than the camera field of view.

- ``Find object`` node: Set the Pickit :ref:`configuration <Configuration>` (setup and product) that should be used for object detection.

.. image:: /assets/images/robot-integrations/ur/pick-and-place-find-object.png
  :scale: 70%
  :align: center

.. _template-pick:

Pick
~~~~

This sequence performs the actual picking motion, which consists of a linear approach to the pick point, a grasping action, and a linear retreat away from it.

.. image:: /assets/images/robot-integrations/ur/pick-and-place-pick.png
  :align: center

.. tip::
  If your robot tool have the means to check pick success, consider incorporating this :ref:`optional check <template-pick-success>` to save cycle time.

**Required inputs**

- ``AbovePickArea`` user-defined :ref:`waypoint <template-waypoints>`.
- ``Tool action: Grasp`` folder: Populate with user-defined grasp logic.

  .. note::
    Its location in the Pick sequence depends on the gripper type set in the pick and place :ref:`configuration <template-pick-and-place>`.
    It can be located before (suction or similar) or after (fingered or similar) ``PickitPick``.

.. _template-pick-pick-strategy:

**Optional inputs**

- ``Pick`` node: Select a strategy for computing ``PickitPrePick`` and ``PickitPostPick``, used in the approach and retreat motions, respectively.

  .. image:: /assets/images/robot-integrations/ur/pick-and-place-pick-strategy.png
    :scale: 70%
    :align: center

.. _template-place:

Place
~~~~~

This sequence places the picked object at the specified dropoff location.

.. image:: /assets/images/robot-integrations/ur/pick-and-place-place.png
  :align: center

**Required inputs**

- ``Dropoff`` user-defined :ref:`waypoint <template-waypoints>`.

  .. tip::
    Some applications require a non-constant dropoff point, such as when parts need to be stacked or palletized.
    In such a case, ``Dropoff`` can be replaced with an instance of Universal Robot's **Palletizing** template, for instance.

- ``Tool action: Release``: Populate with user-defined release logic.

.. _template-optional-actions:

Optional actions
~~~~~~~~~~~~~~~~

The advanced :ref:`configuration <template-pick-and-place>` lists a number of optional actions whose execution can be enabled or disabled during pick and place.
Their default contents are a suggestion, and can be modified.

.. _template-action-before-start:

Action before start
^^^^^^^^^^^^^^^^^^^


This sequence is executed *once* before starting pick and place.
The default implementation performs a *Release* tool action, to prepare the gripper for picking.

This sequence is disbled by default.

.. image:: /assets/images/robot-integrations/ur/pick-and-place-action-before-start.png
  :align: center

.. _template-action-after-end:

Action after end
^^^^^^^^^^^^^^^^

This sequence is executed *once* after pick and place has finished.
The default implementation identifies the termination reason and raises a popup if there are no more pickable objects.
Pickit can discriminate the following situations:

- **Empty ROI:** The :ref:`Region of Interest (ROI) <region-of-interest>` has nothing inside.
- **No objects found:** The ROI is not empty, but the requested object was not found.
- **No reachable objects:** The requested object was found, but is unreachable by the robot.
- **No image captured:** Pickit failed to capture a camera image, possibly due to the camera being disconnected.

This sequence is enabled by default as it provides useful information when setting up or debugging the application.

.. image:: /assets/images/robot-integrations/ur/pick-and-place-action-after-end.png
  :align: center

.. _template-pick-success:

Pick success check
^^^^^^^^^^^^^^^^^^

If your robot tool has the means to check pick success from sensor input (like vacuum or force), the :ref:`Place <template-place>` sequence can be skipped on pick failure, and save cycle time.
The robot will instead proceed to pick a new object.

This action is disabled by default, as it requires additional user input.
When enabled, it adds the following extra logic at the end of the :ref:`Pick <template-pick>` sequence.

  .. image:: /assets/images/robot-integrations/ur/pick-and-place-pick-success-check.png
    :align: center
