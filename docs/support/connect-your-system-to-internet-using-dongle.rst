.. _connect-your-system-to-internet-using-dongle:

Connecting to Pickit via USB dongle
-----------------------------------

.. warning::
  This section refers to a method to bring a Pickit system online that is not supported since April 2020.
  Pickit systems shipped before this date came with a USB 3G dongle, which is no longer active.
  Pickit systems shipped after this date don't come with a USB 3G dongle.

  If your system has a deactivated 3G dongle, you should disconnect it from the Pickit processor, otherwise :ref:`wired LAN connections <connect-your-system-to-internet>` won't work.

.. note:: Since this is a wireless device, it's important that it is
   positioned **outside a metal enclosure** (Faraday cage). In case your
   Pickit system is in such an enclosure, you may use an extension cable
   up to 2 m to install the remote service modem outside this enclosure.

   Depending on **3G reception on site**, a Pickit support
   engineer could view and manipulate the Pickit web interface, install
   product and or setup files and perform updates. If the mobile reception
   is bad, viewing and manipulating the interface could be impossible. On
   slow connections, software updates can take up to several hours.

The USB 3G dongle is meant for bringing a Pickit system online.
A Pickit SIM card is already inside so this works out of the box.
Pickit systems were shipped with two different types of USB 3G dongles,
use the images below as a reference to check which type of dongle came
with your Pickit system.

Type 1
~~~~~~

.. image:: /assets/images/support/3g-dongle-type-1.jpg

The USB dongle can be plugged into any available USB port of your
Pickit system. No configuration is required.

+------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Status LED       | Indication                                                                                                                      |
+==================+=================================================================================================================================+
| Solid red        | The modem is initializing.                                                                                                      |
+------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Blinking red     | Check if a SIM/USIM card is inserted. If it is, try to unplug and replug the modem.                                             |
+------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Blinking green   | The card has registered to the network but no Internet connection could be made.                                                |
|                  | Try reinserting the USB modem and restarting the Pickit processor. If that doesn’t help, contact a Pickit support engineer.     |
+------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Solid Green      | The network is available with a successful Internet connection. A Pickit support engineer can now access the system.            |
+------------------+---------------------------------------------------------------------------------------------------------------------------------+

Type 2
~~~~~~

.. image:: /assets/images/support/3g-dongle-type-2.jpg

The USB dongle can be plugged into any available USB port of your
Pickit system. No configuration is required.

+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Status LED                        | Indication                                                                                                                |
+===================================+===========================================================================================================================+
| Blinking green twice (every 3s)   | The USB dongle is powered on.                                                                                             |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Blinking green once (every 3s)    | The USB dongle is registering with a 2G network.                                                                          |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Blinking blue (every 3s)          | The USB dongle is registering with a 3G/3G+ network.                                                                      |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Solid Green                       | The network is available with a successful Internet connection to a 2G network.                                           |
|                                   | A Pickit support engineer can now access the system but the connection might be too slow to perform a software update.    |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Solid Blue                        | The network is available with a successful Internet connection to a 3G network.                                           |
|                                   | A Pickit support engineer can now access the system but the software update might take up to several hours.               |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Solid Cyan                        | The network is available with a successful Internet connection to a 3G+ network.                                          |
|                                   | A Pickit support engineer can now access the system to perform a software update.                                         |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
