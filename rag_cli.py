# rag_cli.py

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

persist_dir = "chroma_db"

def load_vectorstore():
    return Chroma(persist_directory=persist_dir, embedding_function=OpenAIEmbeddings())

def get_cli_commands(query: str, vectorstore) -> str:
    prompt_template = """
You are a helpful assistant specialized in Docker CLI commands.

Context:
{context}

Question: {question}

Please respond ONLY with the exact Docker CLI commands relevant to the question. Do NOT include any explanations or extra text.
Separate multiple commands by new lines.
"""

    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )

    llm = ChatOpenAI(temperature=0.5, model_name="gpt-4")

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(),
        return_source_documents=False,
        chain_type_kwargs={"prompt": prompt}
    )

    raw_result = qa.run(query)

    # Filter to show only lines that look like Docker CLI commands
    commands = []
    for line in raw_result.split('\n'):
        line = line.strip()
        if line.startswith('docker ') or line.startswith('docker-'):
            commands.append(line)

    if commands:
        return '\n'.join(commands)
    else:
        # fallback: return entire response if no commands found
        return raw_result
