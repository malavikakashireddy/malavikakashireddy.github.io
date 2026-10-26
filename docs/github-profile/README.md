# Malavika Kashireddy

Software engineer focused on **backend systems, data infrastructure, and developer tools**. I’m completing a **B.S. in Computer Science at the University of Illinois Chicago**, with a **Computer Systems concentration** and **Mathematics minor**, graduating **December 2026**.

I’m seeking **2027 new graduate software engineering roles**, especially in backend engineering, systems, cloud infrastructure, and AI infrastructure. Previously, I worked as a Software Engineer Intern at UI Health on Python/Django APIs, event logging, and analytics.

[Portfolio](https://malavikakashireddy.github.io/) · [LinkedIn](https://www.linkedin.com/in/malavika-kashireddy) · [Email](mailto:kashireddymalavika@gmail.com)

## Selected engineering work

| Project | Implementation and current focus |
| --- | --- |
| [Real-Time Analytics Platform](https://github.com/malavikakashireddy/real-time-analytics-platform) | Python event producer/consumer, Kafka, PostgreSQL persistence, and FastAPI SQL analytics. A review branch adds commit-after-persistence delivery, validation, replay-safe storage, and a throughput/latency harness. |
| [Machinery Find](https://github.com/malavikakashireddy/machinery-find) | Next.js and TypeScript equipment-browsing demo with a REST API and nine sample listings. Review work adds validated filters, request cancellation, error recovery, accessibility improvements, and browser checks. |
| [DevDocs AI](https://github.com/malavikakashireddy/devdocs-ai) | Developer-documentation search project. A review branch extends the FastAPI foundation with local ingestion, persistent SQLite/BM25 search, line-level source references, and a small Recall@k evaluator. Semantic retrieval and RAG are planned. |

### Engineering checks

A GitHub CI smoke run persisted all 500 test events from Kafka to PostgreSQL at a deliberately limited 100 events/second; this checks the pipeline rather than maximum capacity. The review branches also include locally executed tests for idempotent document updates, source references, failed-storage offset handling, malformed-event quarantine, catalog validation, and UI recovery. Each repository’s validation notes distinguish passing local checks from service integrations that still need to run. I’m building reproducible evidence before publishing performance claims.

## Tools and foundations

- **Languages:** Python, C, C++, Go, Java, SQL, TypeScript, JavaScript
- **Backend and data:** FastAPI, Django, PostgreSQL, Redis, API design, data pipelines
- **Infrastructure:** Kafka, Docker, Linux, Git, debugging, logging, observability
- **AI engineering interests:** document ingestion, retrieval evaluation, embeddings, RAG, and LLM applications
- **Computer science:** algorithms, data structures, systems programming, computer architecture, and mathematics

I enjoy understanding a system end to end: how data enters, what happens when a dependency fails, how to test recovery, and how to explain the trade-offs clearly.
