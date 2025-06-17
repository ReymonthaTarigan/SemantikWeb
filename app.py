import streamlit as st
from SPARQLWrapper import SPARQLWrapper, JSON

# ===== Fungsi Query Kalimat (Prasasti Batu Tulis) =====
def search_kalimat(kata):
    sparql = SPARQLWrapper("http://localhost:3030/PrasastiBatuTulis/sparql")
    query = f"""
    PREFIX sk: <http://example.org/sundakuno#>

    SELECT ?no ?kalimat ?arti ?gambar WHERE {{
        ?s a sk:Kalimat ;
           sk:nomor ?no ;
           sk:kalimatSundaKuno ?kalimat ;
           sk:kalimatIndonesia ?arti ;
           sk:gambar ?gambar .
        FILTER (
            CONTAINS(LCASE(?kalimat), LCASE("{kata}")) ||
            CONTAINS(LCASE(?arti), LCASE("{kata}"))
        )
    }}
    ORDER BY ?no
    """
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results["results"]["bindings"]

# ===== Fungsi Query Kamus =====
def search_kamus(kata):
    sparql = SPARQLWrapper("http://localhost:3030/KamusSundaKuno/sparql")
    query = f"""
    PREFIX sk: <http://example.org/sundakuno#>

    SELECT ?sunda ?indo WHERE {{
        ?s a sk:Kamus ;
           sk:sundaKuno ?sunda ;
           sk:indonesia ?indo .
        FILTER (
            CONTAINS(LCASE(?sunda), LCASE("{kata}")) || 
            CONTAINS(LCASE(?indo), LCASE("{kata}"))
        )
    }}
    ORDER BY ?sunda
    """
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results["results"]["bindings"]

# ===== Tampilan Streamlit (dengan desain lebih baik) =====
st.set_page_config(page_title="Penerjemah Sunda Kuno", layout="centered")
st.markdown("<h1 style='text-align: center; ;'>Aplikasi Semantik Web Sunda Kuno</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Terjemahan Prasasti dan Kamus Sunda Kuno ↔ Indonesia</p>", unsafe_allow_html=True)

fitur = st.selectbox("🔍 Pilih fitur:", ["Terjemahan Prasasti Batutulis", "Kamus Sunda ↔ Indonesia"])
search_term = st.text_input("Masukkan kata (Sunda Kuno atau Indonesia):")

if search_term:
    if fitur == "Terjemahan Prasasti Batutulis":
        hasil = search_kalimat(search_term)
        if hasil:
            for row in hasil:
                st.markdown(
                    f"""
                    <div style=' padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
                        <h4 style=';'>Kalimat #{row['no']['value']}</h4>
                        <img src='{row['gambar']['value']}' width='300'><br><br>
                        <b>Sunda Kuno:</b><br>{row['kalimat']['value']}<br><br>
                        <b>Bahasa Indonesia:</b><br>{row['arti']['value']}
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.warning("❌ Tidak ditemukan hasil untuk kata tersebut.")
    
    elif fitur == "Kamus Sunda ↔ Indonesia":
        hasil = search_kamus(search_term)
        if hasil:
            for row in hasil:
                st.markdown(
                    f"""
                    <div style=' padding: 15px; border-radius: 10px; margin-bottom: 15px;'>
                        <b>Sunda Kuno:</b> {row['sunda']['value']}<br>
                        <b>Bahasa Indonesia:</b> {row['indo']['value']}
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.warning("❌ Tidak ditemukan entri kamus.")
