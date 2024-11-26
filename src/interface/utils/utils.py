import streamlit as st


def initialize(db):
    """
    Initialize default settings for the Streamlit interface.
    """
    st.title("Student Grade Management System")

    # Initialize session state variables if not already initialized
    if "db" not in st.session_state:
        st.session_state["db"] = db
