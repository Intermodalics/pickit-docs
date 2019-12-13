.. _reference-frame:

The Pickit reference frame
--------------------------

The Pickit **reference frame** is a coordinate system used throughout the Pickit experience:

- **Setup:** The reference frame is created when :ref:`building the Region of Interest (ROI) box <build-roi-box>`. The ROI box is positioned with respect to it.
- **Detecion:** detected object positions displayed in the :ref:`web interface <detection-grid>` are reported with respect to the reference frame.
- **Picking:** The :ref:`pick strategy <pick-strategy>` specifies the preferred orientation of pick points with respect to the reference frame.

The Pickit reference frame is represented using dashed axes, as shown in the image below, where it appears next to the ROI.

.. image:: /assets/images/Documentation/setup/reference_frame.png
    :scale: 80%
    :align: center