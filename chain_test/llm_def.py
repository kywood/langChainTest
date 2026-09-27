from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableParallel, RunnableBranch, RunnableLambda
from langchain_ollama import ChatOllama, OllamaEmbeddings

# 1. 모델 지정
llm = ChatOllama(
    base_url="http://localhost:11434",
    model="qwen2.5:7b-instruct-q4_K_M"  # 현재 Ollama에 다운로드받은 모델명
)

embeddings = OllamaEmbeddings(
    base_url="http://localhost:11434",
    model="qwen2.5:7b-instruct-q4_K_M"
)
