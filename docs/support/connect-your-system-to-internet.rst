.. _connect-your-system-to-internet:

Bring your Pickit system online
===============================

This article covers how to bring your Pickit system online for the exceptional
event that it requires remote service from a Pickit support engineer.
During normal operation, it's not required to bring your Pickit system online.

.. note::
   If you're interested in **upgrading your Pickit software version**, you don't need to bring your Pickit system online.
   Updates can be downloaded from any computer with Internet access, as described in the :ref:`Pickit system software upgrade <Pickit-system-software-upgrade>` article.

.. warning::
  **Legacy USB dongle connection.** Until April 2020, Pickit systems shipped with a :ref:`3G USB dongle  <connect-your-system-to-internet-using-dongle>` as an additional mechanism for bringing the system online.
  This connection method is no longer supported.

To bring your Pickit system online for remote service, you need a **wired Ethernet connection**, as shown below, to the left of the Pickit processor. 

.. image:: /assets/images/first-steps/connecting-instructions-full.png

Steps to connect via Ethernet
-----------------------------

#. **Plug in an Ethernet cable** (with Internet access) into the **LAN
   port** of the Pickit processor.

#. Navigate to the **Network settings**, by clicking on the Settings
   button at the top-right of the web interface.

   .. image:: /assets/images/support/settings-button-21.png

#. In the **Pickit port labeled 'LAN’** section, make sure that the network settings are correct.
   In particular, the **IP address** field represents Pickit's IP in your network (red arrow below).
   If the network configuration changed, don't forget to click the :guilabel:`Save` button.

   .. image:: /assets/images/support/network-settings-24.png
     :scale: 80%
     :align: center

#. **Check Internet connectivity** by clicking the :guilabel:`Check` button at the bottom of the network settings.
   If you see the following acknowledgement of success, your system is ready for remote service!

   .. image:: /assets/images/support/online-connection-ok.png
     :scale: 70%


Troubleshooting an unsuccessful connection
------------------------------------------

This section provides guidelines to troubleshoot if the connectivity check from step 4 above was not successful.
There are two scenarios that can take place, which are described below.
If connection problems persist after following these guidelines, please contact us at `support@pickit3d.com <mailto:mailto:support@pickit3d.com>`__, and we will assist you in finding a solution.

Not connected to the Internet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If there's no Internet connection, check that:

- The network settings for step 3 above are correct (DHCP vs static, IP address, subnet mask and gateway).
- The Ethernet cable is not physically damaged and that the plugs are well connected to their sockets.
- The cable is connected on one end to the LAN port of the Pickit processor.
- The cable is connected on the other end to a network socket with Internet connection.

Connected to the Internet but not to the Pickit server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pickit communicates with its server using OpenVPN via TCP port 443.
When it can't be reached, contact your system administrator, as it's usually the result of:

- The network configuration preventing Pickit from resolving the name of the OpenVPN server ``vpn.intermodalics.eu``.
- A software firewall filtering incoming connections on port 443.
  Many firewalls block incoming connections by default, unless configured otherwise.
- A perimeter firewall filtering incoming OpenVPN packets.
- A firewall's web filter filtering out VPN communication on port 443, as it doesn't look like normal web traffic.
- A NAT gateway not having a port forwarding rule for TCP 443 to the internal address of the Pickit machine.

.. toctree::
    :hidden:
    :maxdepth: 1
    :glob:

    connect-your-system-to-internet-using-dongle