import streamlit as st

def header_home():
    
    import base64
    with open("public/fusionclass_logo-removebg.png", "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    
    st.markdown(
        f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; margin-bottom:15px; margin-top:15px;">
            <img src="data:image/png;base64,{encoded_image}" width="300" height="150" style="margin-bottom: 0px; border-radius: 1000px;">
            <h1 style="color:#E0E3FF; text-align:center;">FUSION CLASS</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

def header_dashboard():
    import base64
    with open("public/fusionclass_logo-removebg-2.png", "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
        
    st.markdown(
        f"""
        <div style="display:flex; align-items:center; justify-content:flex-start; gap:20px; padding:10px;">
            <img src="data:image/png;base64,{encoded_image}" width="300" height="120px" style="margin-bottom: 0px; border-radius: 15px;">
            <h2 style="color:#0c2c54; text-align:left; white-space:nowrap;">FUSION<br>CLASS</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

