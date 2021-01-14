# StaticsSolver API (V3)

### Table of Contents
* [Dependencies](#dependencies)
* **[Vector](#vector)**
	* [disp](#disp)
	* [add](#add)
	* [mag](#mag)
	* [dot](#dot)
	* [cross](#cross)
	* [unit](#unit)
	* [scalarMult](#scalarmult)
	* [addOrigin](#addorigin)
	* [addComps](#addcomps)
	* [getPointOfAction](#getpointofaction)
	* [getEndpoint](#getendpoint)
	* [getComps](#getcomps)
* **[Load](#load)**
	* [getForce](#getforce)
* **[Truss](#truss)**
	* [generateMembers](#generatemembers)
	* [showMembers](#showmembers)
	* [addSupports](#addsupports)
	* [getForcesOnPoint](#getforcesonpoint)
	* [addExtForces](#addextforces)
	* [getAdjacentJoints](#getadjacentjoints)
	* [solveByJoints](#solvebyjoints)
* [Methods](#methods)
* [sumForces](#sumforces)
* [sumMoments](#summoments)
* [solve](#solve)
* [gaussElim](#gausselim)
* [deg2Rad](#deg2rad)
* [shearMomentDiagram](#shearmomentdiagram)

### Dependencies

This module requires the following modules to be installed already:

* math
* matplotlib
* numpy
* sympy

## Vector

### \__init__

**\__init__(**_self, vecType, a1, a2, a3, pointOfAction, tol=1e-12_**)**

Constructor method for Vector class.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **self** : __*self*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; N/A |
| | **vecType** : __*string*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Vector is defined using Cartesian ('c','Cartesian') or Magnitude ('m','Magnitude'). |
| | **a1** : __*float,symbol*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Fist component. |
| | **a2** : __*float,symbol*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Second component. |
| | **a3** : __*float,symbol*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Third component. |
| | **pointOfAction** : __*tuple*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Tuple defining point upon which force is acting. |
| | **tol** : __*float, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Tolerance for rounding values while defining object. |
| **Returns:** | **None** : __*None*__ |
| **Raises:** | __*None*__ |

### disp

**disp(**_self_**)**

Prints string describing vector.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **self** : __*self*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; N/A |
| **Returns:** | **None** : __*None*__ |
| **Raises:** | __*None*__ |

### add

**add(**_f1,f2_)**

Adds two vectors.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **f1, f2** : __*Vector*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The two vectors to be added. |
| **Returns:** | **Vector** : __*Vector*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The summation of the two vectors. |
| **Raises:** | __*None*__ |

### mag

**mag(**_self_**)**

Returns the magnitude of the vector.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **self** : __*self*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;N/A |
| **Returns:** | **float** : __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The magnitude of the vector. |
| **Raises:** | __*None*__ |

### dot

**dot(**_f1, f2_**)**

Dot product of two vectors.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **f1, f2** : __*Vector*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The vectors to be dotted together. |
| **Returns:** | **<float>** : __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The dot product of the two vectors. |
| **Raises:** | __*None*__ |

### cross

**cross(**_f1, f2_**)**

Cross product of two vectors.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **f1, f2** : __*Vector*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The vectors to be crossed together. |
| **Returns:** | **<float>** : __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The cross product of the two vectors. |
| **Raises:** | __*None*__ |

### unit

**unit(**_self_**)**

Returns a unit vector pointing in the same direction as the vector.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **self** : __*self*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;N/A |
| **Returns:** | **<Vector>** : __*Vector*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The unit vector |
| **Raises:** | __*None*__ |

### scalarMult

**scalarMult(**_v, s_**)**

Multiplies a vector by a scalar.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **v** : __*Vector*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The vector to be scaled. |
| | **s** : __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The value by which to scale the vector. |
| **Returns:** | **<Vector>** : __*Vector*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The scaled vector. |
| **Raises:** | __*None*__ |

### addOrigin

**addOrigin(**_self,point_**)**

Redefines the point at which the vector acts without changing magnitude of vector.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Returns:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Raises:** | __**__ |

### addComps

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Returns:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Raises:** | __**__ |

### getPointOfAction

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Returns:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Raises:** | __**__ |

### getEndpoint

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Returns:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Raises:** | __**__ |

### getComps

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Returns:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Raises:** | __**__ |

## Load

### __init__

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Returns:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Raises:** | __**__ |

### getForce

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Returns:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Raises:** | __**__ |

## Truss

### __init__

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Returns:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Raises:** | __**__ |

### generateMembers

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Returns:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Raises:** | __**__ |

### showMembers

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Returns:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Raises:** | __**__ |

### addSupports

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Returns:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Raises:** | __**__ |

### getForcesOnPoint

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Returns:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Raises:** | __**__ |

### addExtForces

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Returns:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Raises:** | __**__ |

### getAdjacentJoints

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Returns:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Raises:** | __**__ |

### solveByJoints

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Returns:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Raises:** | __**__ |

## Methods

### sumForces

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Returns:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Raises:** | __**__ |

### sumMoments

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Returns:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Raises:** | __**__ |

### solve

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Returns:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Raises:** | __**__ |

### gaussElim

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Returns:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Raises:** | __**__ |

### deg2Rad

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Returns:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Raises:** | __**__ |

### shearMomentDiagram

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Returns:** | **** : __**__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; |
| **Raises:** | __**__ |

