from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from chain_test.llm_def import llm

# 1. 컴포넌트 정의
prompt = ChatPromptTemplate.from_template("지구과학에서 {topic}에 대해 간단히 설명해주세요.")
 # = ChatOpenAI(model="gpt-4o-mini")


output_parser = StrOutputParser()

# 2. 체인 생성
chain = prompt | llm | output_parser

# 3. invoke 메소드 사용
result = chain.invoke({"topic": "지구 자전"})
print("invoke 결과:", result)