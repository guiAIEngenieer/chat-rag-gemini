from datetime import datetime
import os

def auto_title(document):
    return document[0].page_content.split("\n")[0].upper()

def enrich_metadata(chunks, file_path, title):
    for i, doc in enumerate(chunks):
        doc.metadata.update({
            "source": os.path.basename(file_path),
            "title": title,
            "chunk_id": i,
            "ingest_date": datetime.now().isoformat()
        })
    return chunks