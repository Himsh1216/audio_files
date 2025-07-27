import os
from flask import Flask, request, send_file, render_template
from pydub import AudioSegment
import tempfile

app = Flask(__name__)

# Simple function to remove vocals by subtracting stereo channels
# This creates a mono background track approximating the instrumental.

def isolate_background(src_path, dst_path):
    song = AudioSegment.from_file(src_path)
    if song.channels == 2:
        left, right = song.split_to_mono()
        # Invert phase of right channel and overlay to remove center (vocals)
        background = left.overlay(right.invert_phase())
    else:
        background = song
    background.export(dst_path, format='wav')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if 'file' not in request.files:
        return 'No file uploaded', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    with tempfile.TemporaryDirectory() as tmpdir:
        src_path = os.path.join(tmpdir, 'input')
        dst_path = os.path.join(tmpdir, 'output.wav')
        file.save(src_path)
        isolate_background(src_path, dst_path)
        return send_file(dst_path, as_attachment=True, download_name='background.wav')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
