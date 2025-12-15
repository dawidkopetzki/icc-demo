def create_chat_message(model_id: str, prompt: str):
    return {
        "model": f"{model_id}",
        "stream": False,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"{prompt}"
                    },
                ]
            }
        ]
    }
