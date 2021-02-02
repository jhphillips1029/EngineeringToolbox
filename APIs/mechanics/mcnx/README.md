# McnxSolver API

# Table of Contents
* [Dependencies](#dependencies)
* [principleStresses](#principlestresses)
* [stressInvariants](#stressinvariants)
* [octohedralStresses](#octohedralstresses)
* [partition](#partition)
* [quickSort](#quicksort)
* [generateMohrsCircle](#generagemohrscircle)
* [plotMohrsCircle](#plotmohrscircle)

### Dependencies

This module requires the following modules to be installed already:

* math
* matplotlib
* numpy

### principleStresses

**principleStresses(**_stressTensor,method='eigen'_**)**

Determines the principle stresses given a 3x3 tensor describing the state of stress.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **stressTensor** : __*array_like*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Input arrays describing state of stress. |
| | **method** | __*string, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The method with which to determine principle stresses. Default is the eigenvalue approach.
| **Returns:** | **principle_stresses** : __*ndarray*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The principle stresses. |
| **Raises:** | __*None*__ |

### stressInvariants

**stressInvariants(**_stressTensor_**)**

Determines the stress invariants given a 3x3 tensor describing the state of stress.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **stressTensor** : __*array_like*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Input arrays describing state of stress. |
| **Returns:** | **I** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;List of the stress invariants, in order. |
| **Raises:** | __*None*__ |

### octohedralStresses

**octohedralStresses(**_stressTensor_**)**

Determines the octohedral stresses given a 3x3 tensor describing the state of stress.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **stressTensor** : __*array_like*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Input arrays describing state of stress. |
| **Returns:** | **<list>** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;A list containing the octohedral normal stress and octohedral shear stress. |
| **Raises:** | __*None*__ |

### partition

**partition(**_arr, low, high_**)**

Helper function used in quickSort().

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **arr** : __*array_like*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The array to be partitioned. |
| | **low** | __*integer*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The lower index of the portion of the array to be partitioned. |
| | **high** | __*integer*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The higher index of the portion of the array to be partitioned. |
| **Returns:** | **i** : __*integer*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;New index for next partition. |
| **Raises:** | __*None*__ |

### quickSort

**quickSort(**_arr, low, high_**)**

Uses the quick sort algorithm to sort an array of objects.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **arr** : __*array_like*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The array to be sorted. |
| | **low** | __*integer*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The lower index of the portion of the array to be sorted. |
| | **high** | __*integer*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The higher index of the portion of the array to be sorted. |
| **Returns:** | **None** : __*None*__ |
| **Raises:** | __*None*__ |

### generateMohrsCircle

**generateMohrsCircle(**_stressTensor,filename=None,thetaCutPlane=None,show=[0]_**)**

Determines the quantities necessary to plot a Mohr's Circle.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **stressTensor** : __*array_like*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Input arrays describing state of stress. |
| | **filename** | __*string, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;What to name the output file. If 'None', no image will be generated. Default is 'None'. |
| | **thetaCutPlane** | __*float, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Angle at which to determine stresses on cut plane. |
| | **show** | __*list, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;List of images to generate. Default is Mohr's Circle only. |
| **Returns:** | **meDict** : __*dictionary*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Dictionary containing values necessary for plotting Mohr's Circle. |
| **Raises:** | __*None*__ |

### plotMohrsCircle

**plotMohrsCircle(**_filename,sigmaXX,sigmaYY,tauXy,center,radius,sigmaP1,sigmaP2,thetaP1,phi=None,alpha=None,sigma1=None,sigma2=None,tau1=None,thetaCutPlane=None,show=[0],units='MPa'_**)**

Helper function to plot a Mohr's Circle.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **filename** : __*string*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Name of output file. |
| | **sigmaXX** | __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The normal stress acting in the x-direction. |
| | **sigmaYY** | __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The normal stress acting in the y-direction. |
| | **tauXy** | __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The shear stress acting on the x-face in the y-direction. |
| | **center** | __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The center of Mohr's Circle. |
| | **radius** | __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The radius of Mohr's Circle. |
| | **sigmaP1** | __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The first principle stress. |
| | **sigmaP2** | __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The second principle stress. |
| | **thetaP1** | __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The first principle angle. |
| | **phi** | __*float, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Angle necessary for maximum in-plane stress for cut-plane. Default is None. |
| | **alpha** | __*float, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Adjusted angle for cut-plane. Default is None. |
| | **sigma1** | __*float, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;First stress in cut-plane. Default is None. |
| | **sigma2** | __*float, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Second stress in cut-plane. Default is None. |
| | **tau1** | __*float, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Shear stress in cut-plane. Default is None. |
| | **thetaCutPlane** | __*float, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Angle at which to apply cut-plane analysis. Default is None. |
| | **show** | __*list, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Which images to generate. Default is [0]. |
| | **units** | __*string, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Which units to label in images generated. Default is 'MPa'. |
| **Returns:** | **None** : __*None*__ |
| **Raises:** | __*None*__ |

