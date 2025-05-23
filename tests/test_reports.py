from reports import report_payout


def test_report_payout():
    employees = [
        {
            "id": 1,
            "email": "alice@example.com",
            "name": "Alice Johnson",
            "department": "Marketing",
            "hours": 160,
            "rate": 50,
        },
        {
            "id": 2,
            "email": "bob@example.com",
            "name": "Bob Smith",
            "department": "Design",
            "hours": 150,
            "rate": 40,
        },
    ]

    result = report_payout(employees)
    lines = result.splitlines()

    assert lines[0] == "name, department, hours, rate, payout"
    assert "Alice Johnson" in lines[1]
    assert "8000" in lines[1]
    assert "total_hours: 160" in lines[2]
