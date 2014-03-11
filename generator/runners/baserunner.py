from abc import ABCMeta, abstractmethod
import subprocess
import shlex


class BaseRunner(object):
    """Represents a base class for runners of specific language"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def create_run_command(self, path_to_source, path_to_input_file):
        """An abstract method to create a specific run & compile shell command

        Parameters
        ----------
        path_to_source : string
                path to the source file
        path_to_input_file : string
                path to the input file

        Returns
        -------
        string - shell command to compile(and then execute) specified source file
        """
        pass

    @staticmethod
    def prepare_path(path):
        return path.replace(' ', '\ ')

    def run(self, path_to_source, path_to_input_file):
        """Compliles and then runs specified source file with correspond input file
        Parameters
        ----------
        path_to_source : string
                path to the source file
        path_to_input_file : string
                path to the input file

        Returns
        -------
        string - the result of execution
        """
        prepared_path_to_input_file = self.prepare_path(path_to_input_file)
        prepared_path_to_source = self.prepare_path(path_to_source)

        command = self.create_run_command(prepared_path_to_source, prepared_path_to_input_file)

        process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, shell=True)

        return process.stdout.read()