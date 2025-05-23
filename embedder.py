from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings


def build_chroma_from_docs(urls, persist_dir="chroma_db"):
    all_chunks = []

    for url in urls:
        print(f"🌐 Loading from: {url}")
        loader = WebBaseLoader(web_path=url, requests_kwargs={"headers": {"User-Agent": "Mozilla/5.0"}})
        docs = loader.load()

        if not docs:
            print(f" Skipping empty document from: {url}")
            continue

        print(f"🔍 Loaded {len(docs)} documents")
        for i, doc in enumerate(docs[:2]):
            print(f"\n--- Doc {i+1} ---\n{doc.page_content[:300]}")

        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        chunks = splitter.split_documents(docs)
        all_chunks.extend(chunks)

    if not all_chunks:
        raise ValueError(" No documents loaded. Check URLs and network access.")

    print(f"🧠 Total Chunks: {len(all_chunks)}")
    Chroma.from_documents(all_chunks, OpenAIEmbeddings(), persist_directory=persist_dir)
