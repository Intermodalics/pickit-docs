.. _Saving-a-snapshot:

Saving a snapshot in Pickit
============================

A snapshot is a powerful support tool of Pickit.
In a snapshot, both the camera images and detection parameters of the last detection are stored.
This file can be downloaded and sent to anybody with a Pickit system.
This tool allows anybody to give you remote support without a direct connection to your system.

By saving and sending a Pickit snapshot to Pickit support, a Pickit support engineer will analyze your scenario and will give you feedback on your detection settings.

#. Press the :guilabel:`Detect` button under the Pickit viewer to make sure you capture the current scene.
   You have to do this every time you are saving a new snapshot, otherwise the new data is not captured and old data is being saved.
#. Press the yellow **Snapshot** button in the lower left of the Pickit viewer.

   .. image:: /assets/images/documentation/snapshot-button-21.png

#. Specify a name for the snapshot and click the :guilabel:`Save` button (the name is automatically prepended with the date and time).

   .. image:: /assets/images/documentation/save-snapshot-21.png

#. In the :ref:`snapshots page <Snapshots>`, check the snapshot(s) you want to share and click on :guilabel:`Send to Pickit support`.
   Fill in the short form with your contact details and a short message describing the issue.

   .. image:: /assets/images/documentation/send_snapshots_to_support.png

   Alternatively you can also download the snapshot(s) with the :guilabel:`Download` button, and email them to `support@pickit3d.com <mailto:mailto:support@pickit3d.com>`__

When sending a snapshot to Pickit Support it's always very helpful when you send multiple snapshots of different situations:

-  Scene almost empty
-  Scene with a few objects
-  Scene in a starting situation
-  The object you want to pick on its own (only when using the :ref:`Teach engine <Teach>`)

Note that you can also save snapshots via the :ref:`socket interface <socket-communication>` or :ref:`automatically on each detection <Automatically-save-snapshots>`.
