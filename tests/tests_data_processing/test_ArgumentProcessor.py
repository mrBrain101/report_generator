from typing import Callable
import pytest
from src.data_processing.data_processing import *
from src.reports.reports import Report


class TestArgumentProcessor:
    def test_user_provided_valid_CLI_options_to_arguments_parser(
            self, 
            processor_with_parser_only : ArgumentProcessor, 
            setup_test_args : Callable, 
            valid_args : list[str], 
            valid_files : list[str]
            ):
        setup_test_args(valid_args)
        result = processor_with_parser_only._arguments_parser()
        
        assert result.files == valid_files
        for report_type in result.report:
            assert hasattr(Report, report_type)

    def test_user_provided_invalid_CLI_options_to_arguments_parser(
            self, 
            processor_with_parser_only : ArgumentProcessor, 
            setup_test_args : Callable
            ):
        setup_test_args(['data_processing.py', '--fil', '--rep'])
        
        with pytest.raises(SystemExit):
            processor_with_parser_only._arguments_parser()

    def test_user_provided_valid_files_to_arguments_files_checker(
            self, 
            setup_test_args : Callable, 
            valid_args : list[str], 
            temp_files : Callable, 
            valid_files : list[str]
            ):
        setup_test_args(valid_args)
        temp_files(valid_files)
        
        processor = ArgumentProcessor(ArgumentParser(allow_abbrev=False))
        assert processor._arguments_files_checker() is None

    def test_user_provided_nonexistent_files_to_arguments_files_checker(
            self, 
            setup_test_args : Callable
            ):
        nonexistant_files = ['data_processing.py', 
                             '--files', 'nonexistent1.csv', 'nonexistent2.csv', 
                             '--report', 'performance']
        setup_test_args(nonexistant_files)
        
        with pytest.raises(FileNotFoundError, 
                           match='File "nonexistent1.csv" does not exist'):
            processor = ArgumentProcessor(ArgumentParser(allow_abbrev=False))
            processor._arguments_files_checker()