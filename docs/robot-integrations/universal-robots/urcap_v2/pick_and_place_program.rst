.. _urcap-pick-and-place-program:

Example pick and place program
==============================

The program implements a pick and place task where Pickit is used to continuously pick objects from a detection region and place them in a specified dropoff location.
No assumptions are made on how objects are laid out in the detection region, so the program is a good starting point to build a wide range of applications.
Objects can be for instance stacked randomly in a bin, or in a pattern on top of a pallet.

.. image:: /assets/images/robot-integrations/ur/pick-and-place-overview.png
  :align: center

Creating the program
--------------------

.. note::
  This example program uses the Pickit :ref:`pick and place template <urcap-pick-and-place-template>`, which is available for **URCap 2.0** or later and **Pickit 2.2** or later.
  Installation instructions can be found :ref:`here <universal-robots-urcap-installation>`.

1. Create an empty robot program, and in the top *Robot Program* section, set the program to not loop forever (by default it does).

  .. image:: /assets/images/robot-integrations/ur/polyscope-program-loops-forever.png
    :scale: 80%
    :align: center

2. In the the left panel click :guilabel:`URCaps` → :guilabel:`Pickit: pick and place` to :ref:`add an instance <template-insert>` of the :ref:`pick and place template <urcap-pick-and-place-template>`, a program node for executing vision-guided pick and place tasks with *minimal programming effort*.

3. On insertion, two basic questions about the application need to be answered.
   Clicking :guilabel:`Done` initializes the template.

  .. image:: /assets/images/robot-integrations/ur/pick-and-place-basic-configuration.png
    :scale: 70%
    :align: center

The program explained
---------------------

.. image:: /assets/images/robot-integrations/ur/pick-and-place-tree.png
  :align: center

Below the top-level :ref:`pick and place <template-pick-and-place>` node, the three main sequences responsible for :ref:`object detection <template-object-detection>`, :ref:`pick <template-pick>` and :ref:`place <template-place>` can be seen.
Additonally, the optional :ref:`Action after end <template-action-after-end>` sequence is enabled, which by default provides useful information when setting up and debugging the application.

Lines marked in yellow by Polyscope indicate that they (or their nested commands) have uninitialized input parameters that must be set before running the program.
The minimum inputs required to run the pick and place program are:

- **Pickit configuration** (:ref:`setup, product <Configuration>`) used for :ref:`object detection <template-object-detection>`.
- **Three waypoints:** ``Detect``, ``AbovePickArea`` and ``Dropoff`` (:ref:`learn more <template-waypoints>`).
- **Tool actions** for :ref:`grasping <template-pick>` and :ref:`releasing <template-place>` an object.

.. note::

  Before teaching the above waypoints, make sure the Tool Center Point (TCP) is correctly specified for your robot tool.

.. image:: /assets/images/robot-integrations/ur/pick-and-place-waypoints.png
  :align: center

Once the required inputs have been specified, the program should no longer contain commands in yellow.

.. image:: /assets/images/robot-integrations/ur/pick-and-place-tree-all-white.png
  :align: center

That's it! We are now ready to run the program and pick some parts.

Running the program
-------------------

.. include:: ../../run_program_warning.rst

Also, make sure the robot is in **normal mode** and not in **simulation**.

.. image:: /assets/images/robot-integrations/ur/run-program-polyscope-5.png
  :align: center

While the program runs, the state of Pickit object detections can be interactively monitored from Polyscope by clicking the top-level :ref:`pick and place <template-pick-and-place>` node, where a live camera stream is shown.

.. image:: /assets/images/robot-integrations/ur/pick-and-place-top-level-node.png
  :scale: 70%
  :align: center

The pick and place template will by default continue until no more pickable objects are found, and will then exit.
When this happens, the :ref:`Action after end <template-action-after-end>` sequence will raise an informative popup mentioning the reason for no more pickable objects.

Once pick and place is up and running, you can fine-tune its behavior by editing the advanced configuration (accessible from the top-level :ref:`pick and place <template-pick-and-place>` node), or optimizing the motion sequences in :ref:`object detection <template-object-detection>`, :ref:`pick <template-pick>` and :ref:`place <template-place>`.

Happy picking!






