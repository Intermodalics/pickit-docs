.. _teach:

Teach
=====

Pickit Teach is a detection engine that works in 2 steps:

1. **Teach a model**: Teach your object shape to Pickit by:

  * uploading a CAD file.
  * selecting a basic shape (cylinder)
  * showing an object to the camera

2. **Detect the object(s)**: Pickit will then look for similar shaped objects in the scene.

In the image below, first a socket CAD file was uploaded to Pickit (teaching), next similar shaped sockets are found in the bin (detection).

.. image:: /assets/images/documentation/detection/teach/detection.png

.. toctree::
    :maxdepth: 1

    how-to-use-pickit-teach
    explaining-the-teach-detection-parameters

.. tip::
  You can learn about the main ideas behind the Teach engine by watching this :ref:`video tutorial <video-tutorials-what-to-pick>`.