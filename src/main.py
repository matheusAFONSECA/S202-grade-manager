import os
from dotenv import load_dotenv
from database.database_query import Database
from database.tables_db.grade import Grade
from database.tables_db.student import Student
from database.tables_db.subject import Subject
from database.tables_db.teacher import Teacher
from interface.interface_main import Interface


def main():
    # Load environment variables
    load_dotenv(".env")
    uri = os.getenv("NEO4J_URI")
    username = os.getenv("NEO4J_USERNAME")
    password = os.getenv("NEO4J_PASSWORD")
    database_name = os.getenv("NEO4J_DATABASE")

    # Initialize database connection
    db = Database(uri, username, password, database_name)

    # Initialize the Streamlit application
    interface = Interface(db, Student, Teacher, Subject, Grade)

    # Run the Streamlit application
    interface.run()

    # Close the database connection
    db.close()


if __name__ == "__main__":
    main()
