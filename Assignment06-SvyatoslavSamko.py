# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Svyat Samko, 11/18,2026, amended script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
menu_choice: str = ''  # Hold the choice made by the user.
file = None  # Holds a reference to an opened file.

# Classes

class FileProcessor:
    ''' 
    This class contains functions to process files, 
    ie open and read it and 
    write into the file and close it 
    '''

    @staticmethod

    def read_data_from_file(file_name: str, student_data: list):
        student_data = []
        try:
            file_name = open(FILE_NAME, "r")
            student_data = json.load(file_name)
        except Exception as e:
            print("Error: There was a problem with reading the file.")
            print("Please check that the file exists and that it is in a json format.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        finally:
            # Check if a file object exists and is still open
            if file is not None and file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: dict):
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file, indent=2)
            print("The following data was saved to file!")
            for student in students:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            print("Error: There was a problem with writing to the file.")
            print("Please check that the file is not open by another program.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        finally:
            # Check if a file object exists and is still open
            if file is not None and file.closed == False:
                file.close()
class IO:
    '''
    This class contains functions to take inputs from the user
    and return data to the user
     '''
    @staticmethod
    def  output_error_messages(message: str, error: Exception = None):
        pass


    @staticmethod
    def output_menu(menu: str):
        pass

    @staticmethod
    def input_menu_choice():
        # Present the menu of choices
        print(MENU)
        menu_choice = input("What would you like to do: ")
        return menu_choice


    @staticmethod
    def output_student_courses(student_data: list):
        # Process the data to create and display a custom message
        print("-" * 50)
        for student in students:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("Error: There was a problem with your entered data.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        return student_data

# When the program starts, read the file data into a list of lists (table)

# Extract the data from the file

students = FileProcessor.read_data_from_file(FILE_NAME, student_data)

# Present and Process the data
while (True):

    # Present the menu of choices
    menu_choice=IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        IO.input_student_data(student_data = student_data)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data = student_data)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name = FILE_NAME, student_data = student_data)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
