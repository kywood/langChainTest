from langchain_core.prompts import ChatPromptTemplate

from chain_test.llm_def import llm

prompt = ChatPromptTemplate.from_template(
    "You are an expert in astronomy. Answer the question. <Question>: {input}")

# ChatPromptTemplate(input_variables=['input'], messages=[HumanMessagePromptTemplate(
#     prompt=PromptTemplate(input_variables=['input'],
#                           template='You are an expert in astronomy. Answer the question. <Question>: {input}'))])

chain = prompt | llm

response = chain.invoke({"input": "지구의 자전 주기는?"})
print(response.content)
