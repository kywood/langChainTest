from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langgraph.config import get_stream_writer

from chain_test.llm_def import llm


@tool
def process_documents(count: int) -> str:
    """문서를 처리합니다."""
    writer = get_stream_writer()

    for i in range(count):
        # 커스텀 진행 상황 전송
        writer({"progress": f"문서 {i+1}/{count} 처리 중..."})

    return f"{count}개 문서 처리 완료"

# model = init_chat_model("openai:gpt-4o")
model = llm
agent = create_agent(model, tools=[process_documents])

# 커스텀 스트리밍 수신
for event in agent.stream(
    {"messages": [("user", "5개 문서를 처리해주세요")]},
    stream_mode="custom"
):
    print(f"커스텀 이벤트: {event}")