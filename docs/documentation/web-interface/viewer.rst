.. _Viewer:

Viewer
------

The Pickit viewer is the main component of the Pickit web interface
for providing visual feedback on the camera view and detection results.
Textual and quantitative information from the detection results is
provided by the complementary :ref:`detection-grid` component.

The Pickit viewer consists of a number of 2D and 3D views arranged in
tabs:

.. contents::
    :backlinks: top
    :local:
    :depth: 1

The following overlays are shown in all views:

-  Top-left: Camera ID and indicator that a correct camera calibration
   was loaded.
-  Lower-left: :ref:`Snapshot <Saving-a-snapshot>`
   button
-  Top-right: reset viewpoint button (not available
   in 2D view) and change viewer size button.
-  Lower right: View settings for
   customizing a particular view.

.. image:: /assets/images/Documentation/viewer-21-objects.png

Also common to all views, a notification is displayed when no camera is
connected and no snapshot is loaded:

.. image:: /assets/images/Documentation/no-connected-camera-21.png

.. _2d-view:

2D view
~~~~~~~

Live 2D camera image stream when a camera is connected. It always
overlays on top of the image:

-  The Region of Interest box.
-  The Pickit Reference frame.

After each detection, object frames, picking order identifiers and
contour are also shown for a brief period of time.

.. image:: /assets/images/Documentation/viewer-21-2d.png

.. _3d-view:

3D view
~~~~~~~

Live 3D camera image stream when a camera is connected. It also renders:

-  The Region of Interest box.
-  The Pickit Reference, robot base and robot end-effector frames.
-  Optionally: The Pickit camera(s) and robot (Universal Robots only)
   3D models.

.. image:: /assets/images/Documentation/viewer-21-3d.png

.. _points-view:

Points view
~~~~~~~~~~~

Displays the 3D point cloud used in the last Pickit detection. Only
points contained in the ROI box are shown. It also renders the same
additional elements listed for the the 3D view.

.. image:: /assets/images/Documentation/viewer-21-points.png

.. _clusters-view:

Clusters view
~~~~~~~~~~~~~

Displays the 3D point clouds of all clusters found in the last Pickit
detection. Each cluster is shown in a different color. It also renders
the same additional elements listed for the the 3D view.

This view is only available for the Pickit :ref:`Flex <Flex>` and
:ref:`Pattern <Pattern>` detection engines.

.. image:: /assets/images/Documentation/viewer-21-clusters.png

.. _objects-view:

Objects view
~~~~~~~~~~~~

Displays the 3D point clouds of all objects found in the last Pickit
detection. Each object cloud is shown in a different color. 

For all engines, it overlays the pick point of each object with
the picking order identifiers.

For the Pickit :ref:`Flex <Flex>` and :ref:`Pattern <Pattern>`  engines, it
overlays a 2D or 3D model of the geometric shape (e.g. cylinder, rectangle).
For the :ref:`Teach <Teach>`  engine, it overlays the 3D model cloud.
They are colored according to the following criteria:

-  Green: Valid object
-  Red: Invalid object
-  Orange: Unpickable object, e.g. due to collisions between robot tool
   and bin or other objects. When this is the case, the ROI box and
   robot tool are also rendered in orange. 

The objects view also renders the same additional elements listed for
the the 3D view.

.. image:: /assets/images/Documentation/viewer-21-objects.png