import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# 🔧 CONFIG GLOBALE
# -------------------------------------------------
st.set_page_config(
    page_title="Dashboard Pro",
    layout="wide",
    page_icon="📊"
)

# -------------------------------------------------
# 🎨 CSS PERSONNALISÉ
# -------------------------------------------------
st.markdown("""
<style>

html, body, [class*="css"]  {
    font-family: 'Inter', sans-serif;
}

/* Header principal */
.big-title {
    font-size: 32px !important;
    font-weight: 800 !important;
    padding: 0;
    margin-bottom: -10px;
}

/* Sous-titre */
.sub-title {
    font-size: 16px !important;
    color: #888;
}

/* Carte statistique */
.stat-card {
    background: #111827;
    padding: 25px;
    border-radius: 15px;
    text-align: left;
    color: white;
    border: 1px solid #1f2937;
    box-shadow: 0px 2px 4px rgba(0,0,0,0.4);
}

.stat-value {
    font-size: 30px;
    font-weight: 700;
}

.stat-label {
    font-size: 14px;
    color: #9ca3af;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# 📌 SIDEBAR
# -------------------------------------------------
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio(
    "Aller à :", 
    ["Dashboard", "Graphiques", "Données", "Paramètres"]
)

st.sidebar.markdown("---")
st.sidebar.info("Dashboard Pro • Streamlit")

# -------------------------------------------------
# 📊 PAGE : DASHBOARD
# -------------------------------------------------
if page == "Dashboard":
    st.markdown('<p class="big-title">📊 Dashboard général</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Vue d’ensemble des statistiques.</p>', unsafe_allow_html=True)
    st.write("")

    # Fake stats
    revenue = "1 254 300 FCFA"
    users = 785
    growth = "12.8 %"
    orders = 4321

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value">{revenue}</div>
            <div class="stat-label">Revenus</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value">{users}</div>
            <div class="stat-label">Utilisateurs actifs</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value">{growth}</div>
            <div class="stat-label">Croissance</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value">{orders}</div>
            <div class="stat-label">Commandes</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.divider()

    st.subheader("📌 Activité récente")
    st.write("Voici les actions les plus récentes dans la plateforme.")
    st.success("Nouvel utilisateur inscrit : *ID-483928*")
    st.info("Nouveau paiement validé : *Commande #1928*")
    st.warning("2 tentatives de connexion échouées détectées.")

# -------------------------------------------------
# 📈 PAGE : GRAPHIQUES
# -------------------------------------------------
elif page == "Graphiques":
    st.markdown('<p class="big-title">📈 Graphiques</p>', unsafe_allow_html=True)
    st.write("")

    # Data aléatoire
    data = pd.DataFrame({
        "jours": np.arange(1, 8),
        "ventes": np.random.randint(50, 200, 7)
    })

    st.subheader("📊 Ventes sur 7 jours")

    fig, ax = plt.subplots()
    ax.plot(data["jours"], data["ventes"])
    ax.set_xlabel("Jour")
    ax.set_ylabel("Ventes")
    ax.set_title("Ventes hebdomadaires")

    st.pyplot(fig)

    st.divider()

    st.subheader("📌 Données brutes")
    st.dataframe(data)

# -------------------------------------------------
# 📄 PAGE : DONNÉES
# -------------------------------------------------
elif page == "Données":
    st.markdown('<p class="big-title">📄 Données</p>', unsafe_allow_html=True)

    df = pd.DataFrame({
        "Utilisateur": ["Sarah", "Kevin", "Moussa", "Aminata"],
        "Commandes": [5, 2, 8, 6],
        "Statut": ["Actif", "Inactif", "Actif", "Actif"]
    })

    st.dataframe(df)

# -------------------------------------------------
# ⚙️ PAGE : PARAMÈTRES
# -------------------------------------------------
elif page == "Paramètres":
    st.markdown('<p class="big-title">⚙️ Paramètres</p>', unsafe_allow_html=True)

    theme = st.selectbox("Thème", ["Sombre", "Clair"])
    notif = st.checkbox("Activer les notifications")
    st.write("")

    st.success("Paramètres enregistrés (en local).")
