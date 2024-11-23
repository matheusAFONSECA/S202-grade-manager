import streamlit as st
from interface.pages.add_data import AddData
from interface.pages.view_data import ViewData
from interface.pages.db_operations import DBoperations
from interface.pages.manage_relationships import ManageRelationships


class Interface:
    def __init__(self, db, student, teacher, subject, grade):
        self.add_data = AddData(db, student, teacher, subject, grade)
        self.db_operations = DBoperations(db, student, teacher, subject, grade)
        self.view_data = ViewData(db)
        self.manage_relationships = ManageRelationships(
            db, student, teacher, subject, grade
        )

    def run(self):
        st.set_page_config(
            page_title="Student Grade Management System", page_icon="🎓", layout="wide"
        )

        # Sidebar navigation
        menu = st.sidebar.selectbox(
            "Menu", ["Add Data", "View Data", "Relationships", "Database Operations"]
        )

        # Dynamically load and execute the selected page
        if menu == "Add Data":
            self.add_data.run()
        elif menu == "View Data":
            self.view_data.run()
        elif menu == "Relationships":
            self.manage_relationships.run()
        elif menu == "Database Operations":
            self.db_operations.run()
