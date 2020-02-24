.. _robot-independent-interface:

The Pickit interface
====================

This article proposes an Application Programming Interface (API) to be used by robot programs to perform vision-guided pick and place with Pickit.
It consists of a number of global variables and functions that encapsulate the :ref:`socket communication <socket-communication>` between a robot and Pickit.

The interface is meant to be robot-independent, and consists of global variables and functions written in pseudo-code, using a syntax similar to that of `Python <https://www.python.org/>`__.
Translating it to a specific robot programming language should consist of adapting to the syntax, features and best practices of the target language.
Some deviation from the proposed interface might be necessary due to target language limitations, and the implementer is left with the responsibility of making the best compromise between what is possible and the proposed interface.

Refer to the following articles for examples of this interface in use:

- :ref:`robot-independent-program-simple`
- :ref:`robot-independent-pick-and-place-complete`
- :ref:`robot-independent-calibration`

.. note::
  This article assumes an existing implementation of the :ref:`socket communication <socket-communication>` layer.

.. _robot-independent-global-variables:

.. |output-vars| replace:: :ref:`output global variables <robot-independent-global-variables>`

Output global variables
-----------------------

This section enumerates all output variables populated by Pickit when valid
detection results are available, that is, when calling |get_result| returns ``True``.

These variables are typically used by a :ref:`pick and place program <robot-independent-pick-and-place-complete>` in the :ref:`pick <robot-independent-hooks-pick>` and :ref:`place <robot-independent-hooks-place>` hooks.
They refer to the currently selected object for picking.
:ref:`PickitPick <robot-independent-pickit-pick>` is the most commonly used variable, normally in the :ref:`pick <robot-independent-hooks-pick>` hook.
All other variables are used for implementing :ref:`advanced picking or placing <smart-place-examples>`.

.. _robot-independent-pickit-pick:

.. |pickit-pick| replace:: :ref:`PickitPick <robot-independent-pickit-pick>`

.. details:: PickitPick

  +--------------------------------------------------------------------------+
  | Object pick point, represented as a pose variable.                       |
  |                                                                          |
  | From this point it's possible to compute ``PickitPrePick`` and           |
  | ``PickitPostPick`` for performing linear approach and retreat motions.   |
  | See the :ref:`pick <robot-independent-hooks-pick>` hook for an example.  |
  +--------------------------------------------------------------------------+

.. _robot-independent-pickit-pick-id:

.. |pickit-pick-id| replace:: :ref:`PickitPickId <robot-independent-pickit-pick-id>`

.. details:: PickitPickId

  +--------------------------------------------------------------------------+
  | ID of the pick point that was selected for picking, represented as an    |
  | integer.                                                                 |
  +--------------------------------------------------------------------------+

.. _robot-independent-pickit-pick-ref-id:

.. |pickit-pick-ref-id| replace:: :ref:`PickitPickRefId <robot-independent-pickit-pick-ref-id>`

.. details:: PickitPickRefId

  +--------------------------------------------------------------------------+
  | ID of the :ref:`reference pick point <pick-point-reference>` of the      |
  | |pickit-pick-id|, represented as an integer.                             |
  |                                                                          |
  | If |pickit-pick-id| was not created with respect to another pick point   |
  | (that is, it has ``Origin`` as reference), this value will be the same   |
  | as |pickit-pick-id|.                                                     |
  +--------------------------------------------------------------------------+

.. _robot-independent-pickit-pick-off:

.. |pickit-pick-off| replace:: :ref:`PickitPickOff <robot-independent-pickit-pick-off>`

.. details:: PickitPickOff

  +--------------------------------------------------------------------------+
  | Pick point offset, represented as a pose variable.                       |
  |                                                                          |
  | This is the relative transformation between the reference pick point     |
  | (identified by |pickit-pick-ref-id|) and the pick point that was         |
  | selected for picking (identified by |pickit-pick-id|).                   |
  |                                                                          |
  | This offset can be used to place an object consistently, regardless of   |
  | how it was picked (which :ref:`pick point <multiple-pick-points>`,       |
  | whether :ref:`flexible pick orientation <flexible-pick-orientation>` was |
  | used). If a ``Dropoff`` point was specified for an object picked from    |
  | |pickit-pick-ref-id|, it can be translated to |pickit-pick-id| by        |
  | post-multiplying ``Dropoff`` by |pickit-pick-off|.                       |
  |                                                                          |
  | Learn more on how to use this variable in the                            |
  | :ref:`advanced placing examples <smart-place-examples>`.                 |
  +--------------------------------------------------------------------------+

.. _robot-independent-pickit-obj-type:

.. |pickit-obj-type| replace:: :ref:`PickitObjType <robot-independent-pickit-obj-type>`

.. details:: PickitObjType

  +--------------------------------------------------------------------------+
  | Object type, represented as an integer.                                  |
  |                                                                          |
  | The mapping between the object type and its identifier is the following: |
  |                                                                          |
  | **Pickit Teach** Teach model ID                                          |
  |                                                                          |
  |   Use this value to conditionally perform an action depending on the     |
  |   detected model.                                                        |
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
  |                                                                          |
  | **Pickit Bags**                                                          |
  |                                                                          |
  |   An integer that holds information about the bag pattern and the        |
  |   detected layer orientation, according to                               |
  |   :ref:`this table <Bags-robot-program>`.                                |
  +--------------------------------------------------------------------------+

.. _robot-independent-pickit-obj-dim:

.. |pickit-obj-dim| replace:: :ref:`PickitObjDim <robot-independent-pickit-obj-dim>`

.. details:: PickitObjDim

  +--------------------------------------------------------------------------+
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

.. _robot-independent-pickit-obj-age:

.. |pickit-obj-age| replace:: :ref:`PickitObjAge <robot-independent-pickit-obj-age>`

.. details:: PickitObjAge

  +--------------------------------------------------------------------------+
  | Object age, represented as a floating-point number.                      |
  |                                                                          |
  | The object age is the duration, in seconds, elapsed between the          |
  | capturing of the camera image and the moment the object information is   |
  | sent to the robot.                                                       |
  +--------------------------------------------------------------------------+

|

.. _robot-independent-functions:

Functions
---------

The following functions relate to performing object detection. They send a request to Pickit, but don't wait for the response to arrive.
:ref:`Results <robot-independent-global-variables>` from these requests are collected by calling |get_result|, which waits until a response is ready.

.. _robot-independent-find-objects:

.. |find-objects| replace:: :ref:`pickit_find_objects() <robot-independent-find-objects>`

.. details:: pickit_find_objects()

  +--------------------------------------------------------------------------+
  | Trigger a Pickit object detection using the currently active setup and   |
  | product configuration.                                                   |
  |                                                                          |
  | **Implementation**                                                       |
  |   Send :ref:`RC_PICKIT_LOOK_FOR_OBJECTS` and *don't* wait for a response.|
  +--------------------------------------------------------------------------+

.. _robot-independent-find-objects-with-retries:

.. |find-objects-with-retries| replace:: :ref:`pickit_find_objects_with_retries(retries) <robot-independent-find-objects-with-retries>`

.. details:: pickit_find_objects_with_retries(retries)

    +--------------------------------------------------------------------------+
    | Trigger a Pickit object detection *with retries* using the currently     |
    | active setup and product configuration.                                  |
    |                                                                          |
    | As opposed to                                                            |
    | |find-objects|, when no objects are found (but the                       |
    | :ref:`Region of Interest (ROI) <region-of-interest>` is not empty),      |
    | Pickit will retry up to *retries* times to find objects before giving up.|
    |                                                                          |
    | **Parameters**                                                           |
    |   *retries* Maximum number of detection retries.                         |
    |                                                                          |
    | **Implementation**                                                       |
    |   Send :ref:`RC_PICKIT_LOOK_FOR_OBJECTS_WITH_RETRIES` and *don't* wait   |
    |   for a response.                                                        |
    +--------------------------------------------------------------------------+

.. _robot-independent-process-image:

.. |process-image| replace:: :ref:`pickit_process_image() <robot-independent-process-image>`

.. details:: pickit_process_image()

  +--------------------------------------------------------------------------+
  | Trigger a Pickit object detection *without image capture* using the      |
  | currently active setup and product configuration.                        |
  |                                                                          |
  | This function uses the latest captured camera image, which typically     |
  | comes from calling |capture-image| just before.                          |
  |                                                                          |
  | Refer to the documentation of |capture-image| to learn more about the    |
  | recommended usage of this function.                                      |
  |                                                                          |
  | **Implementation**                                                       |
  |   Send :ref:`RC_PICKIT_PROCESS_IMAGE` and *don't* wait for a response.   |
  +--------------------------------------------------------------------------+

.. _robot-independent-get-next-object:

.. |get-next-object| replace:: :ref:`pickit_get_next_object() <robot-independent-get-next-object>`

.. details:: pickit_get_next_object()

  +--------------------------------------------------------------------------+
  | Request the next detected object.                                        |
  |                                                                          |
  | A single object detection run might yield the detection of multiple      |
  | objects. This function allows to request the next available object, if   |
  | any, without the need of triggering a new detection and the time         |
  | overhead it entails.                                                     |
  |                                                                          |
  | It's recommended to use this command only when objects in the            |
  | detection region have not moved (significantly) since the last detection |
  | took place.                                                              |
  | A good example of when to use |get-next-object| is when a                |
  | detection is unreachable by the robot. An example of when using it is    |
  | not recommended would be the following bin picking scenario:             |
  |                                                                          |
  | -  Trigger a Pickit detection that finds multiple objects.               |
  | -  The first object is picked. Since objects are randomly placed in bin, |
  |    neighboring objects move and fall into place.                         |
  | -  Call |get-next-object| and attempt to pick next object.               |
  |    If the next object is one of the neighboring parts that moved, the    |
  |    pick is likely to fail.                                               |
  |                                                                          |
  | When the objects in the detection region have moved, it's better to      |
  | re-trigger object detection instead (by calling                          |
  | |find-objects-with-retries|, for instance).                              |
  |                                                                          |
  | **Implementation**                                                       |
  |   Send :ref:`RC_PICKIT_NEXT_OBJECT` and *don't* wait for a response.     |
  +--------------------------------------------------------------------------+

|

.. note::
  You must collect the results of each request before sending a new one.

.. tip::
  Note that all calls except |get-next-object| (which is very fast) trigger a Pickit object detection run, which can potentially take multiple seconds.

  In your robot program, it's encouraged to perform robot motions or other non-Pickit-detection actions between calls to these functions and |get_result| to save cycle time in your application.
  Refer to the :ref:`pick and place loop <robot-independent-pick-place-loop>` of the simple pick and place program to learn more.

This function collects the results of the above requests:

.. _robot-independent-get-result:

.. |get_result| replace:: :ref:`pickit_get_result() <robot-independent-get-result>`

.. details:: pickit_get_result()

  +--------------------------------------------------------------------------+
  | Wait for Pickit to reply with detection results.                         |
  |                                                                          |
  | |get_result| should always be paired to one of the                       |
  | :ref:`above functions <robot-independent-find-objects>`.                 |
  |                                                                          |
  | **Implementation**                                                       |
  |   Block until a reply from Pickit is received.                           |
  |   When an object has been found, populate the |output-vars| with valid   |
  |   content, which requires these steps:                                   |
  |                                                                          |
  |   - Populate |pickit-pick|, |pickit-obj-type|, |pickit-obj-dim|,         |
  |     and |pickit-obj-age| from the                                        |
  |     :ref:`received response <RC_PICKIT_LOOK_FOR_OBJECTS_response>`.      |
  |   - Send :ref:`RC_PICKIT_GET_PICK_POINT_DATA` and wait for a new         |
  |     response.                                                            |
  |                                                                          |
  |   - If the response status is                                            |
  |     :ref:`PICKIT_GET_PICK_POINT_DATA_OK <response-status>`, populate     |
  |     from the newly                                                       |
  |     :ref:`received response <RC_PICKIT_GET_PICK_POINT_DATA_response>`    |
  |     these variables: |pickit-pick-id|, |pickit-pick-ref-id| and          |
  |     |pickit-pick-off|.                                                   |
  |     Otherwise raise a non-recoverable error and halt program execution.  |
  |                                                                          |
  |   The success of the original request can be queried by calling          |
  |   :ref:`pickit_object_found() <robot-independent-object-found>` after    |
  |   |get_result|.                                                          |
  +--------------------------------------------------------------------------+

|

The following functions are short-running.
The robot sends a request to Pickit and waits for the response, which only consists of a status code.

.. _robot-independent-is-running:

.. details:: pickit_is_running()

  +--------------------------------------------------------------------------+
  | Check whether robot mode is enabled in Pickit.                           |
  |                                                                          |
  | **Implementation**                                                       |
  |   Send :ref:`RC_PICKIT_CHECK_MODE` and wait for a response.              |
  |                                                                          |
  | **Return**                                                               |
  |    ``True`` if the response status is                                    |
  |    :ref:`PICKIT_ROBOT_MODE <response-status>`.                           |
  |                                                                          |
  | All functions in this article except |find-calib-plate| require robot    |
  | mode to be enabled, which can be done from the                           |
  | :ref:`Pickit web interface <web-interface-top-bar>`.                     |
  +--------------------------------------------------------------------------+

.. _robot-independent-configure:

.. details:: pickit_configure(setup, product)

  +--------------------------------------------------------------------------+
  | Loads the specified Pickit :ref:`configuration <Configuration>`          |
  | (setup and product).                                                     |
  |                                                                          |
  | **Parameters**                                                           |
  |                                                                          |
  |   IDs of valid *setup* and *product* configurations currently            |
  |   available in the connected Pickit system.                              |
  |   Available configuration IDs are listed in the                          |
  |   :ref:`Pickit web interface <Configuration>`.                           |
  |                                                                          |
  | **Implementation**                                                       |
  |   Send :ref:`RC_PICKIT_CONFIGURE` and wait for a response.               |
  |                                                                          |
  |   If the response status is not                                          |
  |   :ref:`PICKIT_CONFIG_OK <response-status>`, a non-recoverable error is  |
  |   raised and program execution is halted.                                |
  |   This can happen, for instance, when the parameters correspond to       |
  |   non-existing setup or product IDs.                                     |
  +--------------------------------------------------------------------------+

.. _robot-independent-save-snapshot:

.. details:: pickit_save_snapshot()

  +--------------------------------------------------------------------------+
  | Save a :ref:`snapshot <Snapshots>` with the latest detection results.    |
  |                                                                          |
  | For an example usage, refer to the description of the                    |
  | :ref:`after_end <robot-independent-hooks-after-end>` hook of the pick    |
  | and place program.                                                       |
  |                                                                          |
  | **Implementation**                                                       |
  |   Send :ref:`RC_PICKIT_SAVE_SNAPSHOT` and wait for a response.           |
  |                                                                          |
  | **Return**                                                               |
  |    ``True`` if the response status is                                    |
  |    :ref:`PICKIT_SAVE_SNAPSHOT_OK <response-status>`.                     |
  +--------------------------------------------------------------------------+

.. _robot-independent-capture-image:

.. |capture-image| replace:: :ref:`pickit_capture_image() <robot-independent-capture-image>`

.. details:: pickit_capture_image()

  +--------------------------------------------------------------------------+
  | Capture a camera image *without* triggering object detection.            |
  |                                                                          |
  | This function blocks until image capture has completed, and is           |
  | especially useful when working with a                                    |
  | :ref:`robot-mounted camera <robot-independent-camera-on-robot>`, where   |
  | the robot must remain stationary during image capture, but not during    |
  | detection.                                                               |
  | This function is meant to be used prior to calling |process-image|.      |
  |                                                                          |
  | For fixed camera mounts, it's usually more convenient to call functions  |
  | that combine image capture and processing, like |find-objects| or        |
  | |find-objects-with-retries|.                                             |
  |                                                                          |
  | **Implementation**                                                       |
  |   Send :ref:`RC_PICKIT_CAPTURE_IMAGE` and wait for a response.           |
  |                                                                          |
  | **Return**                                                               |
  |    ``True`` if the response status is                                    |
  |    :ref:`PICKIT_IMAGE_CAPTURED <response-status>`.                       |
  +--------------------------------------------------------------------------+

.. _robot-independent-build-background:

.. details:: pickit_build_background()

  +--------------------------------------------------------------------------+
  | Build the background cloud used by some of the                           |
  | :ref:`advanced Region of Interest filters <advanced-roi-filters>`.       |
  |                                                                          |
  | Calling this function will trigger a camera capture. So, if the camera   |
  | mount is fixed, the robot must not occlude the camera view volume.       |
  | If instead the camera is robot-mounted, the robot must be in the         |
  | detection point (:ref:`more <robot-position-during-capture>`).           |
  |                                                                          |
  | **Implementation**                                                       |
  |   Send :ref:`RC_PICKIT_BUILD_BACKGROUND` and wait for a response.        |
  |                                                                          |
  | **Return**                                                               |
  |    ``True`` if the response status is                                    |
  |    :ref:`PICKIT_BUILD_BKG_CLOUD_OK <response-status>`.                   |
  +--------------------------------------------------------------------------+

|

The following functions are helpers that don't require extra communication with Pickit.
They use the information received in the most recent detection results.
These helpers are typically used as part of conditional expressions, such as an ``if`` statement. 

.. _robot-independent-empty-roi:

.. details:: pickit_empty_roi()

  +--------------------------------------------------------------------------+
  | Check if the last call to |get_result| detected an                       |
  | :ref:`empty Region of Interest (ROI) <detecting-an-empty-roi>`.          |
  |                                                                          |
  | When                                                                     |
  | :ref:`pickit_object_found() <robot-independent-object-found>`            |
  | returns ``False``, it can be due to:                                     |
  |                                                                          |
  | #. The ROI is not empty, but Pickit doesn't detect the active            |
  |    product.                                                              |
  | #. The ROI is empty.                                                     |
  |                                                                          |
  | Use this function if you need to discriminate between these two          |
  | situations.                                                              |
  |                                                                          |
  | **Return**                                                               |
  |    ``True`` if Pickit detected an empty ROI.                             |
  +--------------------------------------------------------------------------+

.. _robot-independent-object-found:

.. details:: pickit_object_found()

  +--------------------------------------------------------------------------+
  | Check if the last call to |get_result| produced valid detection results. |
  |                                                                          |
  |                                                                          |
  | **Return**                                                               |
  |   ``True`` if detection results are available.                           |
  |                                                                          |
  |    When results are available, the |output-vars| have valid contents.    |
  |                                                                          |
  |    This function returns ``False`` when Pickit replied with no detection |
  |    results (nominal usecase); or if |get_result|  was called without a   |
  |    previous detection request to Pickit (should be avoided, as it makes  |
  |    no sense).                                                            |
  +--------------------------------------------------------------------------+

.. _robot-independent-no-object-reachable:

.. details:: pickit_object_reachable()

  +--------------------------------------------------------------------------+
  | Check if the last call to |get_result| produced a reachable              |
  | :ref:`PickitPick <robot-independent-pickit-pick>` (and possibly also     |
  | ``PickitPrePick`` and ``PickitPostPick``).                               |
  |                                                                          |
  | This is an optional, but recommended helper function that performs       |
  | reachability checks on the pick point (and possibly also the approach    |
  | and retreat trajectories).                                               |
  | This function requires the robot programming language to expose          |
  | functionality like joint limits, inverse kinematics and safety plane     |
  | checks.                                                                  |
  |                                                                          |
  | **Return**                                                               |
  |     ``True`` if the checked global variables are reachable by the robot. |
  |                                                                          |
  |     Note that ``pickit_object_reachable() == True`` implies              |
  |     ``pickit_object_found() == True``.                                   |
  +--------------------------------------------------------------------------+

.. _robot-independent-no-image-captured:

.. details:: pickit_no_image_captured()

  +--------------------------------------------------------------------------+
  | Check if object detection was unsuccessful due to a failure to capture a |
  | camera image.                                                            |
  |                                                                          |
  | When this is the case, it typically indicates a hardware disconnection   |
  | issue, such as a loose connector or broken cable. This function can be   |
  | used as trigger to send an alarm to a higher level monitoring system.    |
  |                                                                          |
  | **Return**                                                               |
  |     ``True`` if object detection was unsuccessful due to a failure to    |
  |     capture a camera image.                                              |
  +--------------------------------------------------------------------------+

.. _robot-independent-remaining-objects:

.. details:: pickit_remaining_objects()

  +--------------------------------------------------------------------------+
  | Get the number of remaining detected objects.                            |
  |                                                                          |
  | After calling |get_result|, this function returns the total number of    |
  | object detections minus one, as the first object data is available       |
  | through the |output-vars|.                                               |
  |                                                                          |
  | This value is also equal to the number of times |get-next-object| can be |
  | called. As such, the returned value decreases with each call to          |
  | |get-next-object|.                                                       |
  |                                                                          |
  | **Return**                                                               |
  |    Number of remaining object detections available for query.            |
  +--------------------------------------------------------------------------+

|

Calibration functions
---------------------

There is a single function meant to be used in a :ref:`calibration robot program <robot-independent-calibration>`, and not in a pick and place program.

.. _robot-independent-find-calibration-plate:

.. |find-calib-plate| replace:: :ref:`pickit_find_calibration_plate() <robot-independent-find-calibration-plate>`

.. details:: pickit_find_calibration_plate()

  +--------------------------------------------------------------------------+
  | Trigger detection of the robot-camera calibration plate.                 |
  |                                                                          |
  | This function requires the Pickit web interface to be in the             |
  | :ref:`Calibration <robot-camera-calibration>` page, hence robot mode     |
  | should be disabled.                                                      |
  |                                                                          |
  | **Implementation**                                                       |
  |   Send :ref:`RC_PICKIT_FIND_CALIB_PLATE` and wait for a response.        |
  |                                                                          |
  |   If the respose status is not                                           |
  |   :ref:`PICKIT_FIND_CALIB_PLATE_OK <response-status>`,                   |
  |   a non-recoverable error is raised and program execution is halted.     |
  +--------------------------------------------------------------------------+

|