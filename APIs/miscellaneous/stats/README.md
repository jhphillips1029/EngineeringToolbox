# Stats API

[Back](../../README.md)

### Table of Contents
* [Dependencies](#dependencies)
* [constructTwoWayFrequencyTable](#constructtwowayfrequencytable)
* [displayTwoWayFrequencyTable](#displaytwowayfrequencytable)
* [P](#p)

### Dependencies

This module requires the following modules to be installed already:

* scipy

### constructTwoWayFrequencyTable

**constructTwoWayFrequencyTable**(*v1,v2,v3,v4,t1,t2,t3,t4*)

Constructs a two way frequency table for use with the probability function, filled as shown below.

|  |t1|t2|
|---|---|---|
|**t3**|v1|v2|
|**t4**|v3|v4|

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **v1,v2,v3,v4** : __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The values of the table. |
| | **t1,t2,t3,t4** : __*string*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The titles of the table columns and rows. |
| **Returns:** | **dict** : __*dict*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Dicionary representing the two way frequency table. |
| **Raises:** | __*None*__ |
| | |

### constructTwoWayFrequencyTable

**constructTwoWayFrequencyTable**(*table*)



|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **table** : __*dict*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The table to display. |
| **Returns:** | **None** : __*None*__ |
| | |
| **Raises:** | __*None*__ |
| | |

### P

**P**(*eq,\*\*kwargs*)

Generalized probability function.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **eq** : __*str*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The equation to evaluate |
| | **kwargs** : __*varies*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Additional parameters. |
| **Returns:** | **float** : __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Returns the probability of an event occuring as stated in *eq*. |
| **Raises:** | __*ValueError*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;ValueError raised if no relational operator is recognized and no sample space provided. |
| | __*ValueError*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;ValueError raised if variable provided for Z or T table evaluation is not defined. |
| | __*ValueError*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;ValueError raised if sample size not provided for T table evaluation. |
| | __*ValueError*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;ValueError raised if sample space not defined for union, intersection, or given evaluation. |
| | __*ValueError*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;KeyError raised if left-hand or right-hand side of the equation does not appear in the sample space keys. |
| | __*ValueError*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;ValueError raised if disjointedness is not defined for union evaluation. |
| | __*ValueError*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;ValueError raised if independence is not defined for intersection evaluation. |
| | __*ValueError*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;ValueError raised if all else fails. |

|kwarg Value|Description|
|---|---|
|**varies** : __*float*__|Value of variable listed in T or Z table evaluation equation. Must match case of corresponding variable.|
|**S** : __*dict*__|Dictionary describing sample space.|
|**independent** : __*boolean*__|Whether or not events in sample space are independent.|
|**disjoing** : __*boolean*__|Whether or not events in sample space are disjoint.|

