import streamlit as st

#Configuration de la page
st.set_page_config(
    page_title = "Boubou SY - PORTFOLIO",
    layout = "wide"
)

#Ma partie sidebar
with st.sidebar:
    with st.container(border=True):
        st.image("3.jpg")

    with st.container(border=True):
        st.header("CONTACTS ✆")
    st.markdown("""
    **Nom**: *SY*

    **Prenom**: *Boubou*
    
    **Téléphone 📞**: *+221763315871*

    **Email 📧**:*bouboujaddel19@gmail.com*
    """)

    url_linkedin = "https://www.linkedin.com/in/boubou-sy-32107121a/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3BFynQEFPGS42qJIWUg7yFig%3D%3D"

    # Afficher un badge cliquable
    st.markdown(f"[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)]({url_linkedin})")
    
    st.divider()

    #Mon parcours académique
    with st.container(border=True):
        st.title("EDUCATION 🎓")
    st.markdown("""
    * **2025-2027**: *BTS Géomatique au Centre d'Entrepreunariat et de Développement Technique (CEDT) le "LE G15".*
    
    * **2024-2025**: *Master 1 en géographie, spécialité Environnement, Territoires, Populations et Santé (ETPS) à l'Université Cheikh Anta Diop de Dakar (UCAD).*
    
    * **2021-2024**: *Licence en Géographie à l'Université Cheikh Anta Diop de Dakar (UCAD).*

    * **2020-2021**: *Baccalauréat en série L2 au Lycée de Mboro.*
    """)
    

# Partie profil
with st.container(border=True):
    st.header("**PROFIL 👨‍💼**")

st.subheader("En tant que technicien Supérieur en Géomatique et Géographe spécialisé en santé environnementale, je mets le webmapping au service de la santé des populations. Mon objectif est de concevoir des cartes interactives performantes pour faciliter la prise de décision face aux enjeux sanitaires et environnementaux actuels.🌍")



#Partie Projet Académique

with st.container(border=True):
    st.header("**PROJETS ACADEMIQUES 🎓**")

st.markdown("""
* Collecte des données de localisation des poteaux électrique, des lampadaires et des gargottes dans le quartier Gueule Tapée/Fass/Colobane à l'aide du logiciel Mobile Topographer puis traitement de ces données avec ArcGIS

* Numérisation du quartier Darou Rakhmane (Mboro) à l'aide du logiciel QGIS.

* Création d'un site web calculateur d'indice de masse corporelle (IMC).

* Traitement de données spatiales et réalisation de cartes de situation via ArcGIS.

* Collecte et traitement des données de l'école CEDT << Le G15 >> et des alentours du mosquée
Massalikou Jinaan grace aux outils Mobile Topographer et ArcGIS.

* Réalisation de plan de maison 2D sur le logiciel Autocad.

* Réalisation de plan de maison 3D sur le logiciel SketchUp.

""")

#Partie Expériences

with st.container(border=True):
    st.header("**EXPERIENCES 👷**")

st.markdown("""
* **De Mai à Juin 2025**: Travailleur journalier chargé du suivi et du relevé des débits des forages hydrauliques à l’Industrie Chimique du Sénégal (ICS).

""")



#Partie Compétence

with st.container(border=True):
    st.header("**COMPETENCES**")
    
st.markdown("""
* **Cartographie 🗺️**

* **Programmation avec Python </>**

* **Dessin de plan d'architecture**

* **Gestion de base de données 🛢️**

* **Développement SIG 🌍**

* **Topographie 📍**

* **Géoréférencement & Numérisation**

* **Collecte de données**
""")


#Partie Outils


with st.container(border=True):
    st.header("OUTILS 🛠️")
    


col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

with col1:
    st.image("ArcGIS_globe.png", caption = "ArcGIS Pro")
with col2:
    st.image("acad.png", caption = "Autocad")
with col3:
    st.image("pyth.png", caption = "Python")
with col4:
    st.image("sketch.png", caption = "Sketchup pro")
with col5:
    st.image("qgis.png", caption = "QGIS")
with col6:
    st.image("kobo.png",caption="KoboCollect")
with col7:
    st.image("mt.png",caption="Mobile Topographer")



#-----------PARTIE PROJETS PERSONNELS--------------

with st.container(border=True):
    st.header("PROJETS PERSONNELS")

st.markdown("""
* Créer une application mobile gratuite pour les services de santé nécessiteux et qui sera dédiée au calcul des Indices de Masses corporelles (IMC). 

""")

#--------------FIN-------------------------------


if st.button("♡"):
    st.balloons()
    st.toast("Je vous remercie de votre visite !✅")






