import streamlit as st


class ModulesUpdateData:
    def __init__(self, db):
        self.db = db

    def update_student(self):
        st.subheader("Update Student")
        registration_number = st.number_input(
            "Registration Number", min_value=1, step=1
        )
        new_name = st.text_input("New Name")
        new_course = st.text_input("New Course")

        if st.button("Update Student"):
            query = """
            MATCH (s:Student {registration_number: $registration_number})
            SET s.name = $new_name, s.course = $new_course
            """
            parameters = {
                "registration_number": registration_number,
                "new_name": new_name,
                "new_course": new_course,
            }
            self.db.execute_query(query, parameters)
            st.success(f"Student {registration_number} updated successfully.")

    def update_teacher(self):
        st.subheader("Update Teacher")
        teacher_id = st.number_input("Teacher ID", min_value=1, step=1)
        new_name = st.text_input("New Name")

        if st.button("Update Teacher"):
            query = """
            MATCH (t:Teacher {teacher_id: $teacher_id})
            SET t.name = $new_name
            """
            parameters = {"teacher_id": teacher_id, "new_name": new_name}
            self.db.execute_query(query, parameters)
            st.success(f"Teacher {teacher_id} updated successfully.")

    def update_subject(self):
        st.subheader("Update Subject")
        subject_id = st.text_input("Subject ID")
        new_name = st.text_input("New Name")
        new_teacher_id = st.number_input("New Teacher ID", min_value=1, step=1)

        if st.button("Update Subject"):
            query = """
            MATCH (sub:Subject {subject_id: $subject_id})
            SET sub.name = $new_name, sub.teacher_id = $new_teacher_id
            """
            parameters = {
                "subject_id": subject_id,
                "new_name": new_name,
                "new_teacher_id": new_teacher_id,
            }
            self.db.execute_query(query, parameters)
            st.success(f"Subject {subject_id} updated successfully.")

    def update_grade(self):
        st.subheader("Update Grade")
        grade_id = st.number_input("Grade ID", min_value=1, step=1)
        new_grade = st.number_input(
            "New Grade", min_value=0.0, max_value=100.0, step=0.1
        )

        if st.button("Update Grade"):
            query = """
            MATCH (g:Grade {grade_id: $grade_id})
            SET g.obtained_grade = $new_grade
            """
            parameters = {"grade_id": grade_id, "new_grade": new_grade}
            self.db.execute_query(query, parameters)
            st.success(f"Grade {grade_id} updated successfully.")
