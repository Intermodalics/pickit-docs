.. _Saving-a-snapshot:

Saving a snapshot in Pickit
============================

A snapshot is a powerful support tool of Pickit. In a snapshot both the
camera images and detection parameters of the last detection are stored.
This file can be downloaded and sent to anybody with a Pickit system.
This tool allows anybody to give you remote support without a direct
connection to your system.

By saving and sending a Pickit snapshot to Pickit support. A Pickit
support engineer will analyze your scenario and will give you feedback
on your detection settings.

There are three ways you can save a snapshot: either you save it manually
from the web interface, you save it automatically with every detection
trigger, or you save it from a running robot program. The three options
are detailed in the following sections.

Saving a snapshot from the web interface
----------------------------------------

If the result of a detection is not what you expect, and you would like
to debug later, or have the Pickit support team have a look at it, you can
save a snapshot of that particular case.

#. Press the :guilabel:`Detect` button under the Pickit viewer to make sure
   you capture the current scene.
   You have to do this every time you are saving a new snapshot,
   otherwise, the new data is not captured and old data is being saved.
#. Press the yellow **Snapshot** button in the lower left of the Pickit
   viewer.

   .. image:: /assets/images/Documentation/snapshot-button-21.png

#. Specify a name for the snapshot and click the :guilabel:`Save` button. (The
   file is saved and the name is automatically appended with the date
   and time)

   .. image:: /assets/images/Documentation/save-snapshot-21.png

#. Download this file from the :ref:`snapshots page <Snapshots>`. Check the
   snapshot(s) that you want to download and press the :guilabel:`Download` button.
#. Email this file
   to `support@pickit3d.com <mailto:mailto:support@pickit3d.com>`__

When sending a snapshot to Pickit Support it's always very helpful when
you send multiple snapshots of different situations:

-  Scene almost empty
-  Scene with a few objects
-  Scene in a starting situation
-  The object you want to pick on its own (only when using the :ref:`Teach engine <Teach>`)

.. _Snapshot-automatically-save-snapshots:

Automatically saving a snapshot upon each detection
---------------------------------------------------

Suppose that you are trying out different detection settings, and would like
to have them registered, or simply would like to store all detection results.
In the :ref:`Settings` page, you can choose to :ref:`Automatically-save-snapshots`
upon each detection trigger from the web interface. Once the specified number of
snapshots to be automatically saved is reached, older snapshots are discarded.

.. note:: Snapshots are not automatically saved if the detections are triggered
          while a snapshot is loaded.

.. _Snapshot-save-snapshots-from-robot:

Saving a snapshot from a robot program
--------------------------------------

At a more advanced stage of your project, while running a robot program, you may notice
that Pickit is not always detecting as you expect. For example, you observe that Pickit
struggles to detect any objects. You would like to have a closer look at each problematic
case later, but you don't want to stop your application every time it occurs. If this is a
situation that you can "catch" from the robot program, you can have the robot requesting
Pickit to save a snapshot, by using the :ref:`socket interface <socket-communication>`
command **RC_PICKIT_SAVE_SCENE** (see the documentation of the robot integration of your
robot brand for the actual function name).
