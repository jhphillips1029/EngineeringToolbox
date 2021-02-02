# ThermoSolver API

[Back](../../README.md)

# Table of Contents
* [Dependencies](#dependencies)
* [getState](#getState)

### Dependencies

This module requires the following modules to be installed already:

* json
* pandas
* numpy

### getState

**getState(**_temp=None,press=None,fluid="water",state="SLSV",tables="Wiley",preferTemp=False,debug=False,generic=False,Sat=-1.0e-5,qual=1.0_**)

Gets a state for a fluid and interpolates if necessary.

|                 |                                     |
|-----------------|-------------------------------------|
| **Parameters:** | **temp** : __*float, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp; Temperature. Default is None. |
| | **press** : __*float, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Pressure. Default is None. |
| | **fluid** : __*string, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Working fluid. Default is 'water'. |
| | **state** : __*string, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Physical state of matter. Default is 'SLSV'. |
| | **tables** : __*string, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Which tables to use. Default is 'Wiley'. |
| | **preferTemp** : __*boolean, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Prefer use of temperature tables of pressure tables for SLSV states. Default is False. |
| | **debug** : __*boolean, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Debugging. Default is False. |
| | **generic** : __*boolean, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Provide generic state data. Default is False. |
| | **Sat** : __*float, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Value for 'Sat.' in data. Default is -1.0e-5. |
| | **qual** : __*float, optional*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Quality of SLSV state. Default is 1.0. |
| **Returns:** | **rtn** : __*DataFrame*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Returns a DataFrame describing the state of the fluid. |
| **Raises:** | __*ValueError*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Raises a ValueError if neither temperature or pressure are defined. |
| | __*ValueError*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Raises a ValueError if state is not one of 'SLSV', 'SHV', or 'CL' |
| | __*ValueError*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Raises a ValueError if state not 'SLSV' and either temp or press are None. |
| | __*ValueError*__ |
| | &nbsp;&nbsp;&nbsp;&nbsp;Raises a ValueError is attempting to interpolate with the default value for Sat. |
