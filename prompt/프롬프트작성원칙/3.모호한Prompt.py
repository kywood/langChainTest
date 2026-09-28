from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

from chain_test.llm_def import llm

# llm = init_chat_model("gpt-4o-mini")




# ❌ 모호한 프롬프트
vague_prompt = ChatPromptTemplate.from_template(
    "{topic}에 대해 알려줘."
)

# ✅ 구체적인 프롬프트
specific_prompt = ChatPromptTemplate.from_template(
    """{topic}에 대해 다음 형식으로 설명해주세요:

1. 정의 (1-2문장)
2. 핵심 특징 3가지
3. 실제 활용 사례 2가지

전문 용어는 피하고 초보자도 이해할 수 있게 작성해주세요."""
)

chain = specific_prompt | llm
result = chain.invoke({"topic": "머신러닝"})