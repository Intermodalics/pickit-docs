Build a showcase demo with Teach
================================

This article will guide you in setting up a simple robot picking
showcase demo with Pickit Teach. The Teach engine is the Pickit
solution for finding objects with **complex geometrical shapes** in all
kinds of orientations. In this demo we will be picking electrical plug
shieldings. Click :ref:`here <teach-demo-happy-picking>` to see the video of this demo.

.. contents::
    :backlinks: top
    :local:
    :depth: 1

Requirements
------------

The hardware requirements to set up this demo are:

-  A Pickit vision system
-  A robot and gripper, i.e. UR5 and Robotiq gripper
-  An additional computer or laptop
-  Electrical plug casings, approximate dimensions 110 x 85 x 22 mm
   (contact support@pickit3d.com to get the parts)
-  Two similar bins, approximate dimensions 400 x 300 x 150 mm

.. note:: 
  The length of the fingers of the gripper should be larger than
  the depth of the bin. The main reason is that the head of the robot
  stays out of the bin.

It is assumed that the Pickit system is mounted around 700 mm above the
table and is running correctly. If you are not sure, please follow step
1-4 from our :ref:`quick-start` guide. 

Your first detection (configuring the Pickit files)
---------------------------------------------------

Now that every component is connected to the Pickit system, we are able
to configure Pickit.

In the Pickit :ref:`web-interface`, create a new setup and product file:

-  **Setup 1:** teach_demo_bin_left
-  **Setup 2:** teach_demo_bin_right
-  **Product:** teach_demo

Configuring Pickit comes down to three simple steps:

#. Teaching a model of the part you want to pick.
#. Create a scene where you want to pick these parts.
#. Define a picking strategy.

The information of the model and picking strategy is stored in the
product file and the information of the scene(s) is stored in the
different setup files.

Teaching the model(s)
~~~~~~~~~~~~~~~~~~~~~

Here it is assumed that the parts in this demo only have two ways in which they
can be presented to the camera: either the top or the bottom is
shown. It is assumed that in a random bin, even if a side is shown, that
after a while the part will fall down in the bin and either top or
bottom are shown. Due to this assumption it is sufficient to teach two
models of the part. One model will contain all information of the top of
the part and the second one contains all information of the bottom.

See below for images of both models that are used in the **Detection** page.
Below the images all detection parameters are given. See following
articles on how to use Pickit :ref:`Teach`.

.. image:: /assets/images/examples/teach-demo-model-1.png

.. image:: /assets/images/examples/teach-demo-model-2.png

The following parameters are used in both models:

-  **Matching tolerance:** 4 mm
-  **Minimum matching score:** 75%
-  **Fusion:** None
-  **Downsampling:** 4
-  **Detection speed:** Normal

Note the orientation of the **pick points** for both models, one is
rotated 90° towards the other. The reason for this is that the gripper
is going to approach the bottom and top under a different orientation.

Don't forget to save the settings. This will update the Product file.

Create the scene(s)
~~~~~~~~~~~~~~~~~~~

The second step defines where Pickit has to look for objects. This is
done by defining the :ref:`region-of-interest` (ROI).

Below you can see a picture of a well-defined ROI for this application.
All useless information is filtered out (the bin and the table), and only
information of the parts in the bin is kept. Also make sure that the ROI
is slightly higher than the real bin.

For this demo two different ROI's are defined, one for each bin. Don't
forget to save the settings in the corresponding Setup files.

.. image:: /assets/images/examples/teach-demo-3d.png

.. image:: /assets/images/examples/teach-demo-points.png

Define the picking strategy
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Finally, the picking strategy is defined. For this application, only collisions between tool and bin are checked. This means that Pickit checks if the gripper can
pick the parts without hitting the bin. More information about the
picking strategies can be found in the :ref:`Picking` article.

For this demo, the following parameters are used:

-  **Check collision with:** Bin
-  **Ordering Strategy:** Highest product center

Don't forget to save the settings. This will update the Product file.

Calibration
-----------

Next step is the robot-camera calibration. This process teaches Pickit
where the robot base is located w.r.t. to the camera. This information
is used to transform the object pick points into robot coordinates. A
detailed description in robot-camera calibration can be found in the article :ref:`robot-camera-calibration`. 
Do not forget to save after the calibration is finished.

Your first pick (Program the robot)
-----------------------------------

Now Pickit is configured, the only thing left to do is programming the
robot. The robot used in the demo video is a UR5, but a similar program
can be created on any other robot.

The idea of this program is to start looking for the parts in one bin.
If one is found the robot moves towards the calculated position, opens
its gripper according to which side is found (bottom or top), grasps the
part, gets out of the bin and drops it off in the other bin. The parts
are dropped using the pallet function. This function drops the
parts in different locations of the bin so no stack of parts is
created. The robot starts picking from the other bin either after 8
successful picks or after two unsuccessful detections. 

-  **The UR robot program:** Download
   link \ `here <https://drive.google.com/uc?export=download&id=1Nzqm_fDFosR59ZeQL8D-RrKCDCNLuytF>`__.

.. image:: /assets/images/examples/teach-demo-ur-program.png

.. note:: When performing random bin picking, **always** trigger a new
   detection before picking the next object. The main reason lies in the
   fact that the environment can change when an objects are picked and this
   could lead to undesired miss-picks.

.. warning:: When using the UR download program in the provided link,
   **change the waypoints** to avoid moving the robot to unsafe positions.

.. _teach-demo-happy-picking:

Happy picking!
--------------

Following all these previous steps leads to the next Pickit Teach demo
application, happy picking!

.. raw:: html

  <iframe src="https://drive.google.com/file/d/1BGHPB6mAy-fL-DTyI6c7pp1ExfsPErhY/preview" frameborder="0" allowfullscreen width="640" height="360"> </iframe>
  <br>

If you need any help with one of the steps above, please contact 
`support@pickit3d.com <mailto:mailto://support@pickit3d.com>`__.
