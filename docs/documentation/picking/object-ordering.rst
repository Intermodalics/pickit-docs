.. _object-ordering:

Object ordering
---------------

When multiple objects are detected, object ordering determines the order in which they should be picked.
The following strategies are available:

-  **Highest product:** Sort objects by their pick point location, from largest
   to smallest :ref:`reference frame <reference-frame>` Z-coordinate. This is the most common option.
-  **Lowest product:** The reverse order of 'Highest product'.
-  **Highest product part:** Sort objects by the highest detected point.
-  **Lowest X:** Sort objects by their pick point location, from smallest to largest :ref:`reference frame <reference-frame>` X-coordinate.
-  **Highest X:** The reverse order of 'Lowest X'.
-  **Lowest Y:** Sort objects by their pick point location, from smallest to largest :ref:`reference frame <reference-frame>` Y-coordinate.
-  **Highest Y:** The reverse order of 'Lowest Y'.
-  **Largest product (Flex only):** Objects are sorted from big to small volume or
   surface.
-  **Pattern along the positive X-axis:** See image below.
-  **Pattern along the negative X-axis:** See image below.
-  **Pattern along the positive Y-axis:** See image below.
-  **Pattern along the negative Y-axis:** See image below.
-  **Highest matching score (Teach only):** Sort objects with the
   highest model matching score first.
-  **Top box first (Flex only):** Sort objects with the highest product center
   first, but if multiple sides of a box are recognized, the largest side
   is prefered.

The pattern sort options are useful for depalletization or pallet
loading applications. The picture below illustrates each option:

.. image:: /assets/images/documentation/Object-ordering-pattern.png
