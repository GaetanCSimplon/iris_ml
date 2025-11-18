import streamlit as st 
import requests
import os

# Adresse locale de l'API - Route POST /predict
## URL dynamique
BACKEND_HOST = os.environ.get("BACKEND_URL", "http://127.0.0.1:8000")
API_URL = f"{BACKEND_HOST}/predict"

st.set_page_config(page_title="Iris ML", layout="wide")

st.title("Iris - ML")
st.markdown("""
            Dis-moi comment est ton iris, je te dirai son nom.
            
            Entrez la longueur et la largeur du sépale de votre Iris ainsi que celles de ses pétales. 
            """)

with st.form("iris_form"):
    # En paramètre du slider, dans l'ordre : min_value, max_value, default_value, step
    sepal_length = st.slider("Longueur du sépale (cm)", 4.0, 8.0, 5.1, step=0.1)
    sepal_width = st.slider("Largeur du sépale (cm)", 2.0, 5.0, 3.5, step=0.1)
    petal_length = st.slider("Longueur du pétale (cm)", 1.0, 7.0, 1.4, step=0.1)
    petal_width = st.slider("Largueur du pétale (cm)", 0.1, 3.0, 0.2, step=0.1)
    
    # Bouton de soumission du formulaire
    submitted = st.form_submit_button("Prédire")


if submitted:
    
    iris_data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }
    
    st.write("Envoi des données à l'API...")
    
    try:
        response = requests.post(API_URL, json=iris_data)
        
        if response.status_code == 200:
            result = response.json()
            prediction = result['prediction_class']
            
            st.success(f"D'après le modèle, c'est une **{prediction}** !")
        else:
            st.error(f"Erreur de l'API : {response.status_code}")
            st.write(response.text)
    except requests.exceptions.ConnectionError:
        st.error("Impossible de contacter l'API. Vérifier que le backend est bien lancé sur le port 8000.")
    