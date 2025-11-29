import streamlit as st
from langchain.schema import HumanMessage
from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
from langchain.vectorstores.pinecone import PineconeVectorStore
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings

# Page setup
st.set_page_config(page_title="HealthLens AI")
st.title("📄 HealthLens AI — Smart Medical Insights")
st.write("Upload a medical document and ask questions to get structured and safe insights.")

# API key required for Groq Model
api_key = st.text_input("Enter Your GROQ API Key:", type="password")

uploaded_file = st.file_uploader("Upload Medical PDF", type=["pdf"])

if uploaded_file is not None:
    loader = PyPDFLoader(uploaded_file.name)
    pages = loader.load()
    st.success("📑 PDF Uploaded Successfully!")

if api_key:
    llm = ChatGroq(
        model="llama3-8b-8192",
        api_key=api_key
    )

    question = st.text_input("Ask any medical question:")

    if st.button("Analyze"):
        if not question:
            st.warning("Please ask a question!")
        else:
            prompt = f"Extract only medically accurate insights. Question: {question}"
            response = llm.invoke([HumanMessage(content=prompt)])
            st.markdown("### 🩺 Medical Insights")
            st.success(response.content)
