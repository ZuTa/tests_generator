from baserunner import BaseRunner

class PythonRunner(BaseRunner):
    def create_run_command(self, path_to_source, path_to_input_file):
        return 'python {} < {}'.format(path_to_source, path_to_input_file)
