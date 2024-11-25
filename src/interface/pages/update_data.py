import streamlit as st
from interface.utils.utils import initialize
from interface.modules.modules_update_data import ModulesUpdateData


class UpdateData:
    def __init__(self, db, student, teacher, subject, grade):
        self.db = db
        self.update_data = ModulesUpdateData(db)

    def run(self):
        # Initialize page
        initialize(self.db)

        st.header("Update Data")

        data_type = st.selectbox(
            "Select the data type to update:",
            ["Student", "Teacher", "Subject", "Grade"],
        )

        if data_type == "Student":
            self.update_data.update_student()
        elif data_type == "Teacher":
            self.update_data.update_teacher()
        elif data_type == "Subject":
            self.update_data.update_subject()
        elif data_type == "Grade":
            self.update_data.update_grade()
