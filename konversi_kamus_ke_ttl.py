import pandas as pd


df = pd.read_excel("Kamus.xlsx")


with open("kamus.ttl", "w", encoding="utf-8") as f:
    f.write("@prefix sk: <http://example.org/sundakuno#> .\n\n")
    for i, row in df.iterrows():
        f.write(f"sk:k{i+1} a sk:Kamus ;\n")
        f.write(f'    sk:sundaKuno """{row["Bahasa Sunda Kuno"]}""" ;\n')
        f.write(f'    sk:indonesia """{row["Bahasa Indonesia"]}""" .\n\n')
