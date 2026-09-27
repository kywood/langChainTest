from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from chain_test.llm_def import llm


# 1. 컴포넌트 정의
prompt = ChatPromptTemplate.from_template("지구과학에서 {topic}에 대해 간단히 설명해주세요.")
 # = ChatOpenAI(model="gpt-4o-mini")


output_parser = StrOutputParser()

# 2. 체인 생성
chain = prompt | llm | output_parser


stream = chain.stream({"topic": "지진"})
print("stream 결과:")
for chunk in stream:
    print(chunk, end="", flush=True)
print()

