#*************** Task-1- Aishwarya *******************

name = input("Enter your name: ")
salary = int(input("Enter your monthly salary: "))

print("***** Employee Details *****")
print("Name:", name)
print("Monthly Salary:", salary)

#*************** Task-2- Anuja *******************
print(type(salary))
salary = float(salary)
print(type(salary))

#*************** Task-3- Anuska *******************
# Calculate tax using if statement
if salary > 0:
    tax = salary * 0.10
    print("Tax amount is:", tax)
else:
    tax = 0
    print("Invalid salary! Tax cannot be calculated.")

#*************** Task-4- Asmita *******************
print("-------------------TAXATION SYSTEM OF NEPAL-------------------")
emp_name = []
emp_salary = []
emp_tax = []

while True:
    employee_name = input("Enter employee name: ")
    if employee_name.strip() == "":
        print("Employee name cannot be empty. Please try again.")
        continue
    if employee_name in emp_name:
        print("Employee name already exists. Please enter a unique name.")
        continue

    try:
        employee_salary = float(input("Enter employee salary: "))
        if employee_salary < 0:
            print("Employee salary cannot be negative. Please try again.")
            continue
    except ValueError:
        print("Invalid salary! Please enter a number.")
        continue

    tax = employee_salary * 0.1

    emp_name.append(employee_name)
    emp_salary.append(employee_salary)
    emp_tax.append(tax)

    choice = input("Do you want to add another employee? (yes/no): ").strip().lower()
    if choice != 'yes':
        break

print("\n-------------------TAXATION Report-------------------")
print("Employee Name\tEmployee Salary\tTax Amount")
for i in range(len(emp_name)):
    print(f"{emp_name[i]}\t\t{emp_salary[i]}\t\t{emp_tax[i]}")
