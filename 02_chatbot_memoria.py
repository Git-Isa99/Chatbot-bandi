from pypdf import PdfReader
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)


def leggi_testo_pdf(percorso_file):
    reader = PdfReader(percorso_file)
    testo_completo = ""
    for pagina in reader.pages:
        testo_completo += pagina.extract_text() + "\n"
    return testo_completo


bando1 = leggi_testo_pdf("documenti/bando_innovazione_digitale.pdf")
bando2 = leggi_testo_pdf("documenti/bando_giovani_imprenditori.pdf")

contesto = f"""
--- DOCUMENTO 1: Bando Innovazione Digitale ---
{bando1}

--- DOCUMENTO 2: Bando Giovani Imprenditori ---
{bando2}
"""

system_prompt = f"""
Sei un assistente esperto di finanza agevolata.
Rispondi alle domande dell'utente usando ESCLUSIVAMENTE le informazioni
contenute nei documenti forniti qui sotto.
Se l'informazione richiesta non è presente nei documenti, rispondi
onestamente "Non trovo questa informazione nei documenti disponibili."
Non inventare mai dati, cifre o requisiti.
Cita sempre a quale bando ti stai riferendo nella risposta.

DOCUMENTI DISPONIBILI:
{contesto}
"""

# il modello non ha memoria sua, quindi ad ogni chiamata gli rimando
# tutta la lista dei messaggi scambiati finora, non solo l'ultima domanda
cronologia = [
    {"role": "system", "content": system_prompt}
]

print("Chatbot pronto. Scrivi 'esci' per terminare.\n")

while True:
    domanda = input("Tu: ")

    if domanda.lower() == "esci":
        print("Chatbot chiuso. A presto!")
        break

    cronologia.append({"role": "user", "content": domanda})

    risposta = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=cronologia,
    )

    testo_risposta = risposta.choices[0].message.content
    print(f"\nChatbot: {testo_risposta}\n")

    cronologia.append({"role": "assistant", "content": testo_risposta})
