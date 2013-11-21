Tests Generator
===============

This is a python package which consists of basic classes for generating tests for ACM-like problems.

Usage:

	1. Create new class and inherit from BaseTestGenerator class.
	2. Implement abstract method - generate_inputs(). This method should create input tests and 
       yield them to the caller (python generator).
	3. Create an object of your test generator class.
	4. On created object call generate() method.


