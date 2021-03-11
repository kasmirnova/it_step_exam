import pickle
from employees_all_functions import add_employees, del_employees, \
    print_employees, search_employees_and_bin_search, edit_employees, \
    save_employees, menu_select_sort, my_random


def main():
    with open("employees.txt", "rb") as read_file:
        employees = pickle.load(read_file)

    while True:
        menu = int(input("Choose one of the options \n "
                      " 1) Add \n"
                      " 2) Delete \n"
                      " 3) Output information \n"
                      " 4) Search and Binary Search \n"
                      " 5) Editing \n"
                      " 6) Sort \n"
                      " 7) Fill in randomly \n"
                      " 8) Saving \n"
                      " 0) Exit \n"
                      "Run the option: "))
        if menu > 8 or menu < 0:
            menu = int(input("It should me between 0 and 8. Enter your option: "))
        elif menu == 1:
            add_employees(employees)
        elif menu == 2:
            del_employees(employees)
        elif menu == 3:
            print_employees(employees)
        elif menu == 4:
            search_employees_and_bin_search(employees)
        elif menu == 5:
            edit_employees(employees)
        elif menu == 6:
            menu_select_sort(employees)
        elif menu == 7:
            my_random(employees)
        elif menu == 8:
            save_employees(employees)
        elif menu == 0:
            save_employees(employees)
            break



main()
