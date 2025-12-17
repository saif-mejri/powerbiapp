import streamlit as st
import streamlit.components.v1 as components


# ----------------------------------------------------
# Configuration de la page
# ----------------------------------------------------
st.set_page_config(
    page_title="Suivi des formations et performance",
    layout="wide"
)

# ----------------------------------------------------
# STYLE INTERFACE MODERNE ET PROFESSIONNEL
# ----------------------------------------------------
st.markdown("""
<style>

/* Police Google */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

/* Fond général */
body {
    background-color: #f8fafc;
    font-family: 'Inter', sans-serif;
}

/* Conteneur principal */
section[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
    background-attachment: fixed;
}

/* Barre du haut */
header[data-testid="stHeader"] {
    background-color: transparent;
    border-bottom: none;
}

/* Espacement */
.block-container {
    padding: 3rem 4rem;
    max-width: 1400px;
    margin: 0 auto;
}

/* Titre principal - FIXÉ */
h1 {
    color: #ffffff !important;
    font-weight: 800 !important;
    font-size: 2.8rem !important;
    margin-bottom: 1rem !important;
    letter-spacing: -0.5px !important;
    text-shadow: 0 2px 10px rgba(0,0,0,0.3) !important;
}

/* Sous-titre */
h3 {
    color: #e2e8f0 !important;
    font-weight: 500 !important;
    font-size: 1.2rem !important;
    line-height: 1.6 !important;
    margin-bottom: 2rem !important;
}

/* Texte général */
p {
    color: #cbd5e1;
    font-size: 15px;
}

/* Bouton Streamlit personnalisé */
.stButton > button {
    background: linear-gradient(135deg, #dc2626 0%, #991b1b 100%) !important;
    color: #ffffff !important;
    border: none !important;
    padding: 12px 28px !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    font-size: 16px !important;
    transition: all 0.3s ease !important;
    cursor: pointer !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%) !important;
}

/* Messages d'alerte - WARNING */
div[data-baseweb="notification"] {
    background: #fef3c7 !important;
    border-left: 4px solid #d97706 !important;
    border-radius: 10px !important;
    padding: 1.2rem !important;
    margin: 1rem 0 !important;
    color: #78350f !important;
}

div[data-baseweb="notification"] svg {
    fill: #d97706 !important;
}

/* Messages INFO */
.element-container:has(.stAlert) {
    background: #dbeafe !important;
    border-left: 4px solid #2563eb !important;
    border-radius: 10px !important;
    padding: 1.2rem !important;
    color: #1e3a8a !important;
}

/* Liens stylisés */
a {
    color: #3b82f6 !important;
    font-weight: 600 !important;
    text-decoration: none !important;
    transition: all 0.3s ease;
    padding: 10px 18px;
    border-radius: 8px;
    background: rgba(59, 130, 246, 0.15);
    display: inline-block;
    margin: 8px 5px;
    border: 2px solid #3b82f6;
}

a:hover {
    background: rgba(59, 130, 246, 0.25) !important;
    transform: translateX(5px);
    color: #2563eb !important;
}

/* Carte pour l'iframe */
.iframe-container {
    background: white;
    border-radius: 12px;
    padding: 1rem;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
    margin-top: 2rem;
}

/* Footer Streamlit */
footer {
    visibility: hidden;
}

/* Animation fade-in */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.block-container > div {
    animation: fadeIn 0.6s ease-out;
}

/* Forcer la couleur du texte dans les alertes */
.stAlert p, .stAlert div, .stAlert span {
    color: #78350f !important;
}

/* Forcer la couleur dans les info boxes */
div[data-testid="stMarkdownContainer"] p {
    color: #1e3a8a !important;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# CONTENU TEXTE (FR)
# ----------------------------------------------------
components.html(
"""
<div style="
    text-align: center;
    margin-top: 3.5rem;
    margin-bottom: 3rem;
    font-family: 'Inter', sans-serif;
">

    <div style="
        font-size: 3rem;
        font-weight: 800;
        color: white;
        letter-spacing: -0.6px;
        line-height: 1.2;
        margin-bottom: 1.2rem;
        text-shadow: 0 3px 18px rgba(0,0,0,0.45);
    ">
        Suivi des formations et performance<br>
        par agence
    </div>

    

</div>
""",
height=260
)


# Bouton de déconnexion avec style
if st.button("🔒 Déconnexion Power BI"):
    st.warning("⚠️ **Pour vous déconnecter complètement de Power BI :**")
    st.markdown("**Étape 1 :** [🚪 Se déconnecter de Microsoft](https://login.microsoftonline.com/common/oauth2/v2.0/logout)")
    st.markdown("**Étape 2 :** [🏠 Retour au dashboard](https://powerbiapp-mbpdmgw92qprsd8as5m248.streamlit.app/?fbclid=IwY2xjawOvXqBleHRuA2FlbQIxMQBzcnRjBmFwcF9pZAEwAAEeIe-gA7jo9YIjbPQwgoTBp2_IjjeBuE4go2vWwLE_sZV342gHlMxbM4j6e58_aem_eLsM6Do0_Ekud3NLx67x5w)")

st.markdown("<br>", unsafe_allow_html=True)

# ----------------------------------------------------
# IFRAME AVEC CARTE ÉLÉGANTE
# ----------------------------------------------------
st.markdown("""
<div class="iframe-container">
<iframe
    src="https://app.powerbi.com/reportEmbed?reportId=af6e6ebb-7e30-4971-a7a9-7348f7ca25cb&autoAuth=true&ctid=604f1a96-cbe8-43f8-abbf-f8eaf5d85730&filterPaneEnabled=false&navContentPaneEnabled=false"
    width="100%"
    height="650"
    frameborder="0"
    allowfullscreen="true">
</iframe>
</div>
""", unsafe_allow_html=True)