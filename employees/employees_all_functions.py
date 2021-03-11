from utilits import enter_int, find_employees
import pickle
import random


def add_employees(employees: list):
    name = input("Enter the name: ")
    age = enter_int("Enter the age of the employee: ", error_number="There can only be a number")
    new_employees = {"name": name, "age": age}
    employees.append(new_employees)
    return employees


def del_employees(employees: list):
    name = input("Enter the name: ")
    find = find_employees(employees, name)
    employees.remove(find)
    return employees


def print_employees(employees: list):
    for i in employees:
        print(f'{i["name"]}, {i["age"]}')
    return


def search_employees_and_bin_search(employees: list):
    new_list = []
    menu = input("Choose which option you want to search for \n"
                  " 1) Full name \n"
                  " 2) First letters of name \n"
                  " 3) By age \n"
                  "Enter option number:")
    if menu == "1":
        name = input("Enter the name:  ")
        sorted_employees = select_sort(employees, key=lambda x: x["name"])
        bin_search_name = bin_search(sorted_employees, name, key=lambda x: x["name"])
        print("Index: ", bin_search_name)
        new_list.append(sorted_employees[bin_search_name])
    elif menu == "2":
        start_name = input("Enter the first letters of the name: ")
        new_list = list(filter(lambda x: x["name"].startswith(start_name), employees))
    elif menu == "3":
        age = enter_int("Enter the age of the employee: ", error_number="There can only be a number")
        sorted_employees = select_sort(employees, key=lambda x: x["age"])
        bin_search_age = bin_search(sorted_employees, age, key=lambda x: x["age"])
        print("Index: ", bin_search_age)
        new_list.append(sorted_employees[bin_search_age])
    print_employees(new_list)
    return


def edit_employees(employees: list):

    name = input("Enter the name:  ")
    find = find_employees(employees, name)

    new_name = input("Enter a new name: ")
    new_age = enter_int("Enter the new employee age: ", error_number="There can only be a number")
    find["name"] = new_name
    find["age"] = new_age
    return employees


def save_employees(employees: list):
    with open("employees.txt", "wb") as save_file:
        pickle.dump(employees, save_file)


def bin_search(employees: list, element, key):
    start = 0
    end = len(employees) - 1
    count = 0
    while start <= end:
        count += 1
        mid = (end + start) // 2
        if key(employees[mid]) > element:
            end = mid - 1
        elif key(employees[mid]) < element:
            start = mid + 1
        elif key(employees[mid]) == element:
            print(f"Binary search iterations: {count}")
            return mid
    print(f"Binary search iterations: {count}")
    return None


def select_sort(employees: list, key):
    for i in range(len(employees)):
        min_index = i
        for j in range(i, len(employees)):
            if key(employees[j]) < key(employees[min_index]):
                min_index = j
        employees[i], employees[min_index] = employees[min_index], employees[i]
    return employees


def menu_select_sort(employees: list):
    choice = input("Choose one of the options \n "
                    " 1) Sort by name \n"
                    " 2) Sort by age \n"
                    "Enter an option: ")
    if choice == "1":
        print(select_sort(employees, key=lambda x: x["name"]))
    elif choice == "2":
        print(select_sort(employees, key=lambda x: x["age"]))


def my_random(employees):
    num = int(input("Enter the number of random employees: "))
    for i in range(num):
        name = ["Tom", "Jane", "Olya", "Max", "Ann", "Kate", "Vlad", "Oleg", "Marina", "Inna", "Kirill"]
        random_name = random.choice(name)
        age = random.randint(5, 100)
        rand_employees = {"name": random_name, "age": age}
        print(rand_employees)
        employees.append(rand_employees)
    return employees
