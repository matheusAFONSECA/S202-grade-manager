import streamlit as st
from interface.utils.utils import initialize
from interface.modules.modules_manage_relationships import ModulesManageRelationships


class ManageRelationships:
    def __init__(self, db, student, teacher, subject, grade):
        self.db = db
        self.student = student
        self.teacher = teacher
        self.subject = subject
        self.grade = grade
        self.manage_relationships = ModulesManageRelationships(db)

    def run(self):
        # Initialize page
        initialize(self.db)

        st.header("Manage Relationships")

        relationship_type = st.selectbox(
            "Select the relationship to create:",
            [
                "Assign Grade to Student",
                "Assign Teacher to Subject",
                "Assign Subject to Student",
                "Assign Teacher to Student",
            ],
        )

        if relationship_type == "Assign Grade to Student":
            self.manage_relationships.assign_grade_to_student()
        elif relationship_type == "Assign Teacher to Subject":
            self.manage_relationships.assign_teacher_to_subject()
        elif relationship_type == "Assign Subject to Student":
            self.manage_relationships.assign_subject_to_student()
        elif relationship_type == "Assign Teacher to Student":
            self.manage_relationships.assign_teacher_to_student()
