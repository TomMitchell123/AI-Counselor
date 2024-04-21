from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# loads BAAI/bge-small-en
# embed_model = HuggingFaceEmbedding()

# loads BAAI/bge-small-en-v1.5
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.ollama import Ollama

# 加载文档

import json
from llama_index.core.query_engine import JSONalyzeQueryEngine

with open('data/cdata.json') as f:
    d = json.load(f)


query_engine = JSONalyzeQueryEngine(
    list_of_dict=d,
    llm= Ollama(model="llama3", request_timeout=900.0),
    verbose=False,
    streaming=True,
)

# 获取用户输入
from IPython.display import Markdown, display

while True:
    query = input("Query:")
    
    query = "ONLY TYPE THE SQL QUERY AND NOTHING ELSE. Here is the question: " + query


    # 提问并打印答案
    response = query_engine.query(query)
    print(response)
