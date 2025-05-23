# rag_docker_cli/main.py

from loader import fetch_docker_pages
from embedder import build_chroma_from_docs
from rag_cli import load_vectorstore, get_cli_commands

def main():
    print(" Fetching Docker documentation...")
    urls = fetch_docker_pages()

    print(" Embedding documents into ChromaDB...")
    build_chroma_from_docs(urls)

    print(" Loading vectorstore...")
    vectorstore = load_vectorstore()

    while True:
        query = input("\n Ask a Docker-related question (or 'exit'):\n> ")
        if query.lower() == "exit":
            break

        print("\n Docker CLI Commands:")
        commands = get_cli_commands(query, vectorstore)
        print(commands)

if __name__ == "__main__":
    main()
