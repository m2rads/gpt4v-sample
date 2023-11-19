import os 
from openai_helper import OpenAIHelper

MODEL = "gpt-4-vision-preview"
MAX_TOKENS = 300

openai_helper = OpenAIHelper(model=MODEL, max_tokens=MAX_TOKENS)

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


# Create an instance of OpenAIHelper
openai_helper = OpenAIHelper(model="gpt-4-vision-preview", max_tokens=300)

# Use the methods of OpenAIHelper
img_path = "frames/frame.jpg"
encoded_image = openai_helper.encode_img(img_path)
req_payload = payload(encoded_image)
response = openai_helper.hit_openai(req_payload)

print(response)




# def main(): 

#     while True: 
#         # path to your image
#         img_path = os.path.join(os.getcwd(), "./frames/frame.jpg")

#         # getting the base64 encoding 
#         base64_img = encode_img(img_path)

#         # analyze posture
#         print("openai is calculating :)")
#         latex = hit_openai(base64_img)

#         print("openai returned")
#         print(latex)

#         # wait for 5 sec 
#         time.sleep(5)


# if __name__ == "__main__":
#     main()
