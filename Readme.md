# ArchiveIQ - Self Hosted NotebookLM

## Core Concept

This project is a self hosted alternative to NotebookLM designed for private deployment. It allows users to ingest and organize personal documents across multiple formats, build a searchable knowledge graph, and query the data using local LLMs via LM Studio or Ollama. The system emphasizes privacy, modularity, and efficient performance on modest hardware, making it suitable for personal use cases where data should remain local.

The initial release will support widely used formats including PDF, TXT, Markdown, DOCX, CSV, PNG, and JPEG. Additional formats such as EPUB, audio, and video will be added in future iterations. Support for adding copied text and images as well as websites will be added in future iterations.

Key goals:
- Provide a private, extensible knowledge assistant that draws it's knowledge from your provided documents.
- Support bring-your-own-LLM integration.
- Maintain lightweight deployment optimized for Docker on resource-constrained hardware.
- Ensure reproducibility and maintainability through code quality checks and experiment tracking.

---

## Planned Architecture
*Note: The architecture is subject to change as the project evolves. This is a rough draft.*

### Ingestion Layer
- n8n workflows automate ingestion from local folders, APIs, or cloud storage.
- Trigger pipelines when new files are added.

### Parsing and Preprocessing
- PySpark jobs handle text extraction, normalization, and chunking.
- Format specific parsers for PDF, DOCX, TXT, Markdown, CSV, and image OCR.
- Metadata extraction for document type, source, and timestamps.

### Knowledge Graph and Embeddings
- Embeddings generated using lightweight models (e.g., sentence transformers).
- Graph structure links related documents and topics.
- Enables semantic search and contextual retrieval.

### LLM Integration
- Local LLMs (LM Studio, Ollama) serve as the main conversational interface.
- Smaller internal models handle summarization, classification, and OCR.
- Retrieval augmented generation pipeline: query → retrieve relevant chunks → summarize → LLM response.

### Experiment Tracking
- MLflow tracks performance of helper models (summarizers, classifiers, OCR).
- Logs metrics such as accuracy, runtime, and resource usage.
- Supports model comparison and reproducibility.

### Code Quality
- SonarQube enforces static analysis and code quality standards.
- Ensures maintainability and community adoption.

### Frontend
- Lightweight frontend UI for file upload, browsing, and querying. Library to be decided.
- Displays source snippets and citations alongside responses.

### Deployment
- Dockerized microservices for ingestion, processing, LLM bridge, tracking, and quality checks.
- Multi-stage builds to minimize image size.
- Configurable for CPU fallback to support weaker hardware.

---

## Roadmap

*Note: The roadmap is subject to change as the project develops. This is the current set of ideas to be implemented in the planned sequence.*

1. **MVP**
   - Support PDF, TXT, Markdown, DOCX, CSV, PNG, JPEG & copied text.
   - Basic ingestion, parsing, embeddings, and LLM query interface.

2. **Phase 2**
   - Add EPUB and additional image formats (WebP, BMP).
   - Add support for websites via URL. Add web scraper in the backend.

3. **Phase 3**
   - Add Note saving functionality.
   - Add Query history functionality.
   - Add scheduled query functionality.

4. **Phase 4**
   - Audio support with speech-to-text integration.

5. **Phase 5**
   - Video support with frame extraction and OCR.

---
