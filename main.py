import os

from dotenv import load_dotenv

from src.database import Database
from src.grade import Grade
from src.student import Student
from src.subject import Subject
from src.teacher import Teacher

load_dotenv("/home/pedro/inatel/database_II/lab/projects/01/.env")

# Access the environment variables
uri = os.getenv("NEO4J_URI")
username = os.getenv("NEO4J_USERNAME")
password = os.getenv("NEO4J_PASSWORD")
database_name = os.getenv("NEO4J_DATABASE")

print(f"uri: {uri}")
print(f"username: {username}")
print(f"password: {password}")
print(f"database_name: {database_name}")

# Initialize the Database connection
db = Database(uri, username, password, database_name)
db.drop_all()

# Create instances and nodes in the database
print("Creating student in the database...")
student = Student(1, "Computer Science", "Alice", db)
student.create_student()

print("Creating teacher in the database...")
teacher = Teacher(101, "Dr. Smith", db)
teacher.create_teacher()

print("Creating subject in the database...")
subject = Subject("CS101", "Intro to Computer Science", 101, db)
subject.create_subject()

print("Creating grade in the database...")
grade = Grade(1, 95.0, "CS101", 101, db)
grade.create_grade()

# Establish relationships
print("Adding a relationship between student and teacher...")
student.add_teacher(teacher)
print("Adding a relationship between student and subject...")
student.add_subject(subject)
print("Adding a relationship between student and grade...")
student.add_grade(grade)
print("Adding a relationship between teacher and subject...")
teacher.add_subject(subject)

# Close the database connection
db.close()
