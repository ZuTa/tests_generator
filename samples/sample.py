import os, sys

from random import randint
from itertools import chain

# Add path to generator package to be able to import necessary modules
path_to_package = os.path.realpath('../generator')
if path_to_package not in sys.path:
    sys.path.append(path_to_package)

from basegenerator import BaseTestsGenerator
from basegenerator import Lang

class SampleTestsGenerator(BaseTestsGenerator):

    def generate_easy_inputs(self):
        for i in xrange(10):
            yield '{} {}\n'.format(randint(-10, 10), randint(-10, 10))

    def generate_hard_inputs(self):
        for i in xrange(10):
            yield '{} {}\n'.format(randint(-sys.maxint, sys.maxint), randint(-sys.maxint, sys.maxint))

    def generate_inputs(self):
        easy = self.generate_easy_inputs()

        hard = self.generate_hard_inputs()

        return chain(easy, hard)

py_generator = SampleTestsGenerator(
    Lang.Python,
    'author_solution.py',
    test_name_format = 'test{0:03}',
    input_path = 'Tests/',
    output_path = 'Tests/',
    input_ext = '.in',
    output_ext = '.out')

py_generator.generate()

