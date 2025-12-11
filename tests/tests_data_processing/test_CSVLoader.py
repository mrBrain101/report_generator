import pytest

from src.data_processing.data_processing import CSVLoader


class TestCSVLoader:
    def test_user_provided_the_files_with_invalid_extension(self, 
                                                            setup_test_args,
                                                            monkeypatch,
                                                            tmp_path):
        invalid_extension = ['data_processing.py', 
                             '--files', 'test1.txt', 'test2.txt', 
                             '--report', 'performance']
        setup_test_args(invalid_extension)
        temp_dir = tmp_path / 'test_dir'
        temp_dir.mkdir()  
        monkeypatch.chdir(temp_dir)

        for file in ['test1.txt', 'test2.txt']: 
            (temp_dir / file).write_text('test')
        
        with pytest.raises(ValueError, 
                           match=('File "test1.txt" is not a CSV file. '
                                  'Check the file extension')):
            loader = CSVLoader()
            loader.load()

    def test_user_provided_the_files_with_valid_extension_and_data(
            self, 
            monkeypatch : pytest.MonkeyPatch, 
            tmp_path, 
            setup_test_args, 
            valid_args
            ):
        temp_dir = tmp_path / 'test_dir'
        temp_dir.mkdir()  
        monkeypatch.chdir(temp_dir)
        for file in ['test1.csv', 'test2.csv']: 
            (temp_dir / file).write_text(
                'name, position, completed_tasks, performance, skills, team, '
                'experience_years\nAlbert, Frontend, 1, 4.5, Python, Mobile, 3\n'
                )

        setup_test_args(valid_args)

        loader = CSVLoader()
        employee_data = loader.load()

        assert len(employee_data) == 2