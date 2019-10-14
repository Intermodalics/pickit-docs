.. _pickit-processor:

Pickit processor
================

The Pickit processor is a rack mount computer on which the Pickit
software is installed. It is responsible for doing all calculations to
detect your objects in a 3D point cloud and send the coordinates to the
robot for picking.

Read \ :ref:`this article <installation>` to learn how to set up the processor
in your picking application.

Processor version
-----------------

There are currently two hardware versions of the Pickit processor: 1.0
and 2.0. Both versions look very similar from the outside, but when
taking a closer look, you'll notice that they are equipped with
different hardware components on the inside.

Since many technical specifications stay the same between processor
versions 1.0 and 2.0, the section below only differentiates between the
two processor versions if there is a difference.

What is the version of my Pickit processor?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two ways to look up the version of your Pickit processor:

#. By looking at the back of the processor, you can see if a GTX
   graphics card is installed. If this is the case, the Pickit
   processor version is 2.0, otherwise, it's 1.0.
#. By looking at the Pickit software version at the top left of the
   Pickit interface in your browser. If the software version specifies
   1.x, then your processor version is 1.0, otherwise, it's 2.0.

What is the difference between Pickit version 1.0 and 2.0?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These are the most important differences between Pickit versions 1.0
and 2.0:

-  From a **hardware** perspective, Pickit processor 2.0 has a GTX
   graphics card, more powerful CPU and power supply to work with
   the \ :ref:`Pickit M-HD camera <m-hd-camera>`.
   The Pickit processor 1.0 has no graphics card.
-  From a **software** perspective, Pickit processor 1.0 runs Pickit
   software versions 1.x. Pickit processor 2.0 runs Pickit software
   versions 2.x. Software version 2.x is the platform that will receive
   the new product updates, while software version 1.x will only receive
   bug fixes and security updates.

Technical specifications
------------------------

The technical specifications in this section apply to both processor
versions 1.0 and 2.0 unless mentioned otherwise.

-  Processor: 6 cores (12 threads) at 3.7 Ghz
-  19-inch server: rack compatible (2U)
-  Temperature: -20°C to 70°C
-  Vibrations: Operating, 5 Grms, 5-500 Hz, 3 axes
-  IP rating: IP54
-  Power supply: 9-32V DC 160W
-  Humidity: ̃95% @ 40°C (non-condensing)

Processor ports and power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /assets/images/hardware/processor.jpg

The front side of the Pickit processor contains a lid, which can be
opened by rotating the lock handle clockwise. A few ports (which are not
used by Pickit) and some buttons are located under the lid. In case of
a power failure, while the computer is on, it will restart automatically
when power is restored.

.. image:: /assets/images/hardware/processor-back.jpg

All labeled I/O ports and the power connector are placed on the back
side of the processor as shown above. In order to connect the Pickit
processor to a power supply, use the provided IEC cable (C13).

.. warning::
    In case the Pickit processor is positioned vertically and sideways, the air inlet shall not stay at the top. This may affect the ventilation process.

Power consumption specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pickit processor 1.0:

-  While turned off: 25 W
-  Booting: 100 W
-  Idle: 60 W
-  Heavy processing: 130 W

Pickit processor 2.0:

-  While turned off: 25 W
-  Booting: 115 W
-  Idle: 70 W
-  Heavy processing: 160 W

Environmental and operating conditions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Temperature: -20ºC to 70ºC
-  Vibrations: Operating, 5 Grms, 5-500 Hz, 3 axes
-  IP rating: IP54
-  Power supply: 9-32V DC 160W
-  Humidity: ~95% @ 40°C (non-condensing)