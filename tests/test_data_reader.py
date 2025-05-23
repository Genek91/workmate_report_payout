import tempfile

from data_reader import read_employees


def test_read_employees_basic():
    content = (
        "id,email,name,department,hours_worked,hourly_rate\n"
        "1,alice@example.com,Alice,Marketing,160,50\n"
        "2,bob@example.com,Bob,Design,150,40\n"
    )
    with tempfile.NamedTemporaryFile("w+", delete=False) as file:
        file.write(content)
        file_name = file.name

    employees = read_employees(file_name)

    assert len(employees) == 2
    assert employees[0]["id"] == 1
    assert employees[0]["email"] == "alice@example.com"
    assert employees[0]["hours"] == 160
    assert employees[0]["rate"] == 50


def test_read_employees_different_rate_column():
    content = (
        "id,email,name,department,hours_worked,salary\n"
        "1,carol@example.com,Carol,Sales,170,60\n"
    )
    with tempfile.NamedTemporaryFile("w+", delete=False) as file:
        file.write(content)
        file_name = file.name

    employees = read_employees(file_name)

    assert len(employees) == 1
    assert employees[0]["rate"] == 60
