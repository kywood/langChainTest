from langchain_core.prompts import ChatPromptTemplate

from chain_test.llm_def import llm

# RAG 스타일 프롬프트
prompt = ChatPromptTemplate.from_messages([
    ("system", """당신은 문서 기반 Q&A 어시스턴트입니다.

규칙:
1. 오직 제공된 컨텍스트 내의 정보만 사용하세요
2. 컨텍스트에 없는 정보는 "문서에서 해당 정보를 찾을 수 없습니다"라고 답하세요
3. 답변 시 관련 부분을 인용하세요"""),
    ("human", """컨텍스트:
{context}

질문: {question}

위 컨텍스트만을 참고하여 답변해주세요.""")
])

sample_context = """
[회사 출장 규정 v2.0]
제3조 (일비 및 식비)
1. 국내 출장 시 하루 일비는 30,000원으로 지급한다.
2. 식비는 1식당 최대 15,000원까지 영수증 제출 시 정산 가능하다.
3. 법인카드를 사용한 경우 개별 영수증 제출은 생략할 수 있다.
"""


chain = prompt | llm

sample_question = "국내 출장 갔을 때 하루 일비는 얼마인가요?"

# 4. 체인 실행 (invoke 메서드에 변수 전달)
response = chain.invoke({
    "context": sample_context,
    "question": sample_question
})

print(response.content)