from argparse import ArgumentParser, Namespace
from os import path
import csv

from data_model import EmployeeData


class ArgumentProcessor:
    def __init__(self, parser : ArgumentParser) -> None:
        self.parser = parser
        self.arguments = self._arguments_parser()
        self._argument_checker()

    def _arguments_parser(self) -> Namespace:
        self.parser.add_argument('--files', nargs='+', 
                                 required=True)
        self.parser.add_argument('--report', nargs='+', 
                                 required=True)
        self.arguments = self.parser.parse_args()

        return self.arguments
    
    def _argument_checker(self) -> None:
        for file in self.arguments.files:
            if not path.exists(file):
                raise FileNotFoundError(f'File "{file}" does not exist. '
                                        'Check the name and/or the path')
    

class CSVLoader(ArgumentProcessor):
    def __init__(self) -> None:
        super().__init__(ArgumentParser(allow_abbrev=False))
    
    def load(self) -> list[EmployeeData]:
        employee_data : list[EmployeeData] = []
        for file in self.arguments.files:
            with open(file, encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    employee_data.append(EmployeeData(*row)) # type: ignore[arg-type]

        return employee_data