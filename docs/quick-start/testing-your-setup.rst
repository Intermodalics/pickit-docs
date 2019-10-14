Testing your setup
==================

To verify that you have correctly set up your Pickit system, there are two
things you can check for:

#. You can successfully connect to the Pickit web interface from an external computer.
   
   -  Open a :ref:`supported web browser <supported-browsers>` on your external PC and enter http://192.168.66.1 in the address bar.
   -  Now the Pickit user interface is visible inside your web browser.

   .. image:: /assets/images/Documentation/pickit-webinterface-21.png

#. Pickit can successfully reach the IP address of the robot:

   -  From the top bar of the web interface, navigate to the :guilabel:`Settings` page, under **Pickit port labeled 'ROBOT'**.
   -  Insert the **IP address of your robot** in the Robot IP field and press :guilabel:`Check`.
   .. image:: /assets/images/Documentation/pickit-robot-connection.png
      :scale: 70%

If the above steps work as expected, you're ready to go, happy picking!
Else, if one of the steps did not work as expected, please contact us at
`support@pickit3d.com <mailto:mailto:support@pickit3d.com>`__ and we'll help you figure out what's going on.

.. tip:: More details about testing your setup can be found in following articles :ref:`connecting-to-the-web-interface` and :ref:`test-robot-connection`.