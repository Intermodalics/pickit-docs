.. _abb-example-picking-program:

ABB example picking program
===========================

This example program requires that Pickit is installed and set up with your robot.
For installation instructions, please refer to the :ref:`abb-installation-and-setup` article.

Example programs
----------------

By default no **main()** module is loaded.
One of the Pickit example programs can be loaded from :guilabel:`HOME` > :guilabel:`ABB_Pick-it` > :guilabel:`Pick-it` > :guilabel:`Application examples`.

.. note::
  These example programs only works with Pickit software version of 2.2 or greater.
  If you are using a software version prior 2.2, please contact us at `support@pickit3d.com <mailto:support@pickit3d.com>`__, and we will assist you in finding a solution. 

Below the **main()** part of the example program **Pickit_simple_pick_and_place** is shown.
More information about this example program can be found in :ref:`robot-independent-program-simple`.

Also a similar robot program to :ref:`robot-independent-pick-and-place-complete` can be found in the **Applications example** folder.

::

    MODULE Pickit_simple_pick_and_place
        ! User input variables
        CONST num target_picks:=-1;
        CONST num desired_setup:=2;
        CONST num desired_product:=2;
        CONST num max_retries:=5;
        CONST num PrePick_Z_offset:=-100;
        CONST num PostPick_Z_offset:=100;    

        ! Fixed points that need to be taught
        CONST robtarget Detect:=[[0,0,0],[1,0,0,0],[0,0,0,0],[9e9,9e9,9e9,9e9,9e9,9e9]];
        CONST robtarget AbovePickArea:=[[0,0,0],[1,0,0,0],[0,0,0,0],[9e9,9e9,9e9,9e9,9e9,9e9]];
        CONST robtarget DropOff:=[[0,0,0],[1,0,0,0],[0,0,0,0],[9e9,9e9,9e9,9e9,9e9,9e9]];
        ! Variable points computed from Pickit detection results
        VAR robtarget PickitPick:=[[0,0,0],[1,0,0,0],[0,0,0,0],[9e9,9e9,9e9,9e9,9e9,9e9]];
        VAR robtarget PrePick:=[[0,0,0],[1,0,0,0],[0,0,0,0],[9e9,9e9,9e9,9e9,9e9,9e9]];
        VAR robtarget PostPick:=[[0,0,0],[1,0,0,0],[0,0,0,0],[9e9,9e9,9e9,9e9,9e9,9e9]];
        
        PROC main()
            IF NOT pickit_is_running() THEN
                ErrLog 4800, "Pick-it NOT in Robot Mode", "Pick-it is not in Robot Mode.", 
                "In the Pick-it web interface, click on 'Enable Robot Mode',", 
                "and restart the program to start picking.", " ";
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
                IF pickit_is_pose_reachable(PickitPick, tool0) 
                AND pickit_is_pose_reachable(PrePick,tool0) 
                AND pickit_is_pose_reachable(PostPick,tool0) THEN
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
        
        PROC before_start()
            ! Move to home position
            ! Open gripper
        ENDPROC
        
        PROC goto_detection()
            MoveJ Detect,v500,z0,tool0;
        ENDPROC
        
        PROC pick()
            TPWrite "Moving to an object...";
            MoveJ AbovePickArea,v500,z0,tool0;
            MoveL PrePick,v500,z0,tool0;
            MoveL PickitPick,v500,fine,tool0;
            ! Add object grasping logic here.
            MoveL PostPick,v500,z0,tool0;
            MoveJ AbovePickArea,v500,z0,tool0;
        ENDPROC
        
        PROC place()
            MoveJ DropOff,v500,fine,tool0;
            ! Add object releasing logic here.
        ENDPROC
        
        PROC after_end()
            IF NOT pickit_object_found() THEN
                IF Pickit_roi_empty() THEN
                    TPWrite "The ROI is empty.";
                ELSEIF Pickit_no_image_captured() THEN
                    TPWrite "Failed to capture a camera image.";
                ELSEIF NOT(pickit_is_pose_reachable(PickitPick, tool0) 
                AND pickit_is_pose_reachable(PrePick,tool0) 
                AND pickit_is_pose_reachable(PostPick,tool0)) THEN
                    TPWrite "All detections are unreachable.";
                ELSE
                    TPWrite "The ROI is not emptym but the requested object was not found.";
                    Pickit_save_snapshot;
                ENDIF
            ENDIF
        ENDPROC
    ENDMODULE

Define the tool for picking
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a tool with the actual TCP values.
In this example, **tool0** is used.

Set correct constant values
~~~~~~~~~~~~~~~~~~~~~~~~~~~

At the top of the program, the following constants need to be filled in with the correct values: 

- **Desired_setup**: the desired Pickit setup id.
- **Desired_product**: the desired Picket product id.
- **Max_retries**: the maximum number of retries for Pickit.
- **PrePick_Z_offset**: the z-offset for **PrePick** relative to the tool frame.
- **PostPick_Z_offset**: the z-offset for **PostPick** relative to the robot base.

Define fixed points
~~~~~~~~~~~~~~~~~~~

In this example program, three fixed points are used.
These points need to be defined depending on the application.

- **Detect**: Where to perform object detection from.
- **AbovePickArea**: A point roughly above the pick area from which the above two can be reached without collision.
- **DropOff**: Where to place objects.

.. image:: /assets/images/robot-integrations/robot-independent/waypoints.png

Add grasping/releasing logic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In **before_start()**, **pick()** and **place()** the correct grasping and release logic should be added.

Execute the picking program
---------------------------

.. include:: ../run_program_warning.rst

Now you can run the program.
Happy picking!