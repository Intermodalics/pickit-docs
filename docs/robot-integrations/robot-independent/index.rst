.. _robot-independent-index:

Robot-independent Pickit integration
====================================

The articles in this section describe the interaction between Pickit and a robot in a way that is independent of the robot brand.
As such, they provide all the necessary information for integrating a new robot brand into Pickit. Such an effort requires implementing two layers, presented below: **interface** and **communication**.

Interface
---------

The Application Programming Interface (API) layer is what the robot programmer interacts with.
The following articles can be used as a reference on how to structure the API of a new robot integration, and how the API should be used from robot programs to perform vision-guided pick and place with Pickit.

The articles present content in robot-independent pseudo-code. When developing a new integration, code examples need to be adapted to the syntax, features and best practices of the target robot programming language, but the key concepts and ideas remain the same.

  .. toctree::
    :glob:
    :maxdepth: 1
    
    interface.rst
    pick-and-place-simple.rst
    pick-and-place.rst
    calibration.rst

  .. toctree::
    :glob:
    :maxdepth: 1
    :hidden:
    
    socket.rst

Communication
-------------

The communication layer takes care of the low-level data exchange between the robot and Pickit by implementing the :ref:`Pickit socket communication protocol <socket-communication>`. This part of the integration is typically not visible to the robot programmer, and is abstracted by the interface layer.

Pickit also supports communication via `ROS <https://www.ros.org/>`__. 
Refer to the following article about :ref:`the Pickit ROS interface <ros>` to learn more. 
