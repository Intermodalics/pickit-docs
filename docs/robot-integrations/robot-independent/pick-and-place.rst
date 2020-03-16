.. _robot-independent-pick-and-place-complete:

Complete pick and place program
===============================

Overview
--------

This article presents a robot-independent pick and place logic that serves as a great starting point to build real applications on.
It consists of a more feature-rich version of the :ref:`simple pick and place logic <pick-and-place-simple-logic>`, which presents the basic ideas behind pick and place.
It is highly recommended to read that article first.
A complete description of the Pickit interface can be found :ref:`here <robot-independent-interface>`.

All the logic presented here is written in robot-independent pseudo-code using a syntax similar to that of `Python <https://www.python.org/>`__.
The program can be `downloaded here <https://drive.google.com/uc?export=download&id=1-eANenWTbOOLIhR8KnAaRn7T3vDDFISj>`__ and, similar to the :ref:`simple pick and place program <robot-independent-program-simple>`, it consists of two main parts:

- :ref:`Generic pick and place function <pick-and-place-logic>`, which typically remains constant across applications.
- :ref:`Application-specific hooks <pick-and-place-hooks>` that depend on things like the robot, the gripper, the part to pick and the cell layout.

The minimum inputs required to run a pick and place program are the same as for the :ref:`simple pick and place logic <robot-independent-pick-and-place-inputs>`.

.. _pick-and-place-logic:

Generic pick and place function
-------------------------------

.. literalinclude:: code/pick-and-place.py
  :language: python
  :linenos:
  :lines: 19-66
  :emphasize-lines: 1, 13, 20-40, 48

Click below to expand a flowchart of the implemented logic.

.. details:: Flowchart

  .. image:: /assets/images/robot-integrations/robot-independent/pick-and-place-full.png
    :align: center
    :scale: 70%

|

The lines that differ with respect to the :ref:`simple pick and place logic <pick-and-place-simple-logic>` are highlighted above, and implement the following additional features:

- The ability to not only *pick all objects* (the default), but also to specify a *target number of picks*.
- Some robot tools have the means to measure pick success. When this is available, cycle time can be optimized by skipping the place motion on pick failure, and instead proceed to trigger a new object detection.
- Wrap the logic in a ``pick_and_place`` function, so it can be reused more easily and with less code duplication. It outputs the *number of successful picks*, and takes as inputs:

  - **Required:** the Pickit :ref:`configuration <Configuration>`, ``setup`` and ``product``.
  - **Optional:** ``target_picks``, which defaults to -1 (*pick all*); and ``retries``, which denotes how many times to retry object detection when the :ref:`Region of Interest (ROI) <region-of-interest>` is not empty, but no objects are detected.


.. _pick-and-place-hooks:

Application-specific hooks
--------------------------

The ``pick_and_place`` function requires the following application-specific hooks to be defined.
Click on the entries below to expand them and learn more about their default implementation and behavior:

.. _robot-independent-hooks-before-start:

.. details:: before_start

  .. literalinclude:: code/pick-and-place.py
    :language: python
    :lines: 70-71

  This hook is executed *once* before starting to pick and place.
  It's recommended to add logic required to bring the robot to a sane configuration before starting to pick objects.
  This can be especially useful when the robot program was previously interrupted at mid-run.

  By default, it makes sure the gripper is open to prepare it for picking an object.

.. _robot-independent-hooks-goto-detection:

.. details:: goto_detection

  .. literalinclude:: code/pick-and-place.py
    :language: python
    :lines: 74-75

  This is a motion sequence that moves the robot to the point from which object detection is triggered.
  For simple applications, this typically corresponds to a single waypoint.

  Some applications using a robot-mounted camera might require a non-constant ``Detect`` point. For instance, when a bin is wider than the camera field of view, multiple detection points are required to fully cover it.

.. _robot-independent-hooks-pick:

.. details:: pick

  .. literalinclude:: code/pick-and-place.py
    :language: python
    :lines: 84-100

  .. note::
    ``movej(p)`` and ``movel(p)`` represent a robot motion to reach waypoint ``p`` following a path interpolated linearly in joint or Cartesian space, respectively.

  The pick sequence performs the actual picking motion, which consists of a linear approach to the pick point, a grasping action, and a linear retreat away from it.

  - The sequence starts and ends at ``AbovePickArea``, a waypoint known to be reachable without collision both from the pick area and from the other :ref:`user-defined waypoints <robot-independent-pick-and-place-inputs>`.

  - The place where ``gripper_grasp()`` is called depends on the type of gripper. Fingered grippers perform the grasp action at the pick point, but for suction-like grippers this typically takes place *before* heading to the pick point.

      .. image:: /assets/images/robot-integrations/robot-independent/tool-action.png
        :align: center
        :scale: 50

  - The pick point, ``PickitPick``, is computed by Pickit.

  - ``PrePick`` is chosen such that the approach motion is aligned with the object, while ``PostPick`` is chosen for a straight-up retreat (which makes it less likely to collide with obstacles like the bin). These strategies have proven to be effective in practice, but they can be overridden, if desired.

      .. image:: /assets/images/robot-integrations/robot-independent/pick-sequence.png
        :align: center

  - It returns a boolean indicating whether the pick was successful.

    .. note::
      The check represented by ``gripper_pick_success()`` assumes that the gripper has the means to check pick success from sensor input (like vacuum or force).
      If this is not the case for your gripper, the ``pick()`` function can simply ``return True`` always, and the pick failure logic will never be triggered.

    |

.. _robot-independent-hooks-on-pick-failure:

.. details:: on_pick_failure

  .. literalinclude:: code/pick-and-place.py
    :language: python
    :lines: 103-104

  This hook is executed whenever the pick success check fails, (see ``gripper_check_success()`` in the :ref:`pick hook <robot-independent-hooks-pick>`).
  The default implementation opens the gripper to prepare it for picking the next object.

.. _robot-independent-hooks-place:

.. details:: place

  .. literalinclude:: code/pick-and-place.py
    :language: python
    :lines: 107-109

  This sequence places the object at the specified dropof location.
  For simple applications the implementation is trivial, as shown above.
  However, some applications require more advanced place motions.

  The robot sometimes needs to know about the way the object was picked, in order to place it appropriately.
  Refer to the :ref:`smart placing <smart-place-examples>` examples to learn how to do this with minimal programming effort.

  It can also be the case that the drop-off point is not constant, as when parts need to be stacked or palletized.
  Many robot programming languages provide helpers and templates for stacking and palletizing, which can replace the fixed ``Dropoff`` point.

.. _robot-independent-hooks-after-end:

.. details:: after_end

  .. literalinclude:: code/pick-and-place.py
    :language: python
    :lines: 112-

  This hook is executed *once* after pick and place has finished.
  The proposed implementation identifies the termination reason and prints an informative statement if there are no more pickable objects.
  This is very useful to debug your application while you're setting it up.

  When getting your application ready for production, you should handle the cases that make sense to you with appropriate logic.
  For instance, a continuous-running application might want to request more parts once all pickable objects have been processed.

  .. literalinclude:: code/action-after-end-example.py
    :language: python

  Notice how the application only stops on non-recoverable errors, and triggers :ref:`saving a snapshot <Saving-a-snapshot>` whenever it fails to empty the :ref:`ROI <region-of-interest>`.
  Inspecting these snapshots allow to improve the application by answering questions like:

  - Are there actually unpicked objects in the ROI, or are there unexpected contents in it?
  - If there are objects, are they detected but unpickable by the robot (because they are unreachable or the picking action failed)?
  - If there are objects, but they are not detected, can we optimize the detection parameters or :ref:`camera location <what-is-the-ideal-distance-to-mount-the-pickit-camera>` to make them detectable?

|

Example usage
-------------

The following is a minimal example of how the pick and place function can be used.

.. literalinclude:: code/pick-and-place-example.py
  :language: python

Advanced topics
---------------

.. _robot-independent-camera-on-robot:

Robot-mounted camera
~~~~~~~~~~~~~~~~~~~~

If a robot-mounted camera is used, it's not possible to perform multiple detection retries (including camera captures) in parallel to the place motion sequence, as camera capture can only take place from the ``Detect`` point.
To correctly handle the robot-mounted camera scenario, replace :ref:`lines 31-34 <pick-and-place-logic>` with the following:

.. literalinclude:: code/camera-on-robot-sequence.py
  :language: python

Notice the use of the functions :ref:`pickit_capture_image() <robot-independent-capture-image>` and :ref:`pickit_process_image() <robot-independent-process-image>`.

A variant of the pick and place function with the above changes, named ``pick_and_place_robot_mounted``, can be `downloaded here <https://drive.google.com/uc?export=download&id=1-eANenWTbOOLIhR8KnAaRn7T3vDDFISj>`__.

