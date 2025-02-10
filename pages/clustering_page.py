import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import plotly.express as px
import joblib
from sklearn.metrics import silhouette_score

def show():
    # Options des modèles
    model_options = {
        "Modèle KMeans cluster ": "kmeans_model.pkl",
       # "Modèle KMeans (sans normalisation, avec date)": "kmeans_model_.pkl",
       # "Modèle KMeans n°2 ": "kmeans_model_norm.pkl",
       # "Modèle KMeans (avec normalisation, avec date)": "kmeans_model_with_date_norm.pkl"
    }

    # Sélection du modèle avec une liste déroulante
    selected_model = st.selectbox("Sélectionnez un modèle de clustering :", list(model_options.keys()))

    # Titre de la page
    st.title("📊 Clustering des Données de Publication")

    # Charger les données
    @st.cache_data
    def load_data():
        df = pd.read_csv('pages/datas/Live_20210128.csv')
        df['status_published'] = pd.to_datetime(df['status_published'], errors='coerce')
        return df

    df = load_data()

    # Séparateur
    st.markdown("---")

    # Affichage des données
    st.write("### Aperçu des données 📄")
    st.dataframe(df.head())

    # Description des modèles
    model_descriptions = {
        "Modèle KMeans n°1 ": "Ce modèle utilise les données brutes sans normalisation et exclut la colonne 'status_published'.",
        #"Modèle KMeans (sans normalisation, avec date)": "Ce modèle utilise les données brutes sans normalisation et inclut la colonne 'status_published'.",
        #"Modèle KMeans (avec normalisation, sans date)": "Ce modèle normalise les données et exclut la colonne 'status_published'.",
        "Modèle KMeans n°2 ": "Ce modèle normalise les données et inclut la colonne 'status_published'.",
    }

    st.write("### 🛠️ Description du modèle sélectionné")
    st.info(model_descriptions[selected_model])

    # Préparation des données
    df_processed = df.drop(['Column1', 'Column2', 'Column3', 'Column4', 'status_id'], axis=1)

    # Gestion de la colonne 'status_published'
    if "avec date" in selected_model:
        df_processed['year'] = df['status_published'].dt.year.astype(float)
        df_processed['month'] = df['status_published'].dt.month.astype(float)
        df_processed['day'] = df['status_published'].dt.day.astype(float)
        df_processed['hour'] = df['status_published'].dt.hour.astype(float)
        df_processed['minute'] = df['status_published'].dt.minute.astype(float)
        df_processed = df_processed.drop(['status_published'], axis=1)
    else:
        df_processed = df_processed.drop(['status_published'], axis=1)

    # Encoder la colonne catégorielle
    le = LabelEncoder()
    df_processed['status_type'] = le.fit_transform(df_processed['status_type'])

    # Normalisation si nécessaire
    if "avec normalisation" in selected_model:
        scaler = MinMaxScaler()
        df_processed = pd.DataFrame(scaler.fit_transform(df_processed), columns=df_processed.columns)
    
    # Appliquer PCA
    pca = PCA(n_components=3)
    features_pca = pca.fit_transform(df_processed.values)
    new_df = pd.DataFrame(features_pca, columns=['PCA1', 'PCA2', 'PCA3'])

    # Charger le modèle KMeans
    kmeans_model = joblib.load(model_options[selected_model])

    # Prédire les clusters
    clusters = kmeans_model.predict(df_processed.values)

    # Calcul du Silhouette Score
    sil_score = silhouette_score(df_processed.values, clusters)
    st.write(f"### 📊 Silhouette Score : `{sil_score:.2f}`")

    # Visualisation des clusters en 3D
    st.write("### 📉 Visualisation des Clusters en 3D")
    fig = px.scatter_3d(new_df, x='PCA1', y='PCA2', z='PCA3', color=clusters.astype(str))
    st.plotly_chart(fig)

    # Visualisation des clusters en 2D
    st.write("### 📈 Visualisation des Clusters en 2D")
    fig = px.scatter(new_df, x='PCA1', y='PCA2', color=clusters.astype(str))
    st.plotly_chart(fig)

    # Afficher le nombre d'observations par cluster
    st.write("### 📊 Nombre d'observations par cluster")
    val = pd.Series(clusters).value_counts()
    st.bar_chart(val)

    # Afficher et télécharger les données d'un cluster spécifique
    st.write("### 🔍 Données d'un Cluster Spécifique")
    cluster = st.number_input("Entrez le numéro du cluster (0 à 5) :", min_value=0, max_value=5, value=0)
    cluster_data = df_processed[clusters == cluster]
    st.dataframe(cluster_data)
    
    # Bouton de téléchargement
    csv = cluster_data.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Télécharger ce cluster", csv, f"cluster_{cluster}.csv", "text/csv")

# Lancer l'affichage si ce fichier est exécuté directement
if __name__ == "__main__":
    show()