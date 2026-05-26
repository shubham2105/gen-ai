from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import HuggingFaceEmbeddings

# This is the the way to generate embeddings locally using Hugging Face models.
embeddings = HuggingFaceEmbeddings(
    model_name = "BAAI/bge-small-en-v1.5",
    encode_kwargs = {"normalize_embeddings": True}
)

vector = embeddings.embed_query("My name is Shubham Dhole and I am a software developer.")

print(len(vector))
print("This are embeddings generated using local Hugging Face models:", vector[:5])

# using Hugging Face Hub integration to generate embeddings
from langchain_huggingface import HuggingFaceEndpointEmbeddings

endpoint_embeddings = HuggingFaceEndpointEmbeddings(
    model= "BAAI/bge-small-en-v1.5",
)

query_results = endpoint_embeddings.embed_query("What is the capital of France?")
print(len(query_results))
print("These are embeddings generated using Hugging Face Hub integration:", query_results[:5])