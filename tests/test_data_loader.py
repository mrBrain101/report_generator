import pytest


class TestArgumentProcessor:
    @pytest.mark.parametrize('files', [['test.csv'], ['test.csv', 'test2.csv']])
    def test_arguments_parser(self, files, report):
        assert True