from abc import ABCMeta, abstractmethod
import subprocess

class BaseRunner(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_run_command(self, path_to_source, path_to_input_file):
        pass

    def run(self, path_to_source, path_to_input_file):
        command = self.create_run_command(path_to_source, path_to_input_file)

        proc = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True, stderr=subprocess.STDOUT)

        return proc.stdout.read()
