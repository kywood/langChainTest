import uvicorn
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage

from chain_test.llm_def import llm

app = FastAPI()
# model = init_chat_model("gpt-4o-mini")
model = llm

@app.get("/stream")
async def stream_response(query: str):
    async def generate():
        async for chunk in model.astream([HumanMessage(content=query)]):
            if chunk.content:
                yield f"data: {chunk.content}\n\n"
        yield "data: [DONE]\n\n"

    return StreamingResponse(
        generate(),
        media_type="text/event-stream"
    )

if __name__ == "__main__":
    # 8000번 포트로 서버 실행
    uvicorn.run(app, host="0.0.0.0", port=8000)