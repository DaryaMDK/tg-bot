import httpx

from app.config.settings import OLLAMA_MODEL, OLLAMA_URL


async def ask_llm(prompt: str) -> str:
    payload = {"model": OLLAMA_MODEL, "prompt": prompt, "stream": False}

    async with httpx.AsyncClient(timeout=120) as client:
        response = await client.post(f"{OLLAMA_URL}/api/generate", json=payload)

        response.raise_for_status()

        data = response.json()

        return data.get("response", "Пустой ответ.")
