import asyncio
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage


async def async_stream():
    # model = init_chat_model("gpt-4o-mini")
    from chain_test.llm_def import llm
    model = llm

    messages = [
        SystemMessage(
            content="당신은 서정적이고 아름다운 시를 쓰는 시인입니다. 한국 말로"
        ),
        HumanMessage(content="짧은 시를 써주세요."),
    ]

    async for chunk in model.astream(messages):
        print(chunk.content, end="", flush=True)

# 실행
asyncio.run(async_stream())