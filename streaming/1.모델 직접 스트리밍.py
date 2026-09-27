from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage

from chain_test.llm_def import llm

# model = init_chat_model("gpt-4o-mini")
model = llm

# 스트리밍 호출
for chunk in model.stream([HumanMessage(content="파이썬의 장점 5가지를 설명해주세요.")]):
    print(chunk.content, end="", flush=True)