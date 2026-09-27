from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage

from chain_test.llm_def import llm

# model = init_chat_model("gpt-4o-mini")
model = llm

# 스트리밍
for chunk in model.stream([HumanMessage(content="짧은 시를 써주세요.")]):
    print(chunk.content, end="", flush=True)