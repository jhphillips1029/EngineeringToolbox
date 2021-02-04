# Delta Design Tool API

[Back](../../README.md)

### Table of Contents
* [Dependencies](#dependencies)
* **[Deltoid](#deltoid)**
	* [coord](#coord)
	* [plot](#plot)
	* [coord_rect](#coord_rect)
	* [plot_rect](#plot_rect)
	* [center](#center)
	* [mark](#mark)
* **[Methods](#methods)**
* [determine_adjacencies](#determine_adjacencies)
* [shared_perimeter](#shared_perimeter)
* [find_red_deltas](#find_red_deltas)
* [get_centers](#get_centers)
* [centroid](#centroid)
* [plot_cluster](#plot_cluster)
* [mark_radiators](#mark_radiators)
* [radiative_length](#radiative_length)
* [get_longest_chain](#get_longest_chain)
* [get_deltan_distances](#get_deltan_distances)

### Dependencies

This module requires the following modules to be installed already:

* matplotlib
* numpy

## Deltoid

### \_\_init\_\_

**\_\_init\_\_**(*self,a,b,o,color=None*)

Constructor method for Deltoid class.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **self** : __*self*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; N/A |
| | **a** : __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;X-coordinate of deltoid, where a unit length one side of a deltoid. |
| | **b** : __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Y-coordinate of deltoid, where a unit length one side of a deltoid. |
| | **o** : __*int*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Orientation of the deltoid, should be 1 or -1. |
| | **color** : __*str*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Color of the deltoid, default is None. |
| **Returns:** | **None** : __*None*__ |
| | |
| **Raises:** | __*None*__ |
| | |

### \_\_str\_\_

**\_\_str\_\_**(*self*)

Overriden class for returning a string representation of a Deltoid object.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **self** : __*self*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; N/A |
| **Returns:** | **str** : __*string*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Returns string representation of Deltoid object. |
| **Raises:** | __*None*__ |
| | |

### coord

**coord**(*self*)

Returns the coordinates of the vertices of the Deltoid.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **self** : __*self*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; N/A |
| **Returns:** | **list** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Returns array of an array of x-coordinates and an array of y-coordinates of points at vertices of Deltoid |
| **Raises:** | __*None*__ |
| | |

### plot

**plot**(*self,axis=None,color=None*)

Plots the Deltoid using matplotlib.pyplot.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **self** : __*self*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; N/A |
|  | **axis** : __*matplotlib.pyplot.axis*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; The matplotlib.pyplot axis to plot the Deltoid on. |
|  | **color** : __*str*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; The color to plot the Deltoid. Will override color specified in \_\_init\_\_(). |
| **Returns:** | **None** : __*None*__ |
| | |
| **Raises:** | __*None*__ |
| | |

### coord\_rect

**coord\_rect**(*self*)

Returns the coordinates of the vertices of the Deltoid in normal Cartesian coordinates.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **self** : __*self*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; N/A |
| **Returns:** | **list** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Returns array of an array of x-coordinates and an array of y-coordinates of points at vertices of Deltoid |
| **Raises:** | __*None*__ |
| | |

### plot\_rect

**plot\_rect**(*self,axis=None,color=None*)

Plots the Deltoid using matplotlib.pyplot in normal Cartesian coordinates.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **self** : __*self*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; N/A |
|  | **axis** : __*matplotlib.pyplot.axis*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; The matplotlib.pyplot axis to plot the Deltoid on. |
|  | **color** : __*str*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; The color to plot the Deltoid. Will override color specified in \_\_init\_\_(). |
| **Returns:** | **None** : __*None*__ |
| | |
| **Raises:** | __*None*__ |
| | |

### center

**center**(*self*)

Returns the center of the Deltoid.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **self** : __*self*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; N/A |
| **Returns:** | **list** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Returns the coordinate point of the center of the Deltoid. |
| **Raises:** | __*None*__ |
| | |

### mark

**mark**(*self,tag,value*)

Returns the center of the Deltoid.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **self** : __*self*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; N/A |
| | **tag** : __*ANY*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The key for in *self.tags* to for which to write the value. |
| | **value** : __*ANY*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The value to enter into *self.tags* |
| **Returns:** | **None** : __*None*__ |
| | |
| **Raises:** | __*None*__ |
| | |

## Methods

### determine_adjacencies

**determine\_adjacencies**(*cluster,allow_repeat=False*)

Determine dictionary of adjacent Deltoids.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **cluster** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The cluster for which to determine adjacencies. |
|  | **allow_repeatable** : __*boolean*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Whether or not to include repeated instances of adjacent modules, default is False. |
| **Returns:** | **dict** : __*dict*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Returns dictionary of arrays of adjacencies, with keys corresponding to the indices in **cluster**. |
| **Raises:** | __*None*__ |
| | |

### shared\_perimeter

**shared\_perimeter**(*d1,d2,return\_points=False*)

Calculate the perimeter shared by two Deltoids.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **d1** : __*Deltoid*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The first Deltoid. |
|  | **d2** : __*Deltoid*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The second Deltoid |
|  | **return\_points** : __*boolean*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Whether or not to return the points used to calculate the distance. |
| **Returns:** | **float** : __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Returns the length of the shared perimeter |
| | **list** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Returns a list including the length of the shared perimeter and the two points used to calculate the length. |
| **Raises:** | __*None*__ |
| | |

### find\_red\_deltas

**find\_red\_deltas**(*cluster*)

Finds and returns the indices of the red deltas in a cluster.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **cluster** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The cluster including Deltoids with color defined as red in **\_\_init\_\_**. |
| **Returns:** | **list** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Returns a list of indices corresponding to the locations of red colored deltas in the cluster. |
| **Raises:** | __*None*__ |
| | |

### get\_centers

**get\_centers**(*cluster*)

Returns a list of all centers from the deltas in the cluster.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **cluster** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The cluster of Deltoids. |
| **Returns:** | **list** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Returns a list of coordinate pairs associated with the centers of deltas in the cluster in the Deltan coordinate system. |
| **Raises:** | __*None*__ |
| | |

### centroid

**centroid**(*cluster*)

Returns the centroid of the cluster.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **cluster** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The cluster of Deltoids. |
| **Returns:** | **list** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Returns the coordinate pair associated with the center of the cluster in the Deltan coordinate system. |
| **Raises:** | __*None*__ |
| | |

### plot\_cluster

**plot\_cluster**(*cluster,ignore\_deltas=False,centers=False,com=False,indices=False,bounding=False,ioi=-1,ioi\_furthest\_point=False,furthest\_points=False,furthest\_point\_method="com",axis=None,nc_weight=1.0*)

Plots the cluster.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **cluster** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The cluster including Deltoids with color defined as red in **\_\_init\_\_** |
| | **ignore\_deltas** : __*boolean*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Whether or not to ignore plotting the Deltoid in the cluster. Default is False. |
| | **centers** : __*boolean*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Whether or not to include center points for each Deltoid in the cluster. Default is False. |
| | **com** : __*boolean*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Whether or not to include the centroid of the cluster. Default is False. |
| | **indices** : __*boolean*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Whether or not to include the indices of each Deltoid in the cluster. Default is False. |
| | **bounding** : __*boolean*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Whether or not to include the bounding circles used to find adjacent Deltoids. Default is False. |
| | **ioi** : __*int*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Index of interest in cluster to highlight. Default is -1. |
| | **ioi\_furthest\_point** : __*boolean*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Whether or not to include the furthest point for the Deltoid at the index of interest. Default is False. |
| | **furthest\_points** : __*boolean*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Whether or not to include the furthest point for each Deltoid in the cluster. Default is False. |
| | **furthest\_points\_method** : __*str*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Which method to use when finding furthest points. Default is 'com'. |
| | **axis** : __*matplotlib.pyplot.axis*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Which axis to plot the cluster on. Default is None. |
| | **nc\_weight** : __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The weight to pass to finding the furthest points. Default is 1.0. |
| **Returns:** | **None** : __*None*__ |
| | |
| **Raises:** | __*None*__ |
| | |

### mark\_radiators

**mark\_radiators**(*cluster,string*)

Creates a tag on each delta for which point to use when calculating radiative lengths. Use 'l' for left-most point, 'r' for right-most point, 'c' for the center point, 'o' if not applicable, and anything else to define a custom length.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **cluster** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The cluster of Deltoids. |
| **Parameters:** | **string** : __*str*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;A string using the tags above without spaces. |
| **Returns:** | **None** : __*None*__ |
| | |
| **Raises:** | __*None*__ |
| | |

### radiative\_length

**radiative\_length**(*cluster,delta*)

Returns the radiative length of the Deltoid at the index specified.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **cluster** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The cluster of Deltoids. |
| | **delta** : __*int*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The index of the Deltoid to evaluate. |
| **Returns:** | **float** : __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The radiative length of the Deltoid specified. |
| **Raises:** | __*None*__ |
| | |

### get\_longest\_chain

**get\_longest\_chain**(*seed,modulize=True*)

Find the longest chain given an index to begin at.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **seed** : __*int*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The index to begin at. |
| | **modulize** : __*boolean*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Whether or not to break at module joints. Default is True. |
| **Returns:** | **chain** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Returns an array of the longest chain found. |
| **Raises:** | __*None*__ |
| | |

### get_deltan_distances

**get_deltan_distances**(*p1,p2*)

Returns the distance between two points in the Deltan coordinate system.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **p1,p2** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The coordinate points of the two points. |
| **Returns:** | **list** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Returns the x- and y-distance between the two points in the Deltan coordinate system. |
| **Raises:** | __*None*__ |
| | |
