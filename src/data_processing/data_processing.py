from argparse import ArgumentParser, Namespace
from os import path
import csv

from .data_model import EmployeeData


class ArgumentProcessor:
    def __init__(self, 
                 parser : ArgumentParser) -> None:
        self.parser = parser
        self.arguments = self._arguments_parser()
        self._arguments_files_checker()

    def _arguments_parser(self) -> Namespace:
        self.parser.add_argument('--files', nargs='+', 
                                 required=True)
        self.parser.add_argument('--report', nargs='+', 
                                 required=True)
        self.arguments = self.parser.parse_args()

        return self.arguments
    
    def _arguments_files_checker(self) -> None:
        for i, file in enumerate(self.arguments.files):
            if not path.exists(self.arguments.files[i]):
                raise FileNotFoundError(
                    f'File "{self.arguments.files[i]}" does not exist'
                    )
                

class CSVLoader(ArgumentProcessor):
    def __init__(self) -> None:
        super().__init__(parser = ArgumentParser(allow_abbrev=False))
    
    def load(self) -> tuple[list[EmployeeData], list[str]]:
        employee_data : list[EmployeeData] = []
        for file in self.arguments.files:
            if not file.endswith('.csv'):
                raise ValueError(f'File "{file}" is not a CSV file. '
                                 'Check the file extension')
            with open(file, encoding='utf-8', newline='') as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    employee_data.append(EmployeeData(*row)) # type: ignore[arg-type]

        return employee_data, self.arguments.report