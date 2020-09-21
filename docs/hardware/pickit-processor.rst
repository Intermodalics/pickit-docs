Pickit processor
================

The Pickit processor is a rack mount computer on which the Pickit
software is installed. It is responsible for doing all calculations to
detect your objects in a 3D point cloud and send the coordinates to the
robot for picking.

Read \ `this
article <https://support.pickit3d.com/article/74-setting-up-your-pick-it-system>`__
to learn how to set up the processor in your picking application.

Technical specifications
------------------------

The technical specifications in this section apply to both processor
versions 1.0 and 2.0 unless mentioned otherwise.

-  Processor: 6 cores (12 threads) at 3.7 Ghz
-  19-inch server: rack compatible (2U)
-  Temperature: -20°C to 70°C
-  Vibrations: Operating, 5 Grms, 5-500 Hz, 3 axes
-  IP rating: IP20
-  Humidity: ̃95% @ 40°C (non-condensing)
-  Input Voltage Range: 100 - 240V
-  Input Current: 50A @115Vac; 100A @230Vac
-  Input Frequency: 47 - 63Hz

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
-  IP rating: IP20
-  Humidity: ~95% @ 40°C (non-condensing)
-  Input Voltage Range: 100 - 240V
-  Input Current: 50A @115Vac; 100A @230Vac
-  Input Frequency: 47 - 63Hz
