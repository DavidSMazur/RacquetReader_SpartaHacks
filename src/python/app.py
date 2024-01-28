from flask import Flask, request, send_file
import os

app = Flask(__name__)

@app.route('/api/process_video', methods=['POST'])
def process_video():
    if 'video' not in request.files:
        return 'No video file provided', 400
    
    video_file = request.files['video']
    if video_file.filename == '':
        return 'No selected video file', 400
    
    # Save the uploaded video file to a temporary directory
    video_path = 'temp/video.mp4'  # Specify the path where you want to save the video
    video_file.save(video_path)
    
    # Process the video here (e.g., using OpenCV, ffmpeg, etc.)
    # Replace this with your actual video processing code
    
    # After processing, return the processed video
    processed_video_path = 'temp/processed_video.mp4'  # Specify the path of the processed video
    return send_file(processed_video_path, as_attachment=True)

@app.route('/api/process_string', methods=['POST'])
def process_string():
    # Get the string from the request data
    data = request.json
    input_string = data.get('input_string')

    # Process the string (you can replace this with your processing logic)
    print("Received string from frontend:", input_string)

    # You can perform any processing here
    
    # Return an empty response
    return '', 200

if __name__ == '__main__':
    app.run(debug=True)
