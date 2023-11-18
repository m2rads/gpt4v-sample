import os 
from openai import OpenAI
import base64
import json
import time
import errno

client = OpenAI()

MODEL = "gpt-4-vision-preview"
MAX_TOKENS = 300


def encode_img(img_path):
    while True:
        try:
            with open(img_path, 'rb') as img_file:
                return base64.b64encode(img_file.read()).decode("utf-8")
        except IOError as e:
            if e.errno != errno.EACCES:
                # Not a "file in use" error, re-raise
                raise
            # File is being written to, wait a bit and retry
            time.sleep(0.1)

def payload(base64_img):
    return [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "This is a math lecture. Identify the math expressions and return what you see on the board as LaTex code only."},
                {
                    "type": "image_url",
                    "image_url": f"data:image/jpeg;base64,{base64_img}"
                }
            ]
        }
    ]


def hit_openai(base64_img): 
    response = client.chat.completions.create(
        model=MODEL,
        messages=payload(base64_img),
        max_tokens=MAX_TOKENS
    )    
    response_text = response.choices[0].message.content
    return response


def main(): 

    while True: 
        # path to your image
        img_path = os.path.join(os.getcwd(), "./frames/frame.jpg")

        # getting the base64 encoding 
        base64_img = encode_img(img_path)

        # analyze posture
        print("openai is calculating")
        latex = hit_openai(base64_img)

        print("openai returned")
        print(latex)

        # wait for 5 sec 
        time.sleep(5)


if __name__ == "__main__":
    main()
