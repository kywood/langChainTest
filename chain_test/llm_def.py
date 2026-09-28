from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableParallel, RunnableBranch, RunnableLambda
from langchain_ollama import ChatOllama, OllamaEmbeddings

# 1. 모델 지정
llm = ChatOllama(
    base_url="http://localhost:11434",
    model="qwen2.5:7b-instruct-q4_K_M",  # 현재 Ollama에 다운로드받은 모델명
    # disable_streaming=True,
    timeout=30.0,  # 30초 타임아웃
    max_retries=2,
)

llmt = ChatOllama(
    base_url="http://localhost:11434",
    model="qwen2.5:7b-instruct-q4_K_M",  # 현재 Ollama에 다운로드받은 모델명
    # disable_streaming=True,
    timeout=30.0,  # 30초 타임아웃
    max_retries=2,
    temperature=0.0
)

embeddings = OllamaEmbeddings(
    base_url="http://localhost:11434",
    model="bge-m3:latest"
)


# 1. 모델 지정
llmv = ChatOllama(
    base_url="http://localhost:11434",
    model="llama3.2-vision:latest"  # 현재 Ollama에 다운로드받은 모델명
)

embeddingsv = OllamaEmbeddings(
    base_url="http://localhost:11434",
    model="qwen2.5:7b-instruct-q4_K_M"
)

llmv2= ChatOllama(
    base_url="http://localhost:11434",
    model="qwen2.5vl:7b"  # 현재 Ollama에 다운로드받은 모델명
)

embeddingsv2 = OllamaEmbeddings(
    base_url="http://localhost:11434",
    model="qwen2.5:7b-instruct-q4_K_M"
)



# 1. 모델 지정
llm2 = ChatOllama(
    base_url="http://localhost:11434",
    model="qwen2.5:7b-instruct-q4_K_M"  # 현재 Ollama에 다운로드받은 모델명
)

embeddings2 = OllamaEmbeddings(
    base_url="http://localhost:11434",
    model="qwen2.5:7b-instruct-q4_K_M"
)
