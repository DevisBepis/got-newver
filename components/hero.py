import streamlit as st

from components.music import weekly_song


def homepage():

    song = weekly_song()

    st.markdown(
        """
        <section class="hero-container">

            <h1 class="hero-title">
                THORNED<br>
                GARDEN
            </h1>

        </section>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="rotation">
            Weekly Rotation
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="song">

            <div class="song-title">

                {song['title']}

            </div>

            <div class="song-artist">

                {song['artist']}

            </div>

            <a
                href="{song['link']}"
                target="_blank"
                class="listen"

            >
                LISTEN →
            </a>

        </div>
        """,
        unsafe_allow_html=True
    )