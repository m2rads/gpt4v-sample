import cv2
import numpy as np


folder = "frames"

stream = cv2.VideoCapture(0)

# Setting up initial frame for comparison
_, last_frame = stream.read()
last_frame_gray = cv2.cvtColor(last_frame, cv2.COLOR_BGR2GRAY)

# Setting up the threshold value
image_width = int(stream.get(cv2.CAP_PROP_FRAME_WIDTH))  # Get width from the stream
image_height = int(stream.get(cv2.CAP_PROP_FRAME_HEIGHT)) # Get height from the stream
num_pixels = image_width * image_height
percent_change = 0.03  # 1% change
threshold = num_pixels * percent_change * 255

while True:
    ret, current_frame = stream.read()
    if not ret:
        break

    current_frame_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
    frame_difference = cv2.absdiff(last_frame_gray, current_frame_gray)
    difference_value = np.sum(frame_difference)

    if difference_value > threshold:
        # Significant change detected - process current_frame here
        print("Significant change detected")
        path = f"./{folder}/frame.jpg"
        cv2.imwrite(path, current_frame)


    last_frame_gray = current_frame_gray

    cv2.imshow("Webcam", current_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

stream.release()
cv2.destroyAllWindows()
