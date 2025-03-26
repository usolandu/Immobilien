import streamlit as st

st.set_page_config(
    page_title="Immobilien Auktion Platforom",
    page_icon=None,
    layout="wide",
)

# Hide Streamlit's default header (which often includes the page name)
hide_streamlit_style = """
    <style>
    header {visibility: hidden;} /* Hide the entire top header */
    #MainMenu {visibility: hidden;} /* Hide the hamburger menu if you want */
    footer {visibility: hidden;}    /* Hide the footer if you want */
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def main():

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    menu_options = [
        "About us",
        "Prozess",
        "Auktion",
        "Bewertung",
        "Blog",
        "Einstellungen",
        "Hilfe"
    ]
    choice = st.sidebar.radio("Go to", menu_options)

    # Navigate to the selected page
    if choice == "About us":
        from _pages import About_Us
        About_Us.run()

    elif choice == "Prozess":
        from _pages import Prozess
        Prozess.run()

    elif choice == "Auktion":
        from _pages import Auktion
        Auktion.run()

    elif choice == "Bewertung":
        from _pages import Bewertung
        Bewertung.run()

    elif choice == "Blog":
        from _pages import Blog
        Blog.run()

    elif choice == "Einstellungen":
        from _pages import Einstellungen
        Einstellungen.run()

    elif choice == "Hilfe":
        from _pages import Hilfe
        Hilfe.run()


if __name__ == "__main__":
    main()
