import streamlit as st

def main():
    # Configure the Streamlit page
    st.set_page_config(
        page_title="Real Estate Auktion Platform",
        layout="wide"
    )

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
        from pages import About_Us
        About_Us.run()

    elif choice == "Prozess":
        from pages import Prozess
        Prozess.run()

    elif choice == "Auktion":
        from pages import Auktion
        Auktion.run()

    elif choice == "Bewertung":
        from pages import Bewertung
        Bewertung.run()

    elif choice == "Blog":
        from pages import Blog
        Blog.run()

    elif choice == "Einstellungen":
        from pages import Einstellungen
        Einstellungen.run()

    elif choice == "Hilfe":
        from pages import Hilfe
        Hilfe.run()


if __name__ == "__main__":
    main()
