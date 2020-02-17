.. _how-to-multiple-thread:

How to make a robot program with multiple threads
=================================================

When programming a robot with Pickit, a separate thread can be devoted to purely communicate with the Pickit system.
The benefits of using a separate thread to communicate with the Pickit system are the following:

-  Robot program becomes cleaner, as all Pickit commands are in a separate thread.
-  If the Pickit camera is fixed to an external structure, multiple detection retries can be triggered while the robot is busy, for instance dropping off a part.
   This saves cycle time when Pickit needs more than one attempt to find a valid detection.

In this article, an example program with multiple threads is shown and elaborated.
The example program is for Universal Robots, similar logic can be implemented for other robot brands.

Example program Universal Robots
--------------------------------

The logic behind this example program is similar as for the :ref:`universal-robots-urcap-example-v1`.
Pickit looks for a part, when a part is found the robot picks it and, while dropping it off, Pickit looks again for a new part.

In this robot program two threads are run simultaneously by the robot.
One thread controls all robot movements and the other thread controls all Pickit commands.
A variable **detecting** is introduced to synchronize both threads.

When the variable **detecting** is **True**, the Pickit system starts triggering detections.
The robot can continue to perform actions, but it should not block the field of view of the camera.
After a part is successfully detected the variable **detecting** is set to **False**.
Now the robot is allowed to enter field of view of the camera and pick the part.
After picking the part, once the robot gets out of the field of view of the camera, the **detecting** variable is again set to **True**, repeating the cycle.

.. image:: /assets/images/faq/ur-multiple-thread.png

This example program can be downloaded
`here <https://drive.google.com/uc?export=download&id=1nHyHMabCKk3wPl5eXQY4l1y9muLUUOQi>`__.