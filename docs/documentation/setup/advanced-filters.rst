.. _advanced-roi-filters:

Advanced filters
----------------

There are a number of advanced Region of Interest filters used for
excluding points \ **inside the ROI box**.

-  :ref:`Flat-curved-region-filter`
-  :ref:`Dynamic-box-based-roi-filter`
-  :ref:`Point-based-roi-filter`
-  :ref:`Plane-based-roi-filter`
-  :ref:`Sphere-based-roi-filter`

.. _Flat-curved-region-filter:

Flat/curved region filter
~~~~~~~~~~~~~~~~~~~~~~~~~

Removes points that belong to flat or curved regions, depending on the selected option.
If curved regions are rejected, a higher curvature threshold results in more points being discarded.
If flat regions are rejected, a lower threshold discards more points.

.. _Dynamic-box-based-roi-filter:

Dynamic Box-based ROI filter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Removes all points in the point cloud that are located at a lower height than the topmost point by more than the specified threshold.
For example, if the highest point has a height of 1 m above the :ref:`Pickit reference frame <reference-frame>` and the threshold is 0.2 m, all points with height under 0.8 m are discarded.

This feature is handy for depalletizing applications, making sure that all objects in the top layer are picked before any object in the next layer.

.. note:: When activated, the **flat/curved region filter** and the **dynamic box-based ROI filter** are applied to every detection.

.. _Point-based-roi-filter:

Point-based ROI filter
~~~~~~~~~~~~~~~~~~~~~~

Removes all points located close to a point present in an image of the
empty workspace.

This feature is handy for removing non-box shaped background elements (hence cannot be removed using the ROI box), such as a fixed bin with slanted walls.

.. note::
  To correctly use this filter:

  #. Make sure that the camera is at a good detection position, and that nothing is occluding the workspace.
  #. Remove all objects from the scene that do not belong to the background, such as objects to be detected.
  #. Press :guilabel:`Build background`. This will trigger a camera capture, allowing Pickit to learn the background points.

.. _Plane-based-roi-filter:

Plane-based ROI filter
~~~~~~~~~~~~~~~~~~~~~~

Removes all points in the point cloud that are located below the most
dominant plane.

The initialization of the plane-based filtering consists of capturing a
reference image of the empty workspace and finding the dominant plane
through all points within the above-defined region of interest box.

This feature is useful in depalletizing applications where layers are separated by cardboard,
and we are interested in detecting only the parts lying on top of the cardboard.
In such cases, the points of the cardboard slow down detections and can make them less accurate.
The plane-based filter allows discarding the points of the underlying cardboard,
even if it is tilted relatively to the Region of Interest.

.. note::
  To correctly use this filter:

  #. Make sure that the camera is at a good detection position, and that nothing is occluding the workspace.
  #. Make sure that the background surface is mostly visible. This is usually the case in applications like the one mentioned above.
  #. Press :guilabel:`Build background`, for Pickit to find the background plane.

.. _Sphere-based-roi-filter:

Sphere-based ROI filter
~~~~~~~~~~~~~~~~~~~~~~~

Removes all points in the point cloud that are located outside the
dominant spherical shape found in the region of interest box.

The initialization of the sphere-based filtering consists of capturing a
reference image of the empty workspace and finding the dominant sphere
through all points within the above-defined region of interest box.

This feature is useful when picking from a bowl-shaped bin.

.. note::
  To correctly use this filter:

  #. Make sure that the camera is at a good detection position, and that nothing is occluding the workspace.
  #. Make sure that the spherical background is mostly visible. If that is not the case, empty it before the next step.
  #. Press :guilabel:`Build background` for Pickit to find the background sphere.
