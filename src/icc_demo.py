import mimetypes

import httpx
import json
import asyncio

from util import create_chat_message

API_BASE_URL = "https://hub.homeport.ai/api"
API_KEY = ""
WORKSPACE_ID = ""
FOLDER_ID = ""
HEADERS = {"Authorization": f"Bearer {API_KEY}"}
FILES_PATH = "../sample_files"
ASSISTANT_ID = ""

"""
Those are example functions to demonstrate the usage of the Homeport API outside the context of an async python notebook.
Here you need to handle asychronous calls on your own.
Use an async framework like FastAPI or an async event loop to call those functions.
Here we use asyncio.run() and httpx.AsyncClient().
"""

async def upload_file(file_name: str):
    url = f"{API_BASE_URL}/files"
    file_path = f"{FILES_PATH}/{file_name}"
    file_bytes = None
    mime_type, _ = mimetypes.guess_type(file_path)
    with open(file_path, "rb") as file:
        file_bytes = file.read()
    if not file_bytes:
        raise ValueError("File is empty or could not be read.")

    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=url,
            headers=HEADERS,
            files={"file": (file_name, file_bytes, mime_type)},
            data={
                "workspace_id": WORKSPACE_ID,
                "folder_id": FOLDER_ID,
                "store_vectors": "true",
            }
        )
        response.raise_for_status()
        print(response.json())


async def list_models():
    url = f"{API_BASE_URL}/openai/models"

    async with httpx.AsyncClient() as client:
        response = await client.get(
            url=url,
            headers=HEADERS,
        )
        response.raise_for_status()
        print(json.dumps(response.json(), indent=2))


async def call_completion_api(model_id: str, prompt: str):
    url = f"{API_BASE_URL}/openai/chat/completions"
    payload = create_chat_message(model_id, prompt)

    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=url,
            headers=HEADERS,
            json=payload
        )
        response.raise_for_status()
        print(json.dumps(response.json(), indent=2))


async def call_assistant_api(prompt: str):
    url = f"{API_BASE_URL}/openai/deployments/{ASSISTANT_ID}/chat/completions?api-version=2024"
    payload = {
        "stream": False,
        "messages": [
            {
                "role": "user",
                "content": f"{prompt}"
            }
        ]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=url,
            headers=HEADERS,
            json=payload
        )
        response.raise_for_status()
        print(json.dumps(response.json(), indent=2))

if __name__ == "__main__":
    asyncio.run(upload_file("DHL.pdf"))
    # asyncio.run(list_models())
    # asyncio.run(
    #     call_completion_api(
    #         model_id="openai/Qwen3-VL-8B-Instruct-Q5_K_M",
    #         prompt="Hello there, how are you?"
    #     ))
    # asyncio.run(
    #     call_assistant_api(
    #         prompt="Summarize the main points of the given documents."
    #     ))
