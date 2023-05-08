import openai

from prompts import chat_system_prompt
from config import code_api_key, code_base_url, openai_api_key

import time

def base_model(prompt: str, temp=0.8, max_tokens: int = 60, n: int = 5) -> str:
    # using cd2 proxy for code-davinci-002: https://github.com/cosmicoptima/openai-cd2-proxy
    openai.api_key = code_api_key
    openai.api_base = code_base_url if code_base_url else 'https://api.openai.com/v1/chat/completions'
    response = openai.Completion.create(
        model="code-davinci-002",
        prompt=prompt,
        temperature=temp,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        n=n
    )
    return response

def chat_model(prompt, model: str = "gpt-3.5-turbo", temp: float = 0.0, max_tokens: int = 10, n: int = 1) -> str:
    time.sleep(20)
    openai.api_key = openai_api_key
    openai.api_base = 'https://api.openai.com/v1/'
    messages = [{"role": "system", "content": chat_system_prompt}, {"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temp,
        max_tokens=max_tokens,
        top_p=1,
        n=n
    )
    return response