.. _example-case-washers:

Pickit example case: Picking of washers
=======================================

This article covers an extensive overview of an actual Pickit application, namely picking randomly overlapping washers out of a bin.
The goal is to drop the washers on a peg, aligned, hence high accuracy is required.
This article covers the basic concepts required for solving this application, as well as the robot program.

Motivation
----------

For this application high accuracy is necessary to drop off the washers.
Such accuracy is not always easy or even possible to achieve when picking the parts straight from the bin.
One of the reasons for this is that, in a random bin, the parts are usually partially occluding by each other.
Furthermore, specifically for this application, a magnetic gripper is used to pick the parts.
Influenced by the magnetic field, the washers tend to move slightly while grasped, and consequently the detection accuracy is lost.

To solve this, a robot program with two steps is introduced.
In the first step, the focus is to pick one part from the bin.
Once the part is picked, it is shown again to the Pickit camera to determine its exact position.
This information is then used to correct the drop off position the part.

See the video below to see the results of this approach.
The video clearly shows the robot correcting its position when dropping off the part, such that the washers fall accurately on the peg, nicely aligned.

.. raw:: html

  <div style="position: relative; padding-bottom: 5%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
    <iframe src="https://drive.google.com/file/d/1KaPsAjKCBHB4pRVqlcnSq8xrF7qKKAHQ/preview" width="640" height="480"></iframe>
  </div>

Robot program
-------------

To set up this application, we provide the **in-hand check** template program, presented below.
The template starts by first picking a part from the bin.
Then, in a second step, the part is presented again to the camera while grasped (hence the name "in-hand"),
and a new detection is triggered, to determine the exact position of the part in the gripper.
If this detection is successful, the part is dropped off neatly on the peg.
Otherwise, the part is dropped back in the bin:
since accuracy is important, if we are not entirely sure of how the part is presented, it is better to simply try again with a different part.

The example program can be downloaded 
`here <https://drive.google.com/uc?export=download&id=1yBcGJEkV0K-By5QvIRH6QiTLySjjsDGB>`__.

.. image:: /assets/images/examples/ur-in-hand-check.png

.. _drop-off-pose:

In order to use the template, you still need to define the variables listed below.

Drop
~~~~

The waypoint **drop** is defined where the part would be dropped off, in case no correction was necessary.
In the template, the robot will never move to this waypoint, but it is used to calculate the corrected waypoints **corr_drop** and **corr_pre_drop**.

For this application, the **drop** waypoint is defined by bringing the TCP of the robot just above the center of the peg.
If the gripper is grasping the washer from the side, when dropping off, the robot will go to a position translated from the **drop** waypoint, such that the part falls centered on the peg, as shown in the image below (right).

.. image:: /assets/images/examples/in-hand-check-tcp-pick-frame-correction.png

.. note::
  The **drop** waypoint is important for the application to work as expected, and is closely tied to the pick frame of the Teach model used during the in-hand check.
  The **drop** waypoint and the pick frame should be such that, if the gripper was grasping the part perfectly aligned with the pick frame, the robot could go to the **drop** waypoint and accurately drop the part on the peg, without any correction. 
  There is an alerting popup message in the template, highlighting this attention point.


Fixed waypoints
~~~~~~~~~~~~~~~

**Home_pose** is the starting position of the robot program.
**Detect_pose** is a waypoint where the robot does not block the field of view of the Pickit camera to look into the bin.
**Present_pose** is a waypoint where the part is presented to the camera for the in-hand check.
**Drop_off_bin** is a waypoint to drop back parts into the bin.

Bin picking setup/product file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For this application, a simple :ref:`setup` file with a ROI box with similar dimensions as the actual bin is created.

In the product file, the :ref:`teach` detection engine is used to find the washers.
To maximize the number of detections, the model consists of a half of the washer, and the pick frame is positioned on the surface.

These files need to be filled in twice in the robot program, in a `Select` command, 
once at the beginning and once after the second step.

In-hand check setup/product file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ROI in this :ref:`setup` should include the isolated washer while it is being grasped by the robot gripper.

The product file is again a :ref:`teach` detection.
This time, a full model of the washer is taught. In this tutorial, we place the pick frame in the center of the model.

.. note::
  Keep in mind that the Teach model pick frame must be defined such that, when dropping off the washer with the robot on **drop**, it falls on the peg.
