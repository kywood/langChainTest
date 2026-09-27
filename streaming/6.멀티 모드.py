from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.tools import tool

from chain_test.llm_def import llm


@tool
def get_weather(city: str) -> str:
    """도시의 날씨를 조회합니다."""
    return f"{city}의 현재 날씨는 맑음, 25도입니다."

model = llm

agent = create_agent(model, tools=[get_weather])

# 에이전트 진행 상황 스트리밍
for event in agent.stream(
    {"messages": [("user", "서울 날씨 알려줘")]},
    stream_mode=["updates", "messages"]
):
    mode, data = event
    if mode == "updates":
        print(f"[상태 업데이트] {data}")
    elif mode == "messages":
        token, _ = data
        if token.content:
            print(f"[토큰] {token.content}")