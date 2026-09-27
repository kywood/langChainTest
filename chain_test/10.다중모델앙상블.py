from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel

from chain_test.llm_def import llm, llm2

prompt = ChatPromptTemplate.from_template("{question}")

# 여러 모델 동시 호출
ensemble_chain = RunnableParallel(
    gpt=prompt | llm | StrOutputParser(),
    claude=prompt | llm2 | StrOutputParser(),
)

# 결과 종합
synthesis_prompt = ChatPromptTemplate.from_template(
    """두 AI의 응답을 비교하고 최선의 답변을 종합하세요:

GPT 응답:
{gpt}

Claude 응답:
{claude}

종합 답변:"""
)

final_chain = (
    ensemble_chain
    | synthesis_prompt
    | llm
    | StrOutputParser()
)

result = final_chain.invoke({"question": "효과적인 학습 방법은?"})

print(result)