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
2. :ref:`Teach from CAD <teach-from-cad>`: upload a Computer Aided Design (CAD) file of your object.


Detecting object(s)
~~~~~~~~~~~~~~~~~~~

Now that you've added your models, it's time to detect objects. 

Place your objects below the camera as shown below, build a new :ref:`region of interest <region-of-interest>` box and press the :guilabel:`Detect` button.

.. image:: /assets/images/Documentation/detection/teach/scene-picture.jpg
  :scale: 25%
  :align: center

At this point, it's possible to verify in the :ref:`Objects view <objects-view>` if the objects are detected.
Note that at this point, all valid detections will be displayed as unpickable (in orange) because the model doesn't have any :ref:`pick points <pick-points-teach>` defined.

.. image:: /assets/images/Documentation/detection/teach/objects-all-unpickable.png
  :scale: 70%
  :align: center

Once :ref:`pick points <pick-points-teach>` have been defined for a model, Pickit can determine if an object is pickable and display the pick points in the :ref:`2D <2d-view>` (below left) and :ref:`Objects <objects-view>` (below right) views.

.. image:: /assets/images/Documentation/detection/teach/objects-pickable.png
  :align: center

Apart from the qualitative information available in the viewer, the :ref:`detection grid <detection-grid>` provides quantitative information for each detection, such as the detected model, the chosen pick point, the matching score, and the object size and position.

If you want to optimize your detections, the article :ref:`Explaining-the-teach-detection-parameters`
goes more in depth on the different parameters of Pickit Teach. We
recommend to experiment with different settings and multiple objects in
different settings (tilted, on top of each other,..)

.. note:: There is a hard limit on the Teach matching time of 5 seconds.
   Before applying any optimization, this limit could be reached.


