from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate

from chain_test.llm_def import llm

# 예시 정의
examples = [
    {"input": "오늘 날씨 어때?", "output": "일상 대화"},
    {"input": "파이썬으로 웹서버 만드는 법", "output": "기술 질문"},
    {"input": "내일 회의 일정 잡아줘", "output": "업무 요청"},
]

# 예시 프롬프트 템플릿
example_prompt = ChatPromptTemplate.from_messages([
    ("human", "{input}"),
    ("ai", "{output}")
])

# Few-shot 프롬프트 생성
few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
)

# 최종 프롬프트
final_prompt = ChatPromptTemplate.from_messages([
    ("system", "사용자의 질문을 다음 카테고리 중 하나로 분류하세요: 일상 대화, 기술 질문, 업무 요청"),
    few_shot_prompt,
    ("human", "{input}")
])

chain = final_prompt | llm
result = chain.invoke({"input": "React 컴포넌트 만드는 방법 알려줘"})


print(result)
print(result.content)
