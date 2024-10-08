# ORM Alchemy Management DB System

This project is a School Management System developed using Python, SQLAlchemy, and PostgreSQL. 
The system allows for the management of students, teachers, subjects, and grades, providing a comprehensive solution for educational institutions.

## Features

- **Student Management**: Add, update, and remove student records.
- **Teacher Management**: Manage teacher profiles and their associated subjects.
- **Subject Management**: Create and manage subjects taught by teachers.
- **Grade Management**: Assign and manage grades for students.
- **Database Migrations**: Seamlessly manage database schema changes with Alembic.

## Examples of commands in the terminal

1) Create a teacher
- py main.py -a create -m Teacher -n 'Boris Jonson'

2) Create a group
- py main.py -a create -m Group -n 'AD-101'  


### Requirements

- Python 3.12
- PostgreSQL
- Docker (optional for running the database)

### Dependencies

Create a virtual environment and activate it:

python -m venv venv

venv\Scripts\activate     # For Windows

source venv/bin/activate  # For Unix
