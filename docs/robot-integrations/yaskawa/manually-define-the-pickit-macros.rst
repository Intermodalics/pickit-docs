.. _manually-define_macros:

Manually define the Pickit macros
=================================

Here we'll explain how to define the Pickit macros manually without overwriting any existing macros.

Define macros
-------------

Booting the controller in **normal mode**, the macros can be defined manually.
To do this go to :guilabel:`SYSTEM` → :guilabel:`SETUP` → :guilabel:`MACRO INST.`.

.. note:: In order to use the example Pickit files, the macros should be defined in the exact same order as shown in the image below.
   Otherwise, the example files should be adapted with the correct macro ID's before being run.

+---------+-------------+-------------+
|         | EXECUTE JOB | SUSPEND JOB |
+=========+=============+=============+
| MACRO1  | PI_CALIB    | `********`  |
+---------+-------------+-------------+
| MACRO2  | PI_LOOK     | `********`  |
+---------+-------------+-------------+
| MACRO3  | PI_WAIT     | `********`  |
+---------+-------------+-------------+
| MACRO4  | PI_NEXT     | `********`  |
+---------+-------------+-------------+
| MACRO5  | PI_CFG      | `********`  |
+---------+-------------+-------------+
| MACRO6  | PI_SAVE     | `********`  |
+---------+-------------+-------------+
| MACRO7  | PI_RUN      | `********`  |
+---------+-------------+-------------+
| MACRO8  | PI_GPPD     | `********`  |
+---------+-------------+-------------+
| MACRO9  | PI_CAPTU    | `********`  |
+---------+-------------+-------------+
| MACRO10 | PI_PROCE    | `********`  |
+---------+-------------+-------------+
| MACRO11 | PI_BUILD    | `********`  |
+---------+-------------+-------------+

Macro argument definition
-------------------------

For macro **PI_CALIB** and **PI_CFG**, arguments need to be defined.

To do this select the **MACROXX** text and press :guilabel:`SELECT`.

Here set **ARG. SET** to **USE** and fill in **COMMENT1**, **TYPE** and **COMMENT2**.
Press :guilabel:`PAGE`, select **define 2**, and fill in **DISPLAY** and **EXPRES"N**.
The values that need to be filled in can be found in the table below.

+--------------+------------+----------------------------------------+-------------------------------------------+
| **Data**     | **ARG.no** | **define 1**                           | **define 2**                              |
|              |            +--------------+----------+--------------+--------------+-------------+--------------+
|              |            | **COMMENT1** | **TYPE** | **COMMENT2** | **COMMENT1** | **DISPLAY** | **EXPRES'N** |
+--------------+------------+--------------+----------+--------------+--------------+-------------+--------------+
| **PI_CALIB** | **1**      | USER FRAME   | B CONST  |              | USER FRAME   | ON          | U/FRAME:     |
+--------------+------------+--------------+----------+--------------+--------------+-------------+--------------+
| **PI_CFG**   | **1**      | SETUP        | I CONST  |              | SETUP        | ON          | SETUP:       |
|              +------------+--------------+----------+--------------+--------------+-------------+--------------+
|              | **2**      | PRODUCT      | I CONST  |              | PRODUCT      | ON          | PRODUCT:     |
|              +------------+--------------+----------+--------------+--------------+-------------+--------------+
|              | **3**      | USER FRAME   | I CONST  | 1-63         | USER FRAME   | ON          | U/FRAME:     |
|              +------------+--------------+----------+--------------+--------------+-------------+--------------+
|              | **4**      | TOOL         | I CONST  | 1-64         | TOOL         | ON          | TOOL:        |
|              +------------+--------------+----------+--------------+--------------+-------------+--------------+
|              | **5**      | TIMEOUT      | I CONST  | ms           | TIMEOUT      | ON          | TIMEOUT:     |
+--------------+------------+--------------+----------+--------------+--------------+-------------+--------------+

If the arguments are set correctly, the screen will be similar as shown below.
Now the Pickit macros are correctly defined, and you're all set to continue with the Yaskawa integration.

.. image:: /assets/images/robot-integrations/yaskawa/yaskawa-macro-arguments.png