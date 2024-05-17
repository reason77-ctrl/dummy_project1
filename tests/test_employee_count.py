from package_reason.employee_count import employee_count

def test_employee_count_single_department():
    data = [('HR', 'Ramesh Basnet'), ('HR', 'Krishna Prasad')]
    result = employee_count(data)
    expected = {'HR': ['Ramesh Basnet', 'Krishna Prasad']}
    assert result == expected


def test_employee_count_multi_depart():
    data = [
        ('Sales','Reason Regmi'),
        ('Marketing','Rakesh Chhetri'),
        ('Sales','Rahul Karki'),
        ('Accounting','Mahesh Sapkota'),
        ('Accounting','Deepa Basnet'),
    ]
    result = employee_count(data)
    expected = {'Sales': ['Reason Regmi', 'Rahul Karki'], 'Marketing': ['Rakesh Chhetri'], 'Accounting': ['Mahesh Sapkota', 'Deepa Basnet']}
    assert result == expected


def test_employee_count_empty_data():
    data = []
    result = employee_count(data)
    expected = {}
    assert result == expected


def test_employee_count_no_employees_in_department():
    data = [('HR', 'Alice'), ('Engineering', 'Bob'), ('HR', 'Carol'), ('Marketing', '')]
    result = employee_count(data)
    expected = {'HR': ['Alice', 'Carol'], 'Engineering': ['Bob'], 'Marketing': ['']}
    assert result == expected