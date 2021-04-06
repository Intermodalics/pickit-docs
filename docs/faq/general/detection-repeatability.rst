Detection repeatability
=======================

Detection repeatability directly influences the picking accuracy. This article describes what it is and how to measure it.

What is detection repeatability
-------------------------------

Due to measurement noise of the camera, detecting twice the same object does not lead to the exact same pick pose.
Detection repeatability measures the variability of the object position across multiple detections.
More precisely, we define the detection repeatability as the range of variation (in mm) of the detection pose of a fixed object.
We typically report the average and maximum variation of the detected pick pose.

It gives a lower bound on the expected picking accuracy.

.. image:: /assets/images/faq/picking-accuracy/detection_repeatability.gif
   :scale: 50%

.. note::
  The detection repeatability is application specific.
  It varies depending on the detected object, the camera and its distance, and detection settings (product file).
  Therefore, it is important to measure the repeatability in conditions as close as possible to your actual application. 

How to measure the detection repeatability of an application
------------------------------------------------------------

To measure the detection repeatability of a given application, the simplest is to detect a fixed part multiple times and collect the detection poses.
To ease the repeatability calculation, Pickit provides a spreadsheet that can easily be duplicated.

You can proceed as follows:

1. Use the detection repeatability calculation spreadsheet of the format of your choice

  a. `Google spreadsheet <https://docs.google.com/spreadsheets/d/1pEzJdVtE91euWIq2SGoJfW8mozWIuQlI-Fnte4bRpjk/template/preview>`__ by clicking `Use template`.

  b. `Microsoft Excel spreadsheet <https://drive.google.com/uc?export=download&id=1Y8XPH6lqchk68LS5fKvegFY5toTCPLFB>`__ by downloading the sheet.

2. Set up a repeatitive detection that always detects the same pick point of the same object (see tip below).

3. Detect the part and copy the object position (from the :ref:`objects table <detection-grid>`) in your detection repeatability calculation spreadsheet.

4. Repeat steps 3 until the spreadsheet is filled.

5. The spreadsheet will show the average and maximum repeatability error. 

.. tip::
  A repeatitive detection should always detect the same pick point of the same object as first result in the :ref:`objects table <detection-grid>`.
  To get a repeatitive detection it is recommended to adapt the product file as follows: 
  
  1. Set an object higher than the others and use highest object :ref:`ordering strategy<object-ordering>`.
  
  2. Enable only one pick point.

  3. For symmetrical objects, make sure that the pick point is exactly in the center of symmetry.

  4. If a :ref:`symmetry axis<pick-point-symmetry-axis>` is explicitly specified, remove it.

  5. Disable any :ref:`tool flexibility<flexible-pick-orientation>`.