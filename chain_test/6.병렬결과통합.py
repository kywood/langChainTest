# 병렬 분석
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel

from chain_test.llm_def import llm

analysis_chain = RunnableParallel(
    pros=ChatPromptTemplate.from_template("{topic}의 장점") | llm | StrOutputParser(),
    cons=ChatPromptTemplate.from_template("{topic}의 단점") | llm | StrOutputParser(),
)

# 결과 통합
synthesis_prompt = ChatPromptTemplate.from_template(
    """다음 분석을 종합하여 결론을 작성하세요:

장점:
{pros}

단점:
{cons}

균형 잡힌 결론을 3문장으로 작성하세요."""
)

# 전체 체인: 병렬 분석 → 통합
full_chain = (
        analysis_chain
        | synthesis_prompt
        | llm
        | StrOutputParser()
)

result = full_chain.invoke({"topic": "인공지능"})
print(result)