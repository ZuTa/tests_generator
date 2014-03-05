from baserunner import BaseRunner


class CPlusPlusRunner(BaseRunner):
    def create_run_command(self, path_to_source, path_to_input_file):
        execution_file_path = path_to_source[:path_to_source.find('.')]

        prefix_for_execution_file = './' if execution_file_path.count('/') == 0 else ''

        return '\"g++ {} -o {} && {}{} < {}\"'.format(
            path_to_source, execution_file_path, prefix_for_execution_file, execution_file_path, path_to_input_file)