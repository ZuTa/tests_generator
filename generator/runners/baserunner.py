from abc import ABCMeta, abstractmethod
import subprocess
import shlex

class BaseRunner(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_run_command(self, path_to_source, path_to_input_file):
        pass

    def prepare_path(self, path):
         return path.replace(' ','\ ')

    def run(self, path_to_source, path_to_input_file):
        prepared_path_to_input_file = self.prepare_path(path_to_input_file)
        prepared_path_to_source = self.prepare_path(path_to_source)

        command = self.create_run_command(prepared_path_to_source, prepared_path_to_input_file)

        proc = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True, stderr=subprocess.STDOUT)

        return proc.stdout.read()
