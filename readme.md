#  Aplikasi Semantik Web Sunda Kuno ↔ Indonesia

Aplikasi ini merupakan **penerjemah prasasti dan kamus Sunda Kuno ke Bahasa Indonesia dan sebaliknya**, yang dibangun menggunakan **Apache Jena** sebagai basis data RDF (triple store) dan **Streamlit** sebagai antarmuka pengguna.

---

## 📂 Struktur Proyek
```
SemantikWeb/
│
├── PrasastiBatuTulis.ttl    # File RDF untuk data kalimat prasasti
├── KamusSundaKuno.ttl       # File RDF untuk data kamus
├── app.py                   # Aplikasi Streamlit 
├── Data.xlsx                # Berisi data prasasti Batutulis
├── Kamus.xlsx               # Berisi data kamus sunda kuno
└── README.md                # Dokumentasi ini
```


---

## 🧩 Prasyarat

Sebelum memulai, pastikan Anda telah menginstal:

- **Python** (disarankan versi 3.8+)
- **Java JDK** (karena Apache Jena berbasis Java)
- **Apache Jena Fuseki**
- **pip** (Python package installer)

---

## 🔧 Langkah-langkah Instalasi & Menjalankan Aplikasi

### 1.  Install Apache Jena Fuseki

1. Unduh Apache Jena Fuseki:  
   [https://jena.apache.org/download/index.cgi](https://jena.apache.org/download/index.cgi)

2. Ekstrak dan buka folder Fuseki:

```
unzip apache-jena-fuseki-*.zip
cd apache-jena-fuseki-*/
```
3. Jalankan Fuseki Server

```
./fuseki-server
```

Fuseki akan berjalan di http://localhost:3030


### 2.  Upload File RDF (.ttl) ke Fuseki

1. Akses Fuseki di browser: http://localhost:3030

2. Klik tombol "Add new dataset".

3. Buat dua dataset (secara terpisah):

- PrasastiBatuTulis

- KamusSundaKuno

4. Setelah membuat masing-masing dataset, klik Upload data dan upload file .ttl yang sesuai:

- Upload PrasastiBatuTulis.ttl ke dataset PrasastiBatuTulis

- Upload KamusSundaKuno.ttl ke dataset KamusSundaKuno



### 3.  Install Dependencies Python

```
pip install streamlit SPARQLWrapper
```

### 4.  Jalankan Aplikasi
```
streamlit run app.py
```
Akses di browser: http://localhost:8501


### Fitur Aplikasi





