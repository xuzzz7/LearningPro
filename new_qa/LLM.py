from openai import OpenAI
import numpy
import time
import torch

class Kimi():
    def __init__(self):

        self.client = OpenAI(
            api_key="sk-Dw2DNfGbCoDOW5klRICCxc8RJ6YNznC7QbGHO3jUm34nDhUQ",
            base_url="https://api.moonshot.cn/v1",
        )

    def answer(self, query):

        completion = self.client.chat.completions.create(
            model="moonshot-v1-8k",
            messages=[
                {"role": "system",
                 "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"},
                {"role": "user", "content": query}
            ],
            temperature=0.3,
        )
        return completion.choices[0].message.content
class Test():
    def __init__(self) -> None:
        pass


class LLM1():
    def __init__(self) -> None:
        pass