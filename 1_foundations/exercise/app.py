import gradio as gr
from openai import OpenAI
import requests
from dotenv import load_dotenv
import os

def main():
    llm_client = OpenAI(base_url="http://127.0.0.1:1234/v1", api_key="lmstudio")
    llm = llm_client.chat.completions.create(
        model="lmstudio",
        messages=[
            {"role": "user", "content": "Hello, how are you?"}
        ]
    )
    print(llm.choices[0].message.content)

def push_noti(message):
    requests.post(
        "https://api.pushover.net/1/messages.json",
        data={
            "token": os.getenv("PUSHOVER_TOKEN"),
            "user": os.getenv("PUSHOVER_USER"),
            "message": message,
        }
    )

if __name__ == "__main__":
    load_dotenv()
    push_noti("Hello, how are you?")
