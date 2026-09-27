from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

from chain_test.llm_def import llm

# 원본 입력을 유지하면서 추가 데이터 할당
chain = (
    RunnablePassthrough.assign(
        # summary 키에 요약 결과 추가
        summary=ChatPromptTemplate.from_template("{text}를 요약") | llm | StrOutputParser()
    )
    | RunnablePassthrough.assign(
        # keywords 키에 키워드 추가
        keywords=ChatPromptTemplate.from_template("{text}의 키워드") | llm | StrOutputParser()
    )
)

result = chain.invoke({"text": "긴 문서 내용..."})

print(result)

# result = {"text": "긴 문서 내용...", "summary": "...", "keywords": "..."}