.. _object-ordering:

Object ordering
---------------

This setting defines in which order the objects are returned to the
robot.

-  **Highest product:** Sort objects by Z value, from the highest
   to the lowest Z value. This is the most common option.
-  **Lowest product:** Reverse ordering from 'Highest product'.
-  **Highest product part:** Sort objects with highest part first.
-  **Lowest X value first:** Orders objects based on object center
   position. From small to large X value.
-  **Highest X value first:** Reverse ordering from 'Lowest X value
   first'.
-  **Lowest Y value first:** Orders objects based on object center
   position. From small to large Y value.
-  **Highest Y value first:** Reverse ordering from 'Lowest Y value
   first'.
-  **Largest product:** Objects are ordered from big to small volume or
   surface.
-  **Pattern along the positive X-axis:** See image below.
-  **Pattern along the negative X-axis:** See image below.
-  **Pattern along the positive Y-axis:** See image below.
-  **Pattern along the negative Y-axis:** See image below.
-  **Highest matching score (Teach only):** Sort objects with the
   highest model matching score first. This only works for the Teach
   detection
-  **Top box first (Flex only):** Sort objects with the highest product center
   first, but if multiple sides of a box are recognized, the bigger side
   is prefered instead of the smaller.

The pattern sort options are useful for depalletization or pallet
loading applications. The picture below illustrates each option:

.. image:: /assets/images/Documentation/Object-ordering-pattern.png
