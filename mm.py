import streamlit as st
import PyPDF2
from transformers import BartTokenizer, BartForConditionalGeneration
import torch

# Page setup
st.set_page_config(page_title="AI PDF Summarizer", layout="centered")
st.title("📄 AI PDF Document Summarizer")
st.markdown("Upload any long academic or technical PDF and get quick summaries powered by AI.")

# Load model/tokenizer with caching
@st.cache_resource
def load_model():
    tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
    model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
    return tokenizer, model

tokenizer, model = load_model()

# Function: Extract text from PDF
def extract_text_from_pdf(uploaded_file, page_range=None):
    reader = PyPDF2.PdfReader(uploaded_file)
    extracted_text = ""
    pages = page_range if page_range else range(len(reader.pages))
    for i in pages:
        try:
            extracted_text += reader.pages[i].extract_text() + "\n"
        except:
            st.warning(f"⚠️ Could not read page {i + 1}")
    return extracted_text

# Function: Summarize text with different detail levels
def generate_summary(text, summary_length="medium"):
    config = {
        "short": {"min_length": 30, "max_length": 80, "length_penalty": 2.5},
        "medium": {"min_length": 50, "max_length": 150, "length_penalty": 2.0},
        "detailed": {"min_length": 100, "max_length": 300, "length_penalty": 1.0}
    }

    inputs = tokenizer(text, return_tensors="pt", truncation=False)
    input_ids = inputs["input_ids"][0]

    # Break into 1024-token chunks
    max_input_length = 1024
    chunks = [input_ids[i:i + max_input_length] for i in range(0, len(input_ids), max_input_length)]

    summaries = []
    for chunk in chunks:
        chunk = chunk.unsqueeze(0)  # batch dimension
        summary_ids = model.generate(
            chunk,
            max_length=config[summary_length]["max_length"],
            min_length=config[summary_length]["min_length"],
            length_penalty=config[summary_length]["length_penalty"],
            num_beams=4,
            early_stopping=True
        )
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        summaries.append(summary)

    return "\n\n".join(summaries)

# UI for uploading PDF
uploaded_file = st.file_uploader("📤 Upload your PDF file", type=["pdf"])

if uploaded_file:
    reader = PyPDF2.PdfReader(uploaded_file)
    total_pages = len(reader.pages)

    with st.expander("🗂️ Optional: Select page range"):
        start = st.number_input("Start page (0-indexed)", 0, total_pages - 1, 0)
        end = st.number_input("End page (0-indexed)", start, total_pages - 1, total_pages - 1)
        page_range = list(range(start, end + 1))

    summary_length = st.radio("📝 Choose summary level:", ["short", "medium", "detailed"], index=1)

    # Description of levels
    if summary_length == "short":
        st.info("🔹 Short: ~2-4 lines per section")
    elif summary_length == "medium":
        st.info("📘 Medium: ~5-8 lines per section")
    else:
        st.info("📚 Detailed: ~10-15 lines per section")

    if st.button("🔍 Generate Summary"):
        with st.spinner("Processing and summarizing..."):
            text = extract_text_from_pdf(uploaded_file, page_range)
            if len(text.strip()) == 0:
                st.error("❌ Could not extract any text from selected pages.")
            else:
                summary = generate_summary(text, summary_length)
                st.success("✅ Summary generated successfully!")
                st.subheader("🧾 Your Summary")
                st.write(summary)

                st.download_button(
                    label="💾 Download Summary as TXT",
                    data=summary,
                    file_name="summary.txt",
                    mime="text/plain"
                )
