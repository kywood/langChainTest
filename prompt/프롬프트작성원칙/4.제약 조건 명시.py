from langchain_core.prompts import ChatPromptTemplate

# 출력 제약 조건을 명확히 지정
prompt = ChatPromptTemplate.from_messages([
    ("system", """당신은 기술 문서 작성 전문가입니다.

응답 규칙:
- 문장은 간결하게 (20단어 이내)
- 능동태 사용
- 전문 용어 사용 시 괄호 안에 설명 추가
- 총 200자 이내로 작성"""),
    ("human", "{question}")
])