from abc import ABCMeta, abstractmethod

from runners.csharprunner import CSharpRunner
from runners.pythonrunner import PythonRunner

class Lang:
    Python, CSharp = xrange(2)

class BaseTestGenerator(object):
    """Base class for test generators"""
    __metaclass__ = ABCMeta

    def __init__(
        self,
        lang,
        author_solution,
        test_name_format = '{0:03}',
        input_path = '',
        output_path = '',
        input_ext = '.dat',
        output_ext = '.ans'):
        """
        Constructor. Creates an instance of base test generator class
        Parameters: TODO
        """
        self.lang = lang
        self.author_solution = author_solution
        self.test_name_format = test_name_format
        self.input_path = input_path
        self.output_path = output_path
        self.input_ext = input_ext
        self.output_ext = output_ext

        self.tests_count = 0
        self.runner = self.create_runner(lang)

    @abstractmethod
    def generate_inputs(self):
        pass

    def create_runner(self, lang):
        return {
            0 : PythonRunner(),
            1 : CSharpRunner()
        }[lang]

    def create_test_name(self):
        self.tests_count += 1

        return self.test_name_format.format(self.tests_count)

    def create_input_test_name(self, test_name): return test_name + self.input_ext

    def create_output_test_name(self, test_name): return test_name + self.output_ext

    def writeto(self, path, content):
        f = open(path, 'w')

        f.write(content)

        f.close()

    def run_author_solution(self, input_file):
        return self.runner.run(self.author_solution, input_file)

    def generate(self):
        """
        Generates input and output tests
        """
        for content in self.generate_inputs():
            test_name = self.create_test_name()

            input_test_path = self.input_path + self.create_input_test_name(test_name)
            output_test_path = self.output_path + self.create_output_test_name(test_name)

            self.writeto(input_test_path, content)

            result = self.run_author_solution(input_test_path)

            self.writeto(output_test_path, result)
