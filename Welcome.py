import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)
st.sidebar.success("Select a demo above.")

def main():
    st.title("Selamat Datang di Proyek Pertanian Presisi :seedling:")
    st.write("Proyek ini bertujuan untuk membantu petani dalam memilih tanaman yang cocok untuk ditanam berdasarkan kondisi tanah dan lingkungan sekitar.")
    
    st.header("Business Understanding")
    st.subheader("Problem Statements :thinking_face:")
    st.write("Diberikan sebuah input berupa fitur nutrisi tanah seperti NPK, kelembapan, temperatur, jumlah pH, jumlah curah hujan. Kemudian output yang diharapkan adalah sebuah label tanaman. Rumusan masalahnya adalah bagaimana kita dapat mengklasifikasikan tanaman yang cocok untuk ditanam berdasarkan input fitur yang ada.")
    
    st.subheader("Goals :dart:")
    st.write("- Dapat memprediksi jenis tanaman yang cocok untuk ditanam.")
    st.write("- Memudahkan petani memilih tanaman yang akan ditanam.")
    st.write("- Membantu para petani dalam penggunaan sumber daya.")
    
    st.subheader("Solution Statements :computer:")
    st.write("Berdasarkan problem statements yang ada yaitu pengklasifikasian tanaman yang cocok untuk ditanam, saya menggunakan salah satu algoritma machine learning yaitu Support Vector Machine.")

    st.write("Untuk menjalankan aplikasi, Anda dapat melihat sidebar di sebelah kiri. Di sana, Anda akan menemukan kolom untuk memasukkan nilai-nilai nutrisi tanah dan lingkungan, dan aplikasi akan memprediksi jenis tanaman yang cocok untuk ditanam.")
if __name__ == "__main__":
    main()
