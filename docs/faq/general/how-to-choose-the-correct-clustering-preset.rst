.. _how-to-clustering-preset:

How to choose the correct clustering preset
===========================================

.. contents::
    :backlinks: top
    :local:
    :depth: 1

The clustering preset is an important parameter when using the detection engines :ref:`Flex` or :ref:`Pattern`.
In this article an example of different clustering methods is showed and
discussed. This example should help you chosing the correct setting for your application.

The scene below is used to explain the different clustering
methods. In the scene there are 3 shampoo bottles next to each other, 4
boxes randomly on top of each other and 4 electrical plug shieldings
separated from each other.  A snapshot of this scene can be downloaded 
`here <https://drive.google.com/uc?export=download&id=1O_N-cxPfPcg-TQpFimSls3jx3sEwM_RW>`__.

.. image:: /assets/images/Documentation/Clustering-2d.png
.. image:: /assets/images/Documentation/Clustering-points.png

Touching parts
~~~~~~~~~~~~~~

These methods look at the change of surface. If a surface change is too
abrupt it is considered as a separate cluster. On the image below the
results of this clustering method is shown. For the shampoo bottles
three different clusters are formed which is good. For the boxes, the 2
boxes that are aligned but under an angle are not clustered apart. The
transition of the surface is to smooth to filter them apart. For the
electrical plug shieldings multiple clusters per part are formed, which
is not good.

**Best results for:**

-  Rounded parts
-  Cylinders: bottles, gas springs, steel bars,..
-  Balls: tennis balls, oranges,..

.. image:: /assets/images/Documentation/Clustering-touching.png

Plane Based Clustering
~~~~~~~~~~~~~~~~~~~~~~

This method looks for flat surfaces in the scene. If two surfaces have a
different orientation they are considered as separate clusters. On the
image below the results of this clustering method is shown. For the
shampoo bottles multiple clusters are formed, which is not good. For the
boxes all of the boxes are clustered apart andno points are missing at
the edges of the surfaces, which is good. For the electrical plug
shieldings multiple clusters per part are formed, which is not good.

**Best results for:**

-  Flat surfaces
-  Boxes

.. image:: /assets/images/Documentation/Clustering-plane-based.png

Non-touching parts
~~~~~~~~~~~~~~~~~~

This method groups points into cluster that are close together. Objects
are clustered apart if there is a physical gap. On the image below the
results of this clustering method is shown. For the shampoo bottles one
big cluster is formed, which is not good. Also the two aligned boxes are
not clustered apart. For the electrical plug shieldings, which are
positioned separated, one cluster per part is formed, which is good.

**Best results for:**

-  (Complex) shapes that are separated

.. image:: /assets/images/Documentation/Clustering-non-touching.png