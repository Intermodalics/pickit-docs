.. _techman-pick-and-place-program:

Example pick and place program
==============================

.. contents::
    :backlinks: top
    :local:
    :depth: 1

Loading the program
-------------------

This example program requires the **Pickit TMflow components** to be installed in your robot. For installation instructions of both the TMflow components and the example programs, please refer to the :ref:`techman-installation` article.

Click the `hamburger icon <https://en.wikipedia.org/wiki/Hamburger_button>`__ on the top-left corner of the user interface, and select **Project**.

    .. image:: /assets/images/robot-integrations/techman/tm-installation-left-panel-project.png
       :scale: 50%
       :align: center

Open the project called ``pickit_pick_and_place``.

The program explained
---------------------

The program implements a simple pick and place task, where Pickit is used to continuously pick objects from a detection region and place them in a specified dropoff location.
No assumptions are made on how objects are laid out in the detection region, so the program is a good starting point to build a wide range of applications.
Objects can be stacked randomly, or in a pattern, touching or not.

.. image:: /assets/images/examples/urcap-program-step-1.png

Inputs
~~~~~~

The program requires the user to specify the following inputs:

Component parameters
^^^^^^^^^^^^^^^^^^^^

-  **Pickit IP address**: See :ref:`tm-init` component.
-  **Pickit configuration**: Setup and product IDs, see :ref:`tm-configure` component.

Points
^^^^^^

There are six points relevant to the application, of which three are fixed and need to be taught by the user, and three are automatically computed from Pickit’s results (prefixed with ``pickit_``).
They are listed in the **Point Manager**.

    .. image:: /assets/images/robot-integrations/techman/tm-pap-point-manager.png
       :scale: 40%
       :align: center

Fixed points
''''''''''''

These points need to be taught by the user:

-  ``detect_pose`` from where to perform object detection.
-  ``dropoff_pose`` where to place objects.
-  ``ref_pose`` a waypoint from which the above two can be reached without collision.
   In simple scenarios, it can be the same as ``detect_pose``.

.. _techman-auto-points:

Automatically computed points
'''''''''''''''''''''''''''''

These points are computed from Pickit’s results, and need **tool shifting** to be applied to them:

-  ``pickit_pose`` The actual picking pose.
-  ``pickit_pre_pose`` Used for the linear approach motion before the pick takes place.
   It consists of ``pickit_pose`` offset along its z-axis,. i.e. it tilts with the object.
-  ``pickit_post_pose`` Used for the linear retreat motion after the pick takes place. It consists of ``pickit_pose`` offset along the robot base z-axis, which typically means straight up.

Tool shifting compensates for the offset of the TCP to be used.
In the :ref:`pick sequence <techman-pick-sequence>` subflow, you must edit each of these points, and select **Tool shift** in the advanced options of the point editor.

    .. image:: /assets/images/robot-integrations/techman/tm-pap-tool-shift.png
       :scale: 32%
       :align: center

Then, apply tool shifting with the following options:

-  The **TCP** to be used for reaching this point.
-  The **keep path** option (as opposed to keep pose).

    .. image:: /assets/images/robot-integrations/techman/tm-pap-tool-shift-keep-path.png
       :scale: 40%
       :align: center

Gripper command
^^^^^^^^^^^^^^^

The :ref:`pick <techman-pick-sequence>` and :ref:`place <techman-place-sequence>` sequences require enabling and disabling the gripper.
They contain by default a ``Set`` node that performs no action.
You should either set the correct variable (e.g. toggle a digital output) or replace the node with an instance of a custom gripper component.

[Optional] Variables
^^^^^^^^^^^^^^^^^^^^

These variables have reasonable default values, but can be overridden if desired:

-  **var_picks** How many objects to pick before successfully terminating the program.
   The default value of zero indicates “pick all”.
-  **var_max_detection_retries** How many times to retry object detection when no objects are found before bailing out.
   Defaults to five.

Program breakdown
-----------------

The pick and place program is structured as follows:

-  **Motion sequence subflows**: There are three different motion sequences for the detection, pick and place actions.
   There are more application-dependent and it’s typical that a user modifies them by adding additional points and custom gripper actions.
-  **Main program**: Contains generic pick and place logic.
   It should be fairly application agnostic, and the user should rarely have to modify it.

The above are described in the following subsections.

Motion sequence subflows
~~~~~~~~~~~~~~~~~~~~~~~~

.. _techman-pick-sequence:

Pick sequence
^^^^^^^^^^^^^

This sequence computes ``pickit_pre_pose`` and ``pickit_post_pose`` relative to the pickit_pose returned by :ref:`tm-getresult`.
It also enables the gripper.

.. image:: /assets/images/robot-integrations/techman/tm-pap-0.png
   :scale: 60 %
   :align: center

Remember to :ref:`apply tool shifting <techman-auto-points>` with **keep path** to ``pickit_pose``, ``pickit_pre_pose`` and ``pickit_post_pose``.
The below image shows how a tool-shifted Point is displayed (see the TCP identifier to the left).

.. image:: /assets/images/robot-integrations/techman/tm-pap-1.png
   :scale: 40 %
   :align: center

Some grippers allow to check pick success (e.g. vacuum check, finger position or force).
The ``set_pick_ok`` node sets the ``var_pick_ok`` to true by default, but this behavior can be overridden to skip placing an object if it was not successfully picked.

.. _techman-place-sequence:

Place sequence
^^^^^^^^^^^^^^

Uses fixed points and the gripper command to place the picked object.

.. image:: /assets/images/robot-integrations/techman/tm-pap-2.png
   :scale: 60 %
   :align: center

Object detection
^^^^^^^^^^^^^^^^

This is a trivial sequence that consists of a single point.
It rarely needs to be modified.

.. image:: /assets/images/robot-integrations/techman/tm-pap-3.png
   :scale: 40 %
   :align: center

.. _techman-main-program:

Main program
~~~~~~~~~~~~

A pattern that is used throughout the program is that whenever a non-recoverable error is found, the flow is directed via a ``Goto`` node to a sequence (``display_msg``) that displays the contents of the ``g_perception_pickit_user_msg`` global variable and stops the program execution.

#. Initialize Pickit using the :ref:`tm-init` component.
   The program requires robot mode to be enabled in the :ref:`Pickit web interface <web-interface-top-bar>` to continue.

  .. note::
    If your Pickit system is not using the default 169.254.5.180 IP address, you should set it in the configuration of the :ref:`init <tm-init>` component.

#. Configure the object detection scenario using the :ref:`tm-configure` component.
   Here the user needs to manually set the setup and product parameters.

   .. image:: /assets/images/robot-integrations/techman/tm-pap-4.png
      :align: center

#. Execute the **detection_sequence** subflow and trigger object detection using the :ref:`tm-findobjects` component.
#. Collect detection results using the :ref:`tm-getresult` component.
#. If there are no more pickable objects, the program terminates. Reasons for termination are:

   #. No object found after *n* consecutive retries.
   #. Empty Region of Interest (ROI).
   #. No camera image.
   #. General failure.

   .. image:: /assets/images/robot-integrations/techman/tm-pap-5.png
    :align: center

#. If there are pickable objects, the **pick_sequence** subflow is executed.
#. If the pick was not successful (c.f. the :ref:`pick sequence <techman-pick-sequence>` for how to check this), a new detection is triggered (back to step 3).

   .. image:: /assets/images/robot-integrations/techman/tm-pap-6.png
      :scale: 60 %
      :align: center

#. Check if enough objects have been picked:

   #. If yes, perform the **place_sequence** subflow and stop the program (below left).
   #. If no, re-trigger object detection using the :ref:`tm-findobjects` component and execute the place sequence in parallel.
      Then go back to step 4 (below right).

   .. image:: /assets/images/robot-integrations/techman/tm-pap-7.png
      :scale: 60 %

Running the program
-------------------

.. caution::
   When running a program for the first time, it is advised to **set a low robot speed**. As such, non-expected behavior (for example due to incorrect programming or wrong calibration) can be identified early enough to prevent the robot from colliding with surrounding objects or people.

.. warning::
   Before running the program, there should exist a valid :ref:`robot camera calibration <robot-camera-calibration>` and that the **tool frame** must be correctly specified.

To allow Pickit to respond to robot requests, Pickit needs to be in **robot mode**, which is enabled in the :ref:`Pickit web interface <web-interface-top-bar>`.