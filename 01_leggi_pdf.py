from pypdf import PdfReader

# funzione per estrarre il testo da un pdf
def leggi_testo_pdf(percorso_file):
    reader = PdfReader(percorso_file)
    testo_completo = ""

    for pagina in reader.pages:
        testo_completo += pagina.extract_text() + "\n"

    return testo_completo


# provo la funzione sui due bandi
testo_bando1 = leggi_testo_pdf("documenti/bando_innovazione_digitale.pdf")
testo_bando2 = leggi_testo_pdf("documenti/bando_giovani_imprenditori.pdf")

print("=== TESTO BANDO 1 ===")
print(testo_bando1[:300])
print("\n=== TESTO BANDO 2 ===")
print(testo_bando2[:300])
