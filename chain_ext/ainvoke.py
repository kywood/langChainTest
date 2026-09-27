import nest_asyncio
import asyncio

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from chain_test.llm_def import llm

# nest_asyncio 적용 (구글 코랩 등 주피터 노트북에서 실행 필요)
nest_asyncio.apply()


prompt = ChatPromptTemplate.from_template("지구과학에서 {topic}에 대해 간단히 설명해주세요.")
 # = ChatOpenAI(model="gpt-4o-mini")


output_parser = StrOutputParser()

# 2. 체인 생성
chain = prompt | llm | output_parser


# 비동기 메소드 사용 (async/await 구문 필요)
async def run_async():
    result = await chain.ainvoke({"topic": "해류"})
    print("ainvoke 결과:", result[:50], "...")

asyncio.run(run_async())