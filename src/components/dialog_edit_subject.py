import streamlit as st
from src.database.db import update_subject


@st.dialog("Edit Subject")
def edit_subject_dialog(subject):
    # Pre-fill existing subject details so the teacher can update only what changed.
    st.write("Update the subject details")
    sub_code = st.text_input("Subject Code", value=subject["subject_code"])
    sub_name = st.text_input("Subject Name", value=subject["name"])
    sub_section = st.text_input("Section", value=subject["section"])

    if st.button("Save Changes", type="primary", width="stretch"):
        if sub_code and sub_name and sub_section:
            try:
                update_subject(subject["subject_id"], sub_code, sub_name, sub_section)
                st.toast("Subject updated successfully!")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {str(e)}")
        else:
            st.warning("Please fill all the fields")
