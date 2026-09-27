from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage

from chain_test.llm_def import llm

# model = init_chat_model("gpt-4o-mini")

model = llm

# 모델 호출 - AIMessage 반환
response = model.invoke([HumanMessage(content="안녕하세요!")])

print(type(response))  # AIMessage
print(response.content)  # "안녕하세요! 무엇을 도와드릴까요?"


print(f"내용: {response.content}")
print(f"토큰 사용량: {response.usage_metadata}")
print(f"응답 메타데이터: {response.response_metadata}")

if response.tool_calls:
    for tool_call in response.tool_calls:
        print(f"도구 이름: {tool_call['name']}")
        print(f"도구 인자: {tool_call['args']}")