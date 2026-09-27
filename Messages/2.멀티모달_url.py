import base64

import httpx
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage

from chain_test.llm_def import llmv, llm, llmv2

model = llmv2
# model = llmv
# #
# # # 이미지 URL 포함
# message = HumanMessage(
#     content=[
#         {"type": "text", "text": "이 이미지에 무엇이 있나요?"},
#         {
#             "type": "image_url",
#             "image_url": {"url": "https://picsum.photos/id/237/400/300"}
#         },
#     ]
# )
#
# response = model.invoke([message])
# print(response.content)



def get_base64_image(url: str) -> str:
    res = httpx.get(
        url,
        headers={"User-Agent": "langchain-study/0.1 (test@example.com)"},
        follow_redirects=True,
    )
    res.raise_for_status()
    ctype = res.headers.get("content-type", "")
    if not ctype.startswith("image/"):
        raise ValueError(f"이미지 아님: {ctype}")
    return base64.b64encode(res.content).decode("utf-8")

# 2. 실제 존재하는 이미지 URL 지정
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Glowcards.jpg/320px-Glowcards.jpg"
image_url = "https://picsum.photos/id/237/400/300"
base64_data = get_base64_image(image_url)

# 3. 순수 Base64 문자열 전달
message = HumanMessage(
    content=[
        {"type": "text", "text": "이 이미지에 무엇이 있나요? 한국어로 설명해주세요."},
        {
            "type": "image_url",
            "image_url": {"url": base64_data}  # 👈 순수 base64 텍스트 전달
        },
    ]
 )


response = model.invoke([message])
print(response.content)