import datetime
import time

DateCreation = datetime.datetime.today().strftime("%d-%m-%Y")
TimeCreation = time.strftime("%H.%M.%S")

import people

print("Модуль people импортирован")

import salary

print("Модуль salary импортирован")

if __name__ == "__main__":
    salary.calculate_salary()
    people.get_employees()
print("Выполнено")
