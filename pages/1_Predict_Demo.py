import pickle
import joblib
import streamlit as st
import pyautogui

with open('assets/labelencoder/label_encoder_bahasaIndonesia_v2.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

with open('assets/model/svm_model_v2.pkl', 'rb') as f:
    model = pickle.load(f)

with open('assets/scaler/scaler_v2.pkl', 'rb') as f:
    scaler = joblib.load(f)

def predict(nitrogen, fosfor, kalium, suhu, kelembapan, ph, curah_hujan):
    data = [[nitrogen, fosfor, kalium, suhu, kelembapan, ph, curah_hujan]]
    data = scaler.transform(data)
    pred = model.predict(data)
    y_pred_label = label_encoder.inverse_transform(pred)
    return y_pred_label

import streamlit as st

st.set_page_config(
    page_title="Predict Demo",
    page_icon="",
)

st.sidebar.header("Machine Learning Demo")

st.title("    :blue[Crop Recommendation] :seedling:",)
st.write("## Input Data untuk Model Machine Learning")

 # Membagi layar menjadi dua kolom
col1, col2 = st.columns(2)

# Kolom pertama
with col1:
    # Field input untuk nitrogen
    nitrogen = st.number_input("Nitrogen", placeholder="Ketikkan Angka", value=None, min_value=0)

    # Field input untuk fosfor
    fosfor = st.number_input("Fosfor", placeholder="Ketikkan Angka", value=None, min_value=0)

    # Field input untuk kalium
    kalium = st.number_input("Kalium", placeholder="Ketikkan Angka", value=None, min_value=0)

    # Field input untuk curah hujan
    curah_hujan = st.number_input("Curah Hujan", placeholder="Ketikkan Angka", value=None, min_value=0)

# Kolom kedua
with col2:
    # Field input untuk suhu
    suhu = st.number_input("Suhu", placeholder="Ketikkan Angka", value=None, min_value=0)

    # Field input untuk kelembapan
    kelembapan = st.number_input("Kelembapan", placeholder="Ketikkan Angka", value=None, min_value=0)

    # Field input untuk pH
    ph = st.number_input("pH", placeholder="Ketikkan Angka", value=None, min_value=0)

col1, col2 = st.columns([1,4])

# Tombol untuk melakukan prediksi
if st.button(":green[Prediksi]", type='secondary'):
        # Periksa apakah semua field sudah diisi
        if None in (nitrogen, fosfor, kalium, suhu, kelembapan, ph, curah_hujan):
            st.warning("Harap isi semua field sebelum melakukan prediksi!")
        else:
            # Panggil fungsi untuk melakukan prediksi dengan input yang diberikan
            st.write("### Model Sedang melakukan prediksi ...")
            label = predict(nitrogen, fosfor, kalium, suhu, kelembapan, ph, curah_hujan)
            st.write(f"Tanaman yang cocok ditanam adalah **Tanaman {label[0]}**")
            st.write("Done...!!! :smile:")
# Tombol untuk mereset nilai input menjadi default
if st.button("Reset", type='primary'):
    pyautogui.hotkey("ctrl","F5")
    

