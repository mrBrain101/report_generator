import pytest
from src.reports.reports import *


class TestReport:
    def test_make_performance_report(self):
        data = [('Albert', 'Frontend', '1', '1', 'Python', 'Mobile', '3'),
                ('Albert', 'Frontend', '1', '5', 'Python', 'Mobile', '3')]
        employee_data : list[EmployeeData] = (
            [EmployeeData(*row) for row in data]# type: ignore[arg-type]
            )               
        report = Report(employee_data, ['performance'])
        report()

        assert report.performance() == [['Frontend', 3]]

    def test_user_provided_nonexistant_report_type(self):
        with pytest.raises(ValueError, match='No such report "nonexistent"'):
            report = Report([], ['nonexistent'])
