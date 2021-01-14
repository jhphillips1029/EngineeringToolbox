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
| **Returns:** | **float** : __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The dot product of the two vectors. |
| **Raises:** | __*None*__ |

### cross

**cross(**_f1, f2_**)**

Cross product of two vectors.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **f1, f2** : __*Vector*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The vectors to be crossed together. |
| **Returns:** | **Vector** : __*Vector*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The cross product of the two vectors. |
| **Raises:** | __*None*__ |

### unit

**unit(**_self_**)**

Returns a unit vector pointing in the same direction as the vector.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **self** : __*self*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;N/A |
| **Returns:** | **Vector** : __*Vector*__ |
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
| **Returns:** | **Vector** : __*Vector*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The scaled vector. |
| **Raises:** | __*None*__ |

### addOrigin

**addOrigin(**_self,point_**)**

Redefines the point at which the vector acts without changing magnitude of vector.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **self** : __*self*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;N/A |
| | **point** : __*list_like*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Point defining new point of action. |
| **Returns:** | **None** : __*None*__ |
| **Raises:** | __**__ |

### addComps

**addComps(**_self,tag,c1,c2,c3_**)**

Redefines the components of the vector.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **self** : __*self*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;N/A |
| | **tag** : __*string*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Determines the method in which the vector is defined. |
| | **c1, c2, c3** : __*float, symbol*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The components of the vector. |
| **Returns:** | **None** : __*None*__ |
| **Raises:** | __*None*__ |

### getPointOfAction

**getPointOfAction(**_self_**)**

Gets point from which the vector acts.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **self** : __*self*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;N/A |
| **Returns:** | **tuple** : __*tuple*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Tuple describing a point in 3D space. |
| **Raises:** | __*None*__ |

### getEndpoint

**getEndpoint(**_self_**)**

Gets point at the tip of the vector.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **self** : __*self*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;N/A |
| **Returns:** | **tuple** : __*tuple*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Tuple describing a point in 3D space. |
| **Raises:** | __*None*__ |

### getComps

**getComps(**_self_**)**

Returns the components of the vector.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **self** : __*self*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;N/A |
| **Returns:** | **tuple** : __*tuple*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Tuple describing the components of the vector. |
| **Raises:** | __*None*__ |

## Load

### \__init__

**\__init__(**_self,expr,start,end,axis2,axis1=1_**)**

Constructor for Load class.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **self** : __*self*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;N/A |
| | **expr** : __*lambda function*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The expression defining the loading scenario. |
| | **start,end** : __*tuple*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Tuples defining the boundaries of the loading. |
| | **axis2** : __*integer*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Defines the direction of the loading. |
| | **axis1** : __*integer, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Defines the axis the loading takes place on. |
| **Returns:** | **None** : __*None*__ |
| **Raises:** | __*None*__ |

### getForce

**getForce(**_self,start,end,num=1000_**)**

Returns the resultant force from the defined portion of loading.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **self** : __*self*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;N/A |
| | **start,end** : __*tuple*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Tuples defining the boundaries of the portion to use. |
| | **num** : __*integer, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Defines the number of partitions used in numerical integration. Default is 1000. |
| **Returns:** | **Vector** : __*Vector*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The force from the portion of loading defined. |
| **Raises:** | __*None*__ |

## Truss

### \__init__

**\__init__(**_self,points_**)**

Constructor for the Truss class

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **self** : __*self*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;N/A |
| | **points** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;List of tuples defining points in space. |
| **Returns:** | **None** : __*None*__ |
| **Raises:** | __*None*__ |

### generateMembers

**generateMembers(**_self,connections_**)**

Defines where truss members exist. Use the form \[(A,\[B,C,D]),(B,\[D,E]),...]. Do not repeat connections.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **self** : __*self*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;N/A |
| | **connections** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;List of tuples defining points with form defined above. |
| **Returns:** | **None** : __*None*__ |
| **Raises:** | __*None*__ |

### showMembers

**showMembers(**_self_**)**

Print information defining truss members.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **self** : __*self*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;N/A |
| **Returns:** | **None** : __*None*__ |
| **Raises:** | __*None*__ |

### addSupports

**addSupports(**_self,supports_**)**

Defines supports for truss.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **self** : __*self*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;N/A |
| | **supports** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;List of supports. |
| **Returns:** | **None** : __*None*__ |
| **Raises:** | __*None*__ |

### getForcesOnPoint

**getForcesOnPoint(**_self,point_**)**

Returns the forces acting at the point specified.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **self** : __*self*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;N/A |
| | **point** : __*tuple*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Tuple defining point of interest. |
| **Returns:** | **Vector** : __*Vector*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Vector representing net force acting on point. |
| **Raises:** | __*None*__ |

### addExtForces

**addExtForces(**_self,extForces_**)**

Define external forces acting on truss object.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **self** : __*self*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;N/A |
| | **extForces** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;List of Vectors defining external forces acting on truss object. |
| **Returns:** | **None** : __*None*__ |
| **Raises:** | __*None*__ |

### getAdjacentJoints

**getAdjacentJoints(**_self,point_**)**

Returns list of adjacent joints connected by truss members.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **self** : __*self*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;N/A |
| | **point** : __*tuple*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Point of interest. |
| **Returns:** | **rtn** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;List of adjacent joints connected by truss members. |
| **Raises:** | __*None*__ |

### solveByJoints

**solveByJoints(**_self,jointOrder,show=False_**)**

Determine forces acting in all truss members.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **self** : __*self*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;N/A |
| | **jointOrder** : __*list_like*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;List of joints to proceed through in order to solve. |
| | **show** : __*boolean, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Show the math necessary to solve. Default is False. |
| **Returns:** | **rtn** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;List of forces acting on each truss member |
| **Raises:** | __*None*__ |

## Methods

### sumForces

**sumForces(**_forces_**)**

Sums over a list of vectors for net force.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **forces** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;List of vectors to sum |
| **Returns:** | **F_net** : __*Vector*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Net force acting on object. |
| **Raises:** | __*None*__ |

### sumMoments

**sumMoments(**_point, forces, moments_**)**

Sums over a list of vectors for a net moment about a point.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **point** : __*tuple*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Point to sum moments about. |
| | **forces, moments** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Lists of Vectors to sum moments of about defined point. |
| **Returns:** | **M_net** : __*Vector*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Net moment acting about the point. |
| **Raises:** | __*None*__ |

### solve

**solve(**_eqs, u, slns=None, subs=None, show=False, solver='default'_**)**

Solves system of equations.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **eqs** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;List of SymPy expressions. |
| | **u** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;List of SymPy symbols for unknowns. |
| | **slns** : __*list, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;List of non-zero solutions to solve for. Default is None. |
| | **subs** : __*list, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;List of tuples in \[(symbol,value)] order. Will substitute value in for symbol. Default is None. |
| | **show** : __*boolean, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Determines whether or not to show the math used to solve. Default is False. |
| | **solver** : __*string, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Determine the solver to use. Default is 'default'. |
| **Returns:** | **rtn** : __*ndarray*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Array of values solved for. |
| **Raises:** | __*TypeError*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;TypeError raised if the length of eqs and u are unequal |
| | __*TypeError*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;TypeError raised if the length of eqs and solns are unequal while solns is not None. |

### gaussElim

**gaussElim(**_A,B_)**

Gauss elimination algorithm.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **A,B** : __*ndarray*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The arrays of coefficients and solutions. |
| **Returns:** | **rtn** : __*ndarray*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Solution for the unknown array. |
| **Raises:** | __*None*__ |

### deg2Rad

**deg2Rad(**_deg_**)**

Converts degrees to radians

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **deg** : __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Value of angle in degrees |
| **Returns:** | **float** : __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Value of angle in radians |
| **Raises:** | __**__ |

### shearMomentDiagram

**shearMomentDiagram(**_loads,forces,moments,startPt,stopPt,axis=1,num=1000,sigFigs=3,saveAs=None_**)**

Plots a shear-moment diagram given geometric and loading information.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **loads** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;List of Load objects acting on object. |
| | **forces, moments** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;List of Vector objects acting on object, including reaction forces and moments. |
| | **startPt, stopPt** : __*tuple*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Tuples describing boundary points. |
| | **axis** : __*integer, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Defines axis for shear-moment diagram analysis. Default is 1. |
| | **num** : __*integer, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Defines number of partitions for numerical integration. Default is 1000. |
| | **sigFigs** : __*integer, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Defines number of significant figures to display on diagrams. Default is 3. |
| | **saveAs** : __*string, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Name of file to save diagram to. |
| **Returns:** | **tuple** : __*tuple*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Tuple containing the length array, shear arrays, and moment arrays. |
| **Raises:** | __*None*__ |

