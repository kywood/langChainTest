# MessagePromptTemplate 활용
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate

from chain_test.llm_def import llm

chat_prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template("이 시스템은 천문학 질문에 답변할 수 있습니다."),
        HumanMessagePromptTemplate.from_template("{user_input}"),
    ]
)

messages = chat_prompt.format_messages(user_input="태양계에서 가장 큰 행성은 무엇인가요?")

print(messages)

chain = chat_prompt | llm | StrOutputParser()

result=  chain.invoke({"user_input": "태양계에서 가장 큰 행성은 무엇인가요?"})

print(result)
