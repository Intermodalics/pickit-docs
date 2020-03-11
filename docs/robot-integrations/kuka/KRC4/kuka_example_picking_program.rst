.. _kuka-example-picking-program:

KUKA example picking program
============================

This example program requires that Pickit is installed and set up with your robot.
For installation instructions, please refer to the :ref:`kuka_installation_and_setup` article.

Make sure that :ref:`robot-camera-calibration` is done.
This can be done by running the :ref:`kuka-calibration-program`.

Example program: PickitSimplePicking
------------------------------------

This example program can be found in **R1** > **Program** > **Pickit**.

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

        BAS(#TOOL,14) ; Tool for picking
        BAS(#BASE,0) ; Robot base

        PTP Detect
        Pickit_detect_with_retr(3)
        WAIT FOR Pickit_get_results() 

        LOOP
            IF Pickit_object_found() THEN
                ;Calculate pick points
                F_Pick=Pickit_get_pose()
                F_PrePick=F_Pick:{X 0.0,Y 0.0,Z -100.0,A 0.0,B 0.0,C 0.0}
                F_PostPick={X 0.0,Y 0.0,Z 100.0,A 0.0,B 0.0,C 0.0}:F_Pick
                
                ; Check if positions are reachable
                PickitAxistest=INVERSE(F_Pick,XHOME,Pickit_ErrStatCheckPos1)
                PickitAxistest=INVERSE(F_PrePick,XHOME,Pickit_ErrStatCheckPos2)
                PickitAxistest=INVERSE(F_PostPick,XHOME,Pickit_ErrStatCheckPos3)
                IF (Pickit_ErrStatCheckPos1==0) AND (Pickit_ErrStatCheckPos2==0) AND (Pickit_ErrStatCheckPos3==0) THEN
                    PTP AbovePickArea
                    LIN F_PrePick
                    LIN F_Pick
                    ;Add grasping logic
                    LIN F_PostPick
                    LIN AbovePickArea
                    PTP Detect
                    Pickit_detect_with_retr(3)
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

- First it is checked if Pickit is set to :ref:`Robot mode <web-interface-top-bar>`.
- If so, the robot moves to its detect pose and a detection is triggered.
- If an object is found, it's checked if the pick positions are reachable for the robot.
- If the object is reachable, the robot moves to the object to pick it.
  Next, the robot moves to a fixed drop off position.
  During these motions when the robot is out the field of view of the camera, a new Pickit detection is triggered immediately.
- If the object is not reachable the robot requests another object.
- If the ROI is empty, the program stops.
- If no object is found but ROI is not empty, a :ref:`Snapshots` is saved on the Pickit system and the robot program stops. 

.. note:: Depending on which software version you are running the example program can look different, the idea and functionallity are the same.

Define the tool for picking
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a tool with the actual TCP values.
In this example **#TOOL14** is used.

Set correct input arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The commands Pickit_configure and Pickit_detect_with_retr need input arguments.
See :ref:`` for more information about these arguments.

Define fixed positions
~~~~~~~~~~~~~~~~~~~~~~

In this example program 4 fixed positions are used.
These positions need to be defined depending on the application.

- **Home**: Where the robot will start the program.
- **Detect**: Where to perform object detection from.
- **AbovePickArea**: A point roughly above the pick area from which the above two can be reached without collision.
- **Dropit**: Where to place objects.

Add grasping/releasing logic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At the **pi pose** and **drop off pose** positions, grasping and releasing logic needs to be added, respectively.

Execute the picking program
---------------------------

Now you can run the program.
Happy picking!