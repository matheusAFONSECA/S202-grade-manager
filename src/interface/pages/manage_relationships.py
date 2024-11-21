import streamlit as st
from interface.utils.utils import initialize


class ManageRelationships:
    def __init__(self, db, student, teacher, subject, grade):
        self.db = db
        self.student = student
        self.teacher = teacher
        self.subject = subject
        self.grade = grade

    def run(self):
        # Initialize page
        initialize(self.db)

        st.header("Manage Relationships")
        st.write(
            "Work on relationships like assigning teachers to subjects, students to grades, etc."
        )
