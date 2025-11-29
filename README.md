# HealthLens AI — Smart Medical Insights

HealthLens AI is an **AI assistant for doctors and clinics** that can read medical documents (PDFs, reports, guidelines) and answer questions in **clear, safe, and structured language**.

Built by **Manan Patel (Agentic AI & GenAI Developer @ Xomic Infotech)**.

---

## 🩺 What HealthLens AI Does

- 📁 **Upload medical documents** – lab reports, discharge summaries, clinical guidelines, drug sheets  
- 🔍 **Understands the content** using Retrieval-Augmented Generation (RAG)  
- 🤖 **Answers clinical questions** based *only* on the uploaded files  
- ⚠️ **Safety first** – always reminds users that it’s **not a replacement for a licensed doctor**  
- 📝 **Structured responses** – summaries, bullet points, and key highlights  
- 💬 **Chat-style interface** – doctors can ask follow-up questions

Example questions:
- “Summarize the key findings in this CT scan report.”  
- “What are the risk factors mentioned for this patient?”  
- “Explain this lab report in simple language.”  

---

## 🧠 Tech Stack

- **Python 3**
- **Streamlit** – simple web UI
- **scikit-learn (TF-IDF)** – document chunk search
- **PyPDF2** – extract text from PDFs
- **OpenAI API** – medical-style LLM responses
- **python-dotenv** – secure API key handling

---

## 🏗️ Architecture (RAG Overview)

1. User uploads one or more **PDF documents**  
2. App extracts text and splits it into **small chunks**  
3. Uses **TF-IDF + cosine similarity** to find the most relevant chunks for the question  
4. Sends those chunks + question to an **LLM (OpenAI)**  
5. LLM generates an answer that:
   - References the documents
   - Explains in clear English
   - Adds a safety disclaimer

---

## 🚀 Getting Started (Local Setup)

### 1️⃣ Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/healthlens-ai-medical-rag.git
cd healthlens-ai-medical-rag
