from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from chain_test.llm_def import llm

model = llm
prompt = ChatPromptTemplate.from_template("{topic}에 대해 설명해주세요.")

chain = prompt | model | StrOutputParser()

# 체인 스트리밍
for chunk in chain.stream({"topic": "머신러닝"}):
    print(chunk, end="", flush=True)