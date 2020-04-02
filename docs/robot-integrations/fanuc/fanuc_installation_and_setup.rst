.. _fanuc_installation_and_setup:

Fanuc installation and setup
============================

This setup manual helps you setup Pickit with a **Fanuc robot**. The
setup of **Pickit** with a **Fanuc robot** consists of **4 steps**:

.. contents::
    :backlinks: top
    :local:
    :depth: 1

Check controller and software compatibility
-------------------------------------------

Pickit is compatible with controllers as of version **R-30iA** (i.e. R-30iA - V7.X , R-30iB - V8.X and R-30iB plus - V9.X) and the
software module **User Socket Msg** for socket communication is required (the product number for this module is **A05B-2600-R648**).

To verify if that software module is installed open the Status version
ID page by opening :guilabel:`MENU` > :guilabel:`STATUS` > :guilabel:`Version ID` and then click the :guilabel:`ORDER FI` button.

.. image:: /assets/images/robot-integrations/fanuc/fanuc-1.png
    :width: 550

Here you can check now if the module is listed as shown below. Note that
also the software version (V8.30P in the above example) can be verified
here.

.. image:: /assets/images/robot-integrations/fanuc/fanuc-2.png
    :width: 550

Alternatively, a backup of the controller can be made and the
information on the installed software can be found in the following
file: ``~/backup/All Of Above/orderfil.dat``.

To get you started as quickly as possible, Pickit provides:

-  All ASCII files for both the low-level communication as well as an
   example program.  
-  Binaries generated from these ASCII files for software version V7.70, V8.30 and V9.10.
   In case of using an older software version, you might have to
   recompile the ASCII files first.

.. warning:: Note that for the **R-J3iB**, the program names have to be shortened to at maximum 8 characters.

Setup the network connection
----------------------------

Setting up network connection for a Fanuc robot consists of 3 steps:

.. contents::
    :backlinks: top
    :local:
    :depth: 1

Hardware connection
~~~~~~~~~~~~~~~~~~~

The Pickit processor has to be connected to the Fanuc controller using
an Ethernet cable. This Ethernet cable should be plugged in:

 - The **ROBOT** port of the **Pickit processor**; 
 - **Port 1** or **Port 2** of the **Fanuc controller**.

The location of port 1 on the Fanuc is shown for different controller
types in the images below.

.. image:: /assets/images/robot-integrations/fanuc/fanuc-3.png
    :width: 550

.. image:: /assets/images/robot-integrations/fanuc/fanuc-4.png
    :width: 550

The Ethernet cable must be fastened by a cable clamp to prevent tension
being applied to the RJ-45 connector, in case the Ethernet cable is
pulled directly. This clamp is also used to ground the cable shield. 

IP configuration
~~~~~~~~~~~~~~~~

To allow communication between Pickit and the Fanuc controller both
must have an IP address in the same subnet.

By default, the Pickit ROBOT connection (the Ethernet port on the
Pickit processor labeled ROBOT) is configured to have the following
static IP address: **169.254.5.180** with a subnet mask of
**255.255.0.0**.

If this setting is kept, the following has to be done at the Fanuc
controller via  :guilabel:`MENU` > :guilabel:`SETUP` :guilabel:`Host Comm`: 

 - To obtain a static IP, **DHCP** has to be **disabled** on the controller.
 - A **static IP should be set** to e.g. **169.254.5.182** which is an IP in the same subnet as the Pickit IP.

.. image:: /assets/images/robot-integrations/fanuc/fanuc-5.png
    :width: 550

And select the **TCP/IP protocol**:

.. image:: /assets/images/robot-integrations/fanuc/fanuc-6.png
    :width: 550

Next, you have to take the following steps: 

 - **Disable DHCP** by pressing :guilabel:`DHCP`.
 - **Set the correct IP address** and subnet mask for **Port 1** or **Port 2**.
 - **Activate** these new settings via :guilabel:`NEXT` > :guilabel:`INIT`.

To verify now if a network connection can be made between Pickit and
the robot controller, you can create a new host name ‘pickit’ and give
it the Pickit ROBOT connection IP address. After pressing the :guilabel:`PING`
button, you should see the following message printed:

``Ping 169.254.5.180 succeeded``

Socket configuration
~~~~~~~~~~~~~~~~~~~~

Pickit works through socket communication. To work properly Pickit has
to act as the **server** for the socket communication. Hence, the robot
controller has to be configured to be **client**.

To do so, select :guilabel:`Clients` after pressing :guilabel:`SHOW` in the same SETUP protocols menu used above.

.. image:: /assets/images/robot-integrations/fanuc/fanuc-7.png
    :width: 550

Next, select :guilabel:`DETAIL` to configure the client C1 as follows:

.. image:: /assets/images/robot-integrations/fanuc/fanuc-8.png
    :width: 550

To set the Startup State to **START** you have to use the :guilabel:`[[CHOICE]]` button.

To verify if the configuration of the socket is done correctly, you have to reboot the controller and go again to :guilabel:`MENU` > :guilabel:`SETUP` > :guilabel:`Host comm` and then pressing :guilabel:`SHOW` and :guilabel:`CLIENTS`. You should see the following:

.. image:: /assets/images/robot-integrations/fanuc/fanuc-9.png
    :width: 550

Load the program files
----------------------

Loading the program files for a Fanuc robot consists of:

.. contents::
    :backlinks: top
    :local:
    :depth: 1

Additionally we provide some extra insights on registers used by the Karel program.

Download the right files
~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`Download the Pickit Fanuc files <downloads_fanuc>`

The .zip folder contains the following ASCII files:

- ``pick_it_communication15_C.kl`` is a Karel program that cares of the low level communication. This files should not be adapted.

- ``PICKIT_SIMPLE_PICKING.LS`` is a Teach Pendant program that shows a simple pick application for FANUC using Pickit.
  More infomation about this example program can be found in the following article, :ref:`fanuc-example-picking-program`.

- For calibration we provide two Teach Pendant programs;

  - ``PICKIT_MP_CALIBRATE.LS`` for :ref:`multi-poses-calibration`, this program is explained in full in the following article, :ref:`fanuc-calibration-program`.

  - ``PI_CALIBRATE.LS`` for :ref:`single-pose-calibration`.

- The other ``PI_**.LS`` files define short Teach Pendant programs that abstract some of the Pickit logic into more user readable functions. They can also serve as macros that can be called manually.

.. tip:: In case of using Fanuc software version V7.X, V8.X and V9.X , you can directly use the binaries available in the downloaded folder. In the other case, you first have to compile the above files into binaries. 

.. Warning:: Modifying the ``pick_it_communication15_C.kl`` file should only be considered after talking to a Pickit support engineer.

Upload the files to the robot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Uploading the files can be done using an FTP server or by manually loading them on the robot using a USB stick mounted to the Teach Pendant. For the latter, you have to go to :guilabel:`MENU` > :guilabel:`FILE` > :guilabel:`UTIL` > :guilabel:`Set Device` > :guilabel:`Select your device`.

.. image:: /assets/images/robot-integrations/fanuc/fanuc-10.png
    :width: 550

Registers used by the Karel program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Karel program ``pick_it_communication15_C.kl``, which takes care of the low-level communication between the controller and Pickit, uses the following registers to pass on data from the low-level communication to a Teach Pendant application program:

- Data communicated from Pickit via the Karel program to the Teach Pendant application program:

  -  Pose Registers: **PR[51]** - **PR[53]**
  -  Registers: **R[141]** - **R[159]**

More information about what all registers are used for can be found in the following article, :ref:`fanuc_pickit_registers`.

.. tip:: If these registers are already used on your robot. Please contact us at
  `support@pickit3d.com <mailto:mailto:support@pickit3d.com>`__ and we will assist you in finding a solution.

.. tip:: To make the Karel programs visible on the Teach Pendant, you have to set the ``KAREL_ENB`` value to 1 via :guilabel:`MENU` > :guilabel:`NEXT` > :guilabel:`SYSTEM` > :guilabel:`SYSVARS`.

Start and verify communication
------------------------------

Starting and verifying communication for a Fanuc robot consists of 2 steps:

.. contents::
    :backlinks: top
    :local:
    :depth: 1

Start communication
~~~~~~~~~~~~~~~~~~~

To start the communication manually, on the robot you have to run ``PI_OPEN_COMMUNICATION`` manually.

Verify communication
~~~~~~~~~~~~~~~~~~~~

In case the communication was started successfully, you can see the
following on the robot Teach Pendant:

**C1_CONNECTED** is **shown** in the top status barVerify on the
Pickit interface

.. image:: /assets/images/robot-integrations/fanuc/fanuc-13.png
    :width: 550

You can verify the connection from within the Pickit web interface by checking if there is a checkmark next to the robot status label in the top bar.