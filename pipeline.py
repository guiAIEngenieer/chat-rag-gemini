from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from api_connections import gemini_key
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import glob
from datetime import datetime
from uuid import uuid4
import faiss
import os


# Definindo a Chave API do Gemini
os.environ["GOOGLE_API_KEY"] = gemini_key

#Função para carregar todos os pdfs de uma pasta
def load_pdfs(diretorio):
    pdf_files = glob.glob(os.path.join(diretorio,"*.pdf"))
    return pdf_files

# Função que extrai as informações dos documentos
def extract(file):
    loader = PyPDFLoader(file)
    documento_recuperado = loader.load()
    return documento_recuperado

# Função que divide os documentos em chunks
def tranform_chunks(document):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 150,
        chunk_overlap = 15,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    try:
        chunk = text_splitter.split_documents(document)
        print("Chunking Completo com sucesso")
        return chunk
    
    except Exception as e:
        print(f"Ocorreu um erro durante a geração de chunks: {e}")
        return None

# Funções para eniquecimento de Metadados
def title_auto(documento):
    text = documento[0].page_content
    return text.split("\n")[0].upper()
   

def enriquecer_metadados(chunks, file_path, title):
    for i , doc in enumerate(chunks):
        meta = doc.metadata.copy()
        meta['source'] = os.path.basename(file_path)
        meta["title"] = title
        meta["chunk_id"] = i
        meta["ingest_date"] = datetime.now().isoformat()
        doc.metadata = meta
    
    return chunks


# Documentos de Conhecimento
pdfs = load_pdfs(r"Cole aqui o Diretorio")

# Extraindo documentos, Enriquecendo metadados e Transformando em Chunks
all_chunks = []

for index, pdf in enumerate(pdfs):
    try:
        documento_recuperado = extract(pdf)
        chunks = tranform_chunks(documento_recuperado)

        if not chunks:
            continue

        title = title_auto(documento_recuperado)
        chunks = enriquecer_metadados(chunks, pdf , title)

        all_chunks.extend(chunks)
        print(f"Processando documento {index + 1} / {len(pdfs)} ")

    except Exception as e:
        print(f"Ocorreu um erro durante o processo: {e}")


# Indexando ao banco de dados vetorial
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

index_hnsw = faiss.IndexHNSWFlat(3072,32)

faiss_db = FAISS(
    embedding_function=embeddings,
    index=index_hnsw,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={}
)

try:
    uuids = [str(uuid4()) for _ in range(len(all_chunks))]

    faiss_db.add_documents(documents=all_chunks, ids=uuids)
    faiss_db.save_local("faiss-db")

except Exception as e:
    print(f"Ocorreu um erro ao indexar os chunks: {e}")

print("Documentos Carregados com sucesso")