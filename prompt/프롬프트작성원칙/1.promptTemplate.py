from langchain_core.prompts import PromptTemplate

# 템플릿 정의
template = PromptTemplate.from_template(
    "{topic}에 대해 {length}자 이내로 설명해주세요."
)

# 변수 대입
prompt = template.format(topic="인공지능", length="100")
print(prompt)