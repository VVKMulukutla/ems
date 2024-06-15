# Employee Management System

![Python](https://img.shields.io/badge/python-3.8+-brightgreen.svg)

An Employee Management System built with Python using Tkinter for the graphical user interface and SQLite for database management. This system allows for adding, updating, deleting, and viewing employee information, and generating reports.

## Features

- Add new employees
- Update existing employee information
- Delete employee information
- Generate reports in CSV format

## Folder Structure

```
employee_management_system/
│
├── database/
│   └── employee_db.py
├── gui/
│   ├── __init__.py
│   └── main_window.py
├── reports/
│   └── report_generator.py
├── main.py
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.8 or higher

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/employee_management_system.git
   cd employee_management_system
   ```

2. **Create a virtual environment and activate it:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

## Running the Application

Start the application by running the following command:

```sh
python main.py
```

## Generating Reports

To generate a report, run the following command:

```sh
python reports/report_generator.py
```

The report will be saved as `employee_report.csv` in the project directory.

## Contributing

We welcome contributions to enhance this project. Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [SQLite](https://www.sqlite.org/index.html)
- [csv](https://docs.python.org/3/library/csv.html)
```

### 6. Requirements File (`requirements.txt`)

```plaintext
python-dotenv
```

This project should give you a robust starting point for an Employee Management System with a user-friendly interface and basic CRUD functionalities. You can further extend this application by adding more features like searching employees, exporting reports in different formats, and more.