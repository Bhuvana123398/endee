from sentence_transformers import SentenceTransformer
from endee import Endee

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Read data
with open("data/sample.txt", "r") as f:
    documents = f.readlines()

# Create embeddings
embeddings = model.encode(documents)

# Store in Endee
db = Endee(library="requests")
db.add(embeddings, documents)

print("Documents ingested successfully")
