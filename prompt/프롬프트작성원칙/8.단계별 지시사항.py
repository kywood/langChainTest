from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 코드 리뷰 전문가입니다."),
    ("human", """다음 코드를 리뷰해주세요:

<code>
{code}
</code>

다음 순서로 분석해주세요:
1. **기능 요약**: 코드가 수행하는 작업 설명
2. **장점**: 잘 작성된 부분 (2-3가지)
3. **개선점**: 수정이 필요한 부분 (2-3가지)
4. **리팩토링 제안**: 개선된 코드 예시

각 섹션은 명확히 구분하여 작성해주세요.""")
])