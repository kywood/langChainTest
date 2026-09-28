# 2-튜플 형태의 메시지 목록으로 프롬프트 생성 (type, content)
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from chain_test.llm_def import llm

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "이 시스템은 천문학 질문에 답변할 수 있습니다."),
    ("user", "{user_input}"),
])

messages = chat_prompt.format_messages(user_input="태양계에서 가장 큰 행성은 무엇인가요?")

print(messages)

chain = chat_prompt | llm | StrOutputParser()

result=  chain.invoke({"user_input": "태양계에서 가장 큰 행성은 무엇인가요?"})

print(result)
