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

Teach a model based on your product
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pickit provides 2 ways to teach a model of your product.

1. **from camera**: show an object to the camera to teach its shape.
2. **from CAD**: upload a Computer Aided Design (CAD) file of your object.

More details on how to teach model with both methods are given in:

.. toctree::
    :maxdepth: 1

    teach-from-camera
    teach-from-cad

Detecting object(s)
~~~~~~~~~~~~~~~~~~~

Now that you've added your models, it's time to detect objects. 

Place your objects below the camera and create a new region of interest box and press the
:guilabel:`Detect` button. On a successful detection, you will see in the :ref:`2D view <2d-view>`
that a frame appears on the detected objects.

.. image:: /assets/images/Documentation/teach-scene-picture.jpg

In the :ref:`Objects view <objects-view>`, the point cloud models are visualized as a colored
cloud on top of the detected objects. When a detection failed because
for example a threshold parameter was exceeded, the model cloud will be
colored in red. At this point the other objects are colored in orange because no pick point
has been defined yet.

.. image:: /assets/images/Documentation/teach-objects.png

In the Objects table, you can see the detected object dimensions,
matching score and the Model ID that was found. Take a look at this
article to learn how to interpret the :ref:`detection-grid`.

If you want to optimize your detections, the article :ref:`Explaining-the-teach-detection-parameters`
goes more in depth on the different parameters of Pickit Teach. We
advice you to experiment with different settings and multiple objects in
different settings (tilted, on top of each other,..)

.. note:: There is a hard limit on the Teach matching time of 5 seconds.
   Before applying any optimization, this limit could be reached.

The next step is to define on or more :ref:`Pick points<pick-points-teach>`. Once the pick points
are defined, the valid and pickable objects are shown in different colors in the Object viewer.

