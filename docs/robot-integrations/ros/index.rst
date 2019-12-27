.. _ros:

The Pickit ROS interface
========================

Connecting to Pickit using ROS
------------------------------

.. image:: /assets/images/robot-integrations/ros/ros-logo.png

The Pickit system is running a ROS Master, which allows another system to connect to it using the ROS interfaces. Pickit exposes its ROS parameters, nodes and topics using standard ROS messages and a limited set of Pickit specific ROS messages.

.. note::
    Since Pickit’s ROS master is always running on, it is recommended that the client system uses Pickit’s ROS master and does not start its own.

Connecting to Pickit ROS nodes requires you to define the Pickit hostname on the client system. Likewise, the client system’s name must be resolvable on the Pickit system. Preferably, the DNS Server of the client network resolves all hostnames to the LAN IP address of each host. If this is not possible, the host to IP mapping must be added to both Pickit’s and the client’s /etc/hosts.

The Pickit system is also running an ntp server. It can be used to make sure that the time between the client system and the Pickit system stays synchronised.

.. image:: /assets/images/robot-integrations/ros/ros-network.png

Connecting to the Pickit system
--------------------------------

First verify that the Pickit system is reachable from your local system. Execute the following command in a terminal, replacing  ``<pickit-pc>`` with the hostname of your Pickit system.

.. code-block:: bash

    ping <pickit-pc>

The hostname of your Pickit system is shown on the top-left corner of the Pickit web interface, next to the Pickit logo. In the example below, it corresponds to  ``pickit-demo-002``.

.. image:: /assets/images/robot-integrations/ros/ros-pickit-hostname.png

If the ping test fails, please check the network configuration for your local system and make sure that it's in the same network as the Pickit system.

Set your local system to use the `ROS master <http://wiki.ros.org/ROS/EnvironmentVariables#ROS_MASTER_URI>`__ of the **Pickit system**.

.. code-block:: bash

    export ROS_MASTER_URI=http://<pickit-pc>:11311/

Set the `ROS_IP <http://wiki.ros.org/ROS EnvironmentVariables#ROS_IP.2BAC8-ROS_HOSTNAME>`__ environment variable to point to the IP of your **local system**.

.. code-block:: bash

    export ROS_IP=<local-pc-ip>

To test communications, you first need to source a ROS workspace containing the
``im_pickit_msgs`` package.
The package is available in our :ref:`downloads page <downloads:ROS>`.

Refer to the `catkin tools quickstart <http://catkin-tools.readthedocs.io/en/latest/quick_start.html>`__ for details on how to build ROS packages and source ROS workspaces. Once the package has been built and its workspace has been sourced, run the following commands to verify connectivity with the Pickit system:

.. code-block:: bash

    rostopic echo /pickit/heartbeat

If you see a stream of empty messages, then communication with the Pickit system has been established. Now run:

.. code-block:: bash

    rostopic echo /pickit/status

which should produce output similar to the following:

.. code-block:: bash

    state: root.Running.No_action
    setup_file: setup_default.cpf
    product_file: product_flex_example_cylinders.cpf
    setup_changed: False
    product_changed: False

If you instead get an error as shown below, it means that the current ROS workspace does not contain the  ``im_pickit_msgs`` package.

.. code-block:: bash

    ERROR: Cannot load message class for [im_pickit_msgs/PickitStatus]. Are your messages built?

Pickit ROS communication
-------------------------

The command-response mechanism
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Pickit ROS interface is based on using topics. Any connected robot or machine can give commands to Pickit by publishing a string command to the following topic:

.. code-block:: bash

        /pickit/external_cmds
        (type: std_msgs/String)

These commands will trigger Pickit to go into states responsible executing a specific task. The current state can at all times be monitored by subscribing to the following topic:

.. code-block:: bash

        /pickit/status
        (im_pickit_msgs/PickitStatus)

Object detections are published on a topic with a Pickit specific message type:

.. code-block:: bash

        /pickit/objects_wrt_robot_frame
        (type: im_pickit_msgs/ObjectArray)

Available commands
~~~~~~~~~~~~~~~~~~

The following are valid strings that can be passed as payload to the ``/im/pickit/external_cmds`` topic:

-  ``e_look_for_object``: Pickit performs one detection on the latest camera image.
-  ``e_do_stop``: Pickit leaves the continuous testing state.

-  ``e_calibration_requested``: Pickit looks for the robot camera calibration plate.

Changing the Pickit configuration
----------------------------------

To change the active setup or product file, use the  ``/load_config`` service. Product file change example from the command line:

.. code-block:: bash

    rosservice call /load_config "config_type: 2
    path: 'product_<productname>.cpf'
    set_persistent: false"

Where ``config_type`` should be 1 for changing the **setup** file, and 2 for changing the **product** file. More details on the service request and reply arguments can be found in the ``im_pickit_msgs/srv/LoadConfig.srv`` file.

Publishing the robot pose
-------------------------

When using the Pickit ROS interface, Pickit requires the robot pose of the robot being published on the ROS topic ``/pickit/robot_pose``. Robot pose in this context is the transform between robot base frame and robot end effector (without attached tool).

If you can lookup the above transform of your robot via `tf <http://wiki.ros.org/tf2>`__, you can use the Python script below to continuously publish the robot pose to the mentioned ROS topic.

.. code-block:: python
    :linenos:

    #!/usr/bin/env python
    import rospy
    import tf2_ros
    import geometry_msgs.msg


    if __name__ == "__main__":
        rospy.init_node('robot_pose_pub')
        tfBuffer = tf2_ros.Buffer()
        listener = tf2_ros.TransformListener(tfBuffer)

        # Make sure you provide the correct frame ids of your robot via the
        # parameter server.
        tf_base_link = rospy.get_param("~tf_base_link", "pickit/robot_base")
        tf_ee_link = rospy.get_param("~tf_ee_link", "pickit/robot_ee")
        publish_rate = rospy.get_param("~publish_rate", 10.0)
        base_to_ee_pub = rospy.Publisher("/pickit/robot_pose",
                                         geometry_msgs.msg.TransformStamped,
                                         queue_size=10)

        rate = rospy.Rate(publish_rate)
        while not rospy.is_shutdown():
            t = rospy.Time(0)
            try:
                trans_stamped = tfBuffer.lookup_transform(tf_base_link,
                                                          tf_ee_link, t)

            except (tf2_ros.LookupException, tf2_ros.ConnectivityException,
                    tf2_ros.ExtrapolationException):
                rate.sleep()
                continue

            trans_stamped.header.frame_id = "pickit/robot_base"
            trans_stamped.child_frame_id = "pickit/robot_ee"

            base_to_ee_pub.publish(trans_stamped)
            rate.sleep()

Camera URDF
-----------

You can retrieve the camera’s URDF from the ROS parameter server by issuing the following command:

.. code-block:: bash

    rosparam get /camera/camera_description > pickit_camera.urdf

The mesh files of the camera can be fetched from the Pickit system under

.. code-block:: bash

    http://<pickit-pc>/resources/camera/camera_description/meshes/camera_display.dae
    http://<pickit-pc>/resources/camera/camera_description/meshes/camera_hull.dae

With camera URDF and meshes it should be straight forward to build your own ``camera_description`` package and/or to directly integrate it with your robot’s URDF. For more information on this topic see http://wiki.ros.org/urdf/Tutorials.

TF tree
-------

Pickit uses two fixed robot frame names that are important for you if you want to connect your robot’s tf tree with Pickit’s tf tree. A simplified version of the Pickit tf tree for both camera fixed and camera on the robot looks like the following:

Camera fixed TF tree
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    pickit/robot_ee
           ^
           |
           |
           +              robot-camera-calibration
    pickit/robot_base +------------------------------> camera/camera_link

Camera on robot TF tree
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

                        robot-camera-calibration
     pickit/robot_ee  +------------------------------> camera/camera_link
            ^
            |
            |
            +
     pickit/robot_base

Connecting your robot’s tf tree
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Camera fixed
^^^^^^^^^^^^

For the camera fixed case this is fairly simple by publishing a static identity transform between your robot’s base frame (e.g. ``base_link``) and ``pickit/robot_base``. This can be done with `tf2’s static transform publisher <http://wiki.ros.org/tf2_ros#static_transform_publisher>`__. In a ROS launch file this could look like the following:

.. code-block:: xml

    <!-- Publish a static transform (identity) between base_link and
        pickit/robot_base to connect both tf tree. -->
    <node name="static_tf_brdc_pickit_robot" type="static_transform_publisher"
          args="0 0 0 0 0 0 base_link pickit/robot_base" pkg="tf2_ros" />

Camera on robot
^^^^^^^^^^^^^^^

This is similar to the camera fixed case with the addition that you also have to publish an identity transform between your robot’s end-effector frame (without attached tool) and ``pickit/robot_ee``.

.. note::
    It is currently not possible to disable the broadcasting of the tf transform between ``pickit/robot_base`` and ``pickit/robot_ee``. This will cause tf loops if you connect both frames with your corresponding robot frames. Disabling the tf broadcasting will be possible in future releases, contact us if this is a requirement for you and we will see what we can do.

A possible workaround for the tf loop issue would be to run a ROS node that filters the ``/tf`` topic by removing the above mentioned transform. The filtered result could then be published to another topic e.g. ``/tf_filtered``. You would then have to remap from ``/tf`` to ``/tf_filtered`` for all your nodes (that listen to tf) e.g. like this:

.. code-block:: bash

    rosrun rviz rviz /tf:=/tf_filtered

An example script that could to the filtering of the  ``/tf`` topic could look like this:

.. code-block:: python
    :linenos:

    #!/usr/bin/env python
    import rospy
    import tf.msg

    tf_pub = None


    def tf_message_cb(msg):
        global tf_pub
        msg.transforms = filter(lambda x: x.child_frame_id != "pickit/robot_ee" and
                                          x.header.frame_id != "pickit/robot_base",
                                msg.transforms)
       tf_pub.publish(msg)


    if __name__ == '__main__':
        rospy.init_node("tf_filter")
        tf_pub = rospy.Publisher('/tf_filtered', tf.msg.tfMessage, queue_size=10)
        tf_sub = rospy.Subscriber('/tf', tf.msg.tfMessage, tf_message_cb)
        rospy.spin()

Robot camera calibration
------------------------

Doing a robot camera calibration is not (yet) straightforward with the ROS interface. You need to publish certain commands to the ``/pickit/external_cmds`` topic and optionally listen to the ``/pickit/status`` or ``/pickit/status_calib`` topic to get feedback.

Single pose calibration
~~~~~~~~~~~~~~~~~~~~~~~

#. Go to the web interface and setup the calibration for :ref:`single pose <single-pose-calibration>` .
#. Publish the string command ``e_calibration_requested`` on the ``/pickit/external_cmds`` topic.
#. Save the calibration in the setup file (through web interface or ``/save_setup`` service).

Multi poses calibration
~~~~~~~~~~~~~~~~~~~~~~~

#. Go to the web interface and setup the calibration for :ref:`multi poses <multi-poses-calibration>` .
#. Move your robot to at least 5 different poses and for every pose publish the string command ``e_calibration_requested`` on the ``/pickit/external_cmds`` topic. Make sure to wait a couple of seconds (~10s) before moving to the next pose. Alternatively you can listen to the ``/pickit/status_calib`` topic to get notified when Pickit has processed the new calibration pose.
#. Publish the string command ``e_do_calculate_calibration`` on the ``/pickit/external_cmds`` topic.
#. Save the calibration in the setup file (through web interface or ``/save_setup`` service).

Topics of interest
------------------

+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Topic name**                                     | **Description**                                                                                                                                                                                                                                                                           |
+====================================================+===========================================================================================================================================================================================================================================================================================+
| ``/camera/depth_registered/points_3d_rectified``   | Raw calibrated point cloud.                                                                                                                                                                                                                                                               |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``/pickit/camera_to_reference``                    | Transformation between the camera's optical frame and the Pickit reference frame in which the ROI box is given in. This transformation is updated while the robot moves in case the camera is mounted on the robot and the Pickit reference frame is fixed to the robot's base frame.     |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``/pickit/clouds/model_cloud``                     | Point cloud of the currently active Pickit Teach model.                                                                                                                                                                                                                                   |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``/pickit/clouds/pp_scene_cloud``                  | Point cloud used by Pickit for object detection. It only contains points belonging to the Region of Interest.                                                                                                                                                                             |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``/pickit/folder_content``                         | List of available setup and product files.                                                                                                                                                                                                                                                |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``/pickit/is_detecting``                           | Boolean value indicating whether a detection is ongoing. True when a detection is ongoing.                                                                                                                                                                                                |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``/pickit/objects_wrt_reference_frame``            | List of detected objects given in the Pickit reference frame. The message also includes the camera pose with respect to the robot base, the camera to Pickit reference frame transform (same content of  ``/pickit/camera_to_reference``), and detection time.                            |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``/pickit/objects_wrt_robot_frame``                | Same as  ``/pickit/objects_wrt_reference_frame`` but object poses are transformed into the robot's base frame (``pickit/robot_base``). These object poses are the same as the ones the robot can request using the Pickit socket interface.                                               |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``/pickit/robot_calib_to_camera``                  | Transform between the robot and the camera's optical frame. The robot frame depends on the camera mount and is either the robot base ( ``pickit/robot_base``) or the robot flange (``pickit/robot_ee``).                                                                                  |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``/pickit/robot_connection_status``                | Boolean indicating whether the robot is sending pose updates to the Pickit system.                                                                                                                                                                                                        |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``/pickit/robot_pose``                             | The transformation between the robot base and robot flange as sent by the robot.                                                                                                                                                                                                          |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``/pickit/status``                                 | Status information of the Pickit system. Includes the state as well as the currently loaded setup and product file.                                                                                                                                                                       |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``/pickit/viewer/image_out``                       | Camera image corresponding to the 2D view in the Pickit web interface.                                                                                                                                                                                                                    |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The ROS message type of a given topic can be queried from the command
line with the ``rostopic info`` command, and the message payload can be
queried with the \ ``rossmg show`` command, for instance:

::

    $ rostopic info /pickit/objects_wrt_robot_frame
    Type: im_pickit_msgs/ObjectArray
    Publishers:
    ...
    Subscribers:
    ...

    $ rosmsg show im_pickit_msgs/ObjectArray
    <message definition>
