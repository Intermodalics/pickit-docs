.. _kuka-krc4-example-picking-program:

KUKA example picking program
============================

This example program requires that Pickit is installed and set up with your robot.
For installation instructions, please refer to the :ref:`kuka-krc4-installation-and-setup` article.

.. include:: ../../run_program_warning.rst

Example program: PickitSimplePicking
------------------------------------

This example program can be found in **R1** > **Program** > **Pickit**.

.. note::
  This example program only works with Pickit software version of 2.2 or greater.
  If you are using a software version prior 2.2, please contact us at `support@pickit3d.com <mailto:support@pickit3d.com>`__, and we will assist you in finding a solution. 

::

     DEF  PickitSimplePicking ( )
        ;FOLD INI;%{PE}
        ;FOLD USER INI

        PTP HOME 
   
        IF NOT Pickit_is_running() THEN
            PickitMessages(#info, 1) ;Pickit not in ROBOT mode
            HALT
        ENDIF
   
        Pickit_configure(5,4)

        BAS(#TOOL,1) ; Tool for picking
        BAS(#BASE,0) ; Robot base

        PTP Detect
        Pickit_detect_with_retr(5)
        WAIT FOR Pickit_get_results() 

        LOOP
            IF Pickit_object_found() THEN
                ;Calculate pick points
                F_Pick=Pickit_get_pose()
                F_PrePick=F_Pick:{X 0.0,Y 0.0,Z -100.0,A 0.0,B 0.0,C 0.0}
                F_PostPick={X 0.0,Y 0.0,Z 100.0,A 0.0,B 0.0,C 0.0}:F_Pick
                
                ; Check if positions are reachable
                PickitAxistest=INVERSE(F_Pick,XAbovePickArea,Pickit_ErrStatCheckPos1)
                PickitAxistest=INVERSE(F_PrePick,XAbovePickArea,Pickit_ErrStatCheckPos2)
                PickitAxistest=INVERSE(F_PostPick,XAbovePickArea,Pickit_ErrStatCheckPos3)
                IF (Pickit_ErrStatCheckPos1==0) AND (Pickit_ErrStatCheckPos2==0) AND (Pickit_ErrStatCheckPos3==0) THEN
                    PTP AbovePickArea
                    LIN F_PrePick
                    LIN F_Pick
                    ;Add grasping logic
                    LIN F_PostPick
                    LIN AbovePickArea
                    PTP Detect
                    Pickit_detect_with_retr(5)
                    PTP Dropit
                    ;Add release logic           
                    WAIT FOR Pickit_get_results()
                ELSE
                    PickitMessages(#info,2) ;Object not reachable requesting next object..
                    Pickit_next_object()
                    WAIT FOR Pickit_get_results()
                ENDIF
            ELSE   
                IF Pickit_roi_empty() THEN
                    PickitMessages(#info, 3) ;ROI is empty
                    EXIT
                ELSE
                    PickitMessages(#info, 4) ;No objects found
                    Pickit_save_scene()
                    EXIT
                ENDIF
            ENDIF
        ENDLOOP   
     END

The idea of the program is the following:

- First, it is checked whether or not Pickit is in :ref:`Robot mode <web-interface-top-bar>`.
- If so, the robot moves to the ``detect`` pose and a detection is triggered, otherwise the robot program is halted.
- If an object is found, it is checked if the pick, pre-pick and post-pick points are reachable for the robot.
- If the object is reachable, the robot moves to the object to pick it.
  Afterwards, the robot moves to a fixed drop-off position, ``Dropit``.
  As soon as the robot is out of the field of view of the camera, a new Pickit detection is triggered, so that the detection is processed at the same time as the robot moves, optimizing cycle time.
- If the object is not reachable, the robot requests the next detected object.
- If the ROI is empty, the program stops.
- If no object is found, and the ROI is not empty, a :ref:`snapshot <Snapshots>` is saved on the Pickit system and the robot program stops.

.. note:: Depending on which Pickit software version you are running, the example program can look different, even though the functionality is the same.
  We recommend to use the example program shipped with your Kuka connect version

Define the tool for picking
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a tool with the actual TCP values.
In this example **#TOOL1** is used.

Set correct input arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The commands ``Pickit_configure`` and ``Pickit_detect_with_retr`` need input arguments.
See :ref:`kuka-pickit-communication-functions` for more information about these arguments.

Define fixed points
~~~~~~~~~~~~~~~~~~~

In this example program, 4 fixed points are used.
These points need to be defined depending on the application.

- **Home**: Where the robot will start the program.
- **Detect**: Where to perform object detection from.
- **AbovePickArea**: A point roughly above the pick area from which the above two can be reached without collision.
- **Dropit**: Where to place objects.

Add grasping/releasing logic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At the **F_Pick** and **Dropit** points, grasping and releasing logic needs to be added, respectively.

Execute the picking program
---------------------------

Now you can run the program.
Happy picking!