How to use Pickit Bags
======================

This article guides you through the necessary steps to properly use the
Pickit Bags engine.

.. contents::
    :backlinks: top
    :local:
    :depth: 1

Teach the Region of Interest
----------------------------

When teaching the Region of Interest, place the markers on the floor, and not on the pallet. 
The XY-plane of the **reference frame** should be touching the floor plane. 

.. image:: /assets/images/Documentation/bags_roi_markers.png

Fine-tune the Region of Interest such that it includes the pallet, but not the floor. Make
sure that the Region of Interest is tall enough to include the whole pallet with bags.

Choose the bag pattern
----------------------

In the **Detection** page, section **Bag pattern**, specify the pattern in which the bags are
disposed on the pallet.

The Pickit Bags engines supports five patterns: a 3-bag, two 4-bag (crossing and parallel),
a 5-bag and an 8-bag pattern. You can choose the pattern in the **Detection** page, section 
**Bag pattern**. Examples of pallets for each supported bag pattern are shown below.

.. image:: /assets/images/Documentation/bags_supported_patterns.png

Usually, the layers of the pallet are organized such that the orientation of the bag pattern 
alternates from layer to layer, flipping horizontally or vertically (depending on the pattern) 
from the previous layer. Therefore, the bag pattern may be disposed in two possible orientations. 
Pickit detects not only the layer orientation, but also the best picking order, if it has a 
significant impact on the success of the grasping process.

<image for each pattern, examples for both orientations. Note if picking order matters.>

3-bag pattern
~~~~~~~~~~~~~

The 3-bag pattern consists of two horizontal bags and one vertical bag. The two possible layer
orientations are shown below. 

<image example 3-bag layer, both orientations>

4-bag pattern (crossing)
~~~~~~~~~~~~~~~~~~~~~~~~

In the 4-bag (crossing) pattern, the bags form a square, as shown below. If there is significant
overlap between horizontal and vertical bags, it is important that the overlaying bags are picked
first. It is up to the detection algorithm to make sure that the picking order is correct.

<image example 4-bag layer, non-overlapping and overlapping>

4-bag pattern (parallel)
~~~~~~~~~~~~~~~~~~~~~~~~

In the 4-bag (parallel) pattern, the bags are disposed in parallel, in two groups of two. There
is only one possible layer orientation for this bag pattern.

<image emaple 4-bag parallel> 

5-bag pattern
~~~~~~~~~~~~~

The 5-bag patter includes three vertical bags and two horizontal bags. Overlapping may occur 
between the horizontal and vertical bags, and (or) among the two horizontal bags. 

<image example 5-bags no overlap, overlap>

8-bag pattern
~~~~~~~~~~~~~

Finally, the 8-bag pattern consists of six horizontal bags and two vertical bags.

<example 8-bag>

Pallet characteristics
----------------------

Top layer status
~~~~~~~~~~~~~~~~

In the **Detection** page, section **Pallet configuration**, specify whether each layer of
the pallet is full, or incomplete layers may occur. If this checkbox is disabled, Pickit will
first detect whether the layer is full or incomplete, and only then detect the bags, all at 
once. Only the top layer may be incomplete. If this is never the case in your application,
keep this checkbox enabled, allowing Pickit to jump straight to the bags detection.

<image example full and incomplete (same case)>

Automatically detect overlapping bags
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the 5-bag pattern, it is common that the horizontal bags overlap (left bag above right 
bag, or vice-versa). If you want Pickit to detect which bag is overlapping, enable the 
**Automatically compute which of the horizontal bags is overlapping**. Otherwise (if there
is no or little overlap, or if the overlap is always consistent for all layers), keep this 
checkbox disabled, and instead specify an appropriate bag picking order. This is explained 
further in this article.

<image 5-bag layers, different overlappings>

.. warning::
  Currently, the overlapping check can only be applied to the two horizontal bags of the 5-bag
  pattern. For other bags and patterns, the picking order must be set such that overlapping bags
  are picked first.

Pallet dimensions
~~~~~~~~~~~~~~~~~

Specify the length and width of the pallet.

.. image:: /assets/images/Documentation/bags_pallet_dimensions.png

Minimum pallet height
~~~~~~~~~~~~~~~~~~~~~

Finally specify the minimum height of the last layer of the last layer of bags. We recommend
measuring the height of the wooden pallet and adding around 40 mm. This value allows Pickit
tp know when the pallet is empty.

.. note::
  The minimum pallet height is expressed relatively to the reference frame. It is therefore 
  important that the reference frame is at the level of the floor.

.. image:: /assets/images/Documentation/bags_min_pallet_height.png

Picking the bags
----------------

Pick offset
~~~~~~~~~~~

Depending on the type of bags, it might not be optimal to pick the bags from the center, as 
the heaviest part is sometimes located towards the bottom of the bag. For this reason, you
can provide an offset to the pick pose, along the x-frame (red) of the bag. You can find this
option in the **Picking** page, section **Bag pick frame offset**.

<image 5-bags: no offset, offset towards end>

Bag picking order
~~~~~~~~~~~~~~~~~

Finally, in section **Bag picking order**, you can specify the order at which you want the 
bags to be picked, for each possible layer orientation. If bags are overlalping on the pallet,
the picking order is a crucial setting for a successful pick.

<image example 3 bags. overlapping, different orders>

.. note::
  If you are detecting a 5-bag pattern, and have enabled the checkbox **Automatically compute 
  which of the horizontal bags is overlapping**, you can choose whether to pick the vertical or 
  the horizontal bags first. Pickit will automatically detect which of the horizontal bags should
  be picked first.

.. note::
  If you are detecting a 4-bag (crossing) pattern, Pickit automatically detects the best bag
  picking order for you. Thus, the **Bag picking order** section is not shown in the **Picking**
  page. 

