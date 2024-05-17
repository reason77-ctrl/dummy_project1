from package_reason import my_default_dict

def employee_count(data):
    dd = my_default_dict(list)
    for department, employee in data:
        dd[department].append(employee)
    return dd