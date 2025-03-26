import streamlit as st

def run():
    st.title("Bewertung")
    st.write(
        "Füllen Sie die folgenden Informationen aus, um eine KI-gestützte Schätzung für Ihre Immobilie zu erhalten. "
        "Bitte geben Sie so viele Details wie möglich an, um die Genauigkeit zu erhöhen."
    )

    # Tabs für jeden Schritt des Bewertungsformulars erstellen
    tab_prop_id, tab_land, tab_building, tab_condition, tab_legal, tab_market, tab_income, tab_docs = st.tabs([
        "Objektidentifikation",
        "Grundstück & Standortdetails",
        "Gebäudespezifikationen",
        "Zustand & Wartung",
        "Rechtliche & Finanzielle Informationen",
        "Markt- & Vergleichsdaten",
        "Ertragsmöglichkeiten",
        "Dokumenten-Uploads"
    ])

    # 3.1 Objektidentifikation
    with tab_prop_id:
        st.subheader("Objektidentifikation")
        address = st.text_input("Adresse")
        property_type = st.selectbox(
            "Objekttyp",
            ["Einfamilienhaus", "Wohnung", "Mehrfamilienhaus", "Gewerbeimmobilie", "Grundstück"]
        )
        year_construction = st.number_input("Baujahr", min_value=1800, max_value=2100, value=2000)
        year_renovations = st.text_input("Renovierungsjahr(e) (kommagetrennt)")

    # 3.2 Grundstück & Standortdetails
    with tab_land:
        st.subheader("Grundstück & Standortdetails")
        plot_size = st.number_input("Grundstücksgröße (m²)", min_value=0, value=0)
        zoning_info = st.text_input("Zoneninformationen (z. B. Wohngebiet, Gewerbe)")
        topography = st.selectbox("Topographie", ["Flach", "Abfallend", "Unregelmäßig"])
        amenities_distance = st.text_area(
            "Nähe zu Annehmlichkeiten (Entfernungen zu Schulen, Verkehrsmitteln, Geschäften usw.)"
        )
        environmental_factors = st.text_area(
            "Umgebungsfaktoren (Fabriken, Flughäfen, stark befahrene Straßen usw.)"
        )

    # 3.3 Gebäudespezifikationen
    with tab_building:
        st.subheader("Gebäudespezifikationen")
        total_living_area = st.number_input("Gesamtwohnfläche (m²)", min_value=0, value=0)
        num_bedrooms = st.number_input("Anzahl Schlafzimmer", min_value=0, value=0)
        num_bathrooms = st.number_input("Anzahl Badezimmer", min_value=0, value=0)
        other_rooms = st.number_input("Andere Räume", min_value=0, value=0)
        floor_levels = st.number_input("Anzahl Stockwerke", min_value=1, value=1)
        construction_materials = st.text_input("Baumaterialien (Struktur, Dach, Fassade)")
        energy_efficiency = st.text_input("Energieeffizienzklasse")

    # 3.4 Zustand & Wartung
    with tab_condition:
        st.subheader("Zustand & Wartung")
        structural_issues = st.text_area("Strukturelle Integrität (bekannte Probleme mit Fundament, Wänden oder Dach)")
        renovation_history = st.text_area("Renovierungshistorie (was wurde wann gemacht?)")
        maintenance_schedule = st.text_area("Wartungsplan (Häufigkeit der Überprüfungen)")

    # 3.5 Rechtliche & Finanzielle Informationen
    with tab_legal:
        st.subheader("Rechtliche & Finanzielle Informationen")
        ownership_status = st.selectbox("Eigentumsstatus", ["Eigentum", "Erbpacht"])
        existing_tenancies = st.text_area("Bestehende Mietverhältnisse (Konditionen, falls vermietet)")
        mortgage_details = st.text_area("Hypothekendetails (ausstehende Hypotheken oder Pfandrechte)")
        annual_property_taxes = st.number_input("Jährliche Grundsteuern", min_value=0.0, value=0.0)

    # 3.6 Markt- & Vergleichsdaten
    with tab_market:
        st.subheader("Markt- & Vergleichsdaten")
        comparable_sales = st.text_area("Vergleichbare Verkäufe (ähnliche, kürzlich verkaufte Objekte)")
        market_trends = st.text_area("Markttrends (Faktoren, die den Immobilienwert beeinflussen)")

    # 3.7 Ertragsmöglichkeiten
    with tab_income:
        st.subheader("Ertragsmöglichkeiten (für Renditeobjekte)")
        current_rental_income = st.number_input("Aktuelle monatliche Mieteinnahmen", min_value=0.0, value=0.0)
        occupancy_rates = st.text_input("Belegungsquoten (historisch)")
        operating_expenses = st.number_input("Jährliche Betriebskosten", min_value=0.0, value=0.0)

    # 3.8 Dokumenten-Uploads
    with tab_docs:
        st.subheader("Dokumenten-Uploads")
        st.write("Laden Sie unterstützende Dokumente hoch, um die Genauigkeit der Bewertung zu verbessern.")
        floor_plans = st.file_uploader("Grundrisse", type=["pdf", "jpg", "png"], accept_multiple_files=True)
        photographs = st.file_uploader("Fotos", type=["jpg", "png"], accept_multiple_files=True)
        energy_certificates = st.file_uploader("Energieausweise", type=["pdf", "jpg", "png"], accept_multiple_files=True)
        renovation_records = st.file_uploader("Renovierungsunterlagen", type=["pdf", "jpg", "png"], accept_multiple_files=True)

    st.write("---")

    # Button zum Auslösen des KI-Bewertungsprozesses
    if st.button("KI-Bewertung abrufen"):
        # In einer echten Anwendung würden Sie hier die gesammelten Daten an Ihr KI-Modell oder eine API senden.
        # Dies ist nur eine simulierte Antwort.
        st.success("KI-Bewertung abgeschlossen! Geschätzter Wert: CHF 1'234'567.- (Beispiel)")

        st.write("Wenn Sie mit der Bewertung zufrieden sind, können Sie Ihr Objekt im Auktionsbereich anbieten.")
