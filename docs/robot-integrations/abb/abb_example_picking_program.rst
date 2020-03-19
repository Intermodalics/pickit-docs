.. _abb-example-program:

ABB example program
===================

This example program requires that Pickit is installed and set up with your robot.
For installation instructions, please refer to the :ref:`abb-installation-and-setup` article.

.. include:: ../../run_program_warning.rst

Example programs
----------------

By default no **main()** module is loaded.
One of the Pickit example programs can be loaded from **HOME** > **ABB_Pick-it** > **Pick-it** > **Application examples**.

.. note::
  These example programs only works with Pickit software version of 2.2 or greater.
  If you are using a software version prior 2.2, please contact us at `support@pickit3d.com <mailto:support@pickit3d.com>`__, and we will assist you in finding a solution. 

Below the **main()** part of the example program **Pickit_simple_pick_and_place** is showm.
More information about this example program can be found in :ref:`robot-independent-program-simple`.

::

    PROC main()
        IF NOT pickit_is_running() THEN
            ErrLog 4800, "Pick-it NOT in Robot Mode", "Pick-it is not in Robot Mode.", "In the Pick-it web interface, click on 'Enable Robot Mode',", "and restart the program to start picking.", " ";
            Stop;
        ENDIF
        before_start;
        TPWrite "Setting setup and product configuration...";
        pickit_configure desired_setup,desired_product;
        goto_detection;
        TPWrite "Looking for new object(s)";
        pickit_detection_with_retries(max_retries);
        WaitUntil pickit_get_results();
         WHILE TRUE DO
            IF not pickit_object_found() THEN
                ! There are no pickable objects, bail out.
                Break;
            ENDIF
            PickitPick:=pickit_get_pose();
            PrePick := RelTool(PickitPick,0,0,PrePick_Z_offset);
            PostPick := Offs(PickitPick,0,0,PostPick_Z_offset);
            IF pickit_is_pose_reachable(PickitPick, tool0) AND pickit_is_pose_reachable(PrePick,tool0) AND pickit_is_pose_reachable(PostPick,tool0) THEN
                ! Object is pickable!
                pick;
                goto_detection;
                pickit_detection_with_retries(max_retries);
                place;
                WaitUntil pickit_get_results();
            ELSE
                ! Object is unreachable, get the next detection, if any.
                pickit_next_object;
                WaitUntil pickit_get_results();
            ENDIF
            after_end;
         ENDWHILE
    ENDPROC


.. note::
  Also a similar robot program to :ref:`robot-independent-pick-and-place-complete` can be found in the **Applications example** folder.

Define the tool for picking
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a tool with the actual TCP values.
In this example by default **tool0** is used.

Set correct constant values
~~~~~~~~~~~~~~~~~~~~~~~~~~~

At the top of the program following constants needs to be filled in with the correct values: 

- **Desired_setup**: the desired Pickit setup id.
- **Desired_product**: the desired Picket product id.
- **Max_retries**: the maximum number of retries for Pickit.
- **PrePick_Z_offset**: the z-offset for **PrePick** relative to the tool frame.
- **PostPick_Z_offset**: the z-ffset for **PostPick** relative to the robot base.

Define fixed points
~~~~~~~~~~~~~~~~~~~

In this example program, 3 fixed points are used.
These points need to be defined depending on the application.

- **Detect**: Where to perform object detection from.
- **AbovePickArea**: A point roughly above the pick area from which the above two can be reached without collision.
- **DropOff**: Where to place objects.

Add grasping/releasing logic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In **before_start()**, **pick()** and **place()** the correct grasping and release logic should be added.

Execute the picking program
---------------------------

Now you can run the program.
Happy picking!