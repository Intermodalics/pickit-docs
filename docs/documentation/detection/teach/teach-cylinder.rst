.. _teach-cylinder:

Teach cylinder model
--------------------

Teach with cylinder model is the recommended engine for applications with cylindrical objects of known dimensions.
Typical applications are pipes or billets to name a few.

.. note::
  For cylindrical objects of varying dimensions, the recommended engine is :ref:`Flex <Flex>`.

To teach a cylinder model all you have to do is to specify the cylinder diameter and length.
Pickit will then generate a cylinder model.

.. image:: /assets/images/documentation/detection/teach/cylinder_model.png
.. image:: /assets/images/documentation/detection/teach/billets_example.png
   :scale: 45 %

By using the cylinder model, you let Pickit optimize the detection and user experience for this specific shape.
For example, Pickit will automatically make pick points symmetric about the cylinder axis to facilitate picking.
A :ref:`dedicated wizard <cylinder-pick-points-wizard>` will also help you to easily define the pick point of the shape.
