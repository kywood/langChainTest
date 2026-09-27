from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from chain_test.llm_def import llm

# model = init_chat_model("gpt-4o-mini")
model = llm

# 대화 히스토리 구성
messages = [
    SystemMessage(content="당신은 요리 전문가입니다."),
    HumanMessage(content="김치찌개 만드는 법을 알려주세요."),
    AIMessage(content="김치찌개는 다음과 같이 만듭니다..."),
    HumanMessage(content="고기 없이 만들 수 있나요?"),
]

# 컨텍스트를 유지한 응답
response = model.invoke(messages)
print(response.content)