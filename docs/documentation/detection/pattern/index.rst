.. _Pattern:

Pattern
=======

The Pickit Pattern engine is similar to Flex. Pattern looks for 2D objects (rectangles, squares, circles and ellipses) of known fixed size. This allows the Pattern detection engine to solve applications beyond the limits of Flex. For instance, in the case presented below, Pattern can distinguish the individual aluminium blocks, even if they are aligned and touching. Flex, on the other hand, would only recognize the individual blocks if they could be grouped separately, which is not the case in this example.

.. image:: /assets/images/documentation/Pattern-2d.gif

.. toctree::
    :maxdepth: 1

    how-to-use-pickit-pattern
    explaining-the-pattern-detection-parameters
