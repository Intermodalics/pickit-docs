.. _universal-robots-scripts-example-program:

Universal Robots Example Program
================================

.. attention::
   This article describes the legacy way of using Pickit with a
   Universal Robot. For new robot programs, please refer to the :ref:`universal-robots-urcap-installation` article.

This program is part of the Universal Robots package  `which you can
download
here <https://drive.google.com/uc?export=download&id=1VedZYjVvlcyiE4iuqUuF67DsT8545ojU>`__. 

More details about downloading this programs and uploading them on a
Universal Robot can be found in the :ref:`universal-robots-scripts` article.

Loading the example program
---------------------------

In the initialization screen, select  ``Program robot`` and
then \ ``Load program``. Navigate to the folder corresponding to your UR
version and select the program \ **Robot\_picking.urp**. Click Open. The
program is then loaded. 

The example program explained
-----------------------------

The example application program Robot\_picking.txt executes a simple
picking task using Pickit.

.. code-block:: bash

    Init Variables
    BeforeStart
          pickit_port≔5001
          pickit_ip≔"169.254.5.180"
          actual_pose≔get_target_tcp_pose()
          pick_pose≔p[0,0,0,0,0,0]
          pre_pick_offset≔p[0,0,-0.15,0,0,0]
          Script: pickit_functions
          pickit_socket_open()
          Script: pickit_communication
          Script: pickit_transformations
    Robot Program
          MoveJ
               actual_pose
          Loop pickit_is_running()
               'pickit_configure(1,3)'
               If pickit_remaining_objects()≟0
                    pickit_look_for_object()
               Else
                    pickit_next_object()
               Wait pickit_has_response()
               If pickit_object_found()
                    pick_pose≔pickit_get_pose( False )
                    pre_pick_pose≔pose_trans(pick_pose, pre_pick_offset)
                    MoveJ
                         pre_pick_pose
                         pick_pose
                         pre_pick_pose
                    If pickit_object_dim[0] > 0.1
                         MoveJ
                              drop_off_large
                    Else
                         MoveJ
                              drop_off_small

          pickit_socket_close()

Pickit-related code lines are explained in detail:

.. code-block:: bash

          pickit_port≔5001
          pickit_ip≔"169.254.5.180"

The pickit\_port and pickit\_ip must be set to their correct values to
enable communication between the robot and Pickit.

.. code-block:: bash

          pick_pose≔p[0,0,0,0,0,0]
          pre_pick_offset≔p[0,0,-0.15,0,0,0]

The pose of the next detected object to be picked shall be stored in the
pose variable pick\_pose. For each pick, it is intended that the tool
briefly goes to an intermediary position above the actual pick\_pose,
before picking the object. The pre\_pick\_offset defines this offset and
will be used later, adding a negative translational component to the
z-axis of the tool.

.. code-block:: bash

          Script: pickit_functions
          ...
          Script: pickit_communication
          Script: pickit_transformations

Scripts containing relevant Pickit functions are loaded.

.. code-block:: bash

          pickit_socket_open()

.. code-block:: bash

          pickit_socket_close()

Lines 9 and 35 open and close a socket connection with Pickit
respectively.

.. code-block:: bash

          Loop pickit_is_running()

This line indicates that, as long as Pickit is running (i.e., the **RUN
button** is active), the code inside its scope will be executed
repeatedly.

.. code-block:: bash

          'pickit_configure(1,3)'

Pickit is commanded to load the setup and product with codes 1 and 3
respectively. These are the numbers shown next to the setup and product
on the Pickit CONFIGURATION page. If this line is suppressed, Pickit
keeps its current setup and product. If the specified setup or product
does not exist, the program does not proceed. Make sure that the setup
and product passed to pickit\_configure()are the ones you are expecting,
or the robot may have an unexpected behaviour.

.. code-block:: bash

          If pickit_remaining_objects()≟0
                pickit_look_for_object()
          Else
                pickit_next_object()

If only one object was found the last time Pickit searched for objects,
it is ordered to search for objects once again. However, if Pickit
found more than one object in its previous search, the next object is
requested.

.. code-block:: bash

          Wait pickit_has_response()
                If pickit_object_found()
                      pick_pose≔pickit_get_pose( False )
                      pre_pick_pose≔pose_trans(pick_pose, pre_pick_offset)
                      MoveJ
                            pre_pick_pose
                            pick_pose
                            pre_pick_pose

The program waits until Pickit returns the requested object and, if it
is found, the robot shall pick it.The pose that the robot shall reach to
pick the object (pick\_pose) is returned by the function
pickit\_get\_pose(). Before the actual picking, it is desired that the
robot first stops at a distance above the object. This pose is here
called pre\_pick\_pose and is the pick pose translated by 15 cm in the Z
direction, as defined by the variable pre\_pick\_offset. The robot is
commanded to adopt first the pre\_pick\_pose, than the pick\_pose (where
it actually picks the object), and finally the pre\_pick\_pose again.

.. code-block:: bash

          If pickit_object_dim[0] > 0.1
                MoveJ
                      drop_off_large
          Else
                MoveJ
                      drop_off_small

In this example application, it is desired that large and small objects
are dropped in different places. The robot reaches this places by
adopting poses drop\_off\_large and drop\_off\_small respectively. As
such, depending on the object’s dimensions, defined by
pickit\_object\_dim[0], the robot shall adopt the correct pose to reach
the corresponding target place.

Notice that the actual picking is not performed here. The procedure to
grasp and drop depends on the employed gripper.

Running the example program
---------------------------

.. attention::
   Before running the program, it should be verified that the robot-camera
   calibration has been done correctly and that the tool frame has been
   defined correctly.


To allow Pickit to respond to robot requests, Pickit has to be in the
Running state. Press the RUN button on the Pickit web interface.

In order to run the program in the robot controller, at the bottom of
the graphic interface, make sure that **Real robot** is selected and
that the robot speed is set to a safe value. Click on the rewind
button to make sure that the program starts from the beginning - the
program line **Robot Program** shall be highlighted, meaning that’s the
point at which the program will start. Finally click on the play button
to run the program.

.. image:: /assets/images/examples/ur-teach-pendant.png

The program execution can be stopped or paused by clicking in the stop
and pause buttons respectively.

.. danger::
   When running a program for the first time, it is advised to **set a low
   robot speed**. As such, non-expected behaviour (for example due to
   incorrect programming or wrong calibration) can be identified early
   enough to prevent the robot from colliding with surrounding objects or
   people.
