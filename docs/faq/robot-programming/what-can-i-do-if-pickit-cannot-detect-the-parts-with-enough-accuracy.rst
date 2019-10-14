What can I do if Pickit cannot detect the parts with enough accuracy?
=====================================================================

For these applications often a two-step approach is used.
The idea of this is to first pick a part and isolate it.
In the first step, the correct orientation or accuracy is not assumed to be important.
Once the part is isolated, it can be found and repicked with a higher accuracy. 

This second step can be done either by triggering a new detection with Pickit or by a mechanical solution.

New detection
-------------

The most general approach is to drop off the part with the robot in an isolated area and to trigger a new detection.
A good example of this is discussed in the following article: :ref:`example-random-boxes`.

Alternatively for some application the new detection can be done when the robot is still holding the object.
A good example of this is discussed in the following article: :ref:`example-case-washers`.

Mechanical solution
-------------------

The second step can also be done without triggering a new detection.
Often the part is dropped in an intermediate station with lots of compliance.
When dropping the part it will realign itself.
Now the part can be repicked with a higher accuracy.

A typical example of such an intermediate station is a gravitational slider, which is used in `this <https://www.pickit3d.com/videos/a-smart-3-step-application-with-pick-it>`__ application.