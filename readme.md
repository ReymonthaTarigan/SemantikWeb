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

Contoh terminal setelah menjalankan Fuseki Server

![image](https://github.com/user-attachments/assets/9788b254-796c-419e-a6a3-50785dcce1a7)


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

![image](https://github.com/user-attachments/assets/6e4148b2-7b83-42f2-95ef-3c36d76619e3)


### 3.  Install Dependencies Python

```
pip install streamlit SPARQLWrapper
```

### 4.  Jalankan Aplikasi
```
streamlit run app.py
```
Akses di browser: http://localhost:8501


---

## Fitur Aplikasi

Tampilan Awal Aplikasi

![image](https://github.com/user-attachments/assets/11bf2249-4f6c-4161-a277-cc3445556442)

1.Terjemahan Prasasti Batutulis

User dapat memasukkan kata atau kalimat dalam bahasa Indonesia atau bahasa Sunda Kuno dalam kolom pencarian lalu tekan enter. Untuk melihat daftar databasenya, dapat dilihat di Data.xlsx. Setelah memberikan masukan, akan ditampilkan baris prasasti ke berapa, gambar asli di prasastinya, teks sunda kunonya, dan terjemahan bahasa Indonesianya. Contohnya disini saya memasukkan kata "Raja". Hasilnya sebagai berikut.

![image](https://github.com/user-attachments/assets/925cee2a-f70a-46c9-b90a-85b8abbc7cc3)
![image](https://github.com/user-attachments/assets/00a11854-bf16-4185-826a-ab08e66dcc43)

2. Kamus Sunda Kuno

User dapat memasukkan kata atau kalimat  dalam kolom pencarian lalu tekan enter. Untuk melihat daftar databasenya, dapat dilihat di Kamus.xlsx. Setelah memberi masukan, akan ditampilkan kata dalam bahasa Sunda Kuno dan artinya dalam bahasa Indonesia. User dapat memasukkan kata bahasa Sunda Kuno ataupun bahasa Indonesia. Program akan menampilkan data yang mengandung kata yang dimasukkan oleh user. Contohnya disini saya memasukkan kata "Bumi" sehingga hasilnya sebagai berikut :

![image](https://github.com/user-attachments/assets/7ca6666c-2ce2-417f-ab3c-01cfc9e1ebc6)
![image](https://github.com/user-attachments/assets/c958e2ba-beac-4769-bee8-756d67ca7543)
![image](https://github.com/user-attachments/assets/4ada5eae-b8ea-4843-9a10-96d9270720a1)


---

## Sumber Data

- **Prasasti Batutulis** : https://id.wikipedia.org/wiki/Prasasti_Batutulis
- **Kamus Sunda Kuno** : https://jurnal.unpad.ac.id/sosiohumaniora/article/view/19436

   








