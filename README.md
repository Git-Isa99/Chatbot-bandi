# Document Chatbot on Public Funding Programs (PDF)

Chatbot that answers questions about public funding programs ("bandi") based **exclusively** on the content of provided PDF documents, without inventing information that isn't in the text.

Built to practice prompt engineering and grounded question answering on a real use case related to my field of work (public funding / subsidised finance).

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

## Design choices

Grounding. Public funding documents are regulatory texts: a wrong answer about eligibility criteria or deadlines has real consequences. The system prompt therefore forces the model to answer only from the supplied text and to state when the information is absent, rather than falling back on its own prior knowledge.

Context injection over retrieval. With a small document set, passing the full extracted text into the prompt is simpler and avoids the failure modes of a poorly tuned retrieval step (relevant passages not retrieved). The trade-off is that it does not scale — see below.

## Known limitations & next steps

Doesn't scale with document volume. The full document text is passed into the prompt on every query. This works with a handful of documents, but with dozens of full-length bandi it would exceed the model's context window, raise token cost per query, and degrade answer quality, since long contexts dilute the model's attention. Next step: implement true RAG — chunking, embeddings and vector search — so that only the passages relevant to the question are passed to the model.
No source citations. Answers don't yet reference the document and page they come from, which is a requirement in a regulatory domain.
No systematic evaluation. Answer quality has been assessed manually. A test set of question/expected-answer pairs would allow measuring accuracy and comparing configurations.
Text-layer PDFs only. Scanned documents and complex tables — both common in real bandi — are not handled; that would require OCR and table-aware parsing.

## What I learned

- How to design an effective **system prompt** to constrain a model's answers to specific sources
- The core logic of a **RAG** system (providing document context instead of relying solely on the model's prior knowledge)
- How to manage **conversation memory** in a multi-turn application
- How to build a simple user interface with **Streamlit**

## Notes

The included PDF documents are **fictional**, created for demonstration purposes only.

**Author:** Isabel Zaccaria
[LinkedIn](https://linkedin.com/in/isabel-zaccaria-06a443223)
