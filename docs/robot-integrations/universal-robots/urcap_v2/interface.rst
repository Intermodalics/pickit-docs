.. _urcap-interface:

The Pickit URCap interface
==========================

Pickit integrates seamlessly with **Universal Robots** by means of a **URCap plugin**.
This plugin allows to perform vision-guided pick and place with *minimal* programming effort.
For installation instructions please refer to the :ref:`universal-robots-urcap-installation` article.

This article documents the global variables exposed by the :ref:`pick and place template <urcap-pick-and-place-template>`, as well as additional commands and helper functions that can be used in conjuction with it.

.. contents::
    :backlinks: top
    :local:
    :depth: 2


.. _urcap-global-variables:

Global variables
----------------

.. _urcap-global-variables-picking:

Picking
~~~~~~~

These variables are used by the :ref:`pick and place template <urcap-pick-and-place-template>` in the :ref:`Pick <template-pick>` sequence.
They refer to the currently selected object for picking.

.. _urcap-pickit-pick:

+------------------------------------------------------------------------------+
| **PickitPick**                                                               |
+==============================================================================+
| Object pick point, represented as a pose variable.                           |
+------------------------------------------------------------------------------+

.. _urcap-pickit-pre-pick:

+------------------------------------------------------------------------------+
| **PickitPrePick**                                                            |
+==============================================================================+
| Object pre-pick point, represented as a pose variable.                       |
|                                                                              |
| This point is used for performing a linear approach motion to                |
| :ref:`PickitPick <urcap-pickit-pick>`.                                       |
| The strategy used for computing the pre-pick point can be specified in the   |
| :ref:`Pick <template-pick-pick-strategy>` node configuration.                |
+------------------------------------------------------------------------------+

.. _urcap-pickit-post-pick:

+------------------------------------------------------------------------------+
| **PickitPostPick**                                                           |
+==============================================================================+
| Object post-pick point, represented as a pose variable.                      |
|                                                                              |
| This point is used for performing a linear retreat motion from               |
| :ref:`PickitPick <urcap-pickit-pick>`.                                       |
| The strategy used for computing the post-pick point can be specified in the  |
| :ref:`Pick <template-pick-pick-strategy>` node configuration.                |
+------------------------------------------------------------------------------+

.. _urcap-advanced-picking:

Advanced picking
~~~~~~~~~~~~~~~~

These variables expose additional information that can be used when picking an object.
They refer to the currently selected object for picking, and are not used by default by the :ref:`pick and place template <urcap-pick-and-place-template>`.
Learn more about when and how you should use them in the :ref:`smart placing examples <smart-place-examples>`.

.. _urcap-pickit-pick-id:

+--------------------------------------------------------------------------+
| **PickitPickId**                                                         |
+==========================================================================+
| ID of the pick point that was selected for picking, represented as an    |
| integer.                                                                 |
+--------------------------------------------------------------------------+

.. _urcap-pickit-pick-ref-id:

+--------------------------------------------------------------------------+
| **PickitPickRefId**                                                      |
+==========================================================================+
| ID of the pick point with respect to which                               |
| :ref:`PickitPickId <urcap-pickit-pick-id>` was created, represented as   |
| an integer.                                                              |
|                                                                          |
| If the pick point associated to                                          |
| :ref:`PickitPickId <urcap-pickit-pick-id>` was not created with respect  |
| to another pick point, this value will be the same as                    |
| :ref:`PickitPickId <urcap-pickit-pick-id>`.                              |
+--------------------------------------------------------------------------+


.. _urcap-pickit-pick-off:

+--------------------------------------------------------------------------+
| **PickitPickOff**                                                        |
+==========================================================================+
| Pick point offset, represented as a pose variable.                       |
|                                                                          |
| This is the relative transformation between the reference pick point     |
| (identified by :ref:`PickitPickRefId <urcap-pickit-pick-ref-id>`) and    |
| the pick point that was selected for picking (identified by              |
| :ref:`PickitPickId <urcap-pickit-pick-id>`).                             |
|                                                                          |
| If the ``Dropoff`` point is expressed with respect to                    |
| :ref:`PickitPickRefId <urcap-pickit-pick-ref-id>`, you can compensate    |
| for the offset to :ref:`PickitPickId <urcap-pickit-pick-id>` by          |
| post-multiplying ``Dropoff`` by ``PickitPickOff``, i.e.                  |
|                                                                          |
| ``DropoffCorrected = pose_trans(Dropoff, PickitPickOff)``                |
+--------------------------------------------------------------------------+

Object information
~~~~~~~~~~~~~~~~~~

These variables expose additional information about the object beyond where to pick it.
They refer to the latest object detection results sent by Pickit, and are not used by default by the :ref:`pick and place template <urcap-pick-and-place-template>`.

.. _urcap-pickit-obj-type:

+--------------------------------------------------------------------------+
| **PickitObjType**                                                        |
+==========================================================================+
| Object type, represented as an integer.                                  |
|                                                                          |
| The mapping between the object type and its identifier is the following: |
|                                                                          |
| **Pickit Teach** Teach model ID                                          |
|   Use this value to conditionally perform an action depending on the     |
|   detected model. See also :ref:`urcap-advanced-picking`.                |
|                                                                          |
| **Pickit Flex and Pattern**                                              |
|                                                                          |
| -  **Square** 21                                                         |
| -  **Rectangle** 22                                                      |
| -  **Circle** 23                                                         |
| -  **Ellipse** 24                                                        |
| -  **Cylinder** 32                                                       |
| -  **Sphere** 33                                                         |
| -  **Blob** 50                                                           |
+--------------------------------------------------------------------------+

.. _urcap-pickit-obj-dim:

+--------------------------------------------------------------------------+
| **PickitObjDim**                                                         |
+==========================================================================+
| Object dimensions, in meters, represented as a 3D array.                 |
|                                                                          |
| Depending on the object type, the array should be interpreted as follows:|
|                                                                          |
| **Pickit Teach** ``[bbox x, bbox y, bbox z]``                            |
|   Where ``bbox x`` represents the size of the object bounding box along  |
|   its x-axis.                                                            |
|                                                                          |
| **Pickit Flex and Pattern**                                              |
|                                                                          |
| -  **Square** ``[length, length, 0]``                                    |
| -  **Rectangle** ``[length, width, 0]``                                  |
| -  **Circle** ``[diameter, diameter, 0]``                                |
| -  **Ellipse** ``[length, width, 0]``                                    |
| -  **Cylinder** ``[length, diameter, diameter]``                         |
| -  **Sphere** ``[diameter, diameter, diameter]``                         |
| -  **Blob** ``[bbox x, bbox y, bbox z]``                                 |
+--------------------------------------------------------------------------+

.. _urcap-pickit-obj-age:

+--------------------------------------------------------------------------+
| **PickitObjAge**                                                         |
+==========================================================================+
| Object age, represented as a floating-point number.                      |
|                                                                          |
| This object age is the duration, in seconds, elapsed between the         |
| capturing of the camera image and the moment the object information is   |
| sent to the robot.                                                       |
+--------------------------------------------------------------------------+

.. _urcap-commands:

Commands
--------

This section presents a set of commands that add to Polyscope’s existing ones.
In Polyscope 5, they can be inserted in a robot program by selecting :guilabel:`Program` in the header bar, then, on the left panel :guilabel:`URCaps` → :guilabel:`Pickit: commands`.

.. image:: /assets/images/robot-integrations/ur/urcap-interface-commands.png
  :scale: 70%
  :align: center

Next, navigate to the **Command** tab on the right panel select an entry from the **Pickit** **command** drop-down.

.. image:: /assets/images/robot-integrations/ur/urcap-interface-command-dropdown.png
  :scale: 80%
  :align: center

.. _urcap-commands-picking:

Picking.
~~~~~~~~

These are optional commands that can be added to a pick and place robot program, for instance, inside one of the sequences of the :ref:`pick and place template <urcap-pick-and-place-template>`.

.. _command-save-snapshot:

+--------------------------------------------------------------------------+
| **Save snapshot**                                                        |
+==========================================================================+
| Save a snapshot with the latest detection results.                       |
|                                                                          |
| The saved snapshot can then be loaded or downloaded by going to the      |
| :ref:`Snapshots` page on the Pickit web interface and searching for      |
| a file whose name contains the capture timestamp.                        |
|                                                                          |
| **Example usage:** Trigger saving a snapshot on the                      |
| :ref:`action after end <template-action-after-end>` sequence, when no    |
| objects are found (but the ROI is not empty), so it's possible to        |
| investigate the cause.                                                   |
+--------------------------------------------------------------------------+

.. _command-build-background:

+--------------------------------------------------------------------------+
| **Build background**                                                     |
+==========================================================================+
| Build the background cloud used by some of the                           |
| :ref:`advanced Region of Interest filters <advanced-roi-filters>`.       |
|                                                                          |
| Calling this function will trigger a camera capture, so if the camera    |
| mount is fixed, the robot must not occlude the camera view volume.       |
| If instead the camera is robot-mounted, the robot must be in the         |
| detection point (:ref:`more <robot-position-during-capture>`).           |
+--------------------------------------------------------------------------+

Calibration
~~~~~~~~~~~

There is a single command meant to be used in a :ref:`calibration robot program <universal-robots-urcap-calibration>`, and not in a pick and place program.

.. _command-find-calibration-plate:

+--------------------------------------------------------------------------+
| **Find calibration plate**                                               |
+==========================================================================+
| Trigger detection of the robot-camera calibration plate.                 |
|                                                                          |
| This command requires the Pickit web interface to be in the              |
| :ref:`Calibration <robot-camera-calibration>` page, hence robot mode     |
| should be disabled.                                                      |
| When Pickit is not in the :ref:`Calibration <robot-camera-calibration>`  |
| page, a pop-up is shown.                                                 |
+--------------------------------------------------------------------------+


.. _urcap-helper-functions:

Helper functions
----------------

Helper functions return useful information about picking. They are typically used as the expression of a conditional, such as an ``if`` statement, and can be selected from the ``Function`` drop-down. 

.. image:: /assets/images/robot-integrations/ur/urcap-interface-command-function-dropdown.png
  :scale: 70%
  :align: center

.. _urcap-helper-empty-roi:

+--------------------------------------------------------------------------+
| **pickit_empty_roi()**                                                   |
+==========================================================================+
| Call this function in the optional                                       |
| :ref:`action after end <template-action-after-end>` sequence to check if |
| there are no more pickable objects because of an empty                   |
| :ref:`Region of Interest (ROI) <region-of-interest>`.                    |
|                                                                          |
| This check is included in the default implementation of                  |
| :ref:`action after end <template-action-after-end>`.                     |
|                                                                          |
| **Return** ``true`` if Pickit detected an empty ROI.                     |
+--------------------------------------------------------------------------+

.. _urcap-helper-no-object-found:

+--------------------------------------------------------------------------+
| **pickit_no_object_found()**                                             |
+==========================================================================+
| Call this function in the optional                                       |
| :ref:`action after end <template-action-after-end>` sequence to check if |
| there are no more pickable objects because the requested object is not   |
| found, but the :ref:`ROI <region-of-interest>` is not empty.             |
|                                                                          |
| This check is included in the default implementation of                  |
| :ref:`action after end <template-action-after-end>`.                     |
|                                                                          |
| **Return** ``true`` if there are no pickable objects, but the ROI is not |
| empty.                                                                   |
+--------------------------------------------------------------------------+

.. _urcap-helper-no-object-reachable:

+--------------------------------------------------------------------------+
| **pickit_no_object_reachable()**                                         |
+==========================================================================+
| Call this function in the optional                                       |
| :ref:`action after end <template-action-after-end>` sequence to check if |
| there are no more pickable objects because they are detected but         |
| unreachable by the robot.                                                |
|                                                                          |
| This check is included in the default implementation of                  |
| :ref:`action after end <template-action-after-end>`.                     |
|                                                                          |
| **Return** ``true`` If there are detected objects, but all are           |
| unreachable.                                                             |
+--------------------------------------------------------------------------+

.. _urcap-helper-no-image-captured:

+--------------------------------------------------------------------------+
| **pickit_no_image_captured()**                                           |
+==========================================================================+
| Call this function in the optional                                       |
| :ref:`action after end <template-action-after-end>` sequence to check if |
| there are no more pickable objects because Pickit failed to capture a    |
| camera image.                                                            |
|                                                                          |
| When this is the case, it typically indicates a hardware disconnection   |
| issue, such as a loose connector or broken cable. This function can be   |
| used as trigger to send an alarm to a higher level monitoring system.    |
|                                                                          |
| This check is included in the default implementation of                  |
| :ref:`action after end <template-action-after-end>`.                     |
|                                                                          |
| **Return** ``true`` if there are no pickable objects due to a failed     |
| image capture.                                                           |
+--------------------------------------------------------------------------+

.. _urcap-helper-remaining-objects:

+--------------------------------------------------------------------------+
| **pickit_remaining_objects()**                                           |
+==========================================================================+
| Call this function in the :ref:`Pick <template-pick>`,                   |
| :ref:`Place <template-place>`, or the optional                           |
| :ref:`action after end <template-action-after-end>` sequence to query    |
| the remaining number of detected (but potentially unpickable) objects    |
| from the last object detection run.                                      |
|                                                                          |
| **Return** The number of remaining detected objects.                     |
+--------------------------------------------------------------------------+


Low-level interface
-------------------

Apart from the :ref:`pick and place template <urcap-pick-and-place-template>`, Pickit offers a :ref:`low-level interface <urcap-low-level-interface>`.
It exists mainly for backward compatibility with the :ref:`URCap version 1 <universal-robots-urcap-v1>`, and for power users that need to implement application logic that cannot be represented by the pick and place template.
