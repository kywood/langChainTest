from langchain_core.prompts import ChatPromptTemplate

from chain_test.llm_def import llm

prompt = ChatPromptTemplate.from_messages([
    ("system", """당신은 한영 번역가입니다. 자연스러운 번역을 제공하세요.

예시:
입력: "오늘 하루도 화이팅!"
출력: "Have a great day today!"

입력: "맛있게 드세요"
출력: "Enjoy your meal!"

입력: "수고하셨습니다"
출력: "Great job!" 또는 "Thank you for your hard work!"

위 예시처럼 자연스러운 영어 표현으로 번역하세요."""),
    ("human", "다음을 번역해주세요: {text}")
])


chain = prompt | llm

result = chain.invoke({"text": "React 컴포넌트 만드는 방법 알려줘"})


print(result)
print(result.content)
