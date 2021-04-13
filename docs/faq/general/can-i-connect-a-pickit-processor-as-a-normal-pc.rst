Can I connect a Pickit processor as a normal PC?
=================================================

It's **not possible** to access the Pickit processor as a normal PC, so you
cannot plug an external screen and keyboard directly.
The Pickit processor can only be accessed by an external computer over a network
using the Pickit :ref:`web interface <web-interface>`.
Refer to :ref:`this article <connect-computer>` for details on how to connect an
external computer.

An external computer is only needed for setup/configuration and optional
monitoring of Pickit. Once this has been done, the external computer can be
disconnected.

.. image:: /assets/images/first-steps/connecting-instructions.png
  :scale: 70%
  :align: center

If you access the Pickit system via LAN you may have to configure your firewall. Pickit requires that the following ports are reachable:

- **Web interface**: 80, 8080, 8083, 8182, 9999
- **Robot socket interface**: 5001 or 30001
- **Pickit remote access**: 22 (only required for online remote support)
