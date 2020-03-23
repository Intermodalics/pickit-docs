.. _robot-independent-program-simple:

Simple pick and place program
=============================

Overview
--------

This article describes the logic for a simple vision-guided pick and place robot program.
The program continuously picks objects from a detection region and places them in a specified drop-off location until no more pickable objects are found.

The logic has the purpose  of presenting the basic ideas for writing a good pick and place robot program.
It is written in robot-independent pseudo-code using a syntax similar to that of `Python <https://www.python.org/>`__.

.. note::
  This article is ideal for understanding the basics of vision-guided pick and place, but it omits some useful functionality for the sake of clarity.
  The :ref:`Complete pick and place program <robot-independent-pick-and-place-complete>` is a slightly more complex version that can serve as a great starting point to build real applications on.
  A complete description of the Pickit interface can be found :ref:`here <robot-independent-interface>`.

The program can be `downloaded here <https://drive.google.com/uc?export=download&id=1-eANenWTbOOLIhR8KnAaRn7T3vDDFISj>`__ and consists of two main parts:

- :ref:`Generic pick and place logic <pick-and-place-simple-logic>`, which typically remains constant across applications.
- :ref:`Application-specific hooks <pick-and-place-simple-hooks>` that depend on things like the robot, the gripper, the part to pick and the cell layout.

.. _robot-independent-pick-and-place-inputs:

The minimum inputs required to run the pick and place program are:

- **Pickit configuration:** :ref:`setup and product IDs <Configuration>` to use for object detection.
- **Waypoints:**

  - ``Detect`` Where to perform object detection from. Refer to :ref:`this article <robot-position-during-capture>` for guidelines on how to make a good choice.
  - ``Dropoff`` Where to place objects.
  - ``AbovePickArea`` A point roughly above the pick area from which the above two can be reached without collision. In simple scenarios, it can be the same as ``Detect``.

- **Robot tool actions:** ``gripper_grasp()`` and ``gripper_release()``, to grasp and release an object, respectively.

.. image:: /assets/images/robot-integrations/robot-independent/waypoints.png
    :align: center

.. _pick-and-place-simple-logic:

Generic pick and place logic
----------------------------

.. literalinclude:: code/pick-and-place-simple.py
  :language: python
  :linenos:
  :emphasize-lines: 5, 9, 19-20, 24, 25, 27, 34
  :lines: 1-34

Lines where application-specific hooks are called are highlighted above.
The following is a breakdown of the pick and place logic along with a flowchart illustrating it.
Click on the entries below to expand them and learn more:

.. details:: Lines 1-6: Initialization

  .. literalinclude:: code/pick-and-place-simple.py
    :language: python
    :linenos:
    :emphasize-lines: 5
    :lines: -6

  These commands are run once before starting to pick and place. They take care of:

  - :ref:`Checking if Pickit is in robot mode <robot-independent-is-running>`, and bail out if not. Pickit only accepts robot requests when in robot mode.
  - Calling the :ref:`before_start() <robot-independent-hooks-before-start>` hook, which contains application-specific initialization logic.
  - :ref:`Loading the Pickit configuration <robot-independent-configure>` (setup and product) to use for object detection.

.. details:: Lines 8-11: First detection

  .. literalinclude:: code/pick-and-place-simple.py
    :language: python
    :linenos:
    :emphasize-lines: 2
    :lines: 8-11
    :lineno-start: 8

  The first object detection consists of:

  - :ref:`goto_detection() <robot-independent-hooks-goto-detection>` hook, which brings the robot to a configuration from which object detection can take place.
  - :ref:`pickit_find_objects_with_retries(retries) <robot-independent-find-objects-with-retries>` will trigger object detection with retries.
  - :ref:`pickit_get_result() <robot-independent-get-result>` waits for Pickit to reply with detection results.

.. _robot-independent-pick-place-loop:

.. details:: Lines 13-32: Pick and place loop

  .. literalinclude:: code/pick-and-place-simple.py
    :language: python
    :linenos:
    :emphasize-lines: 7-8, 12-13, 15
    :lines: 13-32
    :lineno-start: 13
    :name: pick-and-place-simple-loop

  The pick and place loop executes until there are no more objects to pick.
  The following cases are handled:

  - **There are no pickable objects:** Exit the pick and place loop, as either there are no detected objects or they are all unreachable.
  - **The object is detected and reachable (i.e. pickable):** Execute pick and place and trigger the next object detection.
  - **The object is detected but not reachable:** Get the next object from the last detection run. A single run can yield multiple object detections, and :ref:`pickit_next_object() <robot-independent-get-next-object>` allows to access the next object, if any, without incurring the overhead of running a new detection.

  .. note::
    To save cycle time when executing pick and place, note that object detection is triggered *after* the :ref:`pick() <robot-independent-hooks-pick>` hook, such that it takes place in parallel to :ref:`place() <robot-independent-hooks-place>`.
    This optimization is desirable in almost every application.
    An exception would be when the camera is robot-mounted and the picked object is large enough to block the camera view, as shown below.
    To disable it, move the call to :ref:`place() <robot-independent-hooks-place>` two line above, such that it takes place after :ref:`pick() <robot-independent-hooks-pick>`.

    .. image:: /assets/images/robot-integrations/robot-independent/cycle-time-optimization.png
      :align: center

.. details:: Line 34: Termination

  .. literalinclude:: code/pick-and-place-simple.py
    :language: python
    :linenos:
    :emphasize-lines: 1
    :lines: 34
    :lineno-start: 34

  The :ref:`after_end() <robot-independent-hooks-after-end>` hook is called last, which contains application-specific termination logic.

.. details:: Flowchart

  .. image:: /assets/images/robot-integrations/robot-independent/pick-and-place-simple.png
    :align: center
    :scale: 70%

|

.. _pick-and-place-simple-hooks:

Application-specific hooks
--------------------------

The contents of these hooks are typically specific to a particular application, as they contain motion sequences and logic that depend on the robot cell layout, including:

- The robot type and location
- The camera mount and location
- The parts to pick
- The gripper to use
- The pick and place locations

The following implementations are a good starting point for a general-purpose pick and place application, but it's typically necessary to adapt them to some extent by adding waypoints or extra logic.
A detailed description of these hooks can be found in the :ref:`Complete pick and place program <pick-and-place-hooks>` article.

.. literalinclude:: code/pick-and-place-simple.py
  :language: python
  :linenos:
  :lines: 36-
  :lineno-start: 36
