import streamlit as st

def header_home():
    
    # Read and encode the image
    import base64
    with open("public/fusionclass_logo.png", "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    
    # Display both image and text in a single centered container
    st.markdown(
        f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; margin-bottom:15px; margin-top:15px;">
            <img src="data:image/png;base64,{encoded_image}" width="200" height="100" style="margin-bottom: 5px; border-radius: 1000px;">
            <h1 style="color:#E0E3FF; text-align:center;">FUSION  CLASS</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

