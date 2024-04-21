from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# loads BAAI/bge-small-en
# embed_model = HuggingFaceEmbedding()

# loads BAAI/bge-small-en-v1.5
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
embeddings = embed_model.get_text_embedding("Hello World!")
print(len(embeddings))
print(embeddings[:5])

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.ollama import Ollama

# 加载文档
documents = SimpleDirectoryReader("data").load_data()

# 设置嵌入模型和LLM
Settings.chunk_size = 1024 
Settings.embed_model = embed_model
Settings.llm = Ollama(model="llama3", request_timeout=900.0)

# 创建索引
from llama_index.core.node_parser import SentenceSplitter

index = VectorStoreIndex.from_documents(
    documents, transformations=[SentenceSplitter(chunk_size=1024)]
)

# 创建问答引擎
query_engine = index.as_query_engine(streaming=True)

# 获取用户输入

while True:
    query = input("Query:")


    # 提问并打印答案
    response = query_engine.query(query)
    response.print_response_stream()