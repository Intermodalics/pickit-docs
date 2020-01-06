.. _how-does-the-pickit-3d-camera-work:

How does the Pickit 3D camera work?
====================================

The Pickit 3D cameras use `structured light <https://en.wikipedia.org/wiki/Structured_light>`__ technology.
A known pattern is projected on the scene, and the deformations of the pattern as seen by the camera as it hits surfaces determines how far these surfaces are towards the camera.
This results in a 3D point cloud.

The image below illustrates the structured light principle.
The red triangle represents the projected pattern, while the green triangle represents where the sensor can detect it.
When there is an overlap between the two, 3D data in the form of a point cloud can be obtained, shown as a thick green line.
In this case, there is 3D data for the upper part of the circle and for the flat surface below it.

.. image:: /assets/images/faq/Pickit-camera-3d-data_big.png
   :align: center

All Pickit 3D cameras work according to this principle.
The M and L camera work with structured infrared light and the M-HD camera works with structured visible light.

What surface of the object gets detected by the camera?
-------------------------------------------------------

From the image above you can see that the camera can't obtain 3D data for the full circle.
Only the visible upper part is detected. Both the object shape and location (position and orientation) with respect to the camera determine which surfaces will be detected by the camera.
In this section, two different examples are discussed.

In the image below three circles are placed under the camera.
Here it is shown that the obtained 3D data depends on where objects are located with respect to the camera.
The detected surfaces are those that have a direct line of sight to both the structured light projector and the sensor (red and green triangles, respectively).

.. image:: /assets/images/faq/Pickit-camera-multiple-objects_big.png
   :align: center

An interesting situation arises when a rectangular shape gets placed directly beneath the camera, as in the image below.
In such a case, only the upper side of the rectangle is detected.
There is no 3D information for the standing sides as they are not visible to the camera.

.. image:: /assets/images/faq/Pickit-camera-box_big.png
   :align: center

What are the limits of the Pickit cameras?
-------------------------------------------

There are limits to what the Pickit cameras can detect.
In this section, three different scenarios where 3D data from an object cannot be extracted from the scene are explained.

The first scenario is a special case of the rectangle discussed in the previous section of this article.
Below, the effect of a thin standing edge is shown. The edge itself is rather thin so no 3D data can be obtained on top of it.
Also, 3D data on the flat surface around the edge is missing where there is only visibility to either the structured light projector (red triangle) or the sensor (green triangle), but not both: The region next to the left side of the edge is visible to the sensor but not to the projector.
Conversely, the region next to the right side of the edge is visible to the projector but not to the sensor.

.. image:: /assets/images/faq/Pickit-camera-standing-edge_big.png
   :align: center

The second scenario consists of a transparent object.
In the image below it can be seen that both the structured light and the sensor pass through the object.
So 3D data of the flat surface below the object is returned, but no information of the object itself is obtained.

.. image:: /assets/images/faq/Pickit-camera-transparent_big.png
   :align: center

A third scenario is when the object is reflective.
The structured light that falls on the object will not be reflected towards the camera but away from it.
This makes it impossible to obtain 3D information around the object, as shown in the image below.

.. image:: /assets/images/faq/Pickit-camera-reflective_big.png
   :align: center

The above scenarios exemplify edge cases.
Often parts are only partially reflective or semi-transparent.
When in doubt about a part, it is recommended to test it by placing it under the camera, trigger a detection and inspect the point cloud in the :ref:`Points view <points-view>`.
If not enough 3D data is captured, know that this can be further optimized.
For the Pickit M and L cameras, :ref:`image fusion <image-fusion>` leads to a more stable point cloud.
For the Pickit M-HD camera, a different camera preset can be used.
If still not enough 3D is obtained the parts are too reflective or transparent.
