import pytest
import pathlib
import iniconfig

from src.data_processing.data_processing import *

custom_ini = iniconfig.IniConfig('report_generator.ini')
valid_report_types = custom_ini.get('valid_report_types', 
                                    'valid_report_types', 
                                    [], 
                                    lambda x: x.split("\n"))

@pytest.fixture
def processor_with_parser_only():
    parser = ArgumentParser(allow_abbrev=False)
    processor = ArgumentProcessor.__new__(ArgumentProcessor)
    processor.parser = parser
    return processor

@pytest.fixture
def setup_test_args(monkeypatch : pytest.MonkeyPatch):
    def _setup(args_list : list[str]):
        monkeypatch.setattr('sys.argv', args_list)
    return _setup

@pytest.fixture
def temp_files(tmp_path : pathlib.Path, 
               monkeypatch : pytest.MonkeyPatch):
    def _temp_files(files : list[str]):
        temp_dir = tmp_path / 'test_dir'
        temp_dir.mkdir()
        monkeypatch.chdir(temp_dir)
        
        for file in files:
            (temp_dir / file).write_text('test')
        
        return temp_dir
    
    return _temp_files

@pytest.fixture
def valid_args():
    valid_args = ['data_processing.py', 
                  '--files', 'test1.csv', 'test2.csv', 
                  '--report']
    valid_args.extend(valid_report_types)
    
    return valid_args

@pytest.fixture
def valid_files():
    return ['test1.csv', 'test2.csv']