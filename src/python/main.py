# TODO: sometimes the code saves the output video correctly, see print 'VideoWriter released successfully'

from collections import defaultdict
from pathlib import Path
import cv2
import numpy as np
import pandas as pd
from ultralytics import YOLO

max_track_length = 900  # 1 minute at 15 fps
scale_factor = .5
file_number = '4'

# Load the YOLOv8 model
model = YOLO('models/yolov8n-pose.pt')

# Define video source
video_path = str(Path('data/video/swing_short.mp4'))
video_source = video_path
cap = cv2.VideoCapture(video_source)

# Define directories for saving the output files
data_path = Path(f'data')
output_path = Path(f'output')
output_video_path = output_path / 'video' / f'output_video_{file_number}.mp4'
output_image_path = output_path / 'image' / f'output_image_{file_number}.png'
output_csv_path = output_path / 'csv'

# Create the directories if they don't exist
output_path.mkdir(parents=True, exist_ok=True)
output_path.joinpath('video').mkdir(parents=True, exist_ok=True)
output_path.joinpath('image').mkdir(parents=True, exist_ok=True)
output_path.joinpath('csv').mkdir(parents=True, exist_ok=True)

# Get the video's width, height, and frames per second
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define the codec and VideoWriter object
out = cv2.VideoWriter(str(output_video_path), cv2.VideoWriter_fourcc(*'vp09'), fps, (width, height))

# Store the center and wrist history
center_history = defaultdict(lambda: [])
wrist_history = defaultdict(lambda: [])

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 tracking on the frame, persisting tracks between frames
        results = model.track(frame, persist=True, stream=True)

        for result in results:
            # Get the boxes, track IDs, and keypoints
            boxes = result.boxes.xywh.cpu()
            track_ids = result.boxes.id.int().cpu().tolist()
            keypoints_list = result.keypoints.xy.cpu().tolist()

            # For each tracked object, iterate over its keypoints.
            # If the keypoint is the right wrist (index 10), append its coordinates to the wrist_history for the current track_id.
            # If the wrist_history for the current track_id exceeds the maximum track length, remove the oldest entry.
            for track_id, keypoints in zip(track_ids, keypoints_list):
                for i, keypoint in enumerate(keypoints):
                    x, y = keypoint[:2]  # Only take the first two values
                    if i == 10:  # If the keypoint is the right wrist
                        wrist_history[track_id].append((float(x), float(y)))  # x, y center point
                        if len(wrist_history[track_id]) > max_track_length:
                            wrist_history[track_id].pop(0)

            # For each bounding box and its corresponding track_id, extract the box's coordinates.
            # Append the center point of the box (x, y) to the tracking history for the current track_id.
            # If the tracking history for the current track_id exceeds the maximum track length, remove the oldest entry.
            for box, track_id in zip(boxes, track_ids):
                x, y, w, h = box
                track = center_history[track_id]
                track.append((float(x), float(y)))  # x, y center point
                if len(track) > max_track_length:
                    track.pop(0)

            # Visualize the results on the frame
            annotated_frame = result.plot()

            # Plot the center_history tracking lines
            for track_id in center_history:
                points = np.hstack(center_history[track_id]).astype(np.int32).reshape((-1, 1, 2))
                cv2.polylines(annotated_frame, [points], isClosed=False, color=(230, 230, 230), thickness=10)

            # Plot the wrist_history tracking lines
            for track_id in wrist_history:
                points = np.hstack(wrist_history[track_id]).astype(np.int32).reshape((-1, 1, 2))
                cv2.polylines(annotated_frame, [points], isClosed=False, color=(0, 255, 0), thickness=10)

            # Resize the annotated frame for display
            annotated_frame = cv2.resize(annotated_frame, None, fx=scale_factor, fy=scale_factor)

            # Write the frame to the output video file
            out.write(annotated_frame)
            print(f'writing to {output_video_path}')

            # Display the annotated frame
            cv2.imshow("YOLOv8 Tracking", annotated_frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object
cap.release()

# Release the video writer object
try:
    out.release()
    print("VideoWriter released successfully.")
except cv2.error as e:
    print(f"Error releasing VideoWriter: {e}")

# Save the last frame as an image
cv2.imwrite(output_image_path, annotated_frame)

# Convert the dictionaries to DataFrames
wrist_df = pd.DataFrame.from_dict(wrist_history, orient='index')
center_df = pd.DataFrame.from_dict(center_history, orient='index')

# Save the DataFrames to CSV files
wrist_df.to_csv(output_csv_path / f'wrist_history_{file_number}.csv')
center_df.to_csv(output_csv_path / f'center_history_{file_number}.csv')

# Close the display window
cv2.destroyAllWindows()
