Your first detection
====================

Now that all connections are tested we can start our first detection.
For this we'll use a soda can. Note that this is the final step of this
quick start guide that can be completed without having a robot.
Follow the steps below to do your first detection with Pickit:

-  Make sure that the Pickit camera is mounted 700 mm above a flat work
   space. The work space is now seen in the :ref:`2D view <2d-view>`.
-  In the Pickit user interface press Stop Robot Mode.
-  In the Configuration tab under create a new setup and/or product fill
   in 'Test\_Pickit' twice and press Create.
-  Place the three workspace markers, according the indicated arrows,
   inside the field of view of the camera.
-  Go to the Region of Interest > ROI Box filter and press Use Markers.
   Wait till the blue box is updated. 
-  Set following values for Zmin and Zmax: 10 mm and 150 mm.
-  Press the Save button.

.. image:: /assets/images/First-steps/Empty-roi.png

-  In the Detection tab select Pickit Teach. 
-  Now place a soda can on his side in the middle of the marks.
-  Under define your model(s) press Add a model. Now the :ref:`Model view <model-view>` is
   opened and a point cloud of the soda can is shown.

.. image:: /assets/images/First-steps/Model-soda-can.png

-  Go back to the :ref:`2D view <2d-view>` and press Detect, a Pick Frame (red-green-blue
   arrows) appears above the soda can.
-  Place the soda can somewhere else in between the markers and press
   Detect again.
-  Press the Save button.
-  Congratulations with your first detections!

.. image:: /assets/images/First-steps/First-detection.png

.. tip:: More information about the possibilities of the Pickit system can be
   found in the :ref:`region-of-interest` or the :ref:`teach` section.
