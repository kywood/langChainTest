# 테스트 실행
from chain_test.llm_def import llm

response = llm.invoke("지구의 자전 주기는?")
print(response.content)
pass
