from itertools import groupby
from statistics import mean
from tabulate import tabulate

from src.data_processing.data_model import EmployeeData


class Report:
    def __init__(self, 
                 employee_data : list[EmployeeData], 
                 report_types : list[str]) -> None:
        self.employee_data = employee_data
        self.report_types = report_types
        self._arguments_report_checker(self.report_types)

    def _arguments_report_checker(self, report_types : list[str]) -> None:
        for report in report_types:
            if not hasattr(self, report):
                raise ValueError(f'No such report "{report}"')
            
    def __call__(self) -> None:
        for report in self.report_types:
            method = getattr(self, report)
            method()

    def performance(self):
        data = [{'position': x.position, 'performance': x.performance} 
                for x in self.employee_data]
        sorted_data = sorted(data, key=lambda x: x['position'])

        performance_report : list = []
        for position, group in groupby(sorted_data,
                                       key=lambda x: x['position']):
            mean_performance = mean(x['performance'] for x in group)
            performance_report.append([position, mean_performance])

        performance_report = sorted(performance_report, 
                                    key=lambda x: x[1], 
                                    reverse=True)
        print(tabulate(performance_report, 
                       headers=['Position', 'Performance'],
                       showindex=range(1, len(performance_report)+1), 
                       floatfmt='.2f'))

        return performance_report