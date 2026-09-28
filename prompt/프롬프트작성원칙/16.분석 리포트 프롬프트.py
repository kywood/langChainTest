from langchain_core.prompts import ChatPromptTemplate

from chain_test.llm_def import llm

prompt = ChatPromptTemplate.from_messages([
    ("system", """당신은 비즈니스 분석 전문가입니다.

리포트 작성 규칙:
1. 데이터 기반 분석
2. 명확한 인사이트 도출
3. 실행 가능한 권고안 제시

리포트 구조:
## 요약 (3문장 이내)
## 주요 발견사항 (3-5개 항목)
## 상세 분석
## 권고사항
## 다음 단계"""),
    ("human", """다음 데이터를 분석하고 리포트를 작성해주세요:

데이터:
{data}

분석 목적: {purpose}
대상 독자: {audience}""")
])


# 2. LCEL 체인 생성 (Prompt | LLM)
chain = prompt | llm

# 3. 입력 데이터 및 환경 설정
sample_data = """
[2026년 3분기 모바일 앱 신규 가입자 retention 데이터]
- 총 신규 가입자: 50,000명
- D+1 재방문율: 45% (전분기 대비 +5%p)
- D+7 재방문율: 20% (전분기 대비 -3%p)
- D+30 재방문율: 8% (전분기 대비 -5%p)
- 이탈 유저 주요 피드백: "초기 튜토리얼은 좋으나 1주일 이후 사용할 콘텐츠 부족"
"""

sample_purpose = "3분기 유저 이탈 원인 분석 및 4분기 리텐션 개선 전략 수립"
sample_audience = "C-Level 임원진 및 프로덕트 팀장"

# 4. 체인 실행 (변수 전달)
response = chain.invoke({
    "data": sample_data,
    "purpose": sample_purpose,
    "audience": sample_audience
})

# 5. 결과 출력
print(response.content)
