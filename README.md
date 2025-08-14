# python-basics-assignment
Python Basic Programs – Assignment
Overview

This project contains four basic Python programs demonstrating:

Conditional statements (if-else)

Dictionary operations

File writing

File reading

These scripts are intended for beginners to practice core Python concepts.

Programs
1. Grade Checker (grade_checker.py)

Description:
Takes a score as input and prints a grade based on:

90+ → A

80–89 → B

70–79 → C

60–69 → D

Below 60 → F

Concepts Used:

User input (input())

Conditional statements (if-elif-else)

String formatting

2. Student Grades Dictionary (student_grades.py)

Description:
A menu-driven program to:

Add a new student and grade

Update an existing student’s grade

Display all students and grades

Concepts Used:

Python dictionary

Loops (while True)

Conditional checks (if-else)

Dictionary methods (.items())

3. Write to a File (write_file.py)

Description:
Creates (or overwrites) a text file example.txt and writes sample content to it.

Concepts Used:

File handling (open() with "w" mode)

Context managers (with statement)

Writing strings to a file (.write())

4. Read from a File (read_file.py)

Description:
Reads and displays the content of example.txt.

Concepts Used:

File handling (open() with "r" mode)

Reading file contents (.read())

Execution Instructions

Ensure Python 3.x is installed:

python --version


Run the programs in the following order:

python grade_checker.py
python student_grades.py
python write_file.py
python read_file.py


For read_file.py to work, run write_file.py first to create example.txt.

Folder Structure
.
├── grade_checker.py
├── student_grades.py
├── write_file.py
├── read_file.py
└── example.txt   # generated after running write_file.py
