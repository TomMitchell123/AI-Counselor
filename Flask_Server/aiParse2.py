from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# loads BAAI/bge-small-en
# embed_model = HuggingFaceEmbedding()

# loads BAAI/bge-small-en-v1.5
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.ollama import Ollama


import json
from llama_index.core.query_engine import JSONalyzeQueryEngine

courses = 'data/cdata.json'
pol = 'data/pdata.json'

with open('data/cdata.json') as f:
    d = json.load(f)



query_engine = JSONalyzeQueryEngine(
    list_of_dict=d,
    llm= Ollama(model="llama3", request_timeout=900.0),
    verbose=True,
    streaming=True,
)

from IPython.display import Markdown, display


def call_ai(query):
    query = "ONLY TYPE THE SQL QUERY AND NOTHING ELSE. Here is the question: " + query


    response = query_engine.query(query)
    return str(response)
