import streamlit as st
import pandas as pd

st.set_page_config(page_title="Voedingskeuze Calculator", layout="wide")
st.markdown(
    "<style>iframe { width: 100%; height: 600px; }</style>", unsafe_allow_html=True
)

# Dataset: Voedingsmiddelen en kcal per gram
voedingsmiddelen_kcal = {
    "Basmati rijst (ongekookt)": 3.6,
    "Zilvervliesrijst (ongekookt)": 3.6,
    "Jasmijnrijst (ongekookt)": 3.8,
    "Wilde rijst (ongekookt)": 3.2,
    "Arborio rijst (ongekookt)": 3.8,
    "Kipfilet (rauw)": 1.3,
    "Kalkoenfilet (rauw)": 1.3,
    "Rundvlees (mager, rauw)": 1.4,
    "Magere kwark": 0.58,
    "Volle melk": 0.6,
    "Amandelmelk (ongezoet)": 0.2,
    "Olijfolie": 8.9,
    "Pindakaas (100% pinda's)": 6.5,
    "Honing": 3.5,
}

def bereken_vervanging(huidig_voedingsmiddel, huidige_hoeveelheid, vervangend_voedingsmiddel):
    if huidig_voedingsmiddel in voedingsmiddelen_kcal and vervangend_voedingsmiddel in voedingsmiddelen_kcal:
        kcal_huidig = voedingsmiddelen_kcal[huidig_voedingsmiddel] * huidige_hoeveelheid
        vervangende_hoeveelheid = kcal_huidig / voedingsmiddelen_kcal[vervangend_voedingsmiddel]
        return round(vervangende_hoeveelheid, 1)
    else:
        return None

# Streamlit UI
st.title("Vervangende Voedingskeuzes Calculator")

huidig_voedingsmiddel = st.selectbox("Kies het huidige voedingsmiddel", list(voedingsmiddelen_kcal.keys()))
huidige_hoeveelheid = st.number_input("Hoeveel gram/milliliter eet je nu?", min_value=1.0, step=1.0)
vervangend_voedingsmiddel = st.selectbox("Kies het vervangende voedingsmiddel", list(voedingsmiddelen_kcal.keys()))

if st.button("Bereken Vervanging"):
    resultaat = bereken_vervanging(huidig_voedingsmiddel, huidige_hoeveelheid, vervangend_voedingsmiddel)
    if resultaat:
        st.success(f"Je kunt {huidige_hoeveelheid} gram {huidig_voedingsmiddel} vervangen door {resultaat} gram {vervangend_voedingsmiddel}.")
    else:
        st.error("Voedingsmiddel niet gevonden in de dataset. Controleer je invoer.")
