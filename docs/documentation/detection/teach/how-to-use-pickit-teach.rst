How to use Pickit Teach
-----------------------

This article describes how to get started with the Pickit Teach engine.
Pickit Teach is a detection engine which can search for
objects based on a previously taught model of the object. It is primarily used
to find irregularly shaped objects that don't fit in one of the basic
shape categories, like cylinders, spheres, squares, rectangles, circles or ellipses.

.. contents::
    :backlinks: top
    :local:
    :depth: 1

.. _teach-a-model:

Teach a model based on your part
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::
    :maxdepth: 1
    :hidden:

    teach-from-camera
    teach-from-cad

Pickit provides 2 ways to teach a model of your part:

1. :ref:`Teach from camera <teach-from-camera>`: show an object to the camera to teach its shape.
2. :ref:`Teach from CAD <teach-from-cad>`: upload a Computer Aided Design (CAD) file of your part.


Detecting objects
~~~~~~~~~~~~~~~~~

Now that you've added your models, it's time to detect objects. 

Place your objects below the camera as shown below, build a new :ref:`region of interest <region-of-interest>` box and press the :guilabel:`Detect` button.

.. image:: /assets/images/documentation/detection/teach/scene-picture.jpg
  :scale: 25%
  :align: center

At this point, it's possible to verify in the :ref:`Objects view <objects-view>` if the objects are detected.
Note that at this point, all valid detections will be displayed as unpickable (in orange) because the model doesn't have any :ref:`pick points <pick-points-teach>` defined yet.

.. image:: /assets/images/documentation/detection/teach/objects-all-unpickable.png
  :scale: 70%
  :align: center

Once :ref:`pick points <pick-points-teach>` have been defined for a model, Pickit can determine if an object is pickable and display the pick points in the :ref:`2D <2d-view>` (below left) and :ref:`Objects <objects-view>` (below right) views.

.. image:: /assets/images/documentation/detection/teach/objects-pickable.png
  :align: center

Apart from the qualitative information available in the viewer, the :ref:`detection grid <detection-grid>` provides quantitative information for each detection, such as the detected model, the chosen pick point, the matching score, and the object size and position.

If you want to optimize your detections, the article :ref:`Explaining-the-teach-detection-parameters`
goes more in depth on the different parameters of Pickit Teach. We
recommend to experiment with different settings and multiple objects in
different settings (tilted, on top of each other,..)

.. note:: There is a hard limit on the Teach matching time of 5 seconds.
   Before applying any optimization, this limit could be reached.

.. _teach-flat-objects-note:

A note on flat objects
^^^^^^^^^^^^^^^^^^^^^^

Pickit Teach requires objects to have distinct 3D shape features to be reliably detected.
Flat objects are different from other 3D shapes in the sense that edges are the main source of shape information.

The :ref:`flat objects <teach-flat-objects>` option tells Pickit Teach to focus on shape edges when performing object detection.
The following example shows how to detect thin and flat sheet metal parts with this option.

.. image:: /assets/images/documentation/detection/teach/flat_objects.png
  :align: center
  :scale: 70%

.. tip::
  When :ref:`teaching from camera <teach-from-camera>` the model of a flat object, it is advised to have the model parallel to the ground (not tilted).
  For thin objects, it's advised to raise them during teaching to have a clear height difference with respect to the ground plane.

.. tip::
  When detecting very thin objects, it is advised to include the ground plane when building the :ref:`ROI <region-of-interest>`.
  This makes sure that objects lying directly on the ground are completely included in the ROI.

  Note that, for non-thin objects, it is generally advised to exclude the ground plane from the ROI for performance reasons.
  When the flat objects option is enabled, the ground plane doesn't add a significant performance overhead, as only its edges are considered.
