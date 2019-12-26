.. _How-to-edit-existing-model:


How to edit an existing Pickit Teach model
------------------------------------------

After teaching a model, it is possible to change it, without the need to add
or delete models. This article explains how you can edit an existing model.

.. contents::
    :backlinks: top
    :local:
    :depth: 1

Re-teaching the model cloud
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you wish to change the model cloud from scratch, click on the :guilabel:`Re-teach` button of the
concerned model. This replaces the model cloud by the content of your current
:ref:`Region of Interest (ROI) <region-of-interest>`.

A common example is when you realize that the model cloud quality could be improved. For
instance, a model taught with the camera at a far distance might be missing important
details. In that case, you may want to :guilabel:`Re-teach` it from a closer distance.

**Left: model taught at a long distance to the camera. Right: model re-taught at a short distance to the camera.**

.. image:: /assets/images/Documentation/Teach-model-taught-far-close.png

.. _crop-and-expand-model:

Cropping and expanding a model cloud
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When clicking :guilabel:`Teach from camera` or :guilabel:`Re-teach`, the resulting model
corresponds to the content of the current ROI. The
model point cloud can be cropped or expanded afterwards, using the arrows in the
**Model** view.

On the top left corner of the **Model** view, there is a **Auto-snap crop box**
checkbox. If this option is enabled, the green model box automatically adjusts to
the limits of the model points. This is useful for you to check if the model
contains undesired points that are difficult to spot.

**If there are no undesired points in the model, the auto-snapped model box bounds the model points cleanly.**

.. image:: /assets/images/Documentation/Teach-model-autosnap-on-clean.png

If the model contains undesired points that are difficult to see, the auto-snapped model box
seems larger than the actual model. In the model shown below, undesired points can be found on the
top right corner of the model bounding box.

.. image:: /assets/images/Documentation/Teach-model-autosnap-on-ghostpoints.png

If the auto-snap option is disabled, the green model box is set to whatever you define
using the model arrows.

.. image:: /assets/images/Documentation/Teach-model-autosnap-off.png

.. note::
  Cropping and expanding operations do not replace the model with the content of the
  current ROI. Instead, they work on the point cloud that was captured
  at the moment of teaching. When expanding the model box (making it larger), it is
  possible to include points that were initially outside the ROI at
  the time of teaching.

There are several situations where cropping an existing model is extremely convenient, as opposed
to re-teaching it from scratch:

#. Suppose that, upon teaching the model, undesired small amounts of points, that are
   difficult to spot, are accidentally included in the model cloud. You can quickly
   get rid of these points by cropping them out of the model, without the need to re-teach
   the model with a cleaner workspace.

#. When using Pickit Teach, it is intuitive to teach the whole object to be detected. However,
   depending on the part geometry, this might not lead to the best results. In particular, parts which
   are **almost symmetrical except for a small detail** tend to be fit 180 degrees flipped around
   the symmetry axis. Such wrong fits have a high matching score, since only a small percentage
   of model points are unmatched. Consequently, both good and bad fits have a high score, making it
   difficult to filter out bad fits. The image below illustrates this behavior for an almost symmetrical
   tube, which has one of the tips slightly wider than the other.

   .. image:: /assets/images/Documentation/Teach-full-model-symmetric.png

   A way to increase the score gap between good and bad fits is to crop out some of the redundant
   side of the part, keeping  mainly the small detail in the model. Using the cropped model, a 180
   degree flipped fit will have a much worse matching score than a good fit, since now the percentage
   of unmatched points is larger relatively to the total amount of model points.

   .. image:: /assets/images/Documentation/Teach-cropped-model-symmetric.png

#. As one can guess by the example given above, finding a good Teach model can sometimes be a
   trial-and-error process. Compared to re-teaching a model, cropping an existing one is much
   faster, since this does not require the part to be placed under the camera and the Region of
   Interest to be adjusted. This ease of use allows you to quickly try out different cropped
   versions of the model and compare results.

   .. image:: /assets/images/Documentation/Teach-crop-experiment.png
