# Document Chatbot (RAG) with Python

Chatbot that answers questions about public funding programs ("bandi") based **exclusively** on the content of provided PDF documents, without inventing information that isn't in the text.

Built to practice **prompt engineering** and **RAG (Retrieval-Augmented Generation)** techniques on a real use case related to my field of work (public funding / finance).

## What it does

- Reads text from PDF files (funding programs / regulatory documents)
- Uses that text as context for an AI model (GPT-OSS via the Groq API)
- Answers user questions **only** based on the uploaded documents
- If the information isn't present, it honestly says so instead of making it up
- Keeps conversation memory (you can ask multiple follow-up questions)
- Simple web interface built with Streamlit

## Tech stack

- **Python**
- **pypdf** — text extraction from PDF files
- **Groq API** (open-weight models: GPT-OSS-20B) — fast, free AI inference
- **Streamlit** — web app frontend
- **python-dotenv** — secure API key management

## Project structure

```
chatbot-bandi/
├── documenti/                    # Sample PDFs (fictional funding programs)
│   ├── bando_innovazione_digitale.pdf
│   └── bando_giovani_imprenditori.pdf
├── 01_leggi_pdf.py                # Step 1: extract text from PDF
├── 02_chatbot_memoria.py          # Step 2: chatbot with conversation memory (terminal)
├── app.py                         # Step 3: web interface with Streamlit
└── README.md
```

## How to run it

1. Clone or download this repository
2. Install the dependencies:
   ```
   pip install pypdf openai python-dotenv streamlit
   ```
3. Create a `.env` file in the root folder with your free [Groq](https://console.groq.com) API key:
   ```
   GROQ_API_KEY=your-key-here
   ```
4. Launch the web interface:
   ```
   streamlit run app.py
   ```

## What I learned

- How to design an effective **system prompt** to constrain a model's answers to specific sources
- The core logic of a **RAG** system (providing document context instead of relying solely on the model's prior knowledge)
- How to manage **conversation memory** in a multi-turn application
- How to build a simple user interface with **Streamlit**

## Notes

The included PDF documents are **fictional**, created for demonstration purposes only.


**Author:** Isabel Zaccaria
[LinkedIn](https://linkedin.com/in/isabel-zaccaria-06a443223)
