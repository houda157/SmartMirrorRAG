import chromadb
import pandas as pd
import os

client = chromadb.PersistentClient("data_db")
collection = client.get_collection("events_collection")
#chunking data
# def chunk(text, chunk_size=40, overlap=5):
#     """
#     Splits the input text into chunks of specified size with overlap.
    
#     Parameters:
#     text (str): The input text to be chunked.
#     chunk_size (int): The size of each chunk.
#     overlap (int): The number of overlapping characters between chunks.
    
#     Returns:
#     List[str]: A list of text chunks.
#     """
#     chunks = []
#     start = 0
#     text_length = len(text)
    
#     while start < text_length:
#         end = min(start + chunk_size, text_length)
#         chunk = text[start:end]
#         chunks.append(chunk)
#         start += chunk_size - overlap
    
#     return chunks
# # Read data from CSV file

# if not os.path.exists("data.csv"):
#         raise FileNotFoundError(f"The file {"data.csv"} does not exist.")
    
# df = pd.read_csv("data.csv")
# for idx, row in df.iterrows():
#     # Combine all fields into one paragraph
#     event_text = []
#     event_text = f"""
#     Title: {row['Title']}
#     Type: {row['Type']}
#     Organizer: {row['Organizer']}
#     Date: {row['Date']}
#     Location: {row['Location']}
#     Description: {row['Description']}
#     Agenda: {row['Agenda']}
#     """.strip()
    
#     chunks = chunk(event_text)
    
#       # Create unique IDs for each chunk
#     chunk_ids = [f"{idx}_chunk_{i}" for i in range(len(chunks))]

#     # Create metadata for each chunk
#     chunk_metadata = [
#         {
#             "source": f"event_{idx}",
#             "chunk_number": i,
#             "title": row["Title"]
#         }
#         for i in range(len(chunks))
#     ]

#     # Add to Chroma
#     collection.add(
#         documents=chunks,        # list of chunks
#         metadatas=chunk_metadata, # list of metadata dicts
#         ids=chunk_ids             # list of ids
#     )
    
results  = collection.query(
    query_texts=["what are the events related to AI?"],
    n_results=5
)
print(results["documents"])
    
    
    
    
    



