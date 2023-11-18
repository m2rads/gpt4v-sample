import cv2 
import time
from PIL import Image
import numpy as np 

folder = "frames"

stream = cv2.VideoCapture(0)

# check if the webcam is opened correctly
if not stream.isOpened():
    raise IOError("Cannot open webcam")

time.sleep(2)


while True:
    ret, frame = stream.read()
    if not ret: 
        break 
    # Convert the frame to a PIL image
    pil_img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    #resize the image 
    max_size = 250 
    ratio = max_size / max(pil_img.size)
    new_size = tuple([int(x*ratio) for x in pil_img.size])
    resized_img = pil_img.resize(new_size, Image.LANCZOS)

    # Convert the PIL image back to openCV image
    frame = cv2.cvtColor(np.array(resized_img), cv2.COLOR_RGB2BGR)

    # Save the frame as an iamge and keep overwriting
    print("Calculating your calculation")
    path = f"./{folder}/frame.jpg"
    cv2.imwrite(path, frame)
    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # wait for 2 seconds
    time.sleep(2)

stream.release()
cv2.destroyAllWindows()