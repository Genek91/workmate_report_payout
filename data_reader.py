def read_employees(file_path: str) -> list[dict]:
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    if not lines:
        return []

    header = lines[0].split(",")
    rows = [line.split(",") for line in lines[1:]]

    try:
        idx_id = header.index("id")
        idx_email = header.index("email")
        idx_name = header.index("name")
        idx_department = header.index("department")
        idx_hours = header.index("hours_worked")
    except ValueError as e:
        raise ValueError(f"Отсутствует требуемый столбец: {e}")

    rate_col_names = ["hourly_rate", "rate", "salary"]
    idx_rate = None
    for col in rate_col_names:
        if col in header:
            idx_rate = header.index(col)
            break
    if idx_rate is None:
        raise ValueError("Столбец почасовой ставки не найден.")

    employees = []
    for row in rows:
        employee = {
            "id": int(row[idx_id]),
            "email": row[idx_email],
            "name": row[idx_name],
            "department": row[idx_department],
            "hours": int(row[idx_hours]),
            "rate": int(row[idx_rate])
        }
        employees.append(employee)

    return employees
