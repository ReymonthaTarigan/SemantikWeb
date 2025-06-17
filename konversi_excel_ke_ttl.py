import pandas as pd

l
df = pd.read_excel("Data.xlsx")


with open("sunda_output.ttl", "w", encoding="utf-8") as f:
    f.write("@prefix sk: <http://example.org/sundakuno#> .\n\n")
    for idx, row in df.iterrows():
        f.write(f"sk:data{row['No.']} a sk:Kalimat ;\n")
        f.write(f'    sk:nomor "{row["No."]}" ;\n')
        f.write(f'    sk:gambar "{row["Gambar Aksara"]}" ;\n')
        f.write(f'    sk:kalimatSundaKuno """{row["Kalimat Sunda Kuno"]}""" ;\n')
        f.write(f'    sk:kalimatIndonesia """{row["Kalimat Bahasa Indonesia"]}""" .\n\n')
