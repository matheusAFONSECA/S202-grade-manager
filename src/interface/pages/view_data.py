import pandas as pd
import streamlit as st
from interface.utils.utils import initialize
from interface.modules.modules_view_data import ModulesViewData


class ViewData:
    def __init__(self, db):
        self.db = db
        self.modules_view_data = ModulesViewData(db)

    def run(self):
        # Initialize page
        initialize(self.db)

        st.header("View Data from the Database")
        view_type = st.selectbox(
            "Select data type to view:", ["Students", "Teachers", "Subjects", "Grades"]
        )

        if view_type == "Students":
            st.subheader("Students")
            registration = st.text_input("Filter by Registration (optional)")
            name = st.text_input("Filter by Name (optional)")
            course = st.text_input("Filter by Course (optional)")
            students = self.modules_view_data.get_students(registration, name, course)
            if students:
                # Displaying data in a dataframe
                df = pd.DataFrame(students, columns=["Name", "Registration", "Course"])
                st.dataframe(df)  # Display the dataframe as a table
            else:
                st.write("No students found.")

        elif view_type == "Teachers":
            st.subheader("Teachers")
            registration = st.text_input("Filter by Registration (optional)")
            name = st.text_input("Filter by Name (optional)")
            teachers = self.modules_view_data.get_teachers(registration, name)
            if teachers:
                df = pd.DataFrame(teachers, columns=["Name", "Registration"])
                st.dataframe(df)
            else:
                st.write("No teachers found.")

        elif view_type == "Subjects":
            st.subheader("Subjects")
            subject_id = st.text_input("Filter by Subject ID (optional)")
            subject_name = st.text_input("Filter by Subject Name (optional)")
            teacher_name = st.text_input("Filter by Teacher Name (optional)")
            subjects = self.modules_view_data.get_subjects(
                subject_id, subject_name, teacher_name
            )
            if subjects:
                df = pd.DataFrame(
                    subjects, columns=["Subject Name", "Subject ID", "Teacher Name"]
                )
                st.dataframe(df)
            else:
                st.write("No subjects found.")

        elif view_type == "Grades":
            st.subheader("Grades")
            student_name = st.text_input("Filter by Student Name (optional)")
            course_name = st.text_input("Filter by Course Name (optional)")
            grades = self.modules_view_data.get_grades(student_name, course_name)
            if grades:
                df = pd.DataFrame(
                    grades, columns=["Student Name", "Course", "Grade", "Subject"]
                )
                st.dataframe(df)
            else:
                st.write("No grades found.")
