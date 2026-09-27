from langchain_core.messages import ToolMessage

tool_msg = ToolMessage(
    content="서울의 현재 온도는 25도입니다.",
    tool_call_id="call_abc123",
    name="get_weather"
)

print(tool_msg)