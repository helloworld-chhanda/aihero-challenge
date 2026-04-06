# 📚 FAQ AI Agent with RAG (Retrieval-Augmented Generation)

> An intelligent FAQ assistant that retrieves relevant information from course materials and generates accurate, context-aware answers using LLMs.


\

---

## 🔍 Overview

This project builds an **AI-powered FAQ assistant** for a data engineering course using **Retrieval-Augmented Generation (RAG)**.

### Problem it solves

Large course materials and FAQs are difficult to search efficiently. Users often:

* Ask repetitive questions
* Struggle to find precise answers in documentation
* Need contextual, human-like responses

### Solution

This project:

* Extracts and processes FAQ and documentation from GitHub repositories
* Uses **text + vector search (hybrid retrieval)** to find relevant context
* Feeds results into an LLM to generate accurate answers
* Logs interactions and evaluates performance automatically

### Why it's useful

* Combines **semantic search + keyword search**
* Improves answer quality with **retrieval grounding**
* Includes **evaluation pipeline for agent performance**
* Demonstrates a full **end-to-end RAG system**

---

## ⚙️ Installation

### Requirements

* Python 3.10+
* OpenAI API key
* Internet access

### Dependencies

Install required packages:

```bash
pip install openai sentence-transformers tqdm numpy pydantic-ai frontmatter requests
```

### Clone the repository

```bash
git clone https://github.com/your-username/faq-rag-agent.git
cd faq-rag-agent
```

### Set environment variables

```bash
export OPENAI_API_KEY="your_api_key_here"
```

---

## 🚀 Usage

### 1. Load and process data

```python
dtc_faq = read_repo_data('DataTalksClub', 'faq')
evidently_docs = read_repo_data('evidentlyai', 'docs')
```

### 2. Build search indices

```python
faq_index.fit(data)
faq_vindex.fit(embeddings, data)
```

### 3. Run the agent

```python
question = "Can I join the course now?"
result = await agent.run(user_prompt=question)

print(result.output)
```

### 4. Hybrid search (optional)

```python
results = hybrid_search("Am I eligible for this course?")
```

### 5. Logging interactions

Logs are automatically saved:

```bash
logs/faq_agent_<timestamp>.json
```

---

## ✨ Features

* 🔎 **Hybrid Search**

  * Keyword search (BM25-like)
  * Semantic search (embeddings)

* 🤖 **LLM-Powered Agent**

  * Uses tools for retrieval
  * Generates grounded responses

* 📄 **Automated Chunking**

  * Intelligent document splitting using LLMs

* 🧠 **Embeddings**

  * SentenceTransformers for semantic understanding

* 🧪 **Evaluation System**

  * Automated answer quality checks
  * Checklist-based scoring using LLMs

* 📝 **Logging**

  * Full conversation tracking
  * Debuggable agent behavior

### 🛣️ Roadmap

* Web UI for chat interface
* Streaming responses
* Better ranking/reranking
* Multi-agent orchestration

---

## 🤝 Contributing

Contributions are welcome!

### Guidelines

* Fork the repo
* Create a feature branch
* Submit a pull request

```bash
git checkout -b feature/your-feature-name
```

### Coding standards

* Follow PEP8
* Use type hints where possible
* Write clear, modular functions

---

## 🧪 Tests

Run basic tests manually:

```python
result = await agent.run(user_prompt="Test question")
print(result.output)
```

For evaluation pipeline:

```python
eval_result = await evaluate_log_record(eval_agent, log_record)
```

You can also generate synthetic test questions:

```python
questions = question_generator.run(prompt)
```

---

## 🚀 Deployment (Optional)

### Simple deployment options:

* Streamlit app
* FastAPI backend
* Docker container

### Example (FastAPI idea)

```bash
uvicorn app:main --reload
```

### CI/CD ideas

* GitHub Actions for testing
* Automated evaluation runs
* Model performance tracking

---

## ❓ FAQ / Troubleshooting

### Common Issues

**1. OpenAI API error**

* Ensure API key is set correctly

**2. Empty search results**

* Check indexing step
* Verify embeddings are generated

**3. Slow performance**

* Cache embeddings
* Reduce chunk size

---

## 🙏 Credits / Acknowledgments

* Data from:

  * DataTalksClub FAQ
  * Evidently AI documentation

* Libraries:

  * OpenAI
  * SentenceTransformers
  * Pydantic AI
  * tqdm

* Inspired by:

  * RAG architectures
  * AI agent design patterns

---

## 📜 License

This project is licensed under the **MIT License**.

See the LICENSE file for details.
