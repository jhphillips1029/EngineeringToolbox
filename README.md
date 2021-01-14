# EngineeringToolbox

## Table of Contents
* [Overview](#overview)
	* [Updates](#updates)
	* [History](#history)
	* [Courses Covered](#courses-covered)
* [Using the Code](#using-the-code)
	* [Learning Python](#learning-python)
	* [Downloading](#downloading)
		* [Python](#python)
		* [Anaconda](#anaconda)
		* [This Repository](#this-repository)
	* [Importing a Module](#importing-a-module)
	
## Overview

This is a collection of code I have put together in my spare time. It oringinates from coursework completed in the Mechanical Engineering program at Montana State University. I have made this code available for anyone it may help; however, I do not condone cheating or any practices that might violate MSU's Student Code of Conduct or similar documents at other universities or institutes of higher learning. Basically, just don't cheat. Be a good engineer.

#### Updates

At this time, there are no new updates. This is a brand new repository. Explanations of updates will be posted here.

#### History

The code contained here was written to help me complete assignments in the ME program at MSU. It began with the realization that most of the problems in EGEN201 (Statics) were fairly repetitive and should be easily codable. I ended up going overboard and devoting a substantial amount of time to writing a function that would solve for reaction forces for any statically determinate system.

This helped me see problems in other classes that could be simplified with complex-ish code. Why do something for 6 minutes if you could automate it in 6 hours? You only need 10 repetitions to break even. I proceeded to create "solvers" for common problems for several other classes and continued to do so the next semester.

The original repository, having originated from the engineering mechanics series was named engineeringMechanics, and has since been moved to private and replaced by this repository with better file architecture and an attempt at better layman-style explanations of the code.

#### Courses Covered

As stated before, I do not condone cheating or any other practice that would violate MSU's Student Code of Conduct or any other similar documents. The code is meant as something to either check your work, in which case, I do not take responsibility for any errors that may occur leading to incorrect or conflicting answers that lead to missed points. Additionally, the code is available to simplify work in higher level classes and as an option to see a very generalized way to approach a problem.

| Course  |  Name | Description of Code|
|---------|-------|--------------------|
| EGEN201 | Statics | Solving statically determinate setups, trusses, and shear-moment diagrams |
| EMEC250 | Materials Lab | Basic identification of linear portion of the stress strain curve |
| EELE250 | Circuits | Generates LaTex Circuit diagrams |
| EMEC341 | Adv. Mechanics | I honestly don't remember as of this writing |
| EMEC320 | Thermo I | Wiley data tables and automatic interpolation when pulling data from tables |
| EGEN350 | Appl Data Analysis | Generalized probability function |

## Using the Code

If you already know basic Python, you should be more or less ready to go; however, if you are still pretty green and don't even know/understand the basics of programming as (hopefully) taught in EMEC203, I have linked some Python tutorials below.

If you have already taken EMEC203, 

#### Learning Python

You don't necessarily need to be an expert in Python to be able to use this code, so here are some jumping off points. If you have absolutely no experience, I would recommend checking out the w3schools tutorial. If you have experience with MATLAB, I would recommend checking out the MATLAB to Python Primer.

1. [w3schools Tutorial](https://www.w3schools.com/python/)
	* w3schools is generally where I go to touch up on my syntax if I've been away from Python for a while. The layout is very user-friendly and includes several interactive examples on the site itself.

2. [MATLAB to Python Primer](https://bastibe.de/2013-01-20-a-python-primer-for-matlab-users.html)
	* One of the simplest explanations for the differences between MATLAB and Python that I've found. Provides side-by-side examples of MATLAB code and its Python equivalent.
	
3. [Official Python Tutorial](https://docs.python.org/3/tutorial/)
	* The official Python tutorial. Not as aesthetically pleasing as w3schools, but it is the official source

4. [TutorialsPoint For Python](https://www.tutorialspoint.com/python/index.htm)
	* Another source I generally use for checking syntax and such.

#### Downloading

Here are instructions on downloading Python, Anaconda, and this repository. Obviously, you need Python to run the Python code, so that's a very important part of this. This comes with it's own IDE named IDLE. This is a decent way to start, but I vastly prefer Anaconda over IDLE. Anaconda runs in your browser and provides a superior (in my opinion) user experience. Of course, it is up to you. And obviously, you'll want to download this repository if you want to use it.

###### Python

[Python](https://www.python.org/downloads/)
Here is the download link for Python from the official website. Follow the instructions there for a successful download.

###### Anaconda

[Anaconda](https://www.anaconda.com/products/individual)
Here is the download link for Anaconda from their website. Follow the instructions there for a successful download.
*One note of importance: Anaconda will override the default Python libraries, so installing libraries with Anaconda is different than vanilla Python. Just search Google for 'conda install [package name]' for the install commands.*

###### This Repository

If you scroll back up to the top of the page, you will see a prominent green button labeled 'Code'. Click it, and on the drop down, choose 'Download Zip'. Download this to your workspace folder and unzip it.

#### Importing a Module

To import one of the modules, simply make sure it is in the same folder as the code you are importing it into.
