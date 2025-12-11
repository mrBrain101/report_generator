from src.data_processing.data_processing import CSVLoader
from src.reports.reports import Report


def main() -> None:
    loader = CSVLoader()
    employee_data, report_types = loader.load()
    reports = Report(employee_data, report_types)
    reports()

if __name__ == '__main__':
    main()