.. _Explaining-the-teach-detection-parameters:

Explaining the Teach detection parameters
-----------------------------------------

The Pickit Teach detection engine is designed to detect complex
3D shapes. This article explains its detection parameters.

.. contents::
    :backlinks: top
    :local:
    :depth: 1

HD camera settings (HD camera only)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The HD camera settings are explained in :ref:`M-HD-preset`.

Define models
~~~~~~~~~~~~~~~~~~~~

.. image:: /assets/images/documentation/teach-model-grid-22.png

A list of taught models is shown accompanied by their ID and
the number of points. By default, there are no models defined.

Add a model
^^^^^^^^^^^

Press :guilabel:`Teach from camera` or :guilabel:`Teach from CAD` to teach your first model. The points
currently visible within the ROI are now saved into a model. When the
model is successfully created, the model will automatically be shown in
the tab.

To add extra models, press :guilabel:`+` in the model tab. In one product file, up to 8 different models can be taught.
This means that Pickit Teach is capable of looking for 8 different shapes in one detection.
See :ref:`how-to-multiple-models` on how you can use the model ID in a robot program.

Re-teach a model
^^^^^^^^^^^^^^^^

A model taught from the camera can be retaught by pressing :guilabel:`Re-teach`.
By pressing this button, the points currently visible within the ROI
are saved into the model.

.. warning:: When re-teaching a specific model, the point-cloud
   data from the previous model is overwritten. This action cannot be
   undone.

It is also possible to crop or expand an existing model, without the need
to re-teach it. Refer to the article :ref:`How-to-edit-existing-model` for
further details.

Delete a model
^^^^^^^^^^^^^^

To delete a model, press :guilabel:`Delete` for the specific model.
The action needs to be confirmed in a popup.

.. warning:: Model ID's will be reassigned after deleting a model. If you use model ID's in your robot program, make sure they're up to date after deleting models.

.. warning:: Model data will be lost after deletion confirmation and
   cannot be restored.

Select and visualize a model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A model can be selected by clicking on the respective tab. The open model can then be visualized in a specific
window inside the tab.

Enable or disable a model
^^^^^^^^^^^^^^^^^^^^^^^^^

A model is enabled by default, and can be disabled through the toggle switch at the left of the respective tab. If a model is disabled, it will be ignored in subsequent detection runs. Disabling models is a quick and useful way to check the effect of different combinations of models, or to test distinct models in isolation (by disabling all others).

.. _pick-point-teach:

.. _matching-tolerance:

Matching tolerance
^^^^^^^^^^^^^^^^^^

If the distance between a detected scene point and a point of your model
is below this position tolerance value, then this scene point will
confirm the model point. This parameter has a big impact on the scoring
of the :ref:`minimum-matching-score`.

The following guide will help you find a good value for this parameter, :ref:`how-to-matching-parameters`.

.. image:: /assets/images/documentation/Teach-matching-tolerance.png

.. _minimum-matching-score:

Minimum matching score
^^^^^^^^^^^^^^^^^^^^^^

Minimum percentage of model points that need to be confirmed by scene
points, for the detected object to be considered valid.

.. note:: For CAD models, only the points that could be visible from the camera
          are used in the computation of the matching score.

The following guide will help you find a good value for this parameter, :ref:`how-to-matching-parameters`.

Optimize detections
~~~~~~~~~~~~~~~~~~~

.. _teach-flat-objects:

Flat objects
^^^^^^^^^^^^

Detect objects based on their edges.
This feature is especially useful for flat objects, like sheet metal plates.
When enabled, an additional input to specify the object thickness is needed.

.. _image-fusion:

Image fusion and scene downsampling resolution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Image fusion (applicable for the M and L cameras only) and scene downsampling resolution are explained in :ref:`Optimize-detections`.

Detection speed
^^^^^^^^^^^^^^^

With this parameter, you can specify how hard Pickit Teach tries to
find multiple matches. Slower detection speeds are likely to produce
more matches. There are three available options:

-  **Fast** Recommended for simple scenes with a single or few objects.
-  **Normal** This is the default choice and represents a good
   compromise between a number of matches and detection speed.
-  **Slow** Recommended for scenes with many parts, potentially
   overlapping and in clutter.

**Example:** Two-step bin picking.

#. Pick an individual part from a bin using **Normal** or
   **Slow** detection speed and place it on a flat surface.
#. Perform an orientation check for re-grasping using
   **Fast** detection speed, as the part is isolated. Grasp and place in
   final location.
