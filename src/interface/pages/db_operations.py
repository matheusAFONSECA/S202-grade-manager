import streamlit as st
from interface.utils.utils import initialize
from interface.modules.modules_db_operations import ModulesDBoperations


class DBoperations:
    def __init__(self, db, student, teacher, subject, grade):
        self.db = db
        self.modules = ModulesDBoperations(db, student, teacher, subject, grade)

    def run(self):
        # Initialize page
        initialize(self.db)

        st.header("Database Operations")

        # Botão para dropar todos os dados
        if st.button("Drop All Data"):
            st.session_state["db"].drop_all()
            st.success("All data dropped successfully!")

        # Botão para criar os dados base
        if st.button("Create Base Data"):
            self.modules.create_base_data()
            st.success("Base data created successfully!")
