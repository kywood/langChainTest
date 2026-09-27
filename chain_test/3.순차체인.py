from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from chain_test.llm_def import llm

translate_prompt = ChatPromptTemplate.from_template(
    "다음 한국어를 영어로 번역하세요: {korean_word}"
)

# 2단계: 영어 단어 설명
explain_prompt = ChatPromptTemplate.from_template(
    "다음 영어 단어를 한국어로 자세히 설명하세요: {english_word}"
)

# 체인 1: 번역
chain1 = translate_prompt | llm | StrOutputParser()

# 체인 2: 번역 결과를 입력으로 사용
chain2 = (
        {"english_word": chain1}
        | explain_prompt
        | llm
        | StrOutputParser()
)

# 실행
result = chain2.invoke({"korean_word": "인공지능"})
print(result)