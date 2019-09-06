Pickit example case: Picking of randomly stacked boxes
======================================================

.. image:: /assets/images/examples/example-case-boxes-general.jpg

In this article you will learn how to pick the cardboard boxes in the picture above with Pickit.
We cover the basics of the application as well as the robot program used in this application.
The result will be a working robot application to pick the boxes with a vacuum gripper and drop them off with exact orientation.

For this article we assume knowledge about the basics of Pickit Flex and Pattern.
If you are not yet confident with these detection engines you can get up to speed by reading the following articles: :ref:`Flex` & :ref:`Pattern`

.. contents::
    :backlinks: top
    :local:
    :depth: 1

Motivation
----------

This application picks randomly stacked boxes.
From the way they are presented it is hard to see the orientation of the boxes.
As you can see in the image below: The 3D information shows one big surface.
From the yellow plane it is a challenge to determine the exact location of all five boxes.
Here we will discuss a method that is able to solve these kind of cases.

.. image:: /assets/images/examples/example-case-boxes-3d-clusters.png

The idea to solve this case is to do this in two steps.
In the first step the focus lies on isolating a part by picking it and dropping it on a new location.
In the second step the system looks again to determine the orientation of the isolated box.
After the orientation is determined the box is picked again and stacked in an organized way.

See video below for the result of this approach. Further below everything is explained in detail.

.. raw:: html

  <div style="position: relative; padding-bottom: 5%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
    <iframe src="https://drive.google.com/file/d/16-dCquo9aoAMa05FWR7iSi4byzlyHXTZ/preview" frameborder="0" allowfullscreen width="640" height="480"></iframe>
  </div>

Advanced ROI filter: Dynamic Box-based ROI filter
-------------------------------------------------

The boxes are stacked on a table in different layers.
It seems logical that the robot should always focus on the top most layer first
and afterwards proceed to the next layer.
This is achieved by using the :ref:`Dynamic-box-based-roi-filter`, which discards
any points below a specified distance from the highest point in the Region of
Interest (ROI).
Below the effect of this filter is shown.

Only when all boxes in the top layer are picked, the next layer becomes visible
in the :ref:`Points view <points-view>`, since it now contains the highest points.
For this application the system only keeps the points that are at most 20 mm
below the highest point.

If you are interested in more information about our advanced ROI filters you can have a look a this article: :ref:`advanced-roi-filters`.

.. image:: /assets/images/examples/example-case-boxes-dynamic-roi-filter.png

Small plane strategy
--------------------

In some applications it is hard to determine the correct orientation of parts when they are presented in a random way.
To solve this kind of applications a two step method is applied. In the first step the only aim is to isolate a part.
This is done by attaching our gripper to a part and to drop it somewhere isolated.
For this first step it is not important where the gripper is attached to the part it should just be a good place where the gripper can attach himself.

Here the application is solved by looking for squares with Pickit Pattern.
The dimension of the squares that is looked for is the same as the width of the objects.
By looking for these squares we know that each attachment point is found is always somewhere on the part.
See image below to see how four different attachment points are calculated for the first layer (two for each box).
The system does not look for the object as a whole but will look for small planes on the object good enough to attach himself to.
This is what we call the small plane strategy.

.. image:: /assets/images/examples/example-case-boxes-small-plane-strategy.png

Enforce alignment
-----------------

In this first step the orientation of the part is from no importance.
This means that the pick frames can be forced to be orientated in exactly the same way.
By using the option XYZ||XYZ all pick frames will be orientated exactly as the reference frame.
This allows further optimization of the movement speed of the robot, because the last wrist movement of the robot is not used.
By applying this strategy it means that in the first step all parts will be picked and dropped with the same orientation.

Interested in enforce alignment? See this article about :ref:`enforce-alignment-of-pick-frame-orientation`.

Multiple step program
---------------------

After the first step the part is dropped on an isolated location.
Then a new detection is triggered to determine the complete orientation of the part.
For the second step a second setup and product file are created.
The ROI now focus on the isolated part.
The part itself is detected using Pickit Flex, by looking for rectangles.

The image below shows the complete robot program that has been used for this application.
The second step is done in a second loop in the program.
Right before the loop the setup and product file are changed.
Afterwards the setup and product files are changed back for doing step 1.

.. image:: /assets/images/examples/ur-2-step-template.png

.. _example-empty-roi:

Detect empty ROI-box
--------------------

In the program above, the ``pickit_empty_roi()`` function is used to verify if
there are contents inside the ROI (see :ref:`detecting-an-empty-roi` for more
details).
If the ROI is empty, the program goes back to the first step; else the program
stays in the second step and looks again.

Snapshots
---------

Below you can download three snapshots to see the settings that were used for this application.

.. image:: /assets/images/examples/example-case-boxes-snapshot-1.png

`Demo_SPS_1 <https://drive.google.com/file/d/1p1edGjpiMS1Kn8GB5cBuRCGx7oOXP8wZ/view?usp=sharing>`__

.. image:: /assets/images/examples/example-case-boxes-snapshot-2.png

`Demo_SPS_2 <https://drive.google.com/open?id=1lIP_AjW5D3nDWVkT_-Oyane-jBdSuPV6>`__

.. image:: /assets/images/examples/example-case-boxes-snapshot-3.png

`Demo_SPS_3 <https://drive.google.com/open?id=1nUpbXLw_gAqb_-LXvbp2Px-haxnbSmb7>`__
