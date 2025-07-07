# 🧠 Text Summarizer using LangChain, Groq & Streamlit

This project is a real-time **Text Summarization App** built using **LangChain**, **Groq LLaMA 3 70B**, and **Streamlit**.

It allows users to enter a **YouTube video URL** or **any website link**, and returns a **300-word beautiful summary** using advanced LLMs.

---

## 🚀 Features

- 🔗 **Summarize YouTube or Web URLs**
- 🦜 **LangChain Summarization Chain**
- ⚡ **Groq LLaMA 3 70B Model**
- 🌍 **YoutubeLoader & UnstructuredURLLoader**
- 🎯 **300-word well-formatted summary**
- 🖥️ **Interactive Streamlit UI**
- 🔒 API key security via `.env` file

---

## 📽️ Demo

Watch the full explanation and code walkthrough video here:  
📌 _[(https://www.linkedin.com/feed/update/urn:li:ugcPost:7347820010486013952/)]_  

---

## 🛠️ Tech Stack

| Tool/Library       | Purpose                           |
|--------------------|-----------------------------------|
| 🦜 LangChain       | Prompt chaining and summarization |
| ⚡ Groq LLaMA 3 70B | Fast LLM inference                |
| 🖥️ Streamlit       | Web UI                            |
| 📺 YoutubeLoader   | Load content from YouTube videos  |
| 🌍 UnstructuredURLLoader | Load website content        |
| 🧪 Python + dotenv | Local config + environment vars   |

---

## 🧾 How It Works

1. User enters a **YouTube** or **Website URL**
2. The content is fetched using:
   - `YoutubeLoader` (for YouTube)
   - `UnstructuredURLLoader` (for websites)
3. A prompt is created using `PromptTemplate`
4. LangChain’s `load_summarize_chain` is used with the **Groq Chat model**
5. The output is shown in the UI in **300-word clean summary format**

---

## 💻 Installation

```bash
git clone https://github.com/vishnushankar1/Text-summarizer-with-langchain.git
cd Text-summarizer-with-langchain
pip install -r requirements.txt
