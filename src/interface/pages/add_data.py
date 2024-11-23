import streamlit as st
from interface.utils.utils import initialize


class AddData:
    def __init__(self, db, student, teacher, subject, grade):
        self.db = db
        self.student = student
        self.teacher = teacher
        self.subject = subject
        self.grade = grade

    def run(self):
        # Initialize page
        initialize(self.db)

        st.header("Add Data to the Database")
        data_type = st.selectbox(
            "Select data type to add:", ["Student", "Teacher", "Subject", "Grade"]
        )

        if data_type == "Student":
            st.subheader("Add a Student")
            registration_number = st.number_input(
                "Registration Number", min_value=1, step=1
            )
            name = st.text_input("Name")
            course = st.text_input("Course")
            if st.button("Add Student"):
                student = self.student(
                    registration_number, course, name, st.session_state["db"]
                )
                student.create_student()
                st.success(f"Student {name} added successfully!")

        elif data_type == "Teacher":
            st.subheader("Add a Teacher")
            teacher_id = st.number_input("Teacher ID", min_value=1, step=1)
            name = st.text_input("Name")
            if st.button("Add Teacher"):
                teacher = self.teacher(teacher_id, name, st.session_state["db"])
                teacher.create_teacher()
                st.success(f"Teacher {name} added successfully!")

        elif data_type == "Subject":
            st.subheader("Add a Subject")
            subject_id = st.text_input("Subject ID")
            name = st.text_input(
                "Subject Name"
            )  # Corrigir para 'Subject Name' em vez de 'Name'
            teacher_id = st.number_input("Teacher ID", min_value=1, step=1)
            if st.button("Add Subject"):
                subject = self.subject(
                    subject_id, name, teacher_id, st.session_state["db"]
                )
                subject.create_subject()  # Verifique se o nome da matéria é atribuído corretamente
                st.success(f"Subject {name} added successfully!")

        elif data_type == "Grade":
            st.subheader("Add a Grade")
            grade_id = st.number_input("Grade ID", min_value=1, step=1)
            obtained_grade = st.number_input(
                "Obtained Grade", min_value=0.0, max_value=100.0, step=0.1
            )
            subject_id = st.text_input("Subject ID")
            teacher_id = st.number_input("Teacher ID", min_value=1, step=1)
            if st.button("Add Grade"):
                grade = self.grade(
                    grade_id,
                    obtained_grade,
                    subject_id,
                    teacher_id,
                    st.session_state["db"],
                )
                grade.create_grade()
                st.success(f"Grade {obtained_grade} added successfully!")
