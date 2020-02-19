.. _urcap-low-level-interface:

The Pickit low-level URCap interface
====================================

This article documents the Pickit low-level URCap interface, which consists of a set of global variables, commands and helper functions that allow you to explicitly write the logic of a pick and place application.
A companion article describes an :ref:`example robot program <universal-robots-urcap-example-v1>` written using the low-level interface.

.. note::
  The low-level interface exists mainly for backward compatibility with the :ref:`URCap version 1 <universal-robots-urcap-v1>`, and for power users that need to implement application logic that cannot be represented by the :ref:`pick and place template <urcap-pick-and-place-template>`.

  The :ref:`pick and place template <urcap-pick-and-place-template>` is the preferred way to set up a new pick and place application, as it requires a lower programming effort, and implements a robust execution logic under the hood.

.. contents::
    :backlinks: top
    :local:
    :depth: 2

Global variables
----------------

The URCap plugin exposes global variables under their version 2 names (``CamelCase``), and also under the version 1 names (``snake_case``) for backward compatibility.
For new programs, the version 2 names are recommended.

- :ref:`PickitPick <urcap-pickit-pick>`, also exposed as ``pickit_pose``.
- :ref:`PickitPrePick <urcap-pickit-pre-pick>`, also exposed as ``pickit_pre_pose``.
- :ref:`PickitObjType <urcap-pickit-obj-type>`, also exposed as ``pickit_type``.
- :ref:`PickitObjDim <urcap-pickit-obj-dim>`, also exposed as ``pickit_dim``.

Commands
--------

Picking
~~~~~~~

.. _command-robot-mode-enabled:

+--------------------------------------------------------------------------+
| **Check if robot mode enabled**                                          |
+==========================================================================+
| Checks whether robot mode is enabled in Pickit.                          |
|                                                                          |
| -  If robot mode is enabled, program execution continues.                |
| -  If robot mode is not enabled, a pop-up asks the user if it wants to   |
|    enable it from the robot (as long as there are no unsaved changes).   |
|    Robot mode can also be enabled from the Pickit                        |
|    :ref:`web interface <web-interface-top-bar>`.                         |
|                                                                          |
| All commands listed below require robot mode to be enabled.              |
+--------------------------------------------------------------------------+

.. _command-select:

+--------------------------------------------------------------------------+
| **Select**                                                               |
+==========================================================================+
| Loads the specified setup and product configuration.                     |
| This configuration specifies the behavior of Pickit detections, e.g.     |
| what to look for, in which part of the field of view.                    |
|                                                                          |
|                                                                          |
| **Parameters**                                                           |
|                                                                          |
| - **Setup**                                                              |
|                                                                          |
|   Any of the setup configurations currently available in the             |
|   connected Pickit system.                                               |
|                                                                          |
| - **Product**                                                            |
|                                                                          |
|   Any of the product configurations currently available in the           |
|   connected Pickit system.                                               |
|                                                                          |
| Available configurations are listed in drop-down menus.                  |
|                                                                          |
| **Note:** If you need to change setup or product based on a runtime      |
| decision (not known in advance), consider using the                      |
| :ref:`pickit_configure <helper-function-configure>` helper instead.      |
+--------------------------------------------------------------------------+

.. _command-find-objects:

+--------------------------------------------------------------------------+
| **Find object(s)**                                                       |
+==========================================================================+
| Trigger a Pickit object detection using the currently active setup and   |
| product configuration.                                                   |
|                                                                          |
| The next Pickit command after **Find object(s)** should always be        |
| **Get result**, which waits until a response for the detection request   |
| is ready.                                                                |
|                                                                          |
| Note that it's valid (and sometimes encouraged) to perform robot motions |
| or other non Pickit actions between calls to **Find object(s)** and      |
| **Get result**, for instance.                                            |
|                                                                          |
|    .. image:: /assets/images/robot-integrations/ur/urcap-find-1.png      |
|                                                                          |
|    .. image:: /assets/images/robot-integrations/ur/urcap-find-2.png      |
|                                                                          |
| Refer to the cycle time optimization section of the                      |
| :ref:`universal-robots-urcap-example-v1` article for the motivation      |
| behind performing robot motions while a Pickit detection is.             |
+--------------------------------------------------------------------------+

.. _command-get-next-object:

+--------------------------------------------------------------------------+
| **Get next object**                                                      |
+==========================================================================+
| Request the next detected object.                                        |
|                                                                          |
| A single call to **Find object(s)** might yield the detection of         |
| multiple objects. **Get next object** allows to request the next         |
| available object, if any, without the need of triggering a new detection |
| and the time overhead it entails.                                        |
|                                                                          |
| The next Pickit command after  **Get next object** should always         |
| be **Get result**, which waits until a response for the request          |
| is ready.                                                                |
|                                                                          |
|    .. image:: /assets/images/robot-integrations/ur/urcap-next-1.png      |
|                                                                          |
| It's recommended to use this command only when objects in the            |
| detection region have not moved (significantly) since calling            |
| **Find object(s)**. A good example of when to use **Get next object** is |
| when a detection is unreachable by the robot. An example of when using   |
| **Get next object** is not ideal would be the following bin picking      |
| scenario:                                                                |
|                                                                          |
| -  Trigger Pickit detection that finds multiple objects.                 |
| -  First object is picked. Since objects are randomly placed in bin,     |
|    neighboring objects move and fall into place.                         |
| -  Call **Get next object** and attempt to pick next object. If the next |
|    object is one of the neighboring parts that moved, the pick might     |
|    fail.                                                                 |
|                                                                          |
| When the objects in the detection region have moved, it's better to      |
| re-trigger  **Find object(s)** instead.                                  |
+--------------------------------------------------------------------------+

.. _command-get-result:

+--------------------------------------------------------------------------+
| **Get result**                                                           |
+==========================================================================+
| Wait for Pickit reply with detection results.                            |
| **Get result** should always be the next Pickit command after            |
| a **Find object(s)** or **Get next object** request. It blocks until a   |
| reply from Pickit is received, and the success of the request can then   |
| be queried by calling ``pickit_object_found()``. When an object has      |
| been found, the following global variables are populated:                |
|                                                                          |
| -  Object pick pose: ``pickit_pose``                                     |
| -  Object pre-pick pose: ``pickit_pre_pose``.                            |
|    This pose is computed by applying an offset to ``pickit_pose``        |
|    along a specified direction, as specified by the command parameters.  |
| -  Object dimensions: ``pickit_dim``                                     |
| -  Object type: ``pickit_type``                                          |
|                                                                          |
| **Parameters**                                                           |
|                                                                          |
| - **Pre-pick offset: base frame**                                        |
|                                                                          |
|   ``pickit_pre_pose`` is computed by applying an offset along the z-axis |
|   of the specified frame. Valid options are object frame or robot base   |
|   frame.                                                                 |
|                                                                          |
| - **Pre-pick offset**                                                    |
|                                                                          |
|   Offset in mm applied to compute ``pickit_pre_pose``.                   |
+--------------------------------------------------------------------------+

+--------------------------------------------------------------------------+
| **Save snapshot**                                                        |
+==========================================================================+
| :ref:`Details here. <command-save-snapshot>`                             |
+--------------------------------------------------------------------------+

+--------------------------------------------------------------------------+
| **Build background**                                                     |
+==========================================================================+
| :ref:`Details here. <command-build-background>`                          |
+--------------------------------------------------------------------------+


Calibration
~~~~~~~~~~~

+--------------------------------------------------------------------------+
| **Find calibration plate**                                               |
+==========================================================================+
| :ref:`Details here. <command-find-calibration-plate>`                    |
+--------------------------------------------------------------------------+

.. _urcap-global-helper-functions:

Helper functions
----------------

.. _helper-function-empty-roi:

+--------------------------------------------------------------------------+
| **pickit_empty_roi()**                                                   |
+==========================================================================+
| Check if the last call to :ref:`Get result <command-get-result>`         |
| detected an empty Region of Interest (ROI).                              |
|                                                                          |
| **Return**                                                               |
|    ``true`` if Pickit detected an empty ROI.                             |
|                                                                          |
|    When ``pickit_object_found()`` returns ``false``, it can be due to:   |
|                                                                          |
|    #. The ROI is not empty, but Pickit doesn't detect the active         |
|       product.                                                           |
|    #. The ROI is empty.                                                  |
|                                                                          |
|    Use this function if you need to discriminate between these two       |
|    situations.                                                           |
+--------------------------------------------------------------------------+

.. _helper-function-object-found:

+--------------------------------------------------------------------------+
| **pickit_object_found()**                                                |
+==========================================================================+
| Check if the last call to :ref:`Get result <command-get-result>`         |
| produced valid detection results.                                        |
|                                                                          |
| **Return**                                                               |
|    ``true`` if detection results are available.                          |
|                                                                          |
|    When results are available, the global variables                      |
|    ``PickitPrePick`` and ``PickitPick`` have valid contents.             |
|                                                                          |
|    This function returns false when Pickit replied with no detection     |
|    results (nominal usecase); or if called without making a request to   |
|    Pickit and collecting the results with                                |
|    :ref:`Get result <command-get-result>` (should be avoided, as it      |
|    makes no sense).                                                      |
+--------------------------------------------------------------------------+

.. _helper-function-object-reachable:

+--------------------------------------------------------------------------+
| **pickit_object_reachable()**                                            |
+==========================================================================+
| Check if the last call to :ref:`Get result <command-get-result>`         |
| produced reachable pick and pre-pick poses.                              |
|                                                                          |
| **Return**                                                               |
|     ``true`` if the global variables ``PickitPrePick`` and               |
|     ``PickitPick`` contain poses that are reachable by the robot.        |
|                                                                          |
|     Note that ``pickit_object_reachable() == true`` implies              |
|     ``pickit_object_found() == true``.                                   |
+--------------------------------------------------------------------------+

.. _helper-function-no-image-captured:

+--------------------------------------------------------------------------+
| **pickit_no_image_captured()**                                           |
+==========================================================================+
| Check if object detection was unsuccessful due to a failure to capture a |
| camera image.                                                            |
|                                                                          |
| When this is the case, it typically indicates a hardware disconnection   |
| issue, such as a loose connector or broken cable. This function can be   |
| used as trigger to send an alarm to a higher level monitoring system.    |
|                                                                          |
| **Return**                                                               |
|     ``true`` if object detection was unsuccessful due to a failure to    |
|     capture a camera image.                                              |
+--------------------------------------------------------------------------+

.. _helper-function-remaining-objects:

+--------------------------------------------------------------------------+
| **pickit_remaining_objects()**                                           |
+==========================================================================+
| Get the number of remaining object detections.                           |
| After calling :ref:`Get result <command-get-result>`, this function      |
| returns the total number of object detections minus one, as the first    |
| object data is available through the :ref:`urcap-global-variables`.      |
|                                                                          |
| This value is also equal to the number of times                          |
| :ref:`Get next object <command-get-next-object>` can be called. As such, |
| the returned value decreases with each call to                           |
| :ref:`Get next object <command-get-next-object>`.                        |
|                                                                          |
| **Return**                                                               |
|    Number of remaining object detections available for query.            |
+--------------------------------------------------------------------------+

.. _helper-function-configure:

+--------------------------------------------------------------------------+
| **pickit_configure(setup_id, product_id)**                               |
+==========================================================================+
| Loads the specified setup and product configuration.                     |
| This function is similar to the :ref:`Select <command-select>` command,  |
| but specifies the setup and product by their respective IDs (integers)   |
| as opposed to names from a drop-down.                                    |
|                                                                          |
| Prefer using this function over the :ref:`Select <command-select>`       |
| command when you need to change the setup or product based on a runtime  |
| decision, and the IDs are read from variable values.                     |
|                                                                          |
| **Parameters**                                                           |
|                                                                          |
| - **setup_id**                                                           |
|                                                                          |
|   ID (integer) of a setup configurations currently available in the      |
|   connected Pickit system.                                               |
|                                                                          |
| - **product_id**                                                         |
|                                                                          |
|   ID (integer) of a product configurations currently available in the    |
|   connected Pickit system.                                               |
|                                                                          |
| **Return**                                                               |
|    ``true`` on configuration success: setup and product IDs exist and    |
|    loaded successfully.                                                  |
+--------------------------------------------------------------------------+
