import cv2
import base64
import time
import os
import requests
from openai import OpenAI 

client = OpenAI()

video = cv2.VideoCapture("resources/accessmath-lecture.mp4")
api_key = os.getenv('OPENAI_API_KEY')

base64Frames = []
while video.isOpened():
    success, frame = video.read()
    if not success:
        break
    _, buffer = cv2.imencode(".jpg", frame)
    base64Frames.append(base64.b64encode(buffer).decode("utf-8"))

def display_video(video):
    if not video.isOpened():
        print("Error opening video file")
    else:
        while video.isOpened():
            success, frame = video.read()
            if not success:
                break

            # Display the resulting frame
            cv2.imshow('Frame', frame)

            # Press Q on keyboard to exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

            # Sleep to control frame rate
            time.sleep(0.025)

        # Closes all the frames
        cv2.destroyAllWindows()

# display_video(video)
video.release()
print(len(base64Frames), "frames read.")

PROMPT_MESSAGES = [
    {
        "role": "user",
        "content": [
            "These are frames from a lecture. The only thing I want from you is just to generate LaTeX code based on the math expresions you see on the white board. I do not want any extra text or explenations. Just LaTeX code to represent the math eexpressions on the board.",
            *map(lambda x: {"image": x, "resize": 768}, base64Frames[0::340]),
        ]
    }
]

params = {
    "model": "gpt-4-vision-preview",
    "messages": PROMPT_MESSAGES,
    "max_tokens": 400,
}

result = client.chat.completions.create(**params)
print(result.choices[0].message.content)