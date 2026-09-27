from langchain_core.messages import SystemMessage, HumanMessage

# 기본 시스템 메시지
system_msg = SystemMessage(content="당신은 친절한 한국어 AI 어시스턴트입니다.")

# 상세한 역할 정의
system_msg = SystemMessage(content="""당신은 파이썬 프로그래밍 전문가입니다.
- 초보자도 이해할 수 있게 설명하세요
- 코드 예제를 포함하세요
- 한국어로 답변하세요""")

print(system_msg)
print(system_msg.id )
print(system_msg.name )
print(system_msg.type )
print(system_msg.content )




# 텍스트 메시지
human_msg = HumanMessage(content="파이썬 리스트 컴프리헨션을 설명해주세요.")

# 이름 포함 (선택)
human_msg = HumanMessage(
    content="안녕하세요!",
    name="user_123"
)


print(human_msg )
print(human_msg.id )
print(human_msg.name )
print(human_msg.type )
print(human_msg.content )
