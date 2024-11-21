import streamlit as st

class Interface:
    def __init__(self, db, Student, Teacher, Subject, Grade):
        self.db = db
        self.Student = Student
        self.Teacher = Teacher
        self.Subject = Subject
        self.Grade = Grade
        

    def run(self):
        # Streamlit app
        st.title("Student Grade Management System")

        # Sidebar navigation
        menu = st.sidebar.selectbox("Menu", ["Add Data", "View Data", "Relationships", "Database Operations"])

        if menu == "Add Data":
            st.header("Add Data to the Database")
            data_type = st.selectbox("Select data type to add:", ["Student", "Teacher", "Subject", "Grade"])
            
            if data_type == "Student":
                st.subheader("Add a Student")
                registration_number = st.number_input("Registration Number", min_value=1, step=1)
                name = st.text_input("Name")
                course = st.text_input("Course")
                if st.button("Add Student"):
                    student = self.Student(registration_number, course, name, self.db)
                    student.create_student()
                    st.success(f"Student {name} added successfully!")
            
            elif data_type == "Teacher":
                st.subheader("Add a Teacher")
                teacher_id = st.number_input("Teacher ID", min_value=1, step=1)
                name = st.text_input("Name")
                if st.button("Add Teacher"):
                    teacher = self.Teacher(teacher_id, name, self.db)
                    teacher.create_teacher()
                    st.success(f"Teacher {name} added successfully!")
            
            elif data_type == "Subject":
                st.subheader("Add a Subject")
                subject_id = st.text_input("Subject ID")
                name = st.text_input("Name")
                teacher_id = st.number_input("Teacher ID", min_value=1, step=1)
                if st.button("Add Subject"):
                    subject = self.Subject(subject_id, name, teacher_id, self.db)
                    subject.create_subject()
                    st.success(f"Subject {name} added successfully!")
            
            elif data_type == "Grade":
                st.subheader("Add a Grade")
                grade_id = st.number_input("Grade ID", min_value=1, step=1)
                obtained_grade = st.number_input("Obtained Grade", min_value=0.0, max_value=100.0, step=0.1)
                subject_id = st.text_input("Subject ID")
                teacher_id = st.number_input("Teacher ID", min_value=1, step=1)
                if st.button("Add Grade"):
                    grade = self.Grade(grade_id, obtained_grade, subject_id, teacher_id, self.db)
                    grade.create_grade()
                    st.success(f"Grade {obtained_grade} added successfully!")

        elif menu == "View Data":
            st.header("View Data from the Database")
            view_type = st.selectbox("Select data type to view:", ["Students", "Teachers", "Subjects", "Grades"])
            
            if view_type == "Students":
                st.subheader("Students")
                # Add your query logic to display students here
                st.write("Display Students data")
            
            elif view_type == "Teachers":
                st.subheader("Teachers")
                # Add your query logic to display teachers here
                st.write("Display Teachers data")
            
            elif view_type == "Subjects":
                st.subheader("Subjects")
                # Add your query logic to display subjects here
                st.write("Display Subjects data")
            
            elif view_type == "Grades":
                st.subheader("Grades")
                # Add your query logic to display grades here
                st.write("Display Grades data")

        elif menu == "Relationships":
            st.header("Manage Relationships")
            st.write("Work on relationships like assigning teachers to subjects, students to grades, etc.")

        elif menu == "Database Operations":
            st.header("Database Operations")
            if st.button("Drop All Data"):
                self.db.drop_all()
                st.success("All data dropped successfully!")
