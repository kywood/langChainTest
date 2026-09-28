from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 표 형식 요청
table_prompt = ChatPromptTemplate.from_messages([
    ("system", "응답은 마크다운 표 형식으로 작성하세요."),
    ("human", """다음 프로그래밍 언어들을 비교해주세요: {languages}

| 언어 | 주요 용도 | 장점 | 단점 | 학습 난이도 |
형식으로 작성해주세요.""")
])

# JSON 형식 요청
json_prompt = ChatPromptTemplate.from_messages([
    ("system", "응답은 유효한 JSON 형식으로만 작성하세요. 다른 텍스트는 포함하지 마세요."),
    ("human", """다음 텍스트에서 정보를 추출하세요: {text}

형식:
{{
    "name": "이름",
    "email": "이메일",
    "phone": "전화번호"
}}""")
])

# 번호 목록 형식 요청
list_prompt = ChatPromptTemplate.from_messages([
    ("system", "응답은 번호 목록으로 작성하세요. 각 항목은 한 줄로 간결하게."),
    ("human", "{topic}의 장점 5가지를 알려주세요.")
])