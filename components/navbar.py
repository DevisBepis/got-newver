import streamlit as st

from config import MENU_ITEMS

def navigation():

    col1, col2 = st.columns([9, 1])

    with col2:

        if st.button("MENU", use_container_width=True):

            st.session_state.menu = not st.session_state.get(
                "menu",
                False,
            )

    if st.session_state.get("menu", False):

        st.markdown("---")

        if st.button("HOME", use_container_width=True):
            st.session_state.page = "HOME"
            st.rerun()

        for item in MENU_ITEMS:

            if st.button(item, use_container_width=True):
                st.session_state.page = item
                st.session_state.menu = False
                st.rerun()

        st.markdown("---")