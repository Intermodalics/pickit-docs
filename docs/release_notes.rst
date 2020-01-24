.. _release-notes:

Software release 2.2
====================

The new features of the 2.2 release revolve around improving the picking success, even from deeper, more challenging bins.

1. Teach your parts from CAD files
----------------------------------

Do you need to pick complex 3D parts like crankshafts? :ref:`Teach your part by uploading a single CAD file <teach-from-cad>` and save yourself the effort of teaching multiple camera views. The entire part is captured in one shot and taught to the camera in no time.

.. image:: /assets/images/release-notes_teach-camera-cad.png

.. image:: /assets/images/release-notes_teach-cad-model.png

Alternatively, you can still :ref:`teach your parts with the camera <teach-from-camera>`, with the easy user experience you're already familiar with.

2. Pick more parts
------------------

Pickit is not just about detecting parts, but also about being able to pick them. Our two new features significantly increase the likelihood of objects being pickable.

Multiple pick points
~~~~~~~~~~~~~~~~~~~~

If you ever felt limited because you could only set one pick point for your object, we have some good news: you can now :ref:`specify as many pick points as you want <multiple-pick-points>` for your part. The image below shows an example of a power socket being picked by a suction gripper.

.. image:: /assets/images/release-notes_multiple-pick-points.png

Having multiple pick points increases the likelihood that parts are reachable even if they overlap or are close to obstacles like bin walls. Another advantage is that you can find the pick point that requires the smallest robot displacement to reach. This will minimize robot motion and in turn optimize cycle time.

.. image:: /assets/images/release-notes_multiple-pick-points-pickable.png

Flexible pick orientations
~~~~~~~~~~~~~~~~~~~~~~~~~~

Individual pick points are often subject to some flexibility. For instance, if we pick the power socket with a suction gripper, the flexibility of its bellows allow tolerating some gripper tilt, and rotations about the approach direction.

.. image:: /assets/images/release-notes_flexible-pick-orientations.png

By using together multiple pick points with :ref:`flexible orientation <flexible-pick-orientation>`, all 12 detected parts are pickable in the bin below!

.. image:: /assets/images/release-notes_multiple-flexible-pick-points.png

3. Be more robust to collisions with the robot tool
---------------------------------------------------

To make sure that picking a part will not cause the robot tool to collide with the bin or other objects inside it, Pickit needs to know what the tool looks like. Additional :ref:`tool modelling<robot-tool-model>` features have been added, allowing you to model the tool more realistically. You can model a mounted camera, as well as the bulky joints of the robot, above the gripper. You can also model your tool even if it has a slanted end.

.. image:: /assets/images/release-notes_tool-model.png

4. Pick bags out of pallets with our new Bags engine
----------------------------------------------------

Are you still picking heavy bags from a pallet manually, in a less than ergonomic way? Pickit can lend a hand with its :ref:`Bags engine <Bags>`. Specially designed to recognize a variety of common patterns of bags, this engine will relieve your back.

.. raw:: html

  <iframe src="https://drive.google.com/file/d/1XaH31JdYE9SxFtI_V4cY3pVfSw0oFoxT/preview" frameborder="0" allowfullscreen width="640" height="480"></iframe>
  <br>

5. Enjoy our new web interface features
---------------------------------------

Making sure using Pickit is an enjoyable experience is a top priority for us. Teaching and tuning Teach models has become more intuitive and user-friendly.
You can also choose between :ref:`different visualization options in the web interface <web-interface-top-bar>`. Just adapt your workspace to suit your needs!

.. image:: /assets/images/release-notes_ui-visualizations.gif

6. Save snapshots automatically
-------------------------------

Playing around with the settings to optimize your application, and would like to keep track of your changes and results? With this new feature, you can choose to :ref:`automatically save a snapshot on each detection trigger <Automatically-save-snapshots>`.

Get the update now
------------------

If you have an older Pickit version and would like to try 2.2, check out :ref:`how you can upgrade your system <Pickit-system-software-upgrade>`.
