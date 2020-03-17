Your first detection
====================

Now that all connections are tested we can start our first detection.
For this we'll use a soda can. Note that this is the final step of this
quick start guide that can be completed without having a robot.
Follow the steps below to do your first detection with Pickit:

-  Make sure that the Pickit camera is mounted approximately 700 mm above a flat
   workspace. The workspace is now seen in the :ref:`2D view <2d-view>` on the
   :ref:`Pickit web interface <web-interface>`.
-  In the Pickit web interface press :guilabel:`Disable Robot Mode`.
-  Create a new setup: in the **Setup** tab, on top, click :guilabel:`+ New` and name
   the new setup file 'Test\_Pickit'. Press :guilabel:`Create`.
-  Place the three workspace markers, according the indicated arrows,
   inside the field of view of the camera.
-  Go to the **Build ROI box** section and press :guilabel:`Around QR markers`. This button
   is only enabled if all three Region of Interest markers are visible.
   Wait until the blue box is updated. 
-  Press the :guilabel:`Save` button on top of the Setup tab.

.. image:: /assets/images/first-steps/Empty-roi.png

-  Create a new product: in the **Product** tab, on top, click :guilabel:`+ New` and name
   the new product file 'Test\_Pickit'. Press :guilabel:`Create`. 
-  Make sure that **Pickit Teach** is selected.
-  Now place a soda can on its side in the middle of the marks.
-  Under section **Define your models** press :guilabel:`Teach from camera`. Now a point
   cloud of the soda can is shown in the right side of the tab.
-  Press the :guilabel:`Save` button on top of the **Detection** tab.

.. image:: /assets/images/first-steps/Model-soda-can.png

-  Go back to the :ref:`2D view <2d-view>` and press :guilabel:`Detect`. A pick point (red-green-blue
   arrows) appears above the soda can.
-  Place the soda can somewhere else in between the markers and press
   :guilabel:`Detect` again.
-  Congratulations for your first detection!

.. image:: /assets/images/first-steps/First-detection.png

.. tip::
  You can learn more about the possibilities of Pickit in these video tutorials:

  - :ref:`Where to pick <video-tutorials-where-to-pick>`
  - :ref:`What to pick <video-tutorials-what-to-pick>`
  - :ref:`How to pick <video-tutorials-how-to-pick>`

  and in the :ref:`setup`, :ref:`detection` and :ref:`Picking` articles.
