import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Charger les modèles avec gestion d'erreur
try:
    svm_model = joblib.load("svm_model.pkl")  
    log_reg_model = joblib.load("log_reg_model.pkl")  
    knn_model = joblib.load("knn_model.pkl")  
except Exception as e:
    st.error(f"Erreur lors du chargement des modèles : {e}")

# Charger les données pour récupérer les colonnes de caractéristiques
data = pd.read_csv("diabetes.csv")  
feature_columns = [col for col in data.columns if col.lower() != "outcome"]

# Fonction de prédiction
def predict_diabetes(model, input_data):
    prediction = model.predict(np.array(input_data).reshape(1, -1))
    return "Patient Diabétique" if prediction[0] == 1 else "Patient Non diabétique"

# Interface utilisateur
def show():
    st.title("🩺 Prédiction du Diabète")
    st.markdown("""
        <div style="background-color: #f8f9fa; padding: 10px; border-radius: 10px; text-align: center;">
        💡 Entrez les informations médicales et obtenez une prédiction basée sur l'IA.
        </div>
    """, unsafe_allow_html=True)

    # Diviser l'écran en 3 parties (50% - 50%)
    left_col, center_col, right_col = st.columns([6, 1, 3])

    with left_col:
        st.subheader("📊 Informations du Patient")

        # Diviser la section de saisie en deux colonnes
        col1, col2 = st.columns(2)
        user_inputs = []

        # Remplir les deux colonnes avec 4 champs chacune
        for i, feature in enumerate(feature_columns):
            with (col1 if i < 4 else col2):
                value = st.number_input(
                    f"{feature} 🔍", 
                    min_value=0.0, 
                    max_value=1000.0, 
                    step=0.1, 
                    help=f"Entrez la valeur de {feature}"
                )
                user_inputs.append(value)

    with right_col:
        st.subheader("🤖 Modèle & Résultat")
        
        # Choix du modèle
        model_choice = st.radio(
            "Sélectionnez un modèle :", 
            ["SVM", "Régression Logistique", "KNN"], 
            index=0
        )

        # Bouton de prédiction
        if st.button("⚡ Faire la Prédiction", help="Cliquez pour obtenir une analyse IA"):
            if None not in user_inputs:  # Vérification des entrées (évite les valeurs manquantes)
                model_dict = {
                    "SVM": svm_model,
                    "Régression Logistique": log_reg_model,
                    "KNN": knn_model
                }
                model = model_dict.get(model_choice)

                if model:
                    result = predict_diabetes(model, user_inputs)

                    # Affichage du résultat
                    if result == "Patient Diabétique":
                        st.error(f"🚨 **Résultat : {result}** ❌")
                    else:
                        st.success(f"✅ **Résultat : {result}** 🎉")
                else:
                    st.error("⚠️ Erreur : modèle non disponible.")
            else:
                st.warning("⚠️ **Veuillez remplir toutes les valeurs avant de prédire.**")

# Lancer l'application si exécuté directement
if __name__ == "__main__":
    show()
