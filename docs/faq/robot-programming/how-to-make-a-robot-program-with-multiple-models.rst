.. _how-to-multiple-models:

How to make a robot program with multiple models
================================================

When using the :ref:`Teach` detection engine, Pickit can look for multiple models at the same time.
When doing this often it's desired to do a different action with a robot depending on which model is found.
Typical actions that are model exclusive are:

-  Define how to grip the found model.
-  Define how to drop off the found model.

In this article two example programs with multiple models are shown. One for Universal robots and another for ABB.

Universal Robots
----------------

The variable **pickit_type** is available to use after using the Pickit
URCap **Find object(s)** command. This variable represents the detected model id.
In the example program this id is used to define both a different picking as dropping strategy.

.. image:: /assets/images/faq/simple-picking-mulitple-models-ur.png

This example program can be downloaded 
`here <https://drive.google.com/uc?export=download&id=1IpIrAboDHPQ14zruUoEY2_Gzz4oOkCh5>`__.

ABB
---

The variable **pickit_object.type** is available to use after using the combination of commands **pickit_look_for_object** and
**WaitUntil pickit_has_response()** command. This variable represents the detected model id.
In the example program this id is used to define a different picking and dropping strategy.

::

    PROC Example()
        CONST robtarget drop_off_pose_1:=[[0,0,0],[1,0,0,0],[0,0,0,0],[9e9,9e9,9e9,9e9,9e9,9e9]];
        CONST robtarget drop_off_pose_2:=[[0,0,0],[1,0,0,0],[0,0,0,0],[9e9,9e9,9e9,9e9,9e9,9e9]];
        CONST robtarget detect_pose:=[[0,0,0],[1,0,0,0],[0,0,0,0],[9e9,9e9,9e9,9e9,9e9,9e9]];
        VAR robtarget pick_pose:=[[0,0,0],[1,0,0,0],[0,0,0,0],[9e9,9e9,9e9,9e9,9e9,9e9]];
        VAR robtarget pick_pre_pose:=[[0,0,0],[1,0,0,0],[0,0,0,0],[9e9,9e9,9e9,9e9,9e9,9e9]];

        ! Fill in the correct setup file/product file/offsets.
        CONST num desired_setup:=2;
        CONST num desired_product:=2;
        CONST num pre_pick_Z_offset:=-100;
        CONST num pre_drop_Z_offset:=-100;

        IF NOT pickit_is_running() THEN
            ErrLog 4800, "Pickit NOT in Robot Mode", "Pickit is not in Robot Mode.", "In the Pickit web interface, click on 'Enable Robot Mode',", "and restart the program to start picking.", " ";
            Stop;
        ENDIF

        TPWrite "Setting setup and product configuration...";
        pickit_configure desired_setup,desired_product;

         WHILE TRUE DO
            IF pickit_object_found() THEN
                pick_pose:=pickit_get_pose();
                pick_pre_pose := RelTool(pick_pose,0,0,pre_pick_Z_offset);
                IF pickit_is_pose_reachable(pick_pose, tool0) AND pickit_is_pose_reachable(pick_pre_pose,tool0) THEN
                    IF pickit_object.type = 1 THEN
                        TPWrite "Moving to an object...";
                        MoveJ pick_pre_pose,v500,z0,tool0;
                        MoveL pick_pose,v500,fine,tool0;
                        ! Add object grasping logic for model 1 here.
                        MoveL pick_pre_pose,v500,z0,tool0;
                        TPWrite "Moving to the drop off position...";
                        MoveJ detect_pose,v500,z0,tool0;
                        TPWrite "Looking for new object(s)";
                        pickit_look_for_object;
                        MoveJ RelTool(drop_off_pose_1,0,0,pre_drop_Z_offset), v500,z0,tool0;
                        ! Define drop off position for product 1.
                        MoveL drop_off_pose_1,v500,fine,tool0;
                        ! Add object releasing logic here.
                        MoveL RelTool(drop_off_pose_1,0,0,pre_drop_Z_offset), v500,z0,tool0;
                        MoveJ detect_pose,v500,fine,tool0;
                        WaitUntil pickit_has_response();
                    ELSEIF pickit_object.type = 2 THEN
                        TPWrite "Moving to an object...";
                        MoveJ pick_pre_pose,v500,z0,tool0;
                        MoveL pick_pose,v500,fine,tool0;
                        ! Add object grasping logic for model 2 here.
                        MoveL pick_pre_pose,v500,z0,tool0;
                        TPWrite "Moving to the drop off position...";
                        MoveJ detect_pose,v500,z0,tool0;
                        TPWrite "Looking for new object(s)";
                        pickit_look_for_object;
                        MoveJ RelTool(drop_off_pose_2,0,0,pre_drop_Z_offset), v500,z0,tool0;
                        ! Define drop off position for product 2.
                        MoveL drop_off_pose_2,v500,fine,tool0;
                        ! Add object releasing logic here.
                        MoveL RelTool(drop_off_pose_2,0,0,pre_drop_Z_offset), v500,z0,tool0;
                        MoveJ detect_pose,v500,z0,tool0;
                        WaitUntil pickit_has_response();
                    ENDIF
                ELSE
                    pickit_next_object;
                    TPWrite "Asking for next object";
                    WaitUntil pickit_has_response();
                ENDIF
            ELSE
                ! Define detect position.
                MoveJ detect_pose,v500,z0,tool0;
                pickit_look_for_object;
                TPWrite "Looking for new object(s)";
                WaitUntil pickit_has_response();
            ENDIF

         ENDWHILE

         ! EXIT; ! stop program
    ENDPROC
