import psycopg2

database = "postgres"
user = "postgres"
password = "248Tset12y"

def getAllStudents():
    connection = None
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM STUDENTS;")
        for t in cursor.fetchall():
            print(dict(zip([column[0] for column in cursor.description], t)))
    except Exception as e:
        print("Error: ", e)
        return
    finally:
        if connection:
            cursor.close()
            connection.close()
    print()


def addStudent(first_name, last_name, email, enrollment_date):
    connection = None
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO STUDENTS (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);", (first_name, last_name, email, enrollment_date))
        connection.commit()
    except Exception as e:
        print("Error: ", e)
        return
    finally:
        if connection:
            cursor.close()
            connection.close()
    print("Student added successfully.")
    print()

def updateStudentEmail(student_id, email):
    connection = None
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM STUDENTS WHERE student_id = %s;", (student_id,))
        if cursor.fetchone() is None:
            print(f"No student found with ID {student_id}.")
            print()
            return

        cursor.execute("UPDATE STUDENTS SET email = %s WHERE student_id = %s;", (email, student_id))
        connection.commit()
    except Exception as e:
        print("Error: ", e)
        return
    finally:
        if connection:
            cursor.close()
            connection.close()

    print("Student email updated successfully.")
    print()

def deleteStudent(student_id):
    connection = None
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM STUDENTS WHERE student_id = %s;", (student_id,))
        if cursor.fetchone() is None:
            print(f"No student found with ID {student_id}.")
            print()
            return

        cursor.execute("DELETE FROM STUDENTS WHERE student_id = %s;", (student_id,))
        connection.commit()
    except Exception as e:
        print("Error: ", e)
        return
    finally:
        if connection:
            cursor.close()
            connection.close()

    print("Student deleted successfully.")
    print()
    
def __main__():
    # Example usage
    while True:
        print("----- Welcome to the student database! -----")
        print("Please select an option:")
        print("  1. Get all students")
        print("  2. Add a student")
        print("  3. Update a student's email")
        print("  4. Delete a student")
        print("  5. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                getAllStudents()
            case '2':
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                email = input("Enter email: ")
                enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
                addStudent(first_name, last_name, email, enrollment_date)
            case '3':
                student_id = input("Enter student ID: ")
                email = input("Enter new email: ")
                updateStudentEmail(student_id, email)
            case '4':
                student_id = input("Enter student ID to delete: ")
                deleteStudent(student_id)
            case '5':
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    __main__()