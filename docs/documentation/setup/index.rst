.. _setup:

Setup
=====

In the **Setup** page you define where you want Pickit to look for objects.

.. tip::
  You can learn about the main ideas behind *where to look for objects* by watching this :ref:`video tutorial <video-tutorials-where-to-pick>`.

.. _active-cameras:

Active cameras
--------------

One Pickit processor can be connected to two different Pickit cameras at the same time.
This can be any combination of M and/or L cameras, or an HD and M/L camera combination.
At the moment we do not support two HD cameras connected to the same processor.

Here you select which camera to use in the setup file. Each setup file should have exactly one active camera.

.. note:: This option is only available if multiple cameras are connected to the processor.

.. _region-of-interest:

Region of Interest
------------------

The **Region of Interest box (ROI box)** is the 3D region where object
detection takes place. 

In many applications, the field of view of the Pickit camera is greater
than the region where we want to perform object detection. For example,
in a bin picking application we are only interested in the contents of
the bin. In the image below, we compare the camera field of view
(:ref:`3D <3d-view>` in the Pickit viewer), with the contents of the ROI box
(:ref:`Points <points-view>` in the Pickit viewer).

.. image:: /assets/images/documentation/Region-of-interest-example.png

By specifying a correct ROI box, we get \ **faster detection times**, as
Pickit doesn't have to look for objects where they are not expected. In
the above example, object detection with the shown ROI box is between
two and three times faster than on the entire scene.

The ROI box can also be used to \ **prevent unwanted detections**, for
example if two bins are visible to the camera, but we only want to pick
objects from one. Setting the ROI box around one of the bins will ignore
the contents of the other.

For **bin picking** applications, the ROI box can be used for **bin
representation**, by fitting it to the internal borders of the bin.
Pickit then can (optionally) perform bin collision avoidance and
prevention. Refer to the :ref:`How-can-i-get-a-better-bin-picking-experience`
article for more information on how to make the best use of the ROI box
for such applications.

The ROI box can be defined and modified from the **Setup** page of the Pickit web interface, and the points contained
in it can be visualized in the :ref:`Points view <points-view>`.

.. toctree::
    :maxdepth: 2

    fix-roi-box
    build-roi-box
    fine-tune-roi-box
    detecting-an-empty-roi
    exclude-3d-information-based-on-color
    advanced-filters
    bin-box
