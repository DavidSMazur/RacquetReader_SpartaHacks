from flask import Flask, send_file

app = Flask(__name__)

@app.route('/api/get_video', methods=['GET'])
def get_video():
    video_path = 'output\video\output_video_7.mp4'
    return send_file(video_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
