.. _Explaining-the-flex-detection-parameters:

Explaining the Flex detection parameters
----------------------------------------

The process of detecting objects with the Flex detection engine is all
about step by step testing and fine-tuning parameters until you get a
good result. The parameters for Flex detection are split into five
categories.

.. contents::
    :backlinks: top
    :local:
    :depth: 1

.. _M-HD-preset:

HD camera settings (HD camera only)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /assets/images/Documentation/hd-preset-22.png

The HD camera presets are a set of predefined configurations that optimize the captures of images for specific materials.

This guide helps you chosing a good preset for your application: :ref:`how-to-mhd-preset`.

.. _Group-points-into-clusters:

Group points into clusters
~~~~~~~~~~~~~~~~~~~~~~~~~~

These parameters affect the clustering (grouping) of points. Clustering
points is a way of grouping points belonging to individual objects. A
good way to detect multiple objects is to try and group points that
belong to the same object. The effect of modifying these parameters can
be visualized in the :ref:`Clusters view <clusters-view>`.

There are multiple clustering strategies available, and the choice
initially depends on how the parts are presented in the scene. 

-  For **touching parts**,the system looks at the change of surface. If
   a surface change is to abrupt it is considered as a separate cluster.
   An example where this clustering method is used is for touching
   cylinders or spheres. In the system a few preset configurations exist, and you
   should experiment with them to determine which works best with your
   parts.
-  For **plane-based clustering**, the system looks for flat surfaces.
   If two flat surfaces are touching but their orientation is different, they are considered as separate clusters.
   A typical example where this is used is random boxes in a bin.
-  For **non-touching parts**, you specify the **clustering distance
   threshold**, which represents the minimum distance to consider
   clusters as separate entities. This is typically used for complex shaped parts that are already physically isolated.

Pickit also allows the possibility of **not grouping points into
clusters** at all, and an **expert mode** which is intended mostly for
compatibility with older versions of Pickit. The expert-mode parameters
are such that higher values will typically result in less and/or bigger
clusters, while lower values result in more and/or smaller clusters.

See following article, :ref:`how-to-clustering-preset`, to
see examples and use cases for each clustering method.

.. _Reject-clusters:

Reject clusters
~~~~~~~~~~~~~~~

These parameters are used for rejecting clusters from object
detection. Clusters can be rejected by setting minimum and maximum
values for their **size in number of points**, or their **physical
size** (length, width and height). Clusters can also be rejected if they
touch the **Region of Interest (ROI) box limits** (top, bottom, and/or
sides).

Rejected clusters are not shown in the  :ref:`Clusters view <clusters-view>`,
and their count is listed in the detection summary.

.. image:: /assets/images/Documentation/Reject-clusters.png

.. _Fit-objects-to-clusters:

Fit objects to clusters
~~~~~~~~~~~~~~~~~~~~~~~

These parameters determine the kind of object you want to find. The
effect of modifying them can be visualized in the 
:ref:`Objects view <objects-view>`. Below there is a list of all models and a typical
applications where they are used:

-  **Square** and **rectangle**: cardboard packaging, plastic bags,
   industrial objects.
-  **Circle** and **ellipse**: industrial rings, pipe ends, top of
   soda cans.
-  **Cylinder**: coke cans, tubes, bottles.
-  **Sphere**: oranges, footballs.
-  **Blob** is perfect for detecting objects that can be very well
   clustered but don't have a geometrical shape. Examples for these are
   vegetables and fruit (bananas, peppers ...) and special shaped boxes
   typically on a conveyor belt. 

The image below shows that soda cans can be detected both as cylinders
or circles. Which model is found depends on which side of the is shown
to the camera.

.. image:: /assets/images/Documentation/Flex-soda-cans.gif

For **3D object models** like cylinders and spheres, one can specify:

-  Whether **internal and/or external surfaces** are desired.
-  The **3D matching tolerance**, used to determine the points that
   confirm the object model. 

.. image:: /assets/images/Documentation/3d-matching-tolerance.png

For **2D object models**, Pickit first finds a flat regions and then
looks for the selected model within this surface (square, rectangle, circle or
ellipse). One can specify:

-  Whether the shape is solid or has an internal **hole**, like a ring.
-  Whether to look for the shape in the **outer-most contour only** or
   in the **inner and outer contours**. This is mostly relevant for ring-like shapes, which have
   an internal and external circle.
-  Whether additional :ref:`clustering based on the contours <how-to-cluster-contours>` is needed.
   This option is useful when clustering does not succeed to separate touching objects.
-  The \ **3D matching tolerance**, used to determine the points that
   confirm the flat region.
-  The **2D matching tolerance**, used to determine the points that
   confirm the object model fitting.

.. image:: /assets/images/Documentation/2d-matching-tolerance.png

.. _Filter-objects:

Filter objects
~~~~~~~~~~~~~~

These parameters specify filters for rejecting detected
objects. Rejected objects are shown in the :ref:`detection-grid` as invalid.

Similar to how we reject clusters, objects can be rejected by setting
minimum and maximum values for their  **size in number of points**, or
their **physical size** (length, width, diameter). Additionally,
objects can be rejected depending on the value of the different matching
scores, explained below.

.. _Contour-score:

2D contour score
^^^^^^^^^^^^^^^^

This score only applies to 2D shapes and represents the percentage
of the **2D model contour** that is covered with points within the
**2D matching tolerance**.

.. image:: /assets/images/Documentation/2d-contour-score.png

.. _Surface-score:

2D surface score
^^^^^^^^^^^^^^^^

This score only applies to 2D shapes, and represents the percentage of
the **2D shape surface** that is covered with points taking into account
the **2D and 3D matching tolerance**. 

.. image:: /assets/images/Documentation/2d-surface-score.png

3D scene score
^^^^^^^^^^^^^^

This score applies to all shapes, and represents the percentage of the
**cluster surface** that confirms the **chosen object model**.

The example below is for **cylinders** (in yellow, shown from the side),
but this score can be given for every object shape.

.. image:: /assets/images/Documentation/3d-scene-score.png

.. _Optimize-detections:

Optimize detections
~~~~~~~~~~~~~~~~~~~

These parameters affect the number of points of the captured point cloud
used for object detection. The effect of modifying these parameters can
be visualized in the :ref:`Points view <points-view>`.

Image fusion (M/L camera only)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Image fusion is the combination of multiple camera captures into a
single image. Enabling image fusion can provide  **more detail** in
regions that show flickering in the 2D or 3D live streams. Flickering
typically occurs when working with **reflective materials**. There are
three possible fusion configurations: **None**, **Light fusion** and
**Heavy fusion**.

Image fusion can increase total detection time by up to a second.
The recommended practice is to use None in the absence of flickering,
and try first Light fusion over Heavy fusion when flickering is
present. 

Scene downsampling resolution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The downsampling resolution allows reducing the density of the point
cloud. This parameter has a big impact on detection time, and to a
lesser extent on detection accuracy. More points lead to higher
detection times and higher accuracy, fewer points to lower detection
times and lower accuracy.

In the illustration, you can see an example of setting the scene
downsampling parameter to 1 mm, 4 mm and 10 mm.

.. image:: /assets/images/Documentation/downsampling.png
