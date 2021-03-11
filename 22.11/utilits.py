def enter_int(number, error_number):
    num = input(number)
    while not num.isnumeric():
        print(error_number)
        num = input(number)
    return int(num)


def find_employees(employees, name):
    for elem in employees:
        if elem["name"] == name:
            return elem
    return None
