import streamlit as st
from pathlib import Path

from components.navbar import navigation

from pages.projects import projects_page
from pages.posts import posts_page
from pages.about import about_page
from pages.contact import contact_page

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="Thorned Garden",
    page_icon="🌹",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ----------------------------------
# LOAD CSS
# ----------------------------------

css_file = Path("assets/css/style.css")

if css_file.exists():
    with open(css_file) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True,
        )

# ----------------------------------
# SESSION STATE
# ----------------------------------

if "page" not in st.session_state:
    st.session_state.page = "HOME"

# ----------------------------------
# NAVIGATION
# ----------------------------------

navigation()

# ----------------------------------
# ROUTER
# ----------------------------------

match st.session_state.page:

    case "HOME":
        st.markdown(
            """
            <div class="hero">
                <h1>THORNED GARDEN</h1>
            </div>
            """,
            unsafe_allow_html=True,
        )

    case "PROJECTS":
        projects_page()

    case "POSTS":
        posts_page()

    case "ABOUT":
        about_page()

    case "CONTACT":
        contact_page()