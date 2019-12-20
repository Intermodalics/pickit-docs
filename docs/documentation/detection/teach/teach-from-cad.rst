.. _teach-from-cad:


Teach model from CAD
-----------------------

Teaching an object model is the most important step when setting up
the Pickit Teach engine to detect your object. Make sure that your CAD
file matches the object you want to detect.

To teach a CAD model all you have to do is to upload a CAD model and specify its length unit.
To do so press :guilabel:`Teach from CAD`.

Teaching from CAD has the benefit that the full part geometry is contained in a single model.
For example, the socket model shown below correesponds to a single CAD upload.
In contrast, to teach this model :ref:`from camera <teach-from-camera>`, one would need two models, i.e. two camera captures, one for the top side and one for the bottom side.

.. image:: /assets/images/Documentation/detection/teach/teach-from-cad.png

.. note:: Pickit supports **stl**, **obj** and **ply** formats. Most CAD design editors can export CAD into such formats.
          However, if you do not have such CAD formats, free online converter are available on the internet.

.. note:: if you do not know the length unit of your CAD, the simplest is probably to try one
          (mm being the most common) and tigger a detection with it.
          You will directly see in the Object view if it is the correct lenght unit.
