from baserunner import BaseRunner


class CSharpRunner(BaseRunner):
    def create_run_command(self, path_to_source, path_to_input_file):
        execution_file = path_to_source[:path_to_source.rfind('.')] + '.exe'

        return '\"mcs -warn:0 {} && mono {} < {}\"'.format(path_to_source, execution_file, path_to_input_file)
