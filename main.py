import argparse

from data_reader import read_employees
from reports import generate_report


def parse_args():
    parser = argparse.ArgumentParser(
        description="Скрипт подсчёта зарплаты сотрудников"
    )
    parser.add_argument("files", nargs="+")
    parser.add_argument("--report", required=True)
    return parser.parse_args()


def main():
    args = parse_args()

    employees = []
    for file_path in args.files:
        employees.extend(read_employees(file_path))

    output = generate_report(args.report, employees)
    print(output)


if __name__ == "__main__":
    main()
