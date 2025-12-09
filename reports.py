from itertools import groupby
from statistics import mean
from tabulate import tabulate

from data_model import EmployeeData


class Report:
    def __init__(self, employee_data : list[EmployeeData]) -> None:
        self.employee_data = employee_data

    def perfomance(self) -> None:
        data = [{'position': x.position, 'performance': x.performance} 
                for x in self.employee_data]
        sorted_data = sorted(data, key=lambda x: x['position'])

        res : list = []
        for position, group in groupby(sorted_data,
                                       key=lambda x: x['position']):
            mean_performance = mean(x['performance'] for x in group)
            res.append([position, mean_performance])

        res = sorted(res, key=lambda x: x[1], reverse=True)
        print(tabulate(res, headers=['Position', 'Performance'],
                       showindex=range(1, len(res)+1), floatfmt='.2f'))