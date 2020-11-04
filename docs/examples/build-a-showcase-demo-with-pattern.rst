Build a showcase demo with Pattern
==================================

This article will guide you in setting up a simple robot picking demo
with Pickit Pattern. This detection engine is made for picking
objects with **simple geometrical** **shapes** stacked into an
**organized pattern**. In this demo we are picking cardboard boxes.
Click :ref:`here <pattern-demo-happy-picking>` to see the video of this demo.

.. contents::
    :backlinks: top
    :local:
    :depth: 1

Requirements
------------

The hardware requirements to set up this demo are:

-  A Pickit vision system
-  A robot and gripper, UR5 + vacuum suction cup
-  An additional computer or laptop
-  Cardboard boxes of equal size, i.e. 115 x 65 x 30 mm
   (contact support@pickit3d.com to get exactly these parts).

It is assumed that the Pickit system is mounted around 700 mm above the
table and is running correctly. If you are not sure, please follow step
1-4 from our :ref:`quick-start` guide. 

Your first detection (Configure the Pickit files)
-------------------------------------------------

Now that every component is connected to the Pickit system, we are able
to configure Pickit.

In the Pickit :ref:`web-interface`, create a new setup and product file:

-  **Setup:** pattern_demo.
-  **Product:** pattern_demo.

Configuring the Pickit comes down to three simple steps:

#. Create a scene where you want to pick the parts
#. Define the shape of objects that need to be picked
#. Define a picking strategy

Create a scene
~~~~~~~~~~~~~~

The first step defines where Pickit has to look for objects. This is
done by defining the :ref:`region-of-interest` (ROI). 

Below you can see a picture of a well-defined ROI for this application.
All useless information is filtered out (the table and surroundings), keeping only information of the parts. 

Don't forget to save the settings in the corresponding Setup files.

.. image:: /assets/images/examples/pattern-demo-points.png

Define the detection parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The second step consists in setting up the Pickit Pattern detection
engine. In this application Pickit will look for fixed sized
rectangular shapes.

The images below show the results of the clustering and fitting
steps. See the
following article on how to use Pickit :ref:`Pattern`.

.. image:: /assets/images/examples/pattern-demo-clusters.png

.. image:: /assets/images/examples/pattern-demo-objects.png

In this demo, the following parameters are used:

-  **Clustering:** Non-touching 
-  No **rejecting clusters**
-  **Object model:** rectangle
-  **Contour:** inner and outer
-  **3D tolerance:** 15 mm
-  **2D tolerance:** 10 mm
-  **Expected length:** 115 mm
-  **Expected width:** 65 mm
-  **Expected orientation:** either X||X or X||Y depending on
   the pattern orientation w.r.t. the :ref:`reference frame <reference-frame>` in the :ref:`3D view <3d-view>`.
-  **2D contour score:** 45%
-  **2D surface score:** 95%
-  **Fusion:** None
-  **Downsampling:** 1 mm

Don't forget to save the settings. This will update the Product file.

Define the picking parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Finally the picking strategy is defined. For this application no special
strategies are applied. However, more information about the picking
strategies can be found in the :ref:`Picking` article.

-  **Check collision with:** none
-  **Ordering Strategy:** Highest product center

Don't forget to save the settings. This will update the Product file.

Calibration
-----------

Next step is the robot-camera calibration. This process teaches Pickit
where the robot base is located w.r.t. to the camera. This information
is used to transform the object pick points into robot coordinates. A
detailed description in robot-camera calibration can be found in the article :ref:`robot-camera-calibration`. 
Do not forget to save after the calibration is finished.

Program the robot
-----------------

Now Pickit is configured, the only thing left to do is programming the
robot. The robot used in the demo video is a UR5, but a similar program
can be created on any other robot.

The idea of the program is to trigger a detection and pick all found
parts one by one. The parts are dropped off on a running conveyor. Since
the boxes are nicely stacked and it is unlikely that a part will move
when one is pickit, it is not necessary to trigger a new detection
every time.

-  **The UR robot program:** Download
   link \ `here <https://drive.google.com/uc?export=download&id=1CDlLHGBOY-UKC28ONp_8AvYfquVs0W4V>`__.

.. image:: /assets/images/examples/pattern-demo-ur-program.png

.. warning:: When using the UR download program in the provided link,
   **change the waypoints** to avoid moving the robot to unsafe positions.

.. _pattern-demo-happy-picking:

Happy picking!
--------------

If you followed all steps above, you're ready building your Pickit
product showcase using the Pattern detection engine. Happy picking!

.. raw:: html

  <iframe src="https://drive.google.com/file/d/10b-IjeS_dyV19iv89WcnRObJlfhgguVw/preview" frameborder="0" allowfullscreen width="640" height="360"> </iframe>
  <br>

If you need any help with one of the steps above, please contact 
`support@pickit3d.com <mailto:mailto://support@pickit3d.com>`__.
