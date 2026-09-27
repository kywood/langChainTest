from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda

from chain_test.llm_def import llm


# 입력 변환 함수
def preprocess(input_dict):
    return {
        "processed_text": input_dict["text"].strip().lower(),
        "original": input_dict["text"]
    }

# 출력 변환 함수
def postprocess(output):
    return {
        "result": output,
        "length": len(output)
    }

chain = (
    RunnableLambda(preprocess)
    | ChatPromptTemplate.from_template("분석: {processed_text}")
    | llm
    | StrOutputParser()
    | RunnableLambda(postprocess)
)

result = chain.invoke({"text":"테슬라 가격"})
print(result)