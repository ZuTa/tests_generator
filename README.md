Tests Generator
===============

This is a python package which consists of basic classes for generating tests for ACM-like problems.

Supported languages:

	- Python
	- C#

To add support for another language - you have to:

	1. Create new class inherited from BaseRunner class.
	2. Implement abstract method - create_run_command(). This method should return shell 
	   command to compile and run author's solution with specified input test. 

Usage:

	1. Create new class inherited from BaseTestGenerator class.
	2. Implement abstract method - generate_inputs(). This method should create input tests and 
	   yield them to the caller (python generator).
	3. Create an object of your test generator class.
	4. On created object call generate() method.
