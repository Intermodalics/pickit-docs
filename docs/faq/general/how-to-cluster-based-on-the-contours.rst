.. _how-to-cluster-contours:

How to cluster based on the contours
====================================

Contour clustering is an option mostly used when detecting 2D shapes with Pickit :ref:`Flex`.
Flex expects there to be one cluster per part, but this is not always the case, in particular for 2D shapes.
This additional clustering step divides the contour of a cluster into several segments, allowing Flex to fit ab object on each individual segment.
The remainder of this article presents examples where contour clustering helps to discriminate touching parts.

Boxes touching at a corner
--------------------------

In the image below two boxes that are touching in one corner are shown.
Because the surfaces of the boxes are at the same level, it is not possible to cluster the two boxes apart from each other.
Consequently, Pickit :ref:`Flex` fits one big rectangle on both parts, leading to a wrong fit.

.. image:: /assets/images/faq/touching-rectangles-bad.png

Since we are looking for rectangular shapes, the two corners highlighted in green below can be used to identify the boundary between the shapes and split the contour into two smaller segments, one for each rectangle.

.. image:: /assets/images/faq/cluster-contours-touching-boxes.png

If we go back to the example, a rectangle will be correctly fitted on each box.

.. image:: /assets/images/faq/touching-rectangles-good.png

Boxes touching at an edge
-------------------------

A similar example is when two boxes are touching by an edge but not perfectly aligned, like in the image below.
Again the surfaces are at the same level, so they can't be clustered apart.
Also here, fitting a rectangle on this cluster will not give a good result.

.. image:: /assets/images/faq/aligned-rectangles-bad.png

Here we also have two corners that can help us split up the contour points in two smaller clusters.
In the image below you can see that the contour points are now shown in two different colors.
Now, for every contour cluster, a rectangle is fit and good results are obtained.

.. image:: /assets/images/faq/aligned-rectangles-good.png


Touching circles
----------------

Another example is when two circular objects are touching, as shown in the image below.
Also here the surfaces are at the same level, so they can't be clustered apart.
Fitting one circle on the whole cluster doesn't make sense and leads to bad results.

.. image:: /assets/images/faq/circles-bad.png

If contour clustering is applied to this case, four smaller clusters are obtained.
The contours of the two holes are clustered apart, and also the outer contour is split in two.
In the image below, two circles are fit to the outer contours.
Note that similar results can be obtained by fitting circles on the inner contour clusters.
In this case they are filtered out by using the filtering settings of Pickit :ref:`Flex`.

.. image:: /assets/images/faq/circles-good.png