.. _robot-camera-calibration-yumi:


Calibration with an ABB Yumi
============================

When using Pickit with the YuMi robot, the camera should be **fixed to
an independent structure**. A robot-mounted camera configuration is not
possible due to YuMi payload limitations. Although YuMi is a robot with
two-arms, robot camera calibration only needs to be performed **for one
arm**. Just be mindful that your calibration program uses a tool frame
**attached to the arm holding the calibration plate**. 

**YuMi does not have a standard robot flange**, as most traditional
robots do for mounting equipment. Therefore only
:ref:`multi poses calibration with a fixed camera <multi-poses-calibration>` can
be used.

.. attention::
  The YuMi robot has a limited workspace for moving the calibration plate
  around. Therefore, **a smaller L-shaped calibration plate needs to be
  used**.

.. image:: /assets/images/documentation/Calibration-plate-yumi.jpg

Because it is very important that **this plate cannot move with
respect to the gripper**, during calibration you should attach any
piece to the plate that can be grasped firmly by the fingers of your
YuMi gripper.

.. note::
  You are free to make holes in the calibration plate as long as they are
  not touching the three QR markers.

If this is done, you can perform a :ref:`multi-poses-calibration`
like with any other robot.

Example of attaching a grasping part to the L-shaped plate

.. image:: /assets/images/documentation/Calibration-plate-yumi-grasping-part.jpg

.. image:: /assets/images/documentation/Calibration-plate-yumi-assembly.jpg