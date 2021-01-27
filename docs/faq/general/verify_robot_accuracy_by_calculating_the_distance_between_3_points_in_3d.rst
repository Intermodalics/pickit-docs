How to verify the robot accuracy by calculating the distance between 3 points in 3D
===================================================================================

This articles discribes an easy way to verify the accuracy of a robot.

The idea of this test is to compare real and known distances with the distances perceived by the robot.
For this you need an object that contains distinctive points at which the robot can precisely point, and the distances between the points need to be exactly known.
This could be corners of a table or corners of a sheet of paper.
The robot needs to be able to reach all relevant points.
This article uses 2 `A4 <https://en.wikipedia.org/wiki/Paper_size#/media/File:A_size_illustration2.svg>`__ sheets (equivalent to 1 \ `A3 <https://en.wikipedia.org/wiki/Paper_size#/media/File:A_size_illustration2.svg>`__ sheet)
to illustrate the procedure.

In case of two A4 sheets make sure you attach them accurately and firm to each other as seen in the illustration below.

.. image:: /assets/images/faq/verify-accuracy-paper.png

Lay this paper in such a way that the whole paper is in reach of your robot.

Now point your robot TCP exactly to point A, B and C and on every point write down the TCP coordinates given to you by the robot.
Jog the robot such that the TCP is touching those points. 

.. tip::
  Make sure that the TCP orientation is kept the same for all points. The easiest is to have the TCP oriented at 0 degrees around X, Y and Z. This makes sure that eventual TCP errors are not affecting this test.

Then calculate the distance between 3 corners by using  `this calculator <http://www.calculatorsoup.com/calculators/geometry-solids/distance-two-points.php>`__.

The deviation from the expect distance indicate the accuracy of your robot.

.. note::
  An industrial robot should typically have less than 1 mm error.

For this sheet of paper example, the distances should be close to:

-  A and B: 297 mm
-  B and C: 420 mm
-  A and C: 514.4 mm

**If this is not the case, there is something wrong with the accuracy of the robot.** In that case further refinement of the Pickit calibration will not lead to a beter accuracy.

If this is the case: Good news! There is no indication that there is something wrong with the accuracy of your robot. 
