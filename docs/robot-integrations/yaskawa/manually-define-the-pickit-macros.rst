.. _manually-define_macros:

Manually define the Pickit macros
=================================

Here we'll explain how to define the Pickit macros manually without overwriting any existing macros.

Define macros
-------------

Still in **normal mode**, the macros should be defined manually.
To do this go to :guilabel:`SYSTEM` → :guilabel:`SETUP` → :guilabel:`MACRO INST.`.

.. note:: In order to use the example Pickit files, the macros should be defined in the exact same order as shown in the image below.
   If not, the example files should be addapted with the correct macro ID before running them.

.. image:: /assets/images/robot-integrations/yaskawa/yaskawa-macro.jpg

Macro argument definition
-------------------------

For macro **PIT_CALB** and **PIT_CFG** arguments need to be defined.

To do this select the **MACROXX** text and press :guilabel:`SELECT`.

Here set **ARG. SET** to **USE** and fill in **COMMENT1**, **TYPE** and **COMMENT2**.
Next press :guilabel:`PAGE` and select **define 2**, now you can fill in **DISPLAY** and **EXPRES"N**.
The values that need to be filled in can be found in the table below.

+--------------+------------+----------------------------------------+-------------------------------------------+
| **Data**     | **ARG.no** | **define 1**                           | **define 2**                              |
|              |            +--------------+----------+--------------+--------------+-------------+--------------+
|              |            | **COMMENT1** | **TYPE** | **COMMENT2** | **COMMENT1** | **DISPLAY** | **EXPRES'N** |
+--------------+------------+--------------+----------+--------------+--------------+-------------+--------------+
| **PIT_CALB** | **1**      | USER FRAME   | B CONST  |              | USER FRAME   | ON          | U/FRAME:     |
+--------------+------------+--------------+----------+--------------+--------------+-------------+--------------+
| **PIT_CFG**  | **1**      | SETUP        | I CONST  |              | SETUP        | ON          | SETUP:       |
|              +------------+--------------+----------+--------------+--------------+-------------+--------------+
|              | **2**      | PRODUCT      | I CONST  |              | PRODUCT      | ON          | PRODUCT:     |
|              +------------+--------------+----------+--------------+--------------+-------------+--------------+
|              | **3**      | USER FRAME   | I CONST  | 1-63         | USER FRAME   | ON          | U/FRAME:     |
|              +------------+--------------+----------+--------------+--------------+-------------+--------------+
|              | **4**      | TOOL         | I CONST  | 1-64         | TOOL         | ON          | TOOL:        |
|              +------------+--------------+----------+--------------+--------------+-------------+--------------+
|              | **5**      | TIMEOUT      | I CONST  | ms           | TIMEOUT      | ON          | TIMEOUT:     |
+--------------+------------+--------------+----------+--------------+--------------+-------------+--------------+

When the arguments are set correctly it will look similar as the image below.
Now the Pickit macros are correctly defined and you're all set to continue with the Yaskawa integration.

.. image:: /assets/images/robot-integrations/yaskawa/yaskawa-macro-arguments.png