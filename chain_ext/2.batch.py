from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from chain_test.llm_def import llm


# 1. 컴포넌트 정의
prompt = ChatPromptTemplate.from_template("지구과학에서 {topic}에 대해 간단히 설명해주세요.")
 # = ChatOpenAI(model="gpt-4o-mini")


output_parser = StrOutputParser()

# 2. 체인 생성
chain = prompt | llm | output_parser


topics = ["지구 공전", "화산 활동", "대륙 이동"]
results = chain.batch([{"topic": t} for t in topics])
for topic, result in zip(topics, results):
    print(f"{topic} 설명: {result[:50]}...")  # 결과의 처음 50자만 출력



a=[{"topic": t} for t in topics]

print(a)