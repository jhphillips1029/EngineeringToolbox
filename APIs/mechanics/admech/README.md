# AdMech API

[Back](../../README.md)

### Table of Contents
* [Dependencies](#dependencies)
* [tensorToVector](#tensortovector)
* [vectorToTensor](#vectortotensor)
* [getC](#getc)
* [getS](#gets)

### Dependencies

This module requires the following modules to be installed already:

* numpy

### tensorToVector

**tensorToVector**(*tensor*)

Transforms 3x3 tensor into 1x6 vector and returns it.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **tensor** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The tensor to transform. |
| **Returns:** | **vec** : __*ndarray*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The returned vector. |
| **Raises:** | __*None*__ |
| | |

### vectorToTensor

**vectorToTensor**(*vec*)

Transforms 1x6 vector into 3x3 tensor and returns it.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **vec** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The vector to transform. |
| **Returns:** | **tens** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The returned tensor. |
| **Raises:** | __*None*__ |
| | |

### getC

**getC**(*E,nu*)

Calculates the compliance matrix and returns it.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **E,nu** : __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The Young's Modulus and Poisson's Ratio, respectively. |
| **Returns:** | **C** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The compliance matrix. |
| **Raises:** | __*None*__ |
| | |

### getS

**getS**(*E,nu*)

Calculates the strength matrix and returns it.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **E,nu** : __*float*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The Young's Modulus and Poisson's Ratio, respectively. |
| **Returns:** | **S** : __*list*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;The strength matrix. |
| **Raises:** | __*None*__ |
| | |
