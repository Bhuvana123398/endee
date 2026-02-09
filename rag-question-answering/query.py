from sentence_transformers import SentenceTransformer
from endee import Endee

model = SentenceTransformer("all-MiniLM-L6-v2")
db = Endee(library="requests")

while True:
    query = input("Ask a question (or type exit): ")
    if query.lower() == "exit":
        break

    query_embedding = model.encode([query])
    results = db.similarity_search(query_embedding, k=1)

    print("\n Retrieved Context:")
    for r in results:
        print(r)
