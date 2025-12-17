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
# CHARGER LE FICHIER CSS EXTERNE
# ----------------------------------------------------
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css('style.css')


from PIL import Image
import base64
from io import BytesIO

# Charger et convertir le logo en base64
logo = Image.open("assets/logo.png")
buffered = BytesIO()
logo.save(buffered, format="PNG")
logo_base64 = base64.b64encode(buffered.getvalue()).decode()

components.html(
f"""
<div class="header-container">
    <!-- Logo centré en haut -->
    <div class="logo-wrapper">
        <img src="data:image/png;base64,{logo_base64}" alt="InfiniForma Logo" class="logo-image">
    </div>

    <!-- Titre principal moderne -->
    <div class="main-title">
        Tableau de bord Formations
    </div>

    <!-- Sous-titre élégant -->
    <div class="subtitle">
        Tableau de bord interactif pour analyser les performances et le suivi des formations
    </div>

</div>
""",
height=280
)


# Section de déconnexion avec design moderne - 2 étapes
st.markdown("<div class='logout-section'>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Déconnexion Power BI", use_container_width=True):
        # Ouvrir le modal
        @st.dialog("Déconnexion Power BI")
        def show_logout_modal():
            st.markdown("""
            <div class="modal-content">
                <p class="modal-text">
                    Pour vous déconnecter complètement de Power BI :
                </p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("**Étape 1 :** [Se déconnecter de Microsoft](https://login.microsoftonline.com/common/oauth2/v2.0/logout)")
            st.markdown("**Étape 2 :** [Retour au dashboard](http://localhost:8501/)")

            st.markdown("<br>", unsafe_allow_html=True)

            if st.button("Fermer", use_container_width=True):
                st.rerun()

        show_logout_modal()

st.markdown("</div>", unsafe_allow_html=True)


st.markdown("""
<div class="dashboard-wrapper">
    <div class="dashboard-header">
        <span>Dashboard Power BI - Formations et Performance</span>
    </div>
    <div class="iframe-container">
        <iframe
            src="https://app.powerbi.com/reportEmbed?reportId=af6e6ebb-7e30-4971-a7a9-7348f7ca25cb&autoAuth=true&ctid=604f1a96-cbe8-43f8-abbf-f8eaf5d85730&filterPaneEnabled=false&navContentPaneEnabled=false"
            width="100%"
            height="750"
            frameborder="0"
            allowfullscreen="true"
            class="powerbi-iframe">
        </iframe>
    </div>
</div>
""", unsafe_allow_html=True)