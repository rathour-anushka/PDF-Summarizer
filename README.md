# 📄 AI PDF Summarizer using BART

This project provides an easy-to-use web interface to **summarize lengthy PDF documents** (academic, legal, corporate, etc.) using **Hugging Face's BART transformer model**. Users can upload PDFs, choose specific pages, set summary length (short, medium, or detailed), and download the output.

## 🚀 Demo Features

- 📤 Upload any `.pdf` file
- 🗂️ Optional page range selection
- ✂️ Choose between `short`, `medium`, or `detailed` summaries
- 🤖 Powered by **facebook/bart-large-cnn**
- 📜 View and download the summary as a `.txt` file
- 🔥 Optimized with caching to avoid repeated model loads

---

## 📸 Preview

| Upload PDF | Set Options | View Summary |
|------------|-------------|---------------|
| ![upload](https://via.placeholder.com/200x100) | ![options](https://via.placeholder.com/200x100) | ![summary](https://via.placeholder.com/200x100) |

---

## 🛠 Tech Stack

- [Streamlit](https://streamlit.io/) — for interactive UI
- [PyPDF2](https://pypi.org/project/PyPDF2/) — to extract text from PDFs
- [Hugging Face Transformers](https://huggingface.co/transformers) — for pretrained BART summarization
- [Torch](https://pytorch.org/) — model backend

---

## 💻 Installation

```bash
git clone https://github.com/yourusername/pdf-summarizer
cd pdf-summarizer
pip install -r requirements.txt
