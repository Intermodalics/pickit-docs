.. _bin-box:

Defining the Bin box
---------------------

The Bin box specifies the box that is used to check for collisions with the bin, as described in :ref:`collision prevention <collision-prevention>`.

In most cases, the ROI box is a good approximation of the bin (:ref:`How-can-i-get-a-better-bin-picking-experience`). Therefore, by default Pickit uses the ROI box as Bin box. However, in some applications, it might be interesting to specify different Bin and ROI boxes. For example, when objects stick out of the top of the bin as shown below.


.. image:: /assets/images/documentation/Bin-vs-Roi.png

To do so, go to **Define bin box** and select the Bin to be different than the ROI box. Then you can specify a different height for the bottom and top of your bin. The Bin box will appear in green in the 3D views, so it can be differentiated from the blue ROI box.

.. image:: /assets/images/documentation/Bin-vs-Roi-view.png