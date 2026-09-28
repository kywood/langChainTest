from langchain_core.messages import AIMessage
from langchain_core.prompts import ChatPromptTemplate

from chain_test.llm_def import llm

# 대화형 프롬프트 템플릿
prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 {role} 전문가입니다."),
    ("human", "{question}")
])

# 체인에서 사용
chain = prompt | llm
response = chain.invoke({
    "role": "Python",
    "question": "리스트와 튜플의 차이점은?"
})


print(response)


ai_message = AIMessage(content=str(response))

print(ai_message)