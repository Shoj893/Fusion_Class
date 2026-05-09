import streamlit as st


def style_background_home():

    st.markdown("""
        <style>
                .stApp{
                    background: #0c2c54 !important;
                
                }

                .stApp div[data-testid="stColumn"]{
                    height: 400px;
                    background-color: #E0E3FF !important;
                    padding: 2.5rem !important;  
                    border-radius: 5rem !important;
                }
                
        </style>
                
                """
            ,unsafe_allow_html = True)
    

def style_background_dashboard():

    st.markdown("""
        <style>
                .stApp{
                    background: #E0E3FF !important;
                
                }
                
        </style>
                
                """
            ,unsafe_allow_html = True)
    

def style_base_layout():

    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

        /* Hide top bar of streamlit */
            #MainMenu, footer, header{
                visibility: hidden;
            }
            
            .block-container{
                padding-top:1.5rem !important;
            }
                
            h1{
                font-family: "Climate Crisis", sans-serif !important;
                font-size: 3.5rem !important;
                line-height: 1.1 !important;
                margin-bottom: 0rem !important;
                }

            h2{
                font-family: "Climate Crisis", sans-serif !important;
                font-size: 1.7rem !important;
                line-height: 1.1 !important;
                margin-bottom: 0rem !important;
                }

            h3, h4, p{
                font-family: "Outfit", sans-serif;
            }

            /* Keep form fields white even when a visitor's browser uses dark mode. */
            div[data-testid="stTextInput"] input,
            div[data-testid="stTextArea"] textarea,
            div[data-testid="stSelectbox"] div[data-baseweb="select"] > div,
            div[data-baseweb="input"],
            div[data-baseweb="textarea"]{
                background-color: #ffffff !important;
                color: #0f172a !important;
                border-color: #94a3b8 !important;
            }

            div[data-testid="stTextInput"] input::placeholder,
            div[data-testid="stTextArea"] textarea::placeholder{
                color: #64748b !important;
                opacity: 1 !important;
            }
                
            button{
                border-radius: 1.5rem !important;
                background-color: #0c2c54 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }
                
            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #424874 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: #475569 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button:hover{
                transform: scale(1.05) !important;
                }

            div[data-testid="stDialog"] button[aria-label="Close"]::before{
                content: "×";
                color: white;
                font-size: 1.5rem;
                font-weight: 700;
                line-height: 1;
                }
                
        </style>
                
                """
            ,unsafe_allow_html = True)
