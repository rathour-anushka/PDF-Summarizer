# 📄 AI PDF Summarizer using BART

This project provides a user-friendly web interface to **summarize lengthy PDF documents** (academic, legal, corporate, etc.) using **Hugging Face's BART transformer model**. The tool allows users to upload PDFs, optionally choose specific pages, pick a summary length (short, medium, or detailed), and download the output as a text file.

---

## 🚀 Demo Features

- 📤 Upload `.pdf` files with ease
- 🗂️ Select custom page ranges (optional)
- ✂️ Choose between `short`, `medium`, or `detailed` summaries
- 🤖 Powered by `facebook/bart-large-cnn` from Hugging Face
- 📜 Download generated summaries as `.txt`
- ⚡ Fast with model caching and efficient chunking

---

## 📸 Preview

<table>
  <tr>
    <td align="center"><strong>Upload PDF</strong></td>
    <td align="center"><strong>Set Options</strong></td>
    <td align="center"><strong>View Summary</strong></td>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/rathour-anushka/PDF-Summarizer/blob/main/Screenshot%202025-06-13%20185838.png?raw=true" width="250"/>
    </td>
    <td>
      <img src="https://github.com/rathour-anushka/PDF-Summarizer/blob/main/Screenshot%202025-06-13%20185916.png?raw=true" width="250"/>
    </td>
    <td>
      <img src="https://github.com/rathour-anushka/PDF-Summarizer/blob/main/Screenshot%202025-06-13%20190012.png?raw=true" width="250"/>
    </td>
  </tr>
</table>

---

## 🛠 Tech Stack

- [Streamlit](https://streamlit.io/) — for building the web interface
- [PyPDF2](https://pypi.org/project/PyPDF2/) — to extract text from PDFs
- [Transformers](https://huggingface.co/transformers) — for BART summarization model
- [Torch](https://pytorch.org/) — backend support for inference

---

## 💻 Installation

### 1. Clone the repository
```bash
git clone https://github.com/rathour-anushka/PDF-Summarizer.git
cd PDF-Summarizer
