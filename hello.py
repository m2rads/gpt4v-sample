import os 
from openai_helper import OpenAIHelper

MODEL = "gpt-4-vision-preview"
MAX_TOKENS = 300

def payload(base64_img):
    return [
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": "Analyze the provided image and locate the iphone. Return the coordinates of the iphone in a structured format. Provide the top-left corner, bottom-right corner coordinates and orientation in the format: 'Top-left: (x1, y1), Bottom-right: (x2, y2), Orientation: value'. Also, describe its orientation as either 'horizontal' or 'vertical'."
                },
                {
                    "type": "image_url",
                    "image_url": f"data:image/jpeg;base64,{base64_img}"
                }
            ]
        }
    ]

#                 {"type": "text", "text": "Analyze the provided image and locate the iphone. Return the coordinates of the iphone in a structured format. Provide the top-left corner, bottom-right corner coordinates and orientation in the format: 'Top-left: (x1, y1), Bottom-right: (x2, y2), Orientation: value'. Also, describe its orientation as either 'horizontal' or 'vertical'."},

# Initialize openai
openai_helper = OpenAIHelper(model=MODEL, max_tokens=MAX_TOKENS)

img_path = "frames/frame.jpg"
encoded_image = openai_helper.encode_img(img_path)
req_payload = payload(encoded_image)
response = openai_helper.hit_openai(req_payload)

print(response)
