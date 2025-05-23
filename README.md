## Docker CLI RAG Assistant

A command-line Retrieval-Augmented Generation (RAG) tool that helps you ask natural language questions about Docker CLI and get accurate command suggestions using the latest official documentation.

## Features

- Scrapes official Docker CLI documentation.
- Embeds documentation into a local Chroma vector store.
- Allows natural language querying for Docker commands.
- Uses OpenAI LLMs to return CLI command suggestions.
- Simple interactive command-line interface.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/rag_docker_cli.git
cd rag_docker_cli

2. Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt


4. Set Environment Variables

OPENAI_API_KEY=your_openai_api_key
USER_AGENT=your_custom_user_agent_string

5. Run the Tool

python main.py


## Project Structure

rag_docker_cli/
│
├── main.py                # Entry point for CLI
├── loader.py              # Scrapes Docker CLI docs
├── embedder.py            # Embeds docs using OpenAI and Chroma
├── rag_cli.py             # Sets up retrieval and LLM interaction
├── requirements.txt       # Dependencies
└── README.md              # You're reading this

## Example Questions

how to list running containers?

how do I build an image with docker?

how to push an image to DockerHub?

how to inspect a container?

## Tech Stack

LangChain

ChromaDB

OpenAI API

BeautifulSoup

Python 3.10+
```

Acknowledgements
Docker documentation: https://docs.docker.com/

LangChain for the RAG framework