from langchain_core.prompts import ChatPromptTemplate

from chain_test.llm_def import llm

prompt = ChatPromptTemplate.from_messages([
    ("system", """당신은 교육 콘텐츠 전문가입니다.

대상 청중: {audience}
- 초보자: 비유와 일상 예시 사용, 전문 용어 최소화
- 중급자: 개념과 실습 코드 병행
- 전문가: 심화 내용과 최적화 기법 포함"""),
    ("human", "{topic}에 대해 설명해주세요.")
])

# 대상에 따라 다른 응답
chain = prompt | llm
beginner = chain.invoke({"audience": "초보자", "topic": "API"})
expert = chain.invoke({"audience": "전문가", "topic": "API"})


print(beginner)
print(expert)