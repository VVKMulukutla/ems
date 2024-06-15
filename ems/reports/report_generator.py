import csv
from database.employee_db import get_all_employees

def generate_report(file_path):
    employees = get_all_employees()
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Name', 'Age', 'Department', 'Position', 'Salary'])
        writer.writerows(employees)

if __name__ == "__main__":
    generate_report('employee_report.csv')
