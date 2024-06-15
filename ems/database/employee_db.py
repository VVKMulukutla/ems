import sqlite3

def connect_db():
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            department TEXT,
            position TEXT,
            salary REAL
        )
    ''')
    conn.commit()
    return conn

def add_employee(name, age, department, position, salary):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO employees (name, age, department, position, salary)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, age, department, position, salary))
    conn.commit()
    conn.close()

def update_employee(id, name, age, department, position, salary):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE employees
        SET name = ?, age = ?, department = ?, position = ?, salary = ?
        WHERE id = ?
    ''', (name, age, department, position, salary, id))
    conn.commit()
    conn.close()

def delete_employee(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM employees WHERE id = ?', (id,))
    conn.commit()
    conn.close()

def get_all_employees():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_employee_by_id(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees WHERE id = ?', (id,))
    row = cursor.fetchone()
    conn.close()
    return row
