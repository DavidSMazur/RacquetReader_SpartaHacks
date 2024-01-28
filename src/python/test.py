import cv2
from pathlib import Path

# Define video source
video_path = str(Path('data/video/swing_short.mp4'))

# Get video capture object
cap = cv2.VideoCapture(video_path)

# Get video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define the desired resized width and height
resized_width = int(width * 0.5)  # You can adjust the scaling factor as needed
resized_height = int(height * 0.5)

# Iterate through available codecs and try writing a small video
codecs_to_try = ['MJPG', 'mp4v', 'H264']
for codec in codecs_to_try:
    try:
        # Define the output video file
        output_path = f"output_{codec}.mp4"

        # Initialize VideoWriter with the codec
        fourcc = cv2.VideoWriter_fourcc(*codec)
        out = cv2.VideoWriter(output_path, fourcc, fps, (resized_width, resized_height))  # Use resized dimensions

        # Write all frames
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Resize the frame
            frame_resized = cv2.resize(frame, (resized_width, resized_height))

            out.write(frame_resized)

        # Release VideoWriter
        out.release()
        print(f"Successfully created video with codec: {codec}")

    except Exception as e:
        print(f"Failed to create video with codec {codec}. Error: {e}")

# Release video capture object
cap.release()
