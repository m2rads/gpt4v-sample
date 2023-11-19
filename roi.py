import cv2
import numpy as np
import openai  # Make sure to install OpenAI's Python package

def detect_whiteboard_coordinates(frames):
    # Placeholder for the implementation of the API call to GPT-4V
    # This function should analyze the frames and return the coordinates of the whiteboard
    # Return format: (x, y, width, height)
    # ...
    x, y, width, height = ""
    return (x, y, width, height)  # Replace with actual coordinates obtained from GPT-4V

# Set up the video capture
stream = cv2.VideoCapture(0)
if not stream.isOpened():
    raise IOError("Cannot open webcam")

# Capture initial frames for object detection
NUM_INITIAL_FRAMES = 5 
initial_frames = []
for _ in range(NUM_INITIAL_FRAMES):
    ret, frame = stream.read()
    if ret:
        initial_frames.append(frame)

# Get whiteboard coordinates from GPT-4V
whiteboard_coords = detect_whiteboard_coordinates(initial_frames)
roi_x, roi_y, roi_w, roi_h = whiteboard_coords

# Setting up the threshold value for the ROI
percent_change = 0.03  # 3% change
roi_threshold = roi_w * roi_h * percent_change * 255

# Main loop for change detection
_, last_frame = stream.read()
last_frame_gray = cv2.cvtColor(last_frame, cv2.COLOR_BGR2GRAY)

while True:
    ret, current_frame = stream.read()
    if not ret:
        break

    current_frame_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
    current_frame_roi = current_frame_gray[roi_y:roi_y+roi_h, roi_x:roi_x+roi_w]
    last_frame_roi = last_frame_gray[roi_y:roi_y+roi_h, roi_x:roi_x+roi_w]

    frame_difference = cv2.absdiff(last_frame_roi, current_frame_roi)
    difference_value = np.sum(frame_difference)

    if difference_value > roi_threshold:
        print("Significant change detected in ROI")
        # TODO: Send current_frame to GPT-4V for analysis if needed
        path = f"./frames/frame.jpg"  # Saving the frame
        cv2.imwrite(path, current_frame)

    last_frame_gray = current_frame_gray
    cv2.imshow("Webcam", current_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

stream.release()
cv2.destroyAllWindows()
