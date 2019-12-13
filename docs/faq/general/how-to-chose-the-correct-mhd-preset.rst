.. _how-to-mhd-preset:

How to choose the correct HD camera preset
=========================================

The Pickit HD cameras are high-end cameras with many different options on how to capture a point cloud of the scene.
For instance, the camera can be optimized to better detect bright or dark parts.
When set to detect bright parts typically the captured point cloud is darker, to compensate for the brightness of the parts.
On the contrary when it is set to detect darker parts the point cloud becomes brighter.

This capture was taken with the **Light reflective plastic** setting.
Here you can clearly see that the bright parts of the plates are detected but the dark parts are not.

.. image:: /assets/images/faq/mhd-preset-lrp.png

This capture was taken with the **Dark non-reflective plastic** setting.
Here you can clearly see that the dark parts of the plates are detected but the bright parts are not.

.. image:: /assets/images/faq/mhd-preset-dnrp.png

Next to different settings to capture a point cloud the Pickit HD cameras also have the possibility to trigger multiple captures in a row.
Each capture uses a different setting and the combined image of multiple captures leads to a point cloud which can be better than a single capture.
Taking multiple captures typically results in a better point cloud but also increases point cloud capture time.

This capture was taken with the **Mixed-color plastic** setting.
Here you can see that both the bright and dark parts are detected.

.. image:: /assets/images/faq/mhd-preset-mcp.png

Pickit provides a few M-HD settings presets, which are suitable for capturing the following materials:

-  **Light reflective plastic** (1 capture).
-  **Light non-reflective plastic** (1 capture).
-  **Dark non-reflective plastic** (3 captures).
-  **Dark reflective plastic** (4 captures).
-  **Mixed-color plastic** (3 captures).
-  **Sandblasted metal** (2 captures).
-  **Polished metal** (3 captures).

To find the best setting for your application, it is recommended to try different presets and chose the one that gives the best results for your scene.
The result of a certain preset is best visualized in the :ref:`Points view <points-view>`.

.. hint:: Teaching the same model with different settings can help you choose the best setting, typically the preset that leads to the highest number of points in the model is the best preset for this part.
