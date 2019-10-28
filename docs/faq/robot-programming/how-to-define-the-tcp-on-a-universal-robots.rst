.. _defining-tcp-universal-robots:

How to define the tool center point (TCP) on a Universal Robots
===============================================================

When using a robot it is very important to define the tool center point (TCP) exactly in the way you are using it in your application.

The TCP is defined by the exact translational and rotational difference between the robot flange frame and the tip of the end effector (e.g. a two finger gripper, a vacuum cup, a welding tool, ...).

Example
-------

.. image:: /assets/images/faq/define-tcp-on-a-ur-step-1.png

In this example there is a translation of 220 mm along the Z-axis between the robot flange and the tip of the end effector and no translation along the X and Y axes because the end effector in exactly below the center of the robot flange. All rotations can be set to 0 because the end effector is round and does not have a clear direction.

On a Universal Robot the TCP needs to defined in the screen as shown below. Make sure to input the measured values of your own end effector.

.. image:: /assets/images/faq/define-tcp-on-a-ur-step-2.png

If robot camera calibration was performed succesfully and TCP was defined in the right way a pick result should look like the pick in the green frame. If the TCP was not set in the right way a pick could look like the pick in the red frame.

.. image:: /assets/images/faq/define-tcp-on-a-ur-step-3.png
