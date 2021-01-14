# materialAnalyzer API (V1)

# Table of Contents
* [Dependencies](#dependencies)
* [initData](#initdata)
* [addMaterial](#addmaterial)
* [area](#area)
* [findUTS](#finduts)
* [getYoungsModulus](#getyoungsmodulus)
* [findElasticModulus](#findelasticmodulus)
* [getFailure](#getfailure)
* [findFailure](#findfailure)
* [findPlasticElasticFailureStrain](#findplasticelasticfailurestrain)
* [getYieldStress](#getyieldstress)
* [findYieldStress](#findyieldstress)
* [writeOut](#writeout)
* [plotData](#plotdata)

### Dependencies

This module requires the following modules to be installed already:

* math
* matplotlib
* numpy
* pandas
* warnings

### initData

**initData(**_csvName_**)**

Read in data from file.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **csvName** : __*string*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Name of .csv file containing lab data. |
| **Returns:** | **None** : __*None*__ |
| **Raises:** | __*None*__ |

### addMaterial

**addMaterial(**_matInfo_**)**

Define new material.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **matInfo** : __*dictionary*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Dictionary defining new material. |
| **Returns:** | **None** : __*None*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Returns if number of keys in matInfo and matData do not match. |
| **Raises:** | __*None*__ |

### area

**area(**_diameter_**)**

Calculates circular area.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **diameter** : __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Diameter. |
| **Returns:** | **float** : __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Circular area. |
| **Raises:** | __*None*__ |

### findUTS

**findUTS(**_key_**)**

Returns the ultimate tensile strength of specific material.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **key** : __*string*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Key to select material. |
| **Returns:** | **float** : __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Maximum stress in data. |
| **Raises:** | __*None*__ |

### getYoungsModulus

**getYoungsModulus(**_stress,strain,plot=False_**)**

Find Young's Modulus from stress/strain data.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **stress,strain** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Lists of data for stress and strain. |
| | **plot** : __*boolean, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Determines whether or not to plot results. Default is False. |
| **Returns:** | **m_best** : __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Slope of best fit representing the Young's Modulus. |
| **Raises:** | __*None*__ |

### findElasticModulus

**findElasticModulus(**_stressKey,strainKey_**)**

Wrapper for findYoungsModulus.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **stressKey,strainKey** : __*string*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The keys for the stress and strain data. |
| **Returns:** | **float** : __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Returns the result of findYoungsModulus. |
| **Raises:** | __*None*__ |

### getFailure

**getFailure(**_stress_**)**

Determine failure from stress data.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **stress** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The stress data. |
| **Returns:** | **integer** : __*integer*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Index of failure in stress data. |
| **Raises:** | __*None*__ |

### findFailure

**findFailure(**_stressKey,strainKey_**)**

Wrapper for getFailure.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **stressKey, strainKey** : __*string*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The keys for the stress and strain data.  |
| **Returns:** | **float** : __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The value in the stress data indicated by the index returned by getFailure. |
| **Raises:** | __*None*__ |

### findPlasticElasticFailureStrain

**findPlasticElasticFailureStrain(**_stressKey,strainKey,elasticModulus,totFailStrain_**)**

Find the point of plastic-elastic failure.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **stressKey, strainKey** : __*string*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The keys for the stress and strain data. |
| | **elasticModulus** : __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The material's Young's Modulus. |
| | **totFailStrain** : __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Total strain at failure. |
| **Returns:** | **list** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;List of failStress/E and totFailStrain-failStress/E, where E is the Young's Modulus. |
| **Raises:** | __*None*__ |

### getYieldStress

**getYieldStress(**_strain, stress, offset, E_**)**

Determine offset yield stress.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **strain, stress** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;List of stess and strain data. |
| | **offset** : __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Percent offset. |
| | **E** : __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Young's Modulus. |
| **Returns:** | **float** : __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Returns the offset yield stress. |
| **Raises:** | __*None*__ |

### findYieldStress

**findYieldStress(**_stressKey,strainKey,elasticModulus,offset=.002_**)**

Wrapper for getYieldStress.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **stressKey,strainKey** : __*string*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The keys for the stress and strain data. |
| | **elasticModulus** : __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The Young's Modulus. |
| | **offset** : __*float, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Offset value to find offset yield stress. Default is .002. |
| **Returns:** | **float** : __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Returns the result of getYieldStress(). |
| **Raises:** | __**__ |

### writeOut

**writeOut(**_fname_**)**

Output data to file.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **fname** : __*string*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Name of file to output data to. |
| **Returns:** | **None** : __*None*__ |
| **Raises:** | __*None*__ |

### plotData

**plotData(**_stressKeys,strainKeys,names,totalFailureStrain,fName=None_**)**

Plots data.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **stressKeys,strainKeys** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The keys for the stress and strain data. |
| | **names** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Names of the materials |
| | **totalFailureStrain** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;List of total strain at failure. |
| | **fname** : __*string, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Name of file to output plot to. Default is None. |
| **Returns:** | **None** : __*None*__ |
| **Raises:** | __*None*__ |

