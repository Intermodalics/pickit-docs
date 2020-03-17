 .. _detecting-an-empty-roi:

Detecting an empty ROI box
==========================

.. contents::
  :backlinks: top
  :local:
  :depth: 1

Motivation
~~~~~~~~~~

In some applications, it's relevant to identify when the Region of Interest
(ROI) is empty and take appropriate action.
For example, triggering the refill of an empty bin or buffer table, or
instructing the robot to move one layer down in a depalletizing application.

Consider the case where we're interested in picking boxes from a bin,
as shown below:

.. image:: /assets/images/documentation/Roi-non-empty.png
   :scale: 60 %
   :align: center

Initially, there are many pickable boxes, and the robot proceeds to pick them
one by one. At some point there will be no more boxes to pick. There are
two scenarios that can lead to this state, which Pickit can differentiate:

1. **The ROI is empty**, all boxes have been picked and nothing remains
   in the ROI (below left).

2. **The ROI is not empty**, yet there are no pickable objects.
   This can happen when Pickit detects objects but:

     - Objects are **not pickable**, for instance due to a collision between the
       robot tool and the bin at the pick pose (below right, top blue box).

     - Objects are detected, but **not reliably enough**, for instance due to
       not being visible enough and having a too low matching score (below right,
       bottom yellow box).

.. image:: /assets/images/documentation/Roi-empty.png
   :align: center

Defining an empty ROI
~~~~~~~~~~~~~~~~~~~~~

The ROI box is considered to be empty when it contains less than a certain
number of points. This value is set in the **Setup** page, under
**Define empty ROI box**.

.. image:: /assets/images/documentation/Roi-define-empty.png
   :align: center

The threshold can be manually set, or can be taught by pointing the camera to an
empty ROI (where all objects have been removed) and pressing
:guilabel:`Teach from scene`.
This will perform a camera capture and set the empty ROI threshold based on the
number of points contained in the ROI. The value should probably be low, but
not necessarily zero. For example, plastic bags covering the inner walls of a
bin are hard to fully filter out of the ROI.

.. note::
  The value taught with :guilabel:`Teach from scene` is a lower bound
  and can be manually increased, if desired.
  It should however not exceed the number of points captured when a single
  object is placed inside the box with its smallest side facing the camera.
  Otherwise the object will not be detected.

Confirming an empty ROI
~~~~~~~~~~~~~~~~~~~~~~~

The Pickit web interface indicates in the detection summary when the ROI is
considered to be empty.

.. image:: /assets/images/documentation/Roi-empty-summary.png
   :align: center

When object detection results in no matches, the robot program can confirm
whether it was due to an empty ROI and take appropriate action.
Refer to the documentation of the Pickit robot integrations to learn the exact
commands for your robot brand (:ref:`UR example <helper-function-empty-roi>`),
and to this :ref:`example application <example-empty-roi>`.

Recovery behaviors
~~~~~~~~~~~~~~~~~~

When the ROI is not empty, yet no objects are detected, there are a number of
behaviors that a robot can implement to make the remaining objects detectable.
The following are a few examples:

- If the camera is robot-mounted, the robot can run detections from **different
  viewpoints** that might have better visibility of the remaining parts.

- **Shuffle the ROI contents** to make unreachable or occluded objects pickable.
  For instance, switch to blob detection to identify where ROI contents are,
  and instead of picking them, attempt to knock them down or move them around.

- Signal an alarm and request **human intervention**.
