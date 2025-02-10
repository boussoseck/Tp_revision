import streamlit as st
from pages import prediction_page, clustering_page
# Injecter du CSS personnalisé pour un affichage en plein écran

st.set_page_config(layout="wide")
# Ajout de logo
st.sidebar.image("logodit.jpg", width=2000)
st.markdown(
    """
    <style>
    .main > div {
        max-width: 100%;
        padding-left: 1rem;
        padding-right: 1rem;
    }
    .stButton > button {
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Titre de l'application
st.title("Mon Application de Machine Learning By Afdel Desmond")



# Navbar avec des boutons en bloc
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    if st.button("Accueil"):
        st.session_state.page = "Accueil"
with col2:
    if st.button("À propos"):
        st.session_state.page = "À propos"


st.markdown("---")

# Vérifier si une page est sélectionnée, sinon mettre "Accueil" par défaut
if "page" not in st.session_state:
    st.session_state.page = "Accueil"

# Pages
if st.session_state.page == "Accueil":
    st.header("Accueil")
    st.subheader("✨Bienvenue sur Mon Application de Machine Learning✨")
    st.write("💡 Plongez dans la puissance de l'IA en un clic 🤖📊 : prédisez le risque de diabète grâce à des modèles intelligents 🩺📈, explorez vos données avec des techniques de clustering fascinantes 🎨🔬, analysez vos propres fichiers CSV pour en tirer des insights précieux 📊📂. 🚀 Utilisez les boutons ci-dessous pour naviguer et libérez tout le potentiel du Machine Learning ! 🔎✨📈")
 
    # Boutons pour rediriger vers les différentes pages
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅Prédire le diabète 🩺"):
            st.session_state.page = "Prédiction du Diabète"
    with col2:
        if st.button("✅Explorer le clustering 🎨"):
            st.session_state.page = "Clustering"
    st.markdown("---")

elif st.session_state.page == "À propos":
    st.header("🔍 À propos de l'application")
    st.write("Bienvenue dans notre **Application de Machine Learning** dédiée à la **Prédiction du Diabète** ! 🩺💡")
    st.write("""
        Cette application utilise des **modèles d'Intelligence Artificielle** avancés pour prédire le risque de diabète, en fonction de critères médicaux spécifiques. 
        Grâce à des algorithmes puissants comme **SVM** 🤖, **Régression Logistique** 📊 et **KNN** 🧠, vous pouvez obtenir des résultats fiables et rapides en saisissant simplement les informations médicales du patient.
    """)
    st.write("""
        **💎 Fonctionnalités clés :**
        - **Prédiction du diabète** : Prédisez si un patient est susceptible de développer le diabète en fonction de ses données médicales.
        - **Clustering avec KMeans** : Découvrez les **clusters** cachés dans vos données grâce à l'algorithme **KMeans** 🎨, qui permet de regrouper les données en différentes catégories et de visualiser les tendances en 2D et 3D. 📉📈
        - **Analyse de données** : Chargez vos fichiers **CSV** 📂 et explorez-les pour obtenir des **insights** précieux sur vos données ! 🔍
    """)
    st.write("""
        Cette application a été conçue pour **démontrer la puissance du Machine Learning** dans le domaine de la santé, tout en facilitant l'analyse des données pour les utilisateurs. 
        **Facile à utiliser, rapide et efficace**, elle est idéale pour ceux qui veulent intégrer l'IA dans leurs pratiques médicales. 🌟
    """)
    # st.write("""
    #     **Développée avec soin et passion**, cette application vous permet de naviguer à travers des modèles d'IA et des outils d'analyse pour améliorer vos prises de décision et gagner du temps. 🚀
    # """)
    # Boutons pour rediriger vers les différentes pages
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅Prédire le diabète 🩺"):
            st.session_state.page = "Prédiction du Diabète"
    with col2:
        if st.button("✅Explorer le clustering 🎨"):
            st.session_state.page = "Clustering"
    st.markdown("---")

elif st.session_state.page == "Prédiction du Diabète":
    st.header("Prédiction du Diabète")
    st.write("Cette page permet de prédire le diabète en utilisant différents modèles de Machine Learning.")
    # Importer la page de prédiction
    from pages import prediction_page
    prediction_page.show()
    
elif st.session_state.page == "Clustering":
    st.header("Clustering")
    st.write("Cette page permet de visualiser les résultats de clustering en 2D et 3D.")
    # Importer la page de clustering
    from pages import clustering_page
    clustering_page.show()