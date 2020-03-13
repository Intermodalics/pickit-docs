 .. _detection:

Detection
=========

General engines
---------------

Pickit has three general detection engines, each optimized for a different
type of shape or part arrangement.

- :ref:`Teach <Teach>` is the most versatile engine, and well suited for most
  shapes, both simple and complex. You teach the part you want to detect by
  showing it to the camera or uploading a CAD model of it.
  It is the recommended detection engine for most applications.

- :ref:`Flex <Flex>` is meant for detecting geometric shapes in 3D
  (cylinders and spheres) and 2D (squares, rectangles, circles and ellipses).
  It can detect instances of the same shape with similar or different sizes.

- :ref:`Pattern <Pattern>` is similar to Flex. It looks for 2D shapes
  (rectangles, squares, circles and ellipses) of known fixed size, and is
  especially useful for detecting parts that are aligned and touching.

.. tip::
  You can learn about the main ideas behind the :ref:`Teach <Teach>` engine by watching this :ref:`video tutorial <video-tutorials-what-to-pick>`.

.. toctree::
  :maxdepth: 1
  :hidden:

  Teach <teach/index>
  Flex <flex/index>
  Pattern <pattern/index>

Application-specific engines
----------------------------

Pickit also offers a more application-specific engine, :ref:`Bags <Bags>`, which
is specially designed for detecting bags on a pallet.

.. toctree::
  :maxdepth: 1
  :hidden:

  Bags <bags/index>
