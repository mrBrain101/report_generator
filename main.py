from data_loader import CSVLoader
from reports import Report


def main() -> None:
    loader = CSVLoader()
    employee_data = loader.load()
    performance_report = Report(employee_data)
    performance_report.perfomance()


if __name__ == '__main__':
    main()