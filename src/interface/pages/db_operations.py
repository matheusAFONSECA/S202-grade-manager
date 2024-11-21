import streamlit as st
from interface.utils.utils import initialize

class DBoperations:
    def __init__(self, db):
        self.db = db

    def run(self):
        # Initialize page
        initialize(self.db)

        st.header("Database Operations")
        if st.button("Drop All Data"):
            st.session_state["db"].drop_all()
            st.success("All data dropped successfully!")
