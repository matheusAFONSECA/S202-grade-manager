import streamlit as st


class ModulesManageRelationships:
    def __init__(self, db):
        self.db = db

    def assign_grade_to_student(self):
        st.subheader("Assign Grade to Student")
        student_name = st.text_input("Student Name")
        grade_id = st.number_input("Grade ID", min_value=1, step=1)

        if st.button("Create Relationship"):
            query = """
            MATCH (s:Student {name: $student_name})
            MATCH (g:Grade {grade_id: $grade_id})
            MERGE (s)-[:RECEIVES]->(g)
            """
            parameters = {"student_name": student_name, "grade_id": grade_id}
            self.db.execute_query(query, parameters)
            st.success(f"Assigned Grade {grade_id} to Student {student_name}.")

    def assign_teacher_to_subject(self):
        st.subheader("Assign Teacher to Subject")
        teacher_id = st.number_input("Teacher ID", min_value=1, step=1)
        subject_id = st.text_input("Subject ID")

        if st.button("Create Relationship"):
            query = """
            MATCH (t:Teacher {teacher_id: $teacher_id})
            MATCH (sub:Subject {subject_id: $subject_id})
            MERGE (t)-[:TEACHES]->(sub)
            """
            parameters = {"teacher_id": teacher_id, "subject_id": subject_id}
            self.db.execute_query(query, parameters)
            st.success(f"Assigned Teacher {teacher_id} to Subject {subject_id}.")

    def assign_subject_to_student(self):
        st.subheader("Assign Subject to Student")
        student_name = st.text_input("Student Name")
        subject_id = st.text_input("Subject ID")

        if st.button("Create Relationship"):
            query = """
            MATCH (s:Student {name: $student_name})
            MATCH (sub:Subject {subject_id: $subject_id})
            MERGE (s)-[:STUDIES]->(sub)
            """
            parameters = {"student_name": student_name, "subject_id": subject_id}
            self.db.execute_query(query, parameters)
            st.success(f"Assigned Subject {subject_id} to Student {student_name}.")

    def assign_teacher_to_student(self):
        st.subheader("Assign Teacher to Student")
        student_name = st.text_input("Student Name")
        teacher_id = st.number_input("Teacher ID", min_value=1, step=1)

        if st.button("Create Relationship"):
            query = """
            MATCH (s:Student {name: $student_name})
            MATCH (t:Teacher {teacher_id: $teacher_id})
            MERGE (s)-[:IS_TAUGHT_BY]->(t)
            """
            parameters = {"student_name": student_name, "teacher_id": teacher_id}
            self.db.execute_query(query, parameters)
            st.success(f"Assigned Teacher {teacher_id} to Student {student_name}.")
