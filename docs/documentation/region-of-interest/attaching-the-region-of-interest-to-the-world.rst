Attaching the Region of Interest to the world
---------------------------------------------

Now that you know how to define and modify a ROI box, you need to decide
where it is attached to. The ROI box can be attached to either
the **camera** or the **robot base**. This distinction is meaningful
for robot-mounted camera scenarios:

Camera
~~~~~~

A ROI box attached to the **camera** moves relative to the robot base as
the robot end-effector (and camera) move.To define the ROI box,
a running connection between Pickit and the robot is not required.

.. image:: /assets/images/Documentation/Roi-attached-to-camera.png

Robot base
~~~~~~~~~~

| A ROI box attached to the **robot base** remains stationary relative
  to the robot base as the robot end-effector (and camera) move. 
| This is the recommended attachment for camera-on-robot scenarios. To
  define the ROI box, a running connection between Pickit and the robot
  is **required**.

Refer to the :ref:`Attach-the-roi-box-to-the-robot-base`
article for an example application.

.. image:: /assets/images/Documentation/Roi-attached-to-robot-base.png