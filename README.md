# 🚀 AWS Bedrock HLD Generator

An AI-powered, serverless High-Level Design (HLD) document generator built using Amazon Bedrock, Titan Embeddings, and Claude 3 Haiku.

This project demonstrates how to implement a Retrieval-Augmented Generation (RAG) pipeline on AWS to automatically transform Business Requirement Documents (BRDs) into structured, architecture-ready HLD documents in HTML format.

---

# 📌 Project Overview

Manually converting Business Requirement Documents (BRDs) into High-Level Design (HLD) documents is time-consuming and often inconsistent.

This solution automates the process using:

- Semantic search via vector embeddings
- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)
- Serverless AWS architecture

The system retrieves the most relevant sections from the BRD and generates a structured HLD document using Amazon Bedrock.

---

# 🏗 Architecture Workflow

1. BRD uploaded to Amazon S3  
2. AWS Lambda reads the document  
3. Text is chunked into smaller sections  
4. Amazon Titan Embed Text v2 generates vector embeddings  
5. Cosine similarity identifies the most relevant BRD sections  
6. Claude 3 Haiku (via Bedrock) generates structured JSON output  
7. JSON is converted into an HTML-based HLD document  
8. Final HLD is stored back in Amazon S3  

---

# 🧠 Logical Architecture Flow

```
User
  │
  ▼
Amazon S3 (BRD)
  │
  ▼
AWS Lambda
  │
  ├── Titan Embeddings (Vector Generation)
  │
  ├── Cosine Similarity (Semantic Search)
  │
  ▼
Claude 3 Haiku (HLD Generation)
  │
  ▼
HTML HLD Output
  │
  ▼
Amazon S3 (Generated Document)
```

---

# 🛠 Technologies Used

- AWS Lambda (Serverless compute)
- Amazon S3 (Document storage)
- Amazon Bedrock
  - Titan Embed Text v2 (Vector embeddings)
  - Claude 3 Haiku (LLM text generation)
- Python (Boto3 SDK)
- Cosine Similarity (Vector comparison)
- HTML (Document generation)

---

# 🔍 Key Concepts Demonstrated

- Retrieval-Augmented Generation (RAG)
- Vector embeddings & semantic similarity search
- Prompt engineering for structured JSON output
- Serverless AI pipeline design
- Cost-optimised LLM usage
- Cloud-native document automation

---

# 📂 Repository Structure

```
aws-bedrock-hld-generator/
│
├── lambda/
│   └── lambda_function.py
│
├── sample-brd/
│   └── digital-retail-banking-brd.md
│
├── sample-output/
│   └── generated_HLD.html
│
├── architecture-diagram.png
├── requirements.txt
└── README.md
```

---

# 🧪 Sample Input

Example BRD includes:

- Business objectives
- Functional requirements
- Non-functional requirements (RPO, RTO, availability)
- Integration requirements
- Security constraints

---

# 📄 Sample Output

Generated HLD includes:

- Project overview
- Architecture summary
- AWS services used
- Security considerations
- Availability strategy
- Integration design
- Assumptions

Output format: `.html`

---

# ⚙️ How It Works (Technical Breakdown)

## 1️⃣ Text Chunking
Large BRDs are split into smaller sections to manage token limits.

## 2️⃣ Embedding Generation
Each chunk is converted into a high-dimensional vector using Titan Embed Text v2.

## 3️⃣ Semantic Retrieval
A query embedding ("Generate High Level Design") is compared with document embeddings using cosine similarity.

Top relevant chunks are selected for context.

## 4️⃣ HLD Generation
Claude 3 Haiku generates a structured JSON-based HLD using the retrieved context.

## 5️⃣ HTML Conversion
Structured JSON is converted into a formatted HTML document.

---

# 🔐 Security Considerations

- IAM-based Bedrock access control
- Secure S3 access permissions
- No hardcoded credentials
- Region-specific model invocation
- Encryption at rest and in transit supported

---

# 💰 Cost Efficiency

- Fully serverless architecture
- Pay-per-request model
- Minimal compute usage
- Token-efficient prompt engineering
- Designed for low-cost experimentation

---

# 🎯 Use Cases

- Automated solution architecture documentation
- Enterprise AI-powered documentation assistant
- Cloud architecture acceleration tool
- Intelligent document processing
- GenAI proof-of-concept implementation

---

# 📈 Resume Value

This project demonstrates hands-on experience with:

- Generative AI on AWS
- Amazon Bedrock integration
- Vector embeddings & semantic search
- Serverless architecture design
- Prompt engineering
- AI-driven document automation

---

# 🚀 Future Enhancements

- Auto-generate architecture diagrams (Mermaid / PlantUML)
- API Gateway integration for web interface
- Vector database integration (OpenSearch / Pinecone)
- Multi-model selection support
- Streaming LLM responses
- CI/CD deployment pipeline

---

# 👨‍💻 Author

Built as a hands-on Generative AI + AWS architecture showcase project.
