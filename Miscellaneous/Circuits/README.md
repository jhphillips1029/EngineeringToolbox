# CiruitMaker API (V1)

# Table of Contents
* [Dependencies](#dependencies)

* **[Comp](#comp)**
	* [wire](#wire)
	* [res](#res)
	* [Isrc](#isrc)
	* [Vsrc](#vsrc)
	* [gnd](#gnd)
* [Methods](#methods)
* [texCircuit](#texcircuit)
* [Thevenin_Norton](#thevenin_norton)

### Dependencies

This module requires the following modules to be installed already:

* math

## Comp

### \_\_init__

**\_\_init__(**_self,start,end=None,compType=None,labels=None,arrowType=None,node=None_**)**

Constructor for Comp class.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **self** : __*self*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;N/A |
| | **start** : __*tuple*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;2D point defining where to start. |
| | **end** : __*tuple, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;2D point defining where to stop. Default is None. |
| | **compType** : __*string, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Type of component to draw. Default is None. |
| | **labels** : __*lsit*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;List of labels to use. Default is None. |
| | **arrowType** : __*string*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;String matching proper regex to define arrow type. Default is None. |
| | **node** : __*string*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;String describing node. Default is None. |
| **Returns:** | **None** : __*None*__ |
| **Raises:** | __*TypeError*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Raises TypeError if both compType and node are None. |

### wire

**wire(**_start,end,arrowType_**)**

Wire component.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **start, end** : __*tuple*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Start and end points. |
| | **arrowType** : __*string*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Arrow type. |
| **Returns:** | **Comp** : __*Comp*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;A wire component. |
| **Raises:** | __*None*__ |

### res

**res(**_start,end,arrowType_**)**

Resistor component.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **start, end** : __*tuple*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Start and end points. |
| | **arrowType** : __*string*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Arrow type. |
| **Returns:** | **Comp** : __*Comp*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;A resistor component. |
| **Raises:** | __*None*__ |

### Isrc

**Isrc(**_start,end,arrowType_**)**

Current source component.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **start, end** : __*tuple*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Start and end points. |
| | **arrowType** : __*string*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Arrow type. |
| **Returns:** | **Comp** : __*Comp*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;A current source component. |
| **Raises:** | __*None*__ |

### Vsrc

**Vsrc(**_start,end,arrowType_**)**

Voltage source component.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **start, end** : __*tuple*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Start and end points. |
| | **arrowType** : __*string*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Arrow type. |
| **Returns:** | **Comp** : __*Comp*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;A voltage source component. |
| **Raises:** | __*None*__ |

### gnd

**gnd(**_start_**)**

Current source component.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **start** : __*tuple*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Start point. |
| **Returns:** | **Comp** : __*Comp*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;A ground component. |
| **Raises:** | __*None*__ |

## Methods

### texCircuit

**texCircuit(**_components_**)**

Generate LaTex code for a circuit diagram.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **components** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;List of Comp objects to draw. |
| **Returns:** | **circuit** : __*string*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;String of LaTex code for circuit diagram. |
| **Raises:** | __**__ |

### Thevenin_Norton

**Thevenin\_Norton(**_V\_OC,I\_SC,R\_t_**)**

Generates Thevenin and Norton equivalent circuits.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **V_OC,I_SC,R_t** : __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Equivalent values for Thevenin and Norton equivalent circuits. |
| **Returns:** | **string** : __*string*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Sting of LaTex code for Thevenin and Norton equivalent circuits. |
| **Raises:** | __*None*__ |

