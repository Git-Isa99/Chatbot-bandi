import streamlit as st
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


@st.cache_data  # cosi non rilegge i pdf ad ogni messaggio
def carica_contesto():
    bando1 = leggi_testo_pdf("documenti/bando_innovazione_digitale.pdf")
    bando2 = leggi_testo_pdf("documenti/bando_giovani_imprenditori.pdf")
    return f"""
--- DOCUMENTO 1: Bando Innovazione Digitale ---
{bando1}

--- DOCUMENTO 2: Bando Giovani Imprenditori ---
{bando2}
"""


contesto = carica_contesto()

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

st.title("🤖 Assistente Bandi - Finanza Agevolata")
st.caption("Fai domande sui bandi caricati. Il chatbot risponde solo in base ai documenti disponibili.")

# session_state serve per non perdere la cronologia ad ogni ridisegno della pagina
if "cronologia" not in st.session_state:
    st.session_state.cronologia = [
        {"role": "system", "content": system_prompt}
    ]

for messaggio in st.session_state.cronologia:
    if messaggio["role"] != "system":
        with st.chat_message(messaggio["role"]):
            st.write(messaggio["content"])

domanda = st.chat_input("Scrivi una domanda sui bandi...")

if domanda:
    with st.chat_message("user"):
        st.write(domanda)
    st.session_state.cronologia.append({"role": "user", "content": domanda})

    with st.chat_message("assistant"):
        with st.spinner("Sto pensando..."):
            risposta = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=st.session_state.cronologia,
            )
            testo_risposta = risposta.choices[0].message.content
            st.write(testo_risposta)

    st.session_state.cronologia.append({"role": "assistant", "content": testo_risposta})
