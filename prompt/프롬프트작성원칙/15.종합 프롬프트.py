from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from chain_test.llm_def import llm

prompt = ChatPromptTemplate.from_messages([
    ("system", """당신은 시니어 Python 개발자입니다.

코드 작성 규칙:
1. PEP 8 스타일 가이드 준수
2. 타입 힌트 포함
3. docstring 작성 (Google 스타일)
4. 적절한 예외 처리
5. 단위 테스트 코드 포함

응답 형식:
1. 먼저 구현 접근 방식 설명 (2-3문장)
2. 메인 코드 블록
3. 사용 예시
4. 단위 테스트 코드"""),
    ("human", """다음 기능을 구현해주세요:

기능: {feature}
입력: {input_spec}
출력: {output_spec}
제약사항: {constraints}""")
])

chain = prompt | llm | StrOutputParser()

result = chain.invoke({
    "feature": "리스트에서 중복 제거하면서 순서 유지",
    "input_spec": "정수 리스트",
    "output_spec": "중복이 제거된 정수 리스트",
    "constraints": "원본 리스트의 순서 유지, O(n) 시간복잡도"
})

print(result)