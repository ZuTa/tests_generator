from abc import ABCMeta, abstractmethod

from runners.csharprunner import CSharpRunner
from runners.pythonrunner import PythonRunner

class Lang:
    '''Represents enumeration of supported languages/compilers'''
    Python, CSharp = xrange(2)

class BaseTestsGenerator(object):
    '''Base class for test generators'''

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
        '''Creates an instance of base test generator class

        Parameters
        ----------
        lang : int
                language identifier of author's solution (0 = Lang.Python, 1 = Lang.CSharp, etc.)
        author_solution : string
                path to the author's source file

        test_name_format : string
                [optional] string format for the names of tests.
        input_path : string
                [optional] path to the location of input tests (where to store input tests).
                By default, input path is current folder.
        output_path : string
                [optional] path to the location of output files (where to store results for correspond input tests).
                By default, output path is current folder.
        input_ext : string
                [optional] an extension for the input file's names. This parameter have to start with dot('.')
                By default, '.dat'
        output_ext : string
                [optional] an extension for the output file's names. This parameter have to start with dot('.')
                By default, '.ans'
        '''
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
        '''An abstract method(generator) which yields an input tests.

        Parameters
        ----------

        Returns
        -------
        iterator
                returns iterator over generated sequence of input tests
        '''
        pass

    def create_runner(self, lang):
        '''Creates a runner by specified language

        Parameters
        ----------
        lang : int
                language identifier of author's solution (0 = Lang.Python, 1 = Lang.CSharp, etc.)

        Returns
        -------
        object of correspond runner defined via specified language's identifier
        '''
        return {
            0 : PythonRunner(),
            1 : CSharpRunner()
        }[lang]

    def create_test_name(self):
        '''Creates test name using the special format

        Parameters
        ----------

        Returns
        -------
        string - formatted test name
        '''
        self.tests_count += 1

        return self.test_name_format.format(self.tests_count)

    def create_input_test_name(self, test_name): return test_name + self.input_ext

    def create_output_test_name(self, test_name): return test_name + self.output_ext

    def writeto(self, path, content):
        '''Writes a content to the specified file

        Parameters
        ----------
        path : string
                path to the file
        content : string
                desired content to write to the file

        Returns
        -------
        '''

        f = open(path, 'w')

        f.write(content)

        f.close()

    def run_author_solution(self, input_file):
        '''Runs an author's solution on specified input

        Parameters
        ----------
        input_file : string
                path to the input file

        Returns
        -------
        string - result of author's solution to the specified input
        '''
        return self.runner.run(self.author_solution, input_file)

    def generate(self):
        '''Generates and stores input/output tests'''
        for content in self.generate_inputs():
            test_name = self.create_test_name()

            input_test_path = self.input_path + self.create_input_test_name(test_name)
            output_test_path = self.output_path + self.create_output_test_name(test_name)

            self.writeto(input_test_path, content)

            result = self.run_author_solution(input_test_path)

            self.writeto(output_test_path, result)
