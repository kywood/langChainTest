import base64

import httpx
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage

from chain_test.llm_def import llmv, llm, llmv2

model = llmv2

MAGIC = {
    b"\xff\xd8\xff": "image/jpeg",
    b"\x89PNG\r\n\x1a\n": "image/png",
    b"GIF8": "image/gif",
    b"RIFF": "image/webp",  # 엄밀히는 [8:12] == b"WEBP"까지 확인
}


def get_base64_image(url: str) -> str:
    res = httpx.get(
        url,
        headers={"User-Agent": "langchain-study/0.1"},
        follow_redirects=True,
    )
    res.raise_for_status()
    data = res.content
    if not any(data.startswith(sig) for sig in MAGIC):
        raise ValueError(
            f"이미지 아님: {res.headers.get('content-type')} / {data[:16]!r}"
        )
    return base64.b64encode(data).decode("utf-8")

# 2. 실제 존재하는 이미지 URL 지정
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Glowcards.jpg/320px-Glowcards.jpg"
image_url = "https://picsum.photos/id/237/400/300"
base64_data = get_base64_image(image_url)

# 3. 순수 Base64 문자열 전달
message = HumanMessage(
    content=[
        {"type": "text", "text": "두 이미질 각각 설명해"},
        {
            "type": "image_url",
            "image_url": {"url": base64_data}  # 👈 순수 base64 텍스트 전달
        },
        {
            "type": "image_url",
            "image_url": {"url": get_base64_image("https://ultralytics.com/images/bus.jpg")}  # 👈 순수 base64 텍스트 전달
        },
    ]
 )


response = model.invoke([message])
print(response.content)