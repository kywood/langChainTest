from langchain_core.prompts import ChatPromptTemplate

# 컨텍스트 없는 프롬프트
without_context = "파이썬 웹 프레임워크를 추천해줘."

# 컨텍스트 포함 프롬프트
with_context = ChatPromptTemplate.from_messages([
    ("system", "당신은 시니어 백엔드 개발자입니다."),
    ("human", """다음 프로젝트 요구사항에 맞는 파이썬 웹 프레임워크를 추천해주세요.

프로젝트 정보:
- 팀 규모: 3명 (주니어 2, 시니어 1)
- 예상 트래픽: 일 10만 요청
- 주요 기능: REST API, 실시간 알림
- 기한: 3개월

각 프레임워크의 장단점과 이 프로젝트에 적합한 이유를 설명해주세요.""")
])