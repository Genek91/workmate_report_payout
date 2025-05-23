def report_payout(employees: list[dict]) -> str:
    result = ["name, department, hours, rate, payout"]

    departments_data = {}
    for employee in employees:
        if employee["department"] in departments_data:
            departments_data[employee["department"]].append(employee)
        else:
            departments_data[employee["department"]] = [employee]

    for departament in departments_data:
        total_hours = 0
        for employee in departments_data[departament]:
            payout = employee["hours"] * employee["rate"]
            result.append(
                f'{employee["name"]}, {employee["department"]}, {employee["hours"]}, {employee["rate"]}, ${payout}'
            )
            total_hours += employee["hours"]

        result.append(f"total_hours: {total_hours}")

    return "\n".join(result)


def generate_report(report_name: str, employees: list[dict]) -> str:
    reports = {
        "payout": report_payout,
    }
    if report_name not in reports:
        raise ValueError(f"Неизвестный тип отчёта: {report_name}")

    return reports[report_name](employees)
