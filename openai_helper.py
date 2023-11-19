import os 
import base64
import time
import errno
from openai import OpenAI

class OpenAIHelper:
    def __init__(self, model="gpt-4-vision-preview", max_tokens=300):
        self.client = OpenAI()
        self.model = model
        self.max_tokens = max_tokens

    def encode_img(self, img_path):
        while True:
            try:
                with open(img_path, 'rb') as img_file:
                    return base64.b64encode(img_file.read()).decode("utf-8")
            except IOError as e:
                if e.errno != errno.EACCES:
                    raise
                time.sleep(0.1)

    def hit_openai(self, payload):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=payload,
            max_tokens=self.max_tokens
        )
        return response.choices[0].message.content
