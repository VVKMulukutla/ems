import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from database.employee_db import add_employee, update_employee, delete_employee, get_all_employees, get_employee_by_id

class EmployeeManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("800x500")
        
        # Variables
        self.id = tk.StringVar()
        self.name = tk.StringVar()
        self.age = tk.StringVar()
        self.department = tk.StringVar()
        self.position = tk.StringVar()
        self.salary = tk.StringVar()
        
        # Title
        title = tk.Label(root, text="Employee Management System", bd=10, relief=tk.GROOVE, font=("times new roman", 40, "bold"))
        title.pack(side=tk.TOP, fill=tk.X)
        
        # Manage Frame
        manage_frame = tk.Frame(root, bd=4, relief=tk.RIDGE, bg="crimson")
        manage_frame.place(x=20, y=100, width=450, height=400)
        
        m_title = tk.Label(manage_frame, text="Manage Employees", bg="crimson", fg="white", font=("times new roman", 30, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)
        
        lbl_name = tk.Label(manage_frame, text="Name", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        
        txt_name = tk.Entry(manage_frame, textvariable=self.name, font=("times new roman", 15, "bold"), bd=5, relief=tk.GROOVE)
        txt_name.grid(row=1, column=1, pady=10, padx=20, sticky="w")
        
        lbl_age = tk.Label(manage_frame, text="Age", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_age.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        
        txt_age = tk.Entry(manage_frame, textvariable=self.age, font=("times new roman", 15, "bold"), bd=5, relief=tk.GROOVE)
        txt_age.grid(row=2, column=1, pady=10, padx=20, sticky="w")
        
        lbl_department = tk.Label(manage_frame, text="Department", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_department.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        
        txt_department = tk.Entry(manage_frame, textvariable=self.department, font=("times new roman", 15, "bold"), bd=5, relief=tk.GROOVE)
        txt_department.grid(row=3, column=1, pady=10, padx=20, sticky="w")
        
        lbl_position = tk.Label(manage_frame, text="Position", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_position.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        
        txt_position = tk.Entry(manage_frame, textvariable=self.position, font=("times new roman", 15, "bold"), bd=5, relief=tk.GROOVE)
        txt_position.grid(row=4, column=1, pady=10, padx=20, sticky="w")
        
        lbl_salary = tk.Label(manage_frame, text="Salary", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_salary.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        
        txt_salary = tk.Entry(manage_frame, textvariable=self.salary, font=("times new roman", 15, "bold"), bd=5, relief=tk.GROOVE)
        txt_salary.grid(row=5, column=1, pady=10, padx=20, sticky="w")
        
        # Button Frame
        btn_frame = tk.Frame(manage_frame, bd=4, relief=tk.RIDGE, bg="crimson")
        btn_frame.place(x=15, y=340, width=420)
        
        addbtn = tk.Button(btn_frame, text="Add", width=10, command=self.add_employee).grid(row=0, column=0, padx=10, pady=10)
        updatebtn = tk.Button(btn_frame, text="Update", width=10, command=self.update_employee).grid(row=0, column=1, padx=10, pady=10)
        deletebtn = tk.Button(btn_frame, text="Delete", width=10, command=self.delete_employee).grid(row=0, column=2, padx=10, pady=10)
        clearbtn = tk.Button(btn_frame, text="Clear", width=10, command=self.clear).grid(row=0, column=3, padx=10, pady=10)
        
        # Detail Frame
        detail_frame = tk.Frame(root, bd=4, relief=tk.RIDGE, bg="crimson")
        detail_frame.place(x=500, y=100, width=780, height=580)
        
        lbl_search = tk.Label(detail_frame, text="Search By", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")
        
        combo_search = ttk.Combobox(detail_frame, width=10, font=("times new roman", 13, "bold"), state='readonly')
        combo_search['values'] = ("Name", "Department", "Position")
        combo_search.grid(row=0, column=1, padx=20, pady=10)
        
        txt_search = tk.Entry(detail_frame, font=("times new roman", 13, "bold"), bd=5, relief=tk.GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")
        
        searchbtn = tk.Button(detail_frame, text="Search", width=10, pady=5).grid(row=0, column=3, padx=10, pady=10)
        showallbtn = tk.Button(detail_frame, text="Show All", width=10, pady=5, command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)
        
        # Table Frame
        table_frame = tk.Frame(detail_frame, bd=4, relief=tk.RIDGE, bg="crimson")
        table_frame.place(x=10, y=70, width=760, height=500)
        
        scroll_x = tk.Scrollbar(table_frame, orient=tk.HORIZONTAL)
        scroll_y = tk.Scrollbar(table_frame, orient=tk.VERTICAL)
        self.employee_table = ttk.Treeview(table_frame, columns=("ID", "Name", "Age", "Department", "Position", "Salary"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)
        self.employee_table.heading("ID", text="ID")
        self.employee_table.heading("Name", text="Name")
        self.employee_table.heading("Age", text="Age")
        self.employee_table.heading("Department", text="Department")
        self.employee_table.heading("Position", text="Position")
        self.employee_table.heading("Salary", text="Salary")
        self.employee_table['show'] = 'headings'
        self.employee_table.column("ID", width=50)
        self.employee_table.column("Name", width=150)
        self.employee_table.column("Age", width=50)
        self.employee_table.column("Department", width=100)
        self.employee_table.column("Position", width=100)
        self.employee_table.column("Salary", width=100)
        self.employee_table.pack(fill=tk.BOTH, expand=1)
        self.employee_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()
        
    def add_employee(self):
        add_employee(
            self.name.get(),
            self.age.get(),
            self.department.get(),
            self.position.get(),
            self.salary.get()
        )
        self.fetch_data()
        self.clear()
        messagebox.showinfo("Success", "Employee added successfully")

    def update_employee(self):
        update_employee(
            self.id.get(),
            self.name.get(),
            self.age.get(),
            self.department.get(),
            self.position.get(),
            self.salary.get()
        )
        self.fetch_data()
        self.clear()
        messagebox.showinfo("Success", "Employee updated successfully")

    def delete_employee(self):
        delete_employee(self.id.get())
        self.fetch_data()
        self.clear()
        messagebox.showinfo("Success", "Employee deleted successfully")

    def fetch_data(self):
        rows = get_all_employees()
        if len(rows) != 0:
            self.employee_table.delete(*self.employee_table.get_children())
            for row in rows:
                self.employee_table.insert('', 'end', values=row)
            self.employee_table.pack()

    def get_cursor(self, ev):
        cursor_row = self.employee_table.focus()
        contents = self.employee_table.item(cursor_row)
        row = contents['values']
        self.id.set(row[0])
        self.name.set(row[1])
        self.age.set(row[2])
        self.department.set(row[3])
        self.position.set(row[4])
        self.salary.set(row[5])

    def clear(self):
        self.id.set("")
        self.name.set("")
        self.age.set("")
        self.department.set("")
        self.position.set("")
        self.salary.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeManagementSystem(root)
    root.mainloop()
