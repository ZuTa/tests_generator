Tests Generator
===============

This is a python package which consists of a basic classes for generating tests for ACM-like problems.

Sample
------
Working example located at sample/ folder. To run an example - you have to:

	1. Create a folder with name 'Tests' next to the sample.py (because sample uses its as 
	   destination for in/out tests)
	2. Run script sample.py. (use may command like this one: python sample.py)
	3. Look into Tests/ folder to enjoy the result

The sample consists of two differen author's solutions (written on C# and Python) to 
famous two-sum problem (add two numbers). sample.py demonstrate two usages - one using
C# source as author's solution and the other one - Python.

Languages
---------

Supported languages:

	- Python
	- C#

To add support for another language - you have to:

	1. Create new class inherited from BaseRunner class.
	2. Implement abstract method - create_run_command(). This method should return shell 
	   command to compile and run author's solution with specified input test. 

Usage
-----
To generate test set for your own problem(s) - you have to:

	1. Create new class inherited from BaseTestGenerator class. (look at the provided sample for more details)
	2. Implement abstract method - generate_inputs(). This method should create input tests and 
	   yield them to the caller (python generator).
	3. Create an object of your test generator class.
	4. Call generate() method on created object.
