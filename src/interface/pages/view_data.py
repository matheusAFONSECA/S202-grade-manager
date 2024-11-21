import streamlit as st
from interface.utils.utils import initialize


class ViewData:
    def __init__(self, db):
        self.db = db

    def run(self):
        # Initialize page
        initialize(self.db)

        st.header("View Data from the Database")
        view_type = st.selectbox(
            "Select data type to view:", ["Students", "Teachers", "Subjects", "Grades"]
        )

        if view_type == "Students":
            st.subheader("Students")
            st.write("Display Students data")

        elif view_type == "Teachers":
            st.subheader("Teachers")
            st.write("Display Teachers data")

        elif view_type == "Subjects":
            st.subheader("Subjects")
            st.write("Display Subjects data")

        elif view_type == "Grades":
            st.subheader("Grades")
            st.write("Display Grades data")
